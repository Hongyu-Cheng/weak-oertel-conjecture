"""Exploration only; conclusions require a separate exact certificate."""
import random, bisect, math, json

def iid_tail(d,coeffs,N=1000):
    dx=1/N; xs=[(i+.5)*dx for i in range(N)]
    hs=[sum(c*(1-x if t==0 else x if t==1 else min(x/t,(1-x)/(1-t))) for t,c in coeffs) for x in xs]
    fs=[h**(d-1) for h in hs]; z=sum(fs); fs=[f/z for f in fs]
    m=sum(x*f for x,f in zip(xs,fs))
    cdf=[0]
    for f in fs:cdf.append(cdf[-1]+f)
    def F(t):
        if t<=0:return 0
        if t>=1:return 1
        u=t/dx;i=int(u)
        return cdf[i]+(u-i)*fs[i]
    return sum(f*(1-F(2*m-x)) for x,f in zip(xs,fs))

random.seed(209)
for d in [2,3,4,5,10,30]:
    best=(iid_tail(d,[(0,1)]),[(0,1)])
    for iteration in range(1500):
        coeffs=[(0,10**random.uniform(-3,1)),(1,10**random.uniform(-3,1))]
        coeffs.extend((random.random(),10**random.uniform(-3,1)) for _ in range(random.randint(0,5)))
        p=iid_tail(d,coeffs,500)
        p=min(p,1-p)
        if p<best[0]:best=(p,coeffs)
    print(d,best,'gamma',(d/(d+1))**d,flush=True)
