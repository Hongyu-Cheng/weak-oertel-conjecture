"""Numerical falsification search only; exact certificates must follow."""
import numpy as np
import json


def capacity(z0, x, l, u, upward=True):
    z = np.arange(len(l), dtype=float)
    r = z-z0
    mid = (l+u)/2
    lo, hi = (mid, u) if upward else (l, mid)
    A = hi-lo
    others = r != 0
    slopes = np.concatenate(((lo[others]-x)/r[others],
                             (hi[others]-x)/r[others]))
    thresholds = x+slopes[:, None]*r
    masses = np.clip(hi-thresholds, 0, A) if upward else np.clip(thresholds-lo, 0, A)
    vals = list(masses.sum(axis=1))
    own = np.clip(hi[z0]-x, 0, A[z0]) if upward else np.clip(x-lo[z0], 0, A[z0])
    vals += [A[:z0].sum()+own, A[z0+1:].sum()+own]
    idx = int(np.argmin(vals))
    return vals[idx], float(slopes[idx]) if idx < len(slopes) else ('minus' if idx==len(slopes) else 'plus')


def screen(l, u):
    l=np.array(l, dtype=float); u=np.array(u, dtype=float)
    A=(u-l)/2
    T=A.sum()/2
    medians=[j for j in range(len(l)) if A[:j+1].sum()>=T and A[j:].sum()>=T]
    results=[]
    for j in medians:
        lo,hi=l[j],u[j]
        for _ in range(48):
            x=(lo+hi)/2
            if capacity(j,x,l,u,True)[0]>=T: lo=x
            else: hi=x
        upper=(lo+hi)/2
        lo,hi=l[j],u[j]
        for _ in range(48):
            x=(lo+hi)/2
            if capacity(j,x,l,u,False)[0]>=T: hi=x
            else: lo=x
        lower=(lo+hi)/2
        results.append((j,lower,upper))
    return T,results


if __name__=='__main__':
    rng=np.random.default_rng(872901)
    tested=0
    for m in range(3,11):
        for _ in range(1200):
            ls=np.sort(rng.integers(-20,21,size=m-1))
            us=-np.sort(rng.integers(-20,21,size=m-1))
            l=np.r_[0,np.cumsum(ls)]
            u=np.r_[0,np.cumsum(us)]
            u=u+int(max(l-u))+int(rng.integers(1,21))
            T,res=screen(l,u)
            tested+=1
            if all(a>b+1e-7 for _,a,b in res):
                record={'l':l.tolist(),'u':u.tolist(),'target':T,'median_bounds':res,'tested':tested}
                print(json.dumps(record),flush=True)
                with open('./own_interval_capacity_candidate.json','w') as f:json.dump(record,f,indent=2)
                raise SystemExit
        print(json.dumps({'m':m,'tested':tested,'status':'no counterexample'}),flush=True)
