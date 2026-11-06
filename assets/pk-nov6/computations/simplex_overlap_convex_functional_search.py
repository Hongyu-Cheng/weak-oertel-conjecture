"""Exploratory convex-subset screen; not a proof of the resulting bound."""
import numpy as np
from scipy.optimize import differential_evolution
from itertools import combinations

T=[np.array(p,float) for p in [(0,0),(1,0),(0,1)]]
cuts=[(np.array([-1.,-1.]),-2/3),(np.array([1.,0.]),1/3),(np.array([0.,1.]),1/3)]

def clip(P,n,b):
    if not P:return []
    out=[]
    for i,p in enumerate(P):
        q=P[(i+1)%len(P)]
        a=float(np.sum(p*n))-b;c=float(np.sum(q*n))-b
        if a>=-1e-12:out.append(p)
        if a*c<0:out.append(p+a/(a-c)*(q-p))
    return out

def area(P):
    if len(P)<3:return 0.
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(P,P[1:]+P[:1])))/2

def J(params):
    P=T
    for angle,offset in np.array(params).reshape((-1,2)):
        P=clip(P,np.array([np.cos(angle),np.sin(angle)]),offset)
    darea=0.
    for i,j in combinations(range(3),2):
        darea+=area(clip(clip(P,*cuts[i]),*cuts[j]))
    return area(P)-3*darea

if __name__=='__main__':
    for count in [1,2,3,4]:
        result=differential_evolution(lambda p:-J(p),[(0,2*np.pi),(-1.1,1.1)]*count,
                                      popsize=18,maxiter=500,tol=1e-9,seed=count,polish=True)
        print(count,'max J / |T|',-result.fun*2,'params',result.x.tolist(),flush=True)
