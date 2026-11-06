"""Falsification screen using simplex divided differences; no proof claim."""
import numpy as np
import json
from pathlib import Path
rng=np.random.default_rng(65155)
for d in [4,5,6,8]:
    best=-1
    for it in range(120000):
        n=rng.normal(size=(d,d));n*=np.exp(rng.normal(size=(d,1)))
        n=np.vstack((n,-n.sum(axis=0)))
        ba=rng.dirichlet(np.ones(d+1)*rng.uniform(.15,3));y=ba[1:]
        t=np.c_[np.zeros(d+1),n]-np.outer(n@y,np.ones(d+1))
        dif=t[:,:,None]-t[:,None,:]
        ii=np.arange(d+1);dif[:,ii,ii]=1
        if abs(dif).min()<1e-5:continue
        den=np.prod(dif,axis=2);pos=np.maximum(t,0)
        Q=np.sum(pos**d/den,axis=1);S=d*np.sum(pos**(d-1)/den,axis=1)
        if Q.min()<1e-7 or Q.max()>1-1e-7 or S.min()<1e-9:continue
        M=np.sum(Q/S);f=d*Q**((d-1)/d)/(S*M)
        phi=f+(d-1)*((sum(f)-f)/d)**(d/(d-1))
        mx=max(phi)
        if mx>best:
            best=mx
            data=dict(d=d,iteration=it,normal=n.tolist(),bary=ba.tolist(),q=Q.tolist(),s=S.tolist(),f=f.tolist(),phi=phi.tolist(),signed=t.tolist())
            Path(f'./simplex_general_circuit_d{d}_best_slab_recovery.json').write_text(json.dumps(data,indent=2))
        if mx>d+1e-5:
            print('CANDIDATE',json.dumps(data),flush=True);break
    print('DONE',d,'max phi',best,flush=True)
