import numpy as np
from scipy.optimize import minimize,LinearConstraint,Bounds
best=1
for N in range(3,61):
 for a in range((N-1)//3+1,(2*(N-1)+2)//3):
  z=np.arange(N)-a
  eq=np.stack([np.ones(N),z]); c=(z>0).astype(float)
  dd=np.zeros((N-2,N))
  for j in range(N-2):dd[j,j:j+3]=[1,-2,1]
  sol=minimize(lambda w:c@w+.5*(w@w),np.ones(N)/N,jac=lambda w:c+w,hess=lambda w:np.eye(N),constraints=[LinearConstraint(eq,[1,0],[1,0]),LinearConstraint(dd,-np.inf,0)],bounds=Bounds(0,np.inf),method='SLSQP',options={'ftol':1e-11,'maxiter':300})
  if sol.success and sol.fun<best:
   best=sol.fun;print(N,a,best,sol.x.tolist(),flush=True)
