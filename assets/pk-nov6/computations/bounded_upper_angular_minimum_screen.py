"""Falsification screen only; any output requires a separate exact certificate."""
import numpy as np
import json

def cap_min(z,w,r,bounded=False):
    ids=z!=0
    breaks=np.r_[-r[ids]/z[ids],(w[ids]-r[ids])/z[ids]]
    if bounded:
        H=max(w)
        lower=max((H-r[z<0])/z[z<0]) if np.any(z<0) else -1e100
        upper=min((H-r[z>0])/z[z>0]) if np.any(z>0) else 1e100
        if lower>upper+1e-8:
            raise AssertionError((lower,upper))
        breaks=np.r_[lower,upper,breaks[(breaks>=lower)&(breaks<=upper)]]
    values=np.clip(r[None,:]+breaks[:,None]*z[None,:],0,w[None,:]).sum(axis=1)
    j=int(np.argmin(values))
    return float(values[j]),float(breaks[j])

def run(seed=673992, attempts=50000):
    rng=np.random.default_rng(seed)
    bestgap=0
    for trial in range(attempts):
        N=int(rng.integers(3,18))
        z=np.arange(N)-(N-1)//2
        curv=rng.integers(0,11,N-2)
        w=np.zeros(N)
        for j,k in enumerate(curv,1): w[j+1]=2*w[j]-w[j-1]-k
        w-=float(w@z/(z@z))*z
        e=np.ones(N)-float(z.sum()/(z@z))*z
        amount=max(-w/e)+float(rng.integers(1,20))
        w+=amount*e
        r=np.zeros(N)
        fractions=rng.choice([0,.25,.5,.75,1],N-2)
        for j,k in enumerate(curv,1):r[j+1]=2*r[j]-r[j-1]-k*fractions[j-1]
        r+=(w@w/2-w@r)/w.sum()
        assert min(w)>0 and abs(w@z)<1e-7*w.sum()
        results=[cap_min(z,w,r),cap_min(z,w,w-r)]
        constrained=[cap_min(z,w,r,True),cap_min(z,w,w-r,True)]
        glob=min(results)
        restricted=min(constrained)
        gap=(restricted[0]-glob[0])/w.sum()
        if gap>max(1e-8,bestgap):
            bestgap=gap
            out=dict(trial=trial,z=z.tolist(),w=w.tolist(),r=r.tolist(),global_results=results,bounded_results=constrained,gap=gap,curv=curv.tolist(),fractions=fractions.tolist())
            print(json.dumps(out),flush=True)
            with open('./bounded_upper_angular_minimum_counter.json','w') as f:json.dump(out,f,indent=2)
            if gap>1e-6:return out
    print('NO COUNTEREXAMPLE in',attempts,'samples')

if __name__=='__main__':run()
