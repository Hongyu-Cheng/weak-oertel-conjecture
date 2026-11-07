"""Falsification screen only; no numerical theorem is asserted."""
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize_scalar
import json
rng=np.random.default_rng(92151)

def hull(p):
 p=np.array(p,dtype=float);return p[ConvexHull(p).vertices]
def area(p):
 q=np.roll(p,-1,axis=0);return np.sum(p[:,0]*q[:,1]-p[:,1]*q[:,0])/2

def centroid(p):
 q=np.roll(p,-1,axis=0);cross=p[:,0]*q[:,1]-p[:,1]*q[:,0]
 return np.sum((p+q)*cross[:,None],axis=0)/(6*area(p))
def norm(p):
 p=hull(p);return (p-centroid(p))/np.sqrt(area(p))
def clip(p,u,h):
 out=[]
 for a,b in zip(p,np.roll(p,-1,axis=0)):
  aa=a@u-h;bb=b@u-h
  if aa>=-1e-13:out.append(a)
  if aa*bb<0:out.append(a+aa/(aa-bb)*(b-a))
 return np.array(out)
def cap(p,u,h):
 pp=clip(p,u,h)
 return 0 if len(pp)<3 else area(pp)
def pair(A,B,u,h):
 cuts=sorted(set(np.r_[A@u-h,h-B@u]))
 def fun(t):return cap(A,u,h+t)+cap(B,u,h-t)
 best=min((fun(t),t) for t in cuts)
 for l,r in zip(cuts[:-1],cuts[1:]):
  if r-l<1e-10:continue
  md=(l+r)/2; f0,f1,f2=fun(l),fun(md),fun(r)
  aa=2*(f0+f2-2*f1);bb=f2-f0-aa
  if aa>1e-10:
   z=-bb/(2*aa)
   if 0<z<1:
    t=l+z*(r-l);best=min(best,(fun(t),t))
 return best

def val(A,B,K,c,ang):
 u=np.array([np.cos(ang),np.sin(ang)]);h=u@c
 f,t=pair(A,B,u,h)
 return cap(K,u,h)+f,t
best=(1e9,None)
for it in range(300):
 def gen():
  if rng.random()<.35:
   a=np.exp(rng.uniform(-1.4,1.4));p=np.array([[-a/2,-1/(2*a)],[a/2,-1/(2*a)],[a/2,1/(2*a)],[-a/2,1/(2*a)]])
   th=rng.uniform(0,2*np.pi);U=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]]);return p@U.T
  return norm(rng.normal(size=(rng.integers(3,9),2)))
 A,B=gen(),gen();M=hull([(a+b)/2 for a in A for b in B]);m=area(M)
 if m>=3:continue
 target=rng.uniform(max(m,1.6),3) if m<3 else m
 th=rng.uniform(0,2*np.pi);v=np.array([np.cos(th),np.sin(th)])
 lo,hi=0.,max(10.,10*target)
 for _ in range(50):
  mid=(lo+hi)/2;K=hull([*M,mid*v])
  if area(K)<target:lo=mid
  else:hi=mid
 K=hull([*M,hi*v]);k=area(K);c=(centroid(A)+centroid(B)+k*centroid(K))/(k+2)
 grid=np.linspace(0,2*np.pi,49)[:-1];vals=[val(A,B,K,c,th)[0] for th in grid]
 ix=np.argsort(vals)[:3];res=[]
 for j in ix:
  opt=minimize_scalar(lambda a:val(A,B,K,c,a)[0],bounds=(grid[j]-np.pi/24,grid[j]+np.pi/24),method='bounded',options={'xatol':1e-10})
  res.append((opt.fun,opt.x,*val(A,B,K,c,opt.x)[1:]))
 raw,theta,alpha=min(res);gap=raw-(k+1)/3
 if gap<best[0]:
  data={'it':it,'gap':gap,'raw':raw,'k':k,'m':m,'theta':theta,'alpha':alpha,'A':A.tolist(),'B':B.tolist(),'K':K.tolist(),'center':c.tolist()}
  best=(gap,data);print(json.dumps(data),flush=True)
  open('./screen_true_mixed_centroid_equal_endpoint_edge_two_sided_best.json','w').write(json.dumps(data,indent=2))
 if gap < -1e-4:break
