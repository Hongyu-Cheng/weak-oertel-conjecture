import numpy as np
from scipy.optimize import differential_evolution

def cap(r,q,x):
 b=1-x
 if q<=0:return r*r
 if q>=b*r:return 0.
 if x<1e-12:return (r-q)**2
 if x>.5-1e-12:return r*r-4*q*q
 if q<=x*r:return r*r-q*q/(x*b)
 return (b*r-q)**2/(b*(b-x))

def radii(v):
 b=.5+.5*v[0];a=(2*b-1)*v[1];c=v[2]
 return (a,b,1.,c)

def objective(v,mode=0):
 rs=radii(v);S=sum(r*r for r in rs);target=2*S/9
 if S<2:return 10+2-S
 costs=[]
 for jj,j in enumerate((1,2)):
  x,beta=v[3+2*jj],v[4+2*jj]
  costs.append(sum(cap(r,rs[j]/3-beta*(k-j),x) for k,r in enumerate(rs)))
 if mode==1:
  return costs[1 if rs[0]**2+rs[1]**2<=1+rs[3]**2 else 0]-target
 return max(costs)-target

if __name__=='__main__':
 bounds=[(.001,1),(.001,1),(.001,1),(0,.5),(-2,2),(0,.5),(-2,2)]
 for mode in (0,1):
  for seed in range(8):
   out=differential_evolution(lambda v:objective(v,mode),bounds,popsize=18,maxiter=1200,tol=1e-9,seed=seed,polish=True)
   print(mode,seed,out.fun,radii(out.x),out.x[3:],flush=True)
