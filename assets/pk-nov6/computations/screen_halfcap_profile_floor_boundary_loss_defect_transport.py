"""Falsification of a precisely specified raw-data sublemma only."""
import numpy as np
from scipy.optimize import minimize
m=20/49

def calc(w):
 z,v,r1,r2=w;x=2-z*z;g=2*z;f=np.array([x,v,g-v]);r3=(2-x*r1-v*r2)/(g-v)
 r=np.array([r1,r2,r3]);q=r*r;C=2+z*z
 alpha=C+z*v/r2**2-C*v/r2
 return f,r,q,alpha
rng=np.random.default_rng(61351);best=None
for big in range(3):
 def constraints(w):
  f,r,q,alpha=calc(w)
  ph=np.array([f[i]+(sum(f)-f[i])**2/4 for i in range(3)])
  return np.r_[f-1e-6,r-np.sqrt(m),np.sqrt(.5)-r,2-ph,q[big]-np.delete(q,big),1-sum(q)+.75*q[big]]
 for _ in range(18):
  w=[rng.uniform(.7,1.3),rng.uniform(.6,1.4),rng.uniform(.64,.85),rng.uniform(.64,.85)]
  R=minimize(lambda w:calc(w)[3],w,method='SLSQP',bounds=[(.1,1.4),(.01,2.79),(np.sqrt(m),np.sqrt(.5)),(np.sqrt(m),np.sqrt(.5))],constraints=[{'type':'ineq','fun':constraints}],options={'maxiter':300,'ftol':1e-12})
  if min(constraints(R.x))>-1e-7 and (best is None or R.fun<best[0]):best=(R.fun,big,R.x,calc(R.x))
print(best)
