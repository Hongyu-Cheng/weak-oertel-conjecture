import numpy as np
from scipy.optimize import minimize_scalar,linprog
from math import sqrt

def q(p,r):
 a,b,c=sorted(p)
 if c-a<1e-14:return a
 cut=(c-b)/(c-a)
 if r<=cut:return c-sqrt(max(0,r*(c-a)*(c-b)))
 return a+sqrt(max(0,(1-r)*(c-a)*(b-a)))

def boundary(p1,p2,beta):
 p1=sorted(p1);p2=sorted(p2)
 bps=sorted(set([0,beta]+[v for v in [(p1[2]-p1[1])/(p1[2]-p1[0]),beta-(p2[2]-p2[1])/(p2[2]-p2[0])] if 0<v<beta]))
 fun=lambda r:(q(p1,r)+q(p2,beta-r))/2
 cand=[(fun(r),r) for r in bps]
 for a,b in zip(bps,bps[1:]):
  fit=minimize_scalar(fun,bounds=(a,b),method='bounded',options={'xatol':1e-11})
  cand.append((fit.fun,fit.x))
 return min(cand)

def trial(B,beta=8/9,N=121):
 A=np.array([[0,0],[1,0],[0,1]])
 ang=np.linspace(0,2*np.pi,N,endpoint=False);U=np.array([np.cos(ang),np.sin(ang)]).T
 vals=[boundary(A@u,B@u,beta) for u in U]
 b=np.array([v[0] for v in vals]);r=np.array([v[1] for v in vals])
 fit=linprog([0,0,-1],A_ub=np.c_[U,np.ones(N)],b_ub=b,bounds=[(None,None)]*3,method='highs')
 return fit.x, U,b,r,fit

if __name__=='__main__':
 rng=np.random.default_rng(516)
 best=1
 for k in range(200):
  L=rng.normal(size=(2,2));L/=sqrt(abs(np.linalg.det(L)))
  B=np.array([[0,0],L[:,0],L[:,1]])
  x,U,b,r,fit=trial(B)
  if x[2]<best:
   best=x[2];print('best',k,best,'B',B.tolist(),'x',x.tolist(),flush=True)
   np.savez('./two_layer_moving_center_best.npz',B=B,x=x,U=U,b=b,r=r)
  if best<-.005:break
