import sys

import numpy as np
from scipy.optimize import minimize
from random import Random
rng=Random(613177)
def data(z):
 E=np.r_[z,1-sum(z)];x,y,z,w=E
 if min(E)<=0:return E,np.ones(4),float('nan')
 L=np.array([x*(1/(x+z)+1/(x+w)-1),y*(1/(y+z)+1/(y+w)-1),z*(1/(x+z)+1/(y+z)-1),w*(1/(x+w)+1/(y+w)-1)])/3
 P=x+y;R=z+w;a=x*y;b=z*w;D=(a-b)**2+a*R+b*P;F=b*(P-a+b)/D;s=3*(b*P-a*R)/(4*D);ls=sorted(L);den=12-1/ls[1]-1/ls[2]
 return E,L,F-4*s/den
best=1.;rec=None
for trial in range(300):
 while True:
  z=np.array([rng.random() for _ in range(4)]);z/=sum(z)
  if max(data(z[:3])[1])<1/3:break
 def obj(z):
  E,L,val=data(z)
  if not np.isfinite(val):return 1e3
  return val
 cons=[{'type':'ineq','fun':lambda z:1-sum(z)-1e-9},{'type':'ineq','fun':lambda z:1/3-data(z)[1]}]
 res=minimize(obj,z[:3],method='SLSQP',bounds=[(1e-9,1-1e-9)]*3,constraints=cons,options={'maxiter':500,'ftol':1e-12})
 E,L,val=data(res.x)
 if min(E)>0 and max(L)<=1/3+1e-9 and val<best:
  best=val;rec=(E,L);print('best',trial,best,E,L,'success',res.success,flush=True)
print('FINAL',best,rec,flush=True)
