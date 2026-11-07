import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import differential_evolution
from simplex_overlap_convex_functional_search import clip,area
H=[np.array(p,float) for p in [(0,0),(3,0),(2,1),(0,1)]]
E=[np.array(p,float) for p in [(0,0),(1,0),(1,1),(0,1)]]
def J(P):
 R=P
 for n,b in [(np.array([1.,0.]),1.),(np.array([0.,1.]),0.),(np.array([-1.,-1.]),-2.)]:R=clip(R,n,b)
 return area(P)-3*area(R)
def val(par):
 P=H
 for th,c in np.array(par).reshape((-1,2)):P=clip(P,np.array([np.cos(th),np.sin(th)]),c)
 V=np.array(P+E);Q=[V[i] for i in ConvexHull(V).vertices]
 return J(P)-J(Q)
for m in [1,2,3]:
 r=differential_evolution(lambda p:-val(p),[(0,2*np.pi),(-4,4)]*m,popsize=12,maxiter=150,seed=m,tol=1e-8)
 print(m,-r.fun,r.x,flush=True)
