import numpy as np
from scipy.optimize import minimize,LinearConstraint,Bounds
rng=np.random.default_rng(19244)
best=1
for N in [3,4,5,7,10,20,40]:
 D=np.zeros((N-2,N))
 for i in range(N-2):D[i,i:i+3]=[1,-2,1]
 for j in sorted(set([0,1,(N-1)//2,N-2,N-1])):
  peak=np.zeros((1,N));peak[0,j]=1
  for p in [1,1.1,1.5,2,3,5,10,20,50]:
   c=(p+1)/(p+2)
   for attempt in range(3):
    xx=np.arange(N)
    if j in [0,N-1]: r=1-abs(xx-j)/(N-1)*rng.uniform(.5,1)
    else:r=1-rng.uniform(.2,.95)*np.maximum((j-xx)/max(j,1),(xx-j)/max(N-1-j,1))
    sol=minimize(lambda r:np.sum(r**(p+1)-c*r**p),r,jac=lambda r:(p+1)*r**p-c*p*r**(p-1),constraints=[LinearConstraint(D,-np.inf,0),LinearConstraint(peak,1,1)],bounds=Bounds(0,1),method='SLSQP',options={'ftol':1e-12,'maxiter':1000})
    if sol.success and sol.fun<best:
     best=sol.fun; print(N,j,p,best,sol.x.tolist(),flush=True)
    if sol.success and sol.fun< -1e-8:raise SystemExit('COUNTER')
