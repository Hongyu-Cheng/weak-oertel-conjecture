"""Numerical falsification only; not a proof or certificate."""
import numpy as np
from scipy.optimize import minimize
from pathlib import Path
import json

rng=np.random.default_rng(489047)
def cap(t):
    p=t[t>0];n=-t[t<0]
    if len(p)==1:
        a=p[0];de=np.prod(a+n);return a**3/de,3*a*a/de
    if len(n)==1:
        a=n[0];de=np.prod(a+p);return 1-a**3/de,3*a*a/de
    if len(p)==2:
        p,q=p;r,s=n
        al=p*s/((p+r)*(p+s)*(q+s));dl=q*r/((p+r)*(q+s)*(q+r))
        return p*(al+dl)+q*q/((q+s)*(q+r)),3*(al+dl)
    raise ValueError
def values(x):
    n=x[:9].reshape(3,3);n=np.vstack((n,-n.sum(axis=0)))
    aa=np.r_[0,x[9:]];bary=np.exp(aa-aa.max());bary/=bary.sum()
    signed=np.c_[np.zeros(4),n]-np.outer(n@bary[1:],np.ones(4))
    if np.min(abs(signed))<1e-12:return None
    qs=np.array([cap(t) for t in signed]);q,s=qs.T
    if min(q)<1e-14 or min(s)<1e-14:return None
    M=(q/s).sum();f=3*q**(2/3)/(s*M)
    phi=f+2*((sum(f)-f)/3)**1.5
    return phi,q,s,f,n,bary,signed
best=-1e9
for it in range(250):
    x=np.r_[rng.normal(size=9),rng.normal(size=3)*1.5]
    def fun(x):
        try:
            val=values(x)
            if val is None:return 1e3
            phi,q,*_=val
            # Insist on a genuinely mixed selected cut and a nontrivial cap band.
            signed=val[-1]
            penalty=100*(max(0,.05-q.min())+max(0,q.max()-.95))
            if (signed[0]>0).sum()!=2:penalty+=10
            return -phi[0]+penalty
        except Exception:return 1e3
    result=minimize(fun,x,method='Nelder-Mead',options={'maxiter':4500,'xatol':1e-10,'fatol':1e-12})
    val=values(result.x)
    if val is None:continue
    phi,q,s,f,n,bary,signed=val
    if fun(result.x)<-best:
        best=-fun(result.x)
        data=dict(iteration=it,phi=phi.tolist(),q=q.tolist(),s=s.tolist(),f=f.tolist(),normal=n.tolist(),bary=bary.tolist(),signed=signed.tolist(),parameters=result.x.tolist())
        Path('./tetrahedral_mixed_selected_best_slab_recovery.json').write_text(json.dumps(data,indent=2))
        print('BEST',it,best,'q',q,'phi',phi,flush=True)
    if max(phi)>3+1e-7:
        print('CANDIDATE',json.dumps(data),flush=True);break
