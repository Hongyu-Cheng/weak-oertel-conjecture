import numpy as np
from scipy.optimize import minimize_scalar
import json
rng=np.random.default_rng(17019)
def depth(K,k,x):
 lo=K[:,0];up=K[:,1];z=np.arange(len(K));dif=z-k;ix=dif!=0
 slopes=((K[ix]-x)/dif[ix,None]).ravel()
 cuts=x+slopes[:,None]*dif
 above=np.clip(up[None,:]-cuts,0,up-lo).sum(axis=1)
 M=(up-lo).sum()
 # Vertical halfspaces are no smaller than their nearby tilted versions.
 return min(above.min(),M-above.max())/M

def best(K):
 vals=[]
 for k,(l,u) in enumerate(K):
  sol=minimize_scalar(lambda x:-depth(K,k,x),bounds=(l,u),method='bounded',options={'xatol':1e-9})
  vals.append((-sol.fun,k,sol.x))
 return max(vals)
def randfam(N):
 lower=np.r_[0,np.cumsum(np.sort(rng.integers(-12,13,N-1)))]
 upper=np.r_[0,np.cumsum(np.sort(rng.integers(-12,13,N-1))[::-1])]
 upper+=max(lower-upper)+rng.integers(1,13)
 return np.array(list(zip(lower,upper)),float)
if __name__=='__main__':
 bestloss=0
 for i in range(6000):
  N=int(rng.integers(3,7)); A=randfam(N);B=randfam(N); C=A+B
  fa,fb,fc=best(A),best(B),best(C)
  loss=min(fa[0],fb[0])-fc[0]
  if loss>bestloss+1e-8:
   bestloss=loss; print(i,loss,fa,fb,fc,A.tolist(),B.tolist(),flush=True)
   with open('./minkowski_depth_best.json','w') as f:json.dump(dict(A=A.tolist(),B=B.tolist(),fa=fa,fb=fb,fc=fc),f)
  if loss>.02:break
