from fractions import Fraction as F
import random
import numpy as np
from scipy.optimize import differential_evolution, minimize_scalar
random.seed(198723)
def cap(r,t,a):
    if t<=0:return r*r
    if t>=a*r:return 0.
    if a==1:return (r-t)**2
    if t<=(1-a)*r:return r*r-t*t/(a*(1-a))
    return (a*r-t)**2/(a*(2*a-1))
def obj(v,rs,j):
    a,b=v
    return sum(cap(r,rs[j]/3-b*(i-j),a) for i,r in enumerate(rs))
best=None
for trial in range(250):
    N=random.randint(3,9)
    slopes=sorted([random.randrange(-20,21)/20 for _ in range(N-1)],reverse=True)
    raw=[0.]
    for s in slopes:raw.append(raw[-1]+s)
    rs=np.array(raw)+random.choice([.2,.5,1.,2.])-min(raw)
    for j in range(N):
        opt=differential_evolution(lambda v:obj(v,rs,j),[(.5,1.),(-4*max(rs),4*max(rs))],tol=1e-8,popsize=9,seed=trial,polish=True)
        if .501<opt.x[0]<.999:
            ends=[]
            for a in [.5,1.]:
                e=differential_evolution(lambda b:obj([a,b[0]],rs,j),[(-4*max(rs),4*max(rs))],tol=1e-10,popsize=12,seed=trial)
                ends.append(e.fun)
            gap=min(ends)-opt.fun
            if gap>1e-5:
                print('COUNTER',trial,'r',rs.tolist(),'j',j,'ab',opt.x.tolist(),'cost',opt.fun,'end',ends,'gap',gap,flush=True)
                raise SystemExit
print('no strict nonvertex minimizer found')
