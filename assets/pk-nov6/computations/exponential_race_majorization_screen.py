"""Falsification only, exact race recurrence is independently auditable."""
import numpy as np,json
rng=np.random.default_rng(1321049)
def prob(x,y):
 p,q=len(x),len(y);F=np.zeros((p+1,q+1));F[:p,q]=1
 for i in range(p-1,-1,-1):
  for j in range(q-1,-1,-1):
   # P(first positive phase ends)=y/(x+y)
   F[i,j]=(y[j]*F[i+1,j]+x[i]*F[i,j+1])/(x[i]+y[j])
 return F[0,0]
best=1;merge=1
for it in range(300000):
 p=int(rng.integers(2,8));q=int(rng.integers(1,8))
 xx=rng.integers(1,80,p);yy=rng.integers(1,80,q);x=xx/xx.sum();y=yy/yy.sum()
 val=prob(x,y);diff=val-(q/(q+1))**q
 if diff<best:
  best=diff
  print(json.dumps({'kind':'bound','it':it,'x':xx.tolist(),'y':yy.tolist(),'prob':val,'gap':diff}),flush=True)
 merged=np.r_[x[0]+x[1],x[2:]];delta=val-prob(merged,y)
 if delta<merge:
  merge=delta
  if merge<0: print(json.dumps({'kind':'merge','it':it,'x':xx.tolist(),'y':yy.tolist(),'prob':val,'delta':delta}),flush=True)
 if best<-1e-9:break
print('finished',best,merge,flush=True)
