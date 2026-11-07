import numpy as np
from scipy.optimize import minimize_scalar
from random import Random
rng=Random(71355)

def qpoint(lo,hi,k,x):
    N=len(lo);z=np.arange(N);M=np.sum(hi-lo)
    den=z-k;idx=np.flatnonzero(den)
    slopes=((np.stack((lo[idx],hi[idx]),axis=1)-x)/den[idx,None]).reshape(-1)
    cuts=x+slopes[:,None]*den[None,:]
    masses=np.clip(hi[None,:]-cuts,0,(hi-lo)[None,:]).sum(axis=1)
    left=np.sum((hi-lo)[:k]);right=np.sum((hi-lo)[k+1:]);own=hi[k]-x
    masses=np.r_[masses,left+own,right+own]
    return min(masses.min(),M-masses.max())

def maximum(lo,hi):
    best=(-1,None,None)
    for k in range(len(lo)):
        r=minimize_scalar(lambda x:-qpoint(lo,hi,k,x),bounds=(lo[k],hi[k]),method='bounded',options={'xatol':1e-9})
        if -r.fun>best[0]:best=(-r.fun,k,r.x)
    return best

for it in range(1200):
    N=rng.randrange(4,8)
    ls=sorted(rng.randrange(-15,16) for _ in range(N-1))
    us=sorted((rng.randrange(-15,16) for _ in range(N-1)),reverse=True)
    lo=np.r_[0,np.cumsum(ls)].astype(float)
    hi=np.r_[0,np.cumsum(us)].astype(float)
    hi+=max(lo-hi)+rng.randrange(1,15)
    centers=(lo+hi)/2;rad=(hi-lo)/2
    times=[0,.25,.5,.75,1]
    vals=[maximum(t*centers-rad,t*centers+rad) for t in times]
    if any(vals[j+1][0]>vals[j][0]+1e-6 for j in range(4)):
        print('HIT',it,'lo',lo.tolist(),'hi',hi.tolist(),'values',vals,flush=True)
        break
else:print('No nonmonotonicity in bounded screen',flush=True)
