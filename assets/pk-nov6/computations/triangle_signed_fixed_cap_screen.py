"""Exploratory screen of the fixed-three-cap signed hemisphere lemma."""
import numpy as np
from scipy.optimize import differential_evolution
from simplex_overlap_convex_functional_search import clip,area
K=[np.array(p,float) for p in [(0,0),(3,0),(0,3)]]
g=np.array([1.,1.])
caps=[(np.array([-1.,-1.]),-2.),(np.array([1.,0.]),1.),(np.array([0.,1.]),1.)]
def J(P):
 d=0
 for i,j in [(0,1),(0,2),(1,2)]:d+=area(clip(clip(P,*caps[i]),*caps[j]))
 return area(P)-3*d

def getP(par):
 P=K
 for th,r in np.array(par).reshape((-1,2)):
  v=np.array([np.cos(th),np.sin(th)])
  P=clip(P,v,float(v@g-r))
 return P

def val(par):
 P=getP(par)
 return min(J(clip(P,*cap)) for cap in caps)
if __name__=='__main__':
    for m in [2,3,4]:
     result=differential_evolution(lambda p:-val(p),[(0,2*np.pi),(0,3)]*m,popsize=14,maxiter=300,seed=m,tol=1e-8)
     print(m,'min fixed J',-result.fun,'params',result.x.tolist(),flush=True)
     print('Q',[p.tolist() for p in getP(result.x)],flush=True)
