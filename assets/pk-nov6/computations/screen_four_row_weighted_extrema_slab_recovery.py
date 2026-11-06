import sys
sys.path.insert(0,'.')
from screen_four_row_simplex_phi_slab_recovery import phi3
from scipy.optimize import differential_evolution
import numpy as np

def mat(v):
 t=np.asarray(v).reshape(4,3)
 return np.array([t[:,0],(1-t[:,0])*t[:,1],(1-t[:,0])*(1-t[:,1])*t[:,2],(1-t[:,0])*(1-t[:,1])*(1-t[:,2])])
for it,l in enumerate([[.1,.3,.3,.3],[.2,.2,.3,.3],[.03,.32,.32,.33],[.01,.01,.32,.66],[.05,.15,.3,.5]]):
 l=np.array(l);c=3*np.array([np.prod(np.delete(l,i))**(1/3) for i in range(4)])
 def fun(v):
  X=mat(v)
  try:return -sum(c[i]*phi3(X[i]) for i in range(4))
  except (ValueError,ZeroDivisionError):return 0
 r=differential_evolution(fun,[(1e-7,1-1e-7)]*12,popsize=10,maxiter=500,tol=1e-8,seed=137+it,polish=True)
 X=mat(r.x)
 print(it,'lambda',l.tolist(),'value',-r.fun,'X',X.tolist(),'phi',[phi3(row) for row in X],flush=True)
