import numpy as np
from scipy.optimize import minimize

def upper(r,l,u,q):
    A=np.c_[np.ones(len(r)),r]
    target=np.r_[q,np.zeros(r.shape[1])]
    def objective(tv):
        cut=A@tv; m=np.clip(u-cut,0,u-l)
        val=np.dot(target,tv)+np.sum((np.maximum(u-cut,0)**2-np.maximum(l-cut,0)**2)/2)
        grad=target-A.T@m
        return val,grad
    ans=minimize(objective,np.r_[np.mean((l+u)/2),np.zeros(r.shape[1])],jac=True,method='BFGS',options={'gtol':1e-9,'maxiter':500})
    cut=np.clip(A@ans.x,l,u); m=u-cut
    if np.max(np.abs(A.T@m-target))>1e-5:return None
    return np.sum((u*u-cut*cut)/2)/q,ans.x,m

def depth(r,l,u,x):
    aa=[np.zeros(2)]
    N=len(r)
    for i in range(N):
        for j in range(i):
            A=r[[i,j]]
            if abs(np.linalg.det(A))<.01:continue
            for vi in [l[i],u[i]]:
                for vj in [l[j],u[j]]:aa.append(np.linalg.solve(A,[vi-x,vj-x]))
    aa=np.asarray(aa)
    downs=np.sum(np.clip(x+np.einsum('ij,kj->ik',aa,r)-l,0,u-l),axis=1)
    ups=np.sum(u-l)-downs
    if min(downs)<min(ups): idx=np.argmin(downs); return downs[idx],aa[idx],'down'
    idx=np.argmin(ups);return ups[idx],aa[idx],'up'

def projectiondepth(r,w):
    ang=[]
    for rr in r:
        if np.any(rr):ang.extend([np.arctan2(rr[1],rr[0])+np.pi/2,np.arctan2(rr[1],rr[0])+3*np.pi/2])
    ang=np.unique(np.mod(ang,2*np.pi));m=sum(w)
    for i,a in enumerate(ang):
        b=ang[(i+1)%len(ang)]+(2*np.pi if i+1==len(ang) else 0)
        v=np.array([np.cos((a+b)/2),np.sin((a+b)/2)])
        m=min(m,sum(w[r@v>=-1e-8]))
    return m

rng=np.random.default_rng(1877)
best=1
for it in range(10000):
    N=int(rng.integers(2,5));z=np.asarray([(i,j) for i in range(N) for j in range(N)],float)
    A=rng.integers(-15,16,(int(rng.integers(2,9)),3));B=rng.integers(-15,16,(int(rng.integers(2,9)),3))
    zz=np.c_[np.ones(len(z)),z]
    l=np.max(zz@A.T,axis=1);u=np.min(zz@B.T,axis=1)
    u=u-min(u-l)+int(rng.integers(0,25))
    M=sum(u-l);q=M/4
    for j in z:
        r=z-j
        if projectiondepth(r,u-l)<q-1e-8:continue
        aa=upper(r,l,u,q);bb=upper(r,-u,-l,q)
        if aa is None or bb is None:continue
        x=(aa[0]-bb[0])/2
        dd=depth(r,l,u,x);rat=dd[0]/M
        if rat<best:
            best=rat
            print('best',it,rat,'z',z.tolist(),'l',l.tolist(),'u',u.tolist(),'j',j.tolist(),'x',x,'depth',dd,'upper',aa,'minuslower',bb,flush=True)
        if rat<.125-1e-8:raise SystemExit
