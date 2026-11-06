import numpy as np
from scipy.optimize import differential_evolution
from triangle_signed_fixed_cap_screen import getP,caps
from simplex_overlap_convex_functional_search import clip,area

def masses(P):
 d=np.array([area(clip(clip(P,*caps[i]),*caps[j])) for i,j in [(0,1),(0,2),(1,2)]])
 v=np.array([area(clip(P,*c)) for c in caps])
 e=v-np.array([d[0]+d[1],d[0]+d[2],d[1]+d[2]])
 return e,d

def val(par):
 e,d=masses(getP(par))
 if min(*e,*d)<1e-9:return -100
 return sum(np.log(e))-sum(np.log(d))
if __name__=='__main__':
    for m in [1,2,3,4]:
     r=differential_evolution(lambda p:-val(p),[(0,2*np.pi),(.0001,3)]*m,popsize=13,maxiter=300,seed=m+51,tol=1e-9)
     P=getP(r.x);e,d=masses(P)
     print(m,'ratio',np.exp(-r.fun),'e',e,'d',d,'Q',[p.tolist() for p in P],flush=True)
