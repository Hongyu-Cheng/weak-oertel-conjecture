"""Exploratory screen only; exact polygon functional once a candidate is found."""
import numpy as np
from scipy.optimize import minimize
from simplex_overlap_convex_functional_search import clip,area
Y=np.linspace(0,1,13)
D=[np.array(p,float) for p in [(1,0),(2,0),(1,1)]]
def value(w):
    P=[np.array([0.,0.])]+[np.array([x,y]) for x,y in zip(w,Y)]+[np.array([0.,1.])]
    R=P
    for n,b in [(np.array([1.,0.]),1.),(np.array([0.,1.]),0.),(np.array([-1.,-1.]),-2.)]:R=clip(R,n,b)
    return area(P)-3*area(R)
def cons(w):return np.diff(w)[:-1]-np.diff(w)[1:]
rng=np.random.default_rng(247)
best=(-1,None)
for i in range(100):
    p=rng.uniform(0,1);q=rng.uniform(0,1)
    init=(1-p)*(np.ones(len(Y))*q)+(p)*(3-Y)
    result=minimize(lambda w:-value(w),init,bounds=[(0,3-y) for y in Y],constraints={'type':'ineq','fun':cons},method='SLSQP',options={'maxiter':1000,'ftol':1e-10})
    if result.success and -result.fun>best[0]:
        best=(-result.fun,result.x);print(i,best,flush=True)
