"""Exact-formula floating diagnostics; not a proof."""
import numpy as np
from scipy.optimize import differential_evolution

def tail(w,p,x):
 a=-(1+p)*w/3;b=(2*p-1)*w/3;c=(2-p)*w/3
 if x<=a:return 1.
 if x>=c:return 0.
 if x<=b:return 1-(x-a)**2/(p*w*w)
 return (c-x)**2/((1-p)*w*w)

def own(R,p,q):
 a,b=1-p,1-q
 S=(1+R+a+R*b)/3
 H=(2*p-1+R*(2*q-1))/6
 m=(R+1)/2
 if p>R*R*q:m=(1+p/R+R*(1-q))/2
 if 1-p>R*R*(1-q):m=(1+R*q+(1-p)/R)/2
 if H>0:return m-own(R,1-p,1-q)
 if a<=R*R*b:return S/2-a/4+(S-a)**2/(4*R*R*b)
 return S/(2*R)-b/4+(S-R*b)**2/(4*a)

def pair(R,p,q,ret=False):
 br=sorted(set([-(1+p)/3,(2*p-1)/3,(2-p)/3,(1+q)*R/3,-(2*q-1)*R/3,-(2-q)*R/3]))
 def P(x):return tail(1,p,x)+tail(R,q,-x)
 candidates=[(P(x),x)for x in br]+[(1,br[0]-1)]
 for x,y in zip(br,br[1:]):
  mid=(x+y)/2;fx,fy,fm=P(x),P(y),P(mid)
  A=2*(fx+fy-2*fm)/(y-x)**2
  if A>1e-8:
   crit=mid-(fy-fx)/(2*A*(y-x))
   if x<crit<y:candidates.append((P(crit),crit))
 best=min(candidates)
 return best if ret else best[0]

if __name__=='__main__':
 for R in [1,1.01,1.1,1.25,1.5,2,2.5,3,4,6,10]:
  res=differential_evolution(lambda v:own(R,*v)+pair(R,*v),[(0,1),(0,1)],tol=1e-10,seed=100,maxiter=300)
  print(R,res.fun,res.x,own(R,*res.x),pair(R,*res.x,ret=True),flush=True)
