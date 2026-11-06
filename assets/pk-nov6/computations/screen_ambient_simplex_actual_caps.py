# Bounded numerical discovery tool. Output is never an exact certificate.
import numpy as np
from scipy.spatial import ConvexHull
from scipy.interpolate import BSpline
from scipy.optimize import differential_evolution, minimize
from math import factorial
from itertools import combinations

def density(h,x):
 h=np.sort(h);return np.nan_to_num(BSpline.basis_element(h,extrapolate=False)(x)*(len(h)-1)/(h[-1]-h[0]),nan=0.)
def triangulate(h,z):
 d=len(h)-2;v=np.vstack([np.zeros(d),np.zeros(d),np.eye(d)])
 pts=[]
 for i in range(len(h)):
  if h[i]==z:pts.append(v[i])
  for j in range(i):
   if (h[i]-z)*(h[j]-z)<0:
    pts.append(((h[i]-z)*v[j]+(z-h[j])*v[i])/(h[i]-h[j]))
 pts=np.unique(np.round(pts,14),axis=0);hu=ConvexHull(pts);c=pts.mean(axis=0)
 sims=np.array([np.vstack([c,pts[f]]) for f in hu.simplices]);vol=np.abs(np.linalg.det(sims[:,1:]-sims[:,[0]]))/factorial(d)
 keep=vol>1e-13;sims=sims[keep];vol=vol[keep]
 return sims,vol

def tail(a):
 # Generic floating divided differences, with explicit full/empty rows.
 d=a.shape[1]-1;out=np.zeros(len(a));full=a.min(axis=1)>=0;out[full]=1
 active=(a.max(axis=1)>0)&~full
 if not active.any():return out
 x=np.sort(a[active],axis=1);p=np.maximum(x,0)**d
 for k in range(1,d+1):
  den=x[:,k:]-x[:,:-k]
  # Rare repeated projections are rechecked later; never certify with this.
  if np.any(abs(den)<1e-11):
   den=np.where(abs(den)<1e-11,1e-11,den)
  p=(p[:,1:]-p[:,:-1])/den
 out[active]=np.clip(p[:,0],0,1)
 return out
cases=[
 [0,4,1.5,.75,.5,.75,3.75],
 [0,4,3,1.25,3,3.25,2.5],
 [0,4,0,0,4,4,4],
 [0,4,.1,.1,3.9,3.9,3.9],
 [0,4,.2,.7,3.6,3.6,3.6],
]
for h in cases:
 h=np.array(h,dtype=float);d=len(h)-2
 ws=density(h,np.array([1,2,3]));M=sum(ws)
 if max(ws)>=M/2:continue
 g=np.array([density(np.append(h,hi),2)/(len(h)*ws[1]) for hi in h[2:]])
 X=[];weights=[]
 for z in (1,2,3):
  sim,vol=triangulate(h,z)
  vv=np.concatenate([np.full((len(sim),d+1,1),z-2.),sim-g],axis=2)
  X.append(vv);weights.append(vol)
 X=np.concatenate(X);weights=np.concatenate(weights);total=sum(weights)
 def fun(n):
  n=np.asarray(n);n=n/max(np.linalg.norm(n),1e-10)
  return np.dot(weights,tail(X@n))/total
 bounds=[(-1,1)]*(d+1)
 opt=differential_evolution(fun,bounds,popsize=8,maxiter=70,tol=1e-8,polish=False,seed=3)
 out=minimize(fun,opt.x,method='Nelder-Mead',options={'maxiter':800,'xatol':1e-8,'fatol':1e-9})
 target=(d/(d+1))**d/2
 print('CASE',h.tolist(),'weights',ws.tolist(),'g',g.tolist(),'best',out.fun,'target',target,'normal',out.x.tolist(),flush=True)
