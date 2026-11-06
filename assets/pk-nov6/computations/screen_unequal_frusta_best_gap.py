"""Bounded scalar frustum falsification screen; not a proof."""
import math
best=(1,None)
for d in range(2,13):
 gam=(d/(d+1))**d
 for ai in range(101):
  a=ai/101;m=d/(d+1)*(1-a**(d+1))/(1-a**d)
  for li in range(301):
   lam=1+li/200
   def tail(t):return (1-min(1,max(a,m+t))**d)/(1-a**d)
   events=[a-m,1-m,lam*(m-1),lam*(m-a),m*(lam-1)/2,0]
   vals=[tail(t)+lam**d*tail(-t/lam) for t in events]+[1,lam**d]
   actual=min(min(vals),1+lam**d-max(vals))
   target=min(1-(max(0,d-lam)/(d+1))**d,2*gam*((1+lam)/2)**d)
   ratio=actual/target
   if ratio<best[0]:best=(ratio,(d,ai,li,actual,target,events,vals))
print('best frustum comparison',best,flush=True)
