from fractions import Fraction as F
from random import Random
from math import prod
rng=Random(83725)
for d in [2,3,4,5,6,8,10,20]:
 gam=F(d,d+1)**d
 for trial in range(30000):
  a=[rng.randint(1,30) for _ in range(d+1)];a=[F(x,sum(a)) for x in a]
  caps=[]
  for i in range(d+1):
   if any(a[j]>F(1,d) for j in range(d+1) if j!=i):continue
   p=d**d*prod(a[j] for j in range(d+1) if j!=i)
   s=p*(d-sum(1/a[j] for j in range(d+1) if j!=i)/(d+1))
   caps.extend([(i,p,s),(-i-1,1-p,-s)])
  lo=max([(F(0),'nonnegative')]+[((gam-p)/(-s),i) for i,p,s in caps if s<0],key=lambda z:z[0]);hi=min([((p-gam)/s,i) for i,p,s in caps if s>0],default=(F(10**10),'none'),key=lambda z:z[0])
  if lo[0]>hi[0]:
   print('COUNTER',d,a,'lo',lo,'hi',hi,'caps',caps,flush=True);raise SystemExit
 print('dimension',d,'30000 exact samples no scalar obstruction',flush=True)
