import numpy as np
from scipy.optimize import differential_evolution, minimize
from fractions import Fraction as F
h=20/97
t=100/291
delta=2*t*(1-2*t)

def clipped_area(poly, n, c):
    oldp=poly[-1]; old=oldp@n-c; out=[]
    for p in poly:
        new=p@n-c
        if (old>=0)!=(new>=0): out.append(oldp+old/(old-new)*(p-oldp))
        if new>=0: out.append(p)
        oldp=p; old=new
    if len(out)<3:return 0.
    a=np.array(out)
    return abs(np.sum(a[:,0]*np.roll(a[:,1],-1)-a[:,1]*np.roll(a[:,0],-1)))/2

def poly(r):return np.array([[h,0],[r,0],[0,r],[0,h]])

def objective(v,eps):
    th,alpha=v
    n=np.array([np.cos(th),np.sin(th)])
    c=t*n.sum()
    return sum(clipped_area(poly(1+eps*z),n,c-alpha*z) for z in [-1,0,1])
for eps in [0,.001,.01,.05,.1,.2]:
    r=differential_evolution(lambda v: objective(v,eps),[(0,2*np.pi),(-2,2)],tol=1e-11,popsize=20,maxiter=400,seed=13)
    print('eps',eps,'min',r.fun,'3delta',3*delta,'difference',r.fun-3*delta,'theta,alpha',r.x,flush=True)
