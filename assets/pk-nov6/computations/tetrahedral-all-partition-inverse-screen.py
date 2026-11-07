import sys

import numpy as np
from scipy.optimize import least_squares,linprog
import random,json
rng=random.Random(894318);gamma=27/64
parts=[(0,1,2,3),(0,2,1,3),(0,3,1,2)]
def centroid(e):
 x,y,z,w=e
 return np.array([x*(1/(x+z)+1/(x+w)-1),y*(1/(y+z)+1/(y+w)-1),z*(1/(x+z)+1/(y+z)-1),w*(1/(x+w)+1/(y+w)-1)])/3

def softmax(h):
 H=np.r_[h,0.];H-=max(H);E=np.exp(H);return E/sum(E)
def quad_data(e,part):
 x,y,z,w=e;P=x+y;R=z+w;a=x*y;b=z*w;D=(a-b)**2+a*R+b*P
 f=b*(P-a+b)/D;co=3*x*y*z*w/D;vals=np.array([1/x,1/y,-1/z,-1/w]);v=np.zeros(4);v[list(part)]=vals
 return f,co*(v[1:]-v[0]),3*(b*P-a*R)/(4*D)
closest=-1e100;minweighted=1.;checked=0;maxroots=0
for trial in range(1500):
 ei=np.array([rng.randint(1,100) for _ in range(4)],float);ei/=sum(ei);lam=centroid(ei)
 caps=[];roots=[]
 for part in parts:
  target=lam[list(part)];found=[]
  starts=[np.zeros(3),np.log(target[:3]/target[3])]
  if part==parts[0]:starts.append(np.log(ei[:3]/ei[3]))
  starts += [np.array([rng.uniform(-5,5) for _ in range(3)]) for _ in range(10)]
  for start in starts:
   res=least_squares(lambda h:centroid(softmax(h))-target,start,bounds=(-15,15),xtol=1e-11,ftol=1e-11,gtol=1e-11,max_nfev=150)
   e=softmax(res.x)
   if np.linalg.norm(centroid(e)-target)>1e-9 or min(e)<1e-8:continue
   if any(np.linalg.norm(e-q)<1e-6 for q in found):continue
   found.append(e);f,q,s=quad_data(e,part);caps.append((f,q,s));roots.append({'part':part,'e':e.tolist(),'f':f,'q':q.tolist(),'s':s})
  maxroots=max(maxroots,len(found))
 for i in range(4):
  if any(lam[j]>1/3+1e-10 for j in range(4) if j!=i):continue
  f=27*np.prod([lam[j]for j in range(4)if j!=i]);v=np.array([3 if j==i else 3-1/lam[j]for j in range(4)]);q=f*(v[1:]-v[0]);s=f*sum(v)/4;caps.append((f,q,s))
 caps += [(1-f,-q,-s)for f,q,s in list(caps)]
 lower=max([0.]+[(gamma-f)/(-s)for f,q,s in caps if s< -1e-10]);upper=min([(f-gamma)/s for f,q,s in caps if s>1e-10],default=1e20);gap=lower-upper
 vec=np.array([q for f,q,s in caps]).T;vals=np.array([f for f,q,s in caps]);lp=linprog(vals,A_eq=np.vstack([np.ones(len(caps)),vec]),b_eq=[1,0,0,0],bounds=(0,None),method='highs')
 if lp.success:minweighted=min(minweighted,lp.fun)
 checked+=1
 if gap>closest:
  closest=gap
  if gap>0 or trial<100:print('best scalar gap',trial,gap,'lambda',lam,'sections',len(caps)//2,'maxroots',maxroots,flush=True)
 if gap>1e-7 or (lp.success and lp.fun<gamma-1e-7):
  rec={'trial':trial,'seed_e':ei.tolist(),'lambda':lam.tolist(),'roots':roots,'caps':[{'f':f,'q':q.tolist(),'s':s}for f,q,s in caps],'scalar_gap':gap,'weighted':lp.fun if lp.success else None,'weights':lp.x.tolist()if lp.success else None}
  open('./tetrahedral-inverse-numerical-candidate.json','w').write(json.dumps(rec,indent=2));print('NUMERICAL CANDIDATE; exact certificate required',gap,'weighted',rec['weighted'],flush=True);break
 if trial%25==0:print('trial',trial,'closest',closest,'minweighted',minweighted,'maxroots',maxroots,flush=True)
else:print('finished',checked,'closest',closest,'minweighted',minweighted,'maxroots',maxroots,flush=True)
