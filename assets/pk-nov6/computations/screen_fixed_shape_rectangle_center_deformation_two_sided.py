import numpy as np
from scipy.optimize import minimize_scalar
from random import Random
rng=Random(220677)
RHOS=[0,.08,.2,.5,1,2,5,15]

def masses(c,w,k,x,al,rho,der=0):
    dz=np.arange(len(c))-k
    m=c[None,:]-x+al[:,None]*dz[None,:]
    q=np.stack((m+(w+rho)/2,m+(rho-w)/2,m+(w-rho)/2,m-(w+rho)/2),axis=-1)
    signs=np.array([1,-1,-1,1])
    if der==0: v=(np.maximum(0,q)**2@signs)/(2*rho)
    elif der==1:v=(np.maximum(0,q)@signs)/rho*dz[None,:]
    else:v=((q>0)@signs)/rho*dz[None,:]**2
    return v.sum(axis=1)

def qpoint(c,w,k,x):
    dz=np.arange(len(c))-k;idx=np.flatnonzero(dz);M=w.sum()
    best=M/2
    # Pure horizontal continuous normal = interval source.
    al=((x-c[idx,None]+np.stack((-w[idx]/2,w[idx]/2),axis=1))/dz[idx,None]).reshape(-1)
    mm=(np.clip(w[None,:]/2+c[None,:]-x+al[:,None]*dz[None,:],0,w[None,:])).sum(axis=1)
    left=w[:k].sum();right=w[k+1:].sum();own=w[k]/2+c[k]-x
    mm=np.r_[mm,left+own,right+own]
    best=min(best,mm.min(),M-mm.max())
    for rho in RHOS[1:]:
        ends=np.array([-(w[idx]+rho)/2,-(w[idx]-rho)/2,(w[idx]-rho)/2,(w[idx]+rho)/2]).T
        al=np.unique(((ends-c[idx,None]+x)/dz[idx,None]).reshape(-1))
        mids=(al[:-1]+al[1:])/2
        second=masses(c,w,k,x,mids,rho,2)
        first=masses(c,w,k,x,mids,rho,1)
        valid=np.abs(second)>1e-9
        star=mids[valid]-first[valid]/second[valid]
        star=star[(star>al[:-1][valid])&(star<al[1:][valid])]
        al=np.r_[al,star]
        mm=masses(c,w,k,x,al,rho)
        best=min(best,mm.min(),M-mm.max())
    # u_x=0: finite weighted uniform intervals at common center.
    alpha=np.unique(np.r_[-.5/dz[idx],.5/dz[idx]])
    mm=(w[None,:]*np.clip(.5+alpha[:,None]*dz[None,:],0,1)).sum(axis=1)
    return min(best,mm.min(),M-mm.max())

def maximum(c,w):
    best=(-1,None,None)
    for k in range(len(c)):
        r=minimize_scalar(lambda x:-qpoint(c,w,k,x),bounds=(c[k]-w[k]/2,c[k]+w[k]/2),method='bounded',options={'xatol':2e-7})
        if -r.fun>best[0]:best=(-r.fun,k,r.x)
    return best

for it in range(100):
    N=rng.randrange(4,7)
    ls=sorted(rng.randrange(-15,16) for _ in range(N-1))
    us=sorted((rng.randrange(-15,16) for _ in range(N-1)),reverse=True)
    lo=np.r_[0,np.cumsum(ls)].astype(float)
    hi=np.r_[0,np.cumsum(us)].astype(float)
    hi+=max(lo-hi)+rng.randrange(1,15)
    w=hi-lo;c=(lo+hi)/2
    scale=w.mean();wn=w/scale;cn=c/scale
    times=[0,.25,.5,.75,1]
    vals=[maximum(t*cn,wn) for t in times]
    if any(vals[j+1][0]>vals[j][0]+2e-5 for j in range(4)):
        print('HIT',it,'lo',lo.tolist(),'hi',hi.tolist(),'values',vals,flush=True)
        break
    if it%10==0:print('checked',it,flush=True)
else:print('No nonmonotonicity in bounded rectangle screen',flush=True)
