"""Falsification only: convex interval projection and affine nonnegative roof.
The resulting 3D convex body has planar trapezoid fibers and exact linear
integer-centroid constraint before floating-point evaluation. No theorem
is inferred from failure to find a counterexample.
"""
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize_scalar
import json
rng=np.random.default_rng(8347271)

def hull(p):
 p=np.asarray(p,float);return p[ConvexHull(p).vertices]
def moments(p):
 q=np.roll(p,-1,axis=0);c=p[:,0]*q[:,1]-p[:,1]*q[:,0];a=c.sum()/2
 return a,((p+q)*c[:,None]).sum(axis=0)/(6*a)
def tail(p,n,t):
 t=np.asarray(t,float);out=np.zeros_like(t)
 for j in range(1,len(p)-1):
  tri=p[[0,j,j+1]];a=abs(np.linalg.det(np.stack((tri[1]-tri[0],tri[2]-tri[0]))))/2
  v=np.sort(tri@n);v0,v1,v2=v
  if v2-v0<1e-12:out+=a*(t<=v0);continue
  f=np.ones_like(t);f=np.where(t>=v2,0.,f)
  if v1>v0+1e-12:f=np.where((t>v0)&(t<v1),1-(t-v0)**2/((v1-v0)*(v2-v0)),f)
  if v2>v1+1e-12:f=np.where((t>=v1)&(t<v2),(v2-t)**2/((v2-v0)*(v2-v1)),f)
  out+=a*f
 return out

def intervals(P):
 out=[]
 for z in range(int(np.ceil(P[:,0].min())),int(np.floor(P[:,0].max()))+1):
  hits=[]
  for p,q in zip(P,np.roll(P,-1,axis=0)):
   if abs(p[0]-z)<1e-10:hits.append(p[1])
   if (p[0]-z)*(q[0]-z)<0:hits.append(p[1]+(q[1]-p[1])*(z-p[0])/(q[0]-p[0]))
  if len(hits)>1 and max(hits)-min(hits)>1e-10:out.append((z,min(hits),max(hits)))
 return np.array(out)

def direction(K,z,y,theta):
 n=np.array([np.cos(theta),np.sin(theta)]);t=n@y
 breaks=np.unique(np.concatenate([(t-p@n)/zz for zz,p in zip(z,K) if zz]))
 def value(v):return sum(tail(p,n,t-v*zz) for zz,p in zip(z,K))
 if len(breaks)<2:return float(value(0)),0.
 L,R=breaks[:-1],breaks[1:];mid=(L+R)/2
 fl,fr,fm=value(L),value(R),value(mid)
 q=2*(fl+fr-2*fm)/(R-L)**2;slope=(fr-fl)/(R-L)
 with np.errstate(divide='ignore',invalid='ignore'):v=mid-slope/(2*q)
 ok=(q>1e-9)&(v>L)&(v<R)
 vals=np.r_[breaks,v[ok],breaks[0]-1,breaks[-1]+1];scores=value(vals);j=np.argmin(scores)
 return float(scores[j]),float(vals[j])

best=1.;count=0
for case in range(1600):
 N=int(rng.integers(3,12));p=np.column_stack((rng.uniform(0,N,size=12),rng.normal(size=12)))
 p[0,0]=0;p[1,0]=N;P=hull(p);rows=intervals(P)
 z,l,u=rows.T;w=u-l;m1=(u*u-l*l)/2
 for k in range(1,N):
  D=np.sum((z-k)*z*w)
  if abs(D)<1e-10:continue
  b0=-np.sum((z-k)*w)/D;bc=-np.sum((z-k)*m1)/D
  lo,hi=-100.,100.
  for zz,tt in P:
   intercept=1+b0*zz;coef=bc*zz+tt
   if abs(coef)<1e-12:
    if intercept<0:lo,hi=1,0;break
   elif coef>0:lo=max(lo,-intercept/coef)
   else:hi=min(hi,-intercept/coef)
  if hi<=lo+1e-9:continue
  for fraction in [.001,.15,.5,.85,.999]:
   c=lo+(hi-lo)*fraction;b=b0+bc*c
   K=[np.array([[ll,0],[uu,0],[uu,1+b*zz+c*uu],[ll,1+b*zz+c*ll]]) for zz,ll,uu in rows]
   ag=[moments(p) for p in K];a=np.array([v[0] for v in ag]);g=np.array([v[1] for v in ag]);M=a.sum();y=(a[:,None]*g).sum(axis=0)/M
   if abs(np.dot(a,z-k))>1e-7*max(1,M):raise RuntimeError('centroid condition')
   th=np.linspace(0,2*np.pi,25,endpoint=False)+.00123
   vals=np.array([direction(K,z-k,y,t)[0] for t in th]);i=np.argmin(vals)
   opt=minimize_scalar(lambda t:direction(K,z-k,y,t)[0],bounds=(th[i]-.28,th[i]+.28),method='bounded')
   val=opt.fun/M;count+=1
   if val<best:
    best=val;info={'case':case,'tests':count,'fraction':fraction,'bound':val,'k':k,'P':P.tolist(),'rows':rows.tolist(),'roof':[1.,b,c],'masses':a.tolist(),'centroid':y.tolist(),'theta':float(opt.x),'cut':direction(K,z-k,y,opt.x),'M':M}
    print(json.dumps(info),flush=True)
    with open('./conditional-centroid-affine-roof-best.json','w') as f:json.dump(info,f,indent=2)
   if best<2/9-1e-7:raise SystemExit
 if count>1500:break
print('finished',count,'best',best,flush=True)
