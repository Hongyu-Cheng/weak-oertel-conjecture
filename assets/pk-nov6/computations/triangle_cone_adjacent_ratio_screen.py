import numpy as np
from scipy.optimize import differential_evolution
from triangle_signed_fixed_cap_screen import getP
from triangle_cone_product_screen import masses

def val(par):
 e,d=masses(getP(par));ad=np.array([d[0]+d[1],d[0]+d[2],d[1]+d[2]])
 if min(*e,*d)<1e-11:return -100
 return min(e/ad)
for m in [2,3,4]:
 r=differential_evolution(lambda p:-val(p),[(0,2*np.pi),(.00001,3)]*m,popsize=18,maxiter=700,seed=m+721,tol=1e-9)
 P=getP(r.x);e,d=masses(P)
 print(m,'min ratio',-r.fun,'e',e,'d',d,'Q',[p.tolist() for p in P],flush=True)
