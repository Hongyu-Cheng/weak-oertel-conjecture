import sys

import numpy as np,itertools
from scipy.optimize import differential_evolution
for d in [3,4,5,6,10,1000000000]:
 a=(d/(2*(d-1)))**.5;gamma=(d/(d+1))**d
 print('dimension',d,'a',a,'gamma',gamma,flush=True)
 for card in range(1,4):
  mask=np.array([i<card for i in range(3)]);best=(1,None)
  for ri in itertools.product([a,1],repeat=3):
   r=np.array(ri)
   def fun(z):
    t=np.array([z[0],(1-z[0])*z[1],(1-z[0])*(1-z[1])]);e=(1-np.dot(t,t))/2
    if e<1e-18:return 1.
    lam=t*(1-t);th=lam/r;th/=sum(th)
    return (e+np.dot(th,t*t*mask))/(2*e+np.dot(t,t*mask))
   res=differential_evolution(fun,[(1e-7,1-1e-7),(1e-7,1-1e-7)],seed=947,tol=1e-9)
   if res.fun<best[0]:best=(res.fun,(ri,res.x))
  print('card',card,'best',best,flush=True)
