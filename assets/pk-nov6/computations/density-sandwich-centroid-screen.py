"""Falsification only: bounded-density centroid/cap candidate."""
import numpy as np
from scipy.optimize import minimize_scalar

N=10000
x=(np.arange(N)+.5)/N

def score(c,f,gamma,details=False):
    t=x-c
    pos=t>=0
    mean=np.dot(f,x)
    target=(c-mean)/2
    baseline=np.dot(f[~pos],t[~pos])
    need=target-baseline
    moments=f*np.abs(t)
    if need < -1e-10 or need > moments.sum()+1e-10:
        return 1e3
    costs=np.where(pos,1-gamma,gamma)*f
    order=np.argsort(np.divide(costs,moments,out=np.full(N,np.inf),where=moments>0))
    cum=np.cumsum(moments[order])
    k=np.searchsorted(cum,need)
    obj=f[pos].sum()-gamma/2-gamma*f[~pos].sum()
    if k:
        obj+=costs[order[:k]].sum()
        need-=cum[k-1]
    if k<N:
        obj+=need*costs[order[k]]/moments[order[k]]
    if details:
        return obj,mean,c,k
    return obj

for d in [1,2,3,5,10,30,100]:
    gamma=(d/(d+1))**d
    profiles=[("cone+",x**(d-1)),("cone-",(1-x)**(d-1)),("uniform",np.ones(N))]
    if d>1:
        for a in [.05,.2,.5,.8,.95]:
            profiles.append(("tent%.2f"%a,np.minimum(x/a,(1-x)/(1-a))**(d-1)))
    for name,f in profiles:
        f=f/f.sum()
        grid=np.linspace(.001,.999,101)
        vals=np.array([score(c,f,gamma) for c in grid])
        i=vals.argmin()
        res=minimize_scalar(lambda c:score(c,f,gamma),bounds=(grid[max(0,i-1)],grid[min(100,i+1)]),method="bounded")
        print(d,name,score(res.x,f,gamma,True),flush=True)
