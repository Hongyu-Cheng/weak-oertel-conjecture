import sys

import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import root,linprog
from itertools import combinations
import json
rng=np.random.default_rng(91037)

def geometry(V):
 hull=ConvexHull(V);edges=sorted({tuple(sorted(e)) for face in hull.simplices for e in combinations(face,2)})
 return hull.volume,np.array(edges)

def section(V,edges,u):
 f=V@u;points=[]
 for i,j in edges:
  if f[i]*f[j]<0:points.append((f[j]*V[i]-f[i]*V[j])/(f[j]-f[i]))
 for i in range(len(V)):
  if abs(f[i])<1e-11:points.append(V[i])
 if len(points)<3:return None
 points=np.array(points);axis=np.eye(3)[np.argmin(abs(u))]
 e1=np.cross(u,axis);e1/=np.linalg.norm(e1);e2=np.cross(u,e1)
 pts=np.stack((points@e1,points@e2),axis=1)
 try:h=ConvexHull(pts)
 except Exception:return None
 poly=pts[h.vertices];nxt=np.roll(poly,-1,axis=0);cross=poly[:,0]*nxt[:,1]-poly[:,1]*nxt[:,0]
 area=sum(cross)/2
 if area<=0:return None
 c=np.sum((poly+nxt)*cross[:,None],axis=0)/(6*area)
 center=c[0]*e1+c[1]*e2
 return area,center,points

def volume_cap(V,edges,u,sec):
 ps=np.concatenate((V[V@u>=0],sec),axis=0)
 return ConvexHull(ps).volume if len(ps)>=4 else 0.

for trial in range(50):
 raw=rng.integers(-4,5,size=(rng.integers(6,13),3)).astype(float)
 try:h=ConvexHull(raw)
 except Exception:continue
 raw=raw[h.vertices];w=rng.integers(1,8,size=len(raw));y=(w[:,None]*raw).sum(axis=0)/sum(w);V=raw-y
 vol,edges=geometry(V);norms=[]
 for start in range(100):
  axis=start%3;ids=[i for i in range(3) if i!=axis]
  def fun(t):
   u=np.zeros(3);u[axis]=1;u[ids]=t;u/=np.linalg.norm(u)
   sec=section(V,edges,u)
   return sec[1][ids] if sec is not None else np.array([1e3,1e3])
  rr=root(fun,rng.uniform(-1.2,1.2,size=2),options={'maxfev':100,'xtol':1e-9})
  if not np.isfinite(rr.x).all() or np.linalg.norm(fun(rr.x))>1e-7:continue
  u=np.zeros(3);u[axis]=1;u[ids]=rr.x;u/=np.linalg.norm(u)
  if np.linalg.norm(section(V,edges,u)[1])>1e-7:continue
  if any(abs(np.dot(u,v))>1-1e-9 for v in norms):continue
  norms.append(u)
 qs=[];costs=[];records=[]
 for u in norms:
  area,cent,pts=section(V,edges,u);frac=volume_cap(V,edges,u,pts)/vol
  for sign,cost in [(1,frac),(-1,1-frac)]:qs.append(sign*area*u/vol);costs.append(cost);records.append((sign*u,cent))
 if not qs:continue
 result=linprog(costs,A_eq=np.vstack([np.array(qs).T,np.ones(len(qs))]),b_eq=[0,0,0,1],bounds=(0,None),method='highs')
 if not result.success:continue
 active=[i for i,v in enumerate(result.x) if v>1e-8]
 print('trial',trial,'vertices',len(V),'stationary lines',len(norms),'minimum',result.fun,'active',len(active),flush=True)
 if result.fun<27/64-1e-6:
  record={'raw':raw.tolist(),'weights_for_center':w.tolist(),'center':y.tolist(),'V':V.tolist(),'caps':[{'normal':records[i][0].tolist(),'center_residual':records[i][1].tolist(),'probability':result.x[i],'cost':costs[i],'q':qs[i].tolist()} for i in active],'value':result.fun}
  open('./general-stationary-section-numerical-candidate.json','w').write(json.dumps(record,indent=2))
  print('NUMERICAL CANDIDATE ONLY; saved for exact certification',flush=True);break
