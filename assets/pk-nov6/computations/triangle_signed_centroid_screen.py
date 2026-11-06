import numpy as np
from scipy.optimize import differential_evolution
from triangle_signed_fixed_cap_screen import getP,J,caps
from simplex_overlap_convex_functional_search import clip,area

def centroid(P):
 if area(P)<1e-12:return np.array([1.,1.])
 terms=[p[0]*q[1]-p[1]*q[0] for p,q in zip(P,P[1:]+P[:1])]
 return sum((p+q)*a for p,q,a in zip(P,P[1:]+P[:1],terms))/(3*sum(terms))
def val(par):
 P=getP(par);c=centroid(P); j=J(clip(P,*caps[0]));delta=2-c[0]-c[1]
 return j-10*max(0,delta)
for m in [2,3]:
 r=differential_evolution(lambda p:-val(p),[(0,2*np.pi),(0,3)]*m,popsize=12,maxiter=250,seed=m+20,tol=1e-8)
 P=getP(r.x)
 print('centroidimp',m,-r.fun,'J0',J(clip(P,*caps[0])),'centroid',centroid(P),'Q',[p.tolist() for p in P],flush=True)
