"""Falsify balanced endpoint capacity s >= (2a-b)/4; numerical screen only."""
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import brentq
import json
rng=np.random.default_rng(452219)
def hull(v):
 v=np.asarray(v,float);return v[ConvexHull(v).vertices]
def area_centroid(v):
 if len(v)<3:return 0.,np.zeros(2)
 w=np.roll(v,-1,axis=0);cr=v[:,0]*w[:,1]-v[:,1]*w[:,0];a=cr.sum()/2
 if a<1e-15:return 0.,np.zeros(2)
 return a,((v+w)*cr[:,None]).sum(axis=0)/(6*a)
def norm(v):
 a,g=area_centroid(v);return (v-g)/np.sqrt(a)
def clip(v,n,c):
 out=[]
 for p,q in zip(v,np.roll(v,-1,axis=0)):
  fp=p@n-c;fq=q@n-c
  if fp>=0:out.append(p)
  if (fp>=0)!=(fq>=0):out.append(p+(q-p)*fp/(fp-fq))
 return np.array(out)
def balanced(v,n,t):
 # Original centroid is zero, tested threshold t>0; mean tested functional negative.
 lo=float(np.min(v@n));hi=float(np.max(v@n))
 if hi<=t:return 0.
 def moment(c):
  a,g=area_centroid(clip(v,n,c));return a*(g@n-t)
 c=brentq(moment,lo,t,xtol=1e-12)
 return area_centroid(clip(v,n,c))[0]
best=100.;accepted=0
for it in range(1000):
 A=norm(hull(rng.normal(size=(rng.integers(3,8),2))))
 C=norm(hull(A+rng.normal(size=A.shape)*rng.uniform(0,.3)))
 D=np.array([(p+q)/2 for p in A for q in C]);D=hull(D)
 a0,_=area_centroid(D)
 if a0>=2:continue
 extra=rng.normal(size=(rng.integers(1,4),2))*rng.uniform(.5,3)
 def body(t):return hull(np.r_[D,t*extra])
 target=rng.uniform(max(a0+1e-5,1.001),1.999)
 high=1.
 while area_centroid(body(high))[0]<target:high*=2
 scale=brentq(lambda s:area_centroid(body(s))[0]-target,0,high)
 K=body(scale);b,g=area_centroid(K);y=b*g/(b+2)
 accepted+=1
 for theta in np.linspace(0,2*np.pi,51,endpoint=False):
  n=np.array([np.cos(theta),np.sin(theta)]);t=float(y@n)
  if t<=1e-9:continue
  sA=balanced(A,n,t);sC=balanced(C,n,t);s=min(sA,sC);ratio=s/((2-b)/4)
  if ratio<best:
   best=ratio;data={'case':it,'ratio':ratio,'b':b,'sA':sA,'sC':sC,'A':A.tolist(),'K':K.tolist(),'C':C.tolist(),'normal':n.tolist(),'threshold':t,'centroid':y.tolist(),'accepted':accepted}
   print(json.dumps(data),flush=True)
   with open('./three-fiber-balanced-peeling-best.json','w') as f:json.dump(data,f,indent=2)
  if ratio<1-1e-7:break
 if best<1-1e-7:break
print('finished',accepted,best,flush=True)
