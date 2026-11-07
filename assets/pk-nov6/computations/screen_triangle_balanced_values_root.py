import numpy as np
from scipy.optimize import minimize
c=128/279
rng=np.random.default_rng(290930)
def dat(x):
 a=np.array([x[0],x[1],1-x[0]-x[1]])
 r,s,t=x[2:]
 b=np.array([[0,s*a[1],t*a[2]],[r*a[0],0,(1-t)*a[2]],[(1-r)*a[0],(1-s)*a[1],0]])
 q=np.array([a[i]**2/np.prod([a[i]+b[i,j] for j in range(3) if j!=i]) for i in range(3)])
 w=a/q
 return a,q,w/w.sum()
for profile in [False,True]:
 best=None
 def constraints(x):
  a,q,w=dat(x)
  vals=list(a-1e-6)+list(c-q)
  if profile: vals += [1-q.sum()+.75*q.max()]
  return np.array(vals)
 for j in range(20):
  aa=rng.dirichlet(np.ones(3)*10)
  x0=np.r_[aa[:2],rng.uniform(.2,.8,3)]
  res=minimize(lambda x:dat(x)[2][0],x0,method='SLSQP',bounds=[(1e-6,.999999)]*2+[(1e-6,.999999)]*3,constraints=[{'type':'ineq','fun':constraints}],options={'maxiter':800,'ftol':1e-11})
  if min(constraints(res.x))>=-1e-7 and (best is None or res.fun<best.fun):best=res
 if best is not None: print('profile',profile,'objective',best.fun,'x',best.x.tolist(),'a q lambda',[v.tolist() for v in dat(best.x)],'minconstraint',min(constraints(best.x)),flush=True)
