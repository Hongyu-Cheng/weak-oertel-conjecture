"""Falsification screen only: three positive planar fibers, equal endpoint areas.
Every tested family is genuinely compatible; no theorem is inferred from a miss.
"""
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize_scalar
import json

rng=np.random.default_rng(918371)

def hull(v):
    v=np.asarray(v,float)
    return v[ConvexHull(v).vertices]
def area_centroid(v):
    w=np.roll(v,-1,axis=0); cross=v[:,0]*w[:,1]-v[:,1]*w[:,0]
    area=cross.sum()/2
    return area,((v+w)*cross[:,None]).sum(axis=0)/(6*area)
def normalize(v):
    a,g=area_centroid(v)
    return (v-g)/np.sqrt(a)
def tail(v,n,t):
    """Area above a projection threshold, exact polynomial formula per fan triangle."""
    total=np.zeros_like(np.asarray(t,float))
    for i in range(1,len(v)-1):
        tri=v[[0,i,i+1]]
        a=abs(np.linalg.det(np.stack([tri[1]-tri[0],tri[2]-tri[0]])))/2
        p=np.sort(tri@n); x=np.asarray(t,float)
        if p[2]-p[0]<1e-14:
            total+=a*(x<=p[0]);continue
        q=np.ones_like(x)
        q=np.where(x>=p[2],0,q)
        if p[1]>p[0]+1e-14:
            q=np.where((x>p[0])&(x<p[1]),1-(x-p[0])**2/((p[1]-p[0])*(p[2]-p[0])),q)
        if p[2]>p[1]+1e-14:
            q=np.where((x>=p[1])&(x<p[2]),(p[2]-x)**2/((p[2]-p[0])*(p[2]-p[1])),q)
        total+=a*q
    return total

def eval_dir(A,K,B,y,theta,details=False):
    n=np.array([np.cos(theta),np.sin(theta)]);t=n@y
    cuts=np.unique(np.r_[A@n-t,t-B@n]);l=cuts[:-1];r=cuts[1:];m=(l+r)/2
    def f(a):return tail(A,n,t+a)+tail(B,n,t-a)
    fl=f(l);fr=f(r);fm=f(m)
    q=2*(fl+fr-2*fm)/(r-l)**2
    lin=(fr-fl)/(r-l)
    with np.errstate(divide='ignore',invalid='ignore'):
        v=m-lin/(2*q)
    good=(q>1e-10)&(v>l)&(v<r)
    candidates=np.r_[cuts,v[good],cuts[0]-1,cuts[-1]+1]
    vals=f(candidates);j=np.argmin(vals)
    out=float(tail(K,n,t)+vals[j])
    return (out,float(candidates[j]),n.tolist()) if details else out

best=1.
for case in range(400):
    def end():
        v=hull(rng.normal(size=(rng.integers(3,8),2)))
        v=normalize(v)
        s=np.exp(rng.uniform(-1.5,1.5)); ang=rng.uniform(0,6.28)
        Q=np.array([[np.cos(ang),-np.sin(ang)],[np.sin(ang),np.cos(ang)]])
        return v@np.diag([s,1/s])@Q
    A=end();B=end();D=np.array([(a+b)/2 for a in A for b in B])
    scale=np.max(np.linalg.norm(D,axis=1))
    extra=rng.normal(size=(rng.integers(1,5),2))*scale*np.exp(rng.uniform(-2,1.8))
    K=hull(np.r_[D,extra]);k,g=area_centroid(K);y=k*g/(k+2);M=k+2
    theta=np.linspace(0,2*np.pi,61,endpoint=False)+.000231
    vals=np.array([eval_dir(A,K,B,y,t) for t in theta]);i=np.argmin(vals)
    opt=minimize_scalar(lambda t:eval_dir(A,K,B,y,t),bounds=(theta[i]-.12,theta[i]+.12),method='bounded')
    val=opt.fun/M
    if val<best:
        best=val; info={'case':case,'depth_upper':best,'A':A.tolist(),'K':K.tolist(),'B':B.tolist(),'y':y.tolist(),'theta':float(opt.x),'cut':eval_dir(A,K,B,y,opt.x,True),'mass':M}
        print(json.dumps(info),flush=True)
        with open('./conditional-centroid-three-fiber-screen-best.json','w') as f:json.dump(info,f,indent=2)
    if best<2/9-1e-7:break
print('finished best',best,flush=True)
