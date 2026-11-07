"""Locate candidate violations only; all final claims need exact certificates."""
import numpy as np
from pathlib import Path
import json

rng=np.random.default_rng(944971)

def caps(t):
    p=t[t>0]; n=-t[t<0]
    if len(p)==1:
        a=p[0]; den=np.prod(a+n)
        return a**3/den,3*a*a/den
    if len(n)==1:
        a=n[0]; den=np.prod(a+p)
        return 1-a**3/den,3*a*a/den
    if len(p)==2 and len(n)==2:
        p,q=p;r,s=n
        al=p*s/((p+r)*(p+s)*(q+s))
        de=q*r/((p+r)*(q+s)*(q+r))
        return p*(al+de)+q*q/((q+s)*(q+r)),3*(al+de)
    raise ValueError(t)

def calc(n,y):
    signed=np.concatenate((np.zeros((4,1)),n),axis=1)-np.outer(n@y,np.ones(4))
    if abs(signed).min()<1e-10:return None
    qs=np.array([caps(t) for t in signed])
    q,s=qs.T
    M=(q/s).sum(); f=3*q**(2/3)/(s*M)
    ph=f+2*((f.sum()-f)/3)**1.5
    return ph,q,s,f,signed

best=-np.inf
for it in range(300000):
    raw=rng.integers(-12,13,size=(3,3))
    if abs(np.linalg.det(raw))<.1:continue
    normals=np.vstack((raw,-raw.sum(axis=0)))
    # Exact small rational source in a broad interior range.
    bary=rng.integers(1,31,size=4)
    y=bary[1:]/bary.sum()
    val=calc(normals,y)
    if val is None:continue
    ph,q,s,f,t=val
    mx=ph.max()
    if mx>best:
        best=mx
        data=dict(iteration=it,normal=normals.tolist(),bary=bary.tolist(),q=q.tolist(),s=s.tolist(),f=f.tolist(),phi=ph.tolist(),signed=t.tolist())
        Path('./tetrahedral_general_circuit_best_slab_recovery.json').write_text(json.dumps(data,indent=2))
    if mx>3+1e-7:
        print('CANDIDATE',json.dumps(data),flush=True);break
    if it%10000==0:print(it,best,flush=True)
else:print('NO COUNTEREXAMPLE FOUND; best',best,flush=True)
