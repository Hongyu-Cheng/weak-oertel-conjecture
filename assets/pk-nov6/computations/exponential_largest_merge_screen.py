"""Bounded falsification of largest-coordinate merging only."""
import numpy as np,json
rng=np.random.default_rng(710734)
def prob(x,y):
 p,q=len(x),len(y);F=np.zeros((p+1,q+1));F[:p,q]=1
 for i in range(p-1,-1,-1):
  for j in range(q-1,-1,-1):F[i,j]=(y[j]*F[i+1,j]+x[i]*F[i,j+1])/(x[i]+y[j])
 return F[0,0]
worst=1;info=None
for it in range(35000):
 p=int(rng.integers(3,9));q=int(rng.integers(1,10));xx=rng.integers(1,200,p);yy=rng.integers(1,200,q)
 if it%3==0:yy=np.ones(q,dtype=int)
 xx=np.sort(xx);x=xx/xx.sum();y=yy/yy.sum();base=prob(x,y)
 for j in [0,p-2]:
  merged=np.r_[x[np.arange(p)!=j][:-1],x[-1]+x[j]]
  delta=base-prob(merged,y)
  if delta<worst:
   worst=delta;info={'it':it,'x':xx.tolist(),'y':yy.tolist(),'merge_index':int(j),'delta':float(delta),'prob':float(base)}
  if delta<-1e-10:
   print(json.dumps(info),flush=True);raise SystemExit
print('finished',json.dumps(info),flush=True)
