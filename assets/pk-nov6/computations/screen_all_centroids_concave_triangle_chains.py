import numpy as np
from scipy.optimize import minimize_scalar
from math import inf
import random
random.seed(93574)
def tail(r,t,a):
    r=np.asarray(r); t=np.asarray(t)
    if a>.999999999:
        return np.minimum(r,np.maximum(r-t,0))**2
    if a<.5000000001:
        return np.where(t<=0,r*r,np.maximum(r*r-4*t*t,0))
    return np.where(t<=0,r*r,np.where(t<=(1-a)*r,r*r-t*t/(a*(1-a)),np.maximum(a*r-t,0)**2/(a*(2*a-1))))
def tiltopt(rs,j,a):
    n=len(rs); q=rs[j]/3; dd=np.arange(n)-j
    breaks=[0.]
    for i,r in enumerate(rs):
        if i==j:continue
        breaks.extend([(q-x*r)/(i-j) for x in [0,1-a,a]])
    breaks=sorted(set(breaks)); xx=breaks.copy()
    for l,r in zip(breaks,breaks[1:]):
        c=(l+r)/2; h=(r-l)/4
        f0=sum(tail(rs,q-c*dd,a)); fm=sum(tail(rs,q-(c-h)*dd,a)); fp=sum(tail(rs,q-(c+h)*dd,a))
        A=(fp+fm-2*f0)/(2*h*h); B=(fp-fm)/(2*h)
        if A>1e-9:
            x=c-B/(2*A)
            if l<x<r:xx.append(x)
    vals=[sum(tail(rs,q-x*dd,a)) for x in xx]; k=int(np.argmin(vals));return vals[k],xx[k]
best=(1,None)
for trial in range(2000):
    n=random.randint(4,13)
    # concave positive radius, normalized maximum one
    slopes=sorted([random.uniform(-1,1) for _ in range(n-1)],reverse=True)
    raw=np.array([0]+list(np.cumsum(slopes)))
    rs=raw-min(raw)+10**random.uniform(-2,0.5)
    rs/=max(rs)
    if max(rs**2)>=sum(rs**2)/2:continue
    vals=[]; pars=[]
    for j in range(n):
        opts=[(tiltopt(rs,j,a)[0],a,tiltopt(rs,j,a)[1]) for a in np.linspace(.5,1,17)]
        v,a,b=min(opts)
        vals.append(v); pars.append([a,b])
    ratio=max(vals)/sum(rs**2)
    if ratio<best[0]:
        best=(ratio,rs.copy());print(trial,'best',ratio,'r',rs.tolist(),'vals',vals,'pars',pars,flush=True)
    if ratio<2/9-1e-5:
        print('FOUND',flush=True);break
