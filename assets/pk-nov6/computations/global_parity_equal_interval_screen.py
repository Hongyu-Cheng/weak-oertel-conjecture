import numpy as np
from scipy.spatial import ConvexHull
import random,json
rng=random.Random(554)
def pts(poly):
 hull=ConvexHull(poly);eq=hull.equations
 out=[]
 for x in range(min(p[0] for p in poly),max(p[0] for p in poly)+1):
  for y in range(min(p[1] for p in poly),max(p[1] for p in poly)+1):
   if np.max(eq[:,:2]@np.array([x,y])+eq[:,2])<1e-8:out.append((x,y))
 return np.array(out,float)
def dep(P,j):
 V=P-j;A=np.repeat(V,2,axis=0);b=np.tile([-.5,.5],len(P));
 ii,jj=np.triu_indices(len(b),1);det=A[ii,0]*A[jj,1]-A[ii,1]*A[jj,0]
 mask=np.abs(det)>1e-9;ii,jj,det=ii[mask],jj[mask],det[mask]
 aa=(b[ii]*A[jj,1]-A[ii,1]*b[jj])/det;bb=(A[ii,0]*b[jj]-b[ii]*A[jj,0])/det
 vals=np.clip(.5+aa[:,None]*V[:,0]+bb[:,None]*V[:,1],0,1).sum(axis=1)
 return min(vals.min(),len(P)/2)
for trial in range(500):
 poly=[(rng.randrange(-3,4),rng.randrange(-3,4)) for _ in range(rng.randrange(3,8))]
 try:P=pts(poly)
 except:continue
 if len(P)>35 or len(P)<3:continue
 ds=[dep(P,j) for j in P];v=max(ds);cent=[tuple(map(int,j)) for j,d in zip(P,ds) if abs(d-v)<1e-8]
 for i,a in enumerate(cent):
  for b in cent[i+1:]:
   if all((a[k]-b[k])%2==0 for k in range(2)):
    out=dict(poly=poly,P=P.tolist(),depth=v,centers=cent,ds=ds)
    open('./global_parity_equal_interval_candidate.json','w').write(json.dumps(out));print('FOUND',out,flush=True);raise SystemExit
 if trial%50==0:print('trial',trial,'N',len(P),'max',v,'cent',cent,flush=True)
print('done no candidate')
