from fractions import Fraction as F
from random import Random
from math import prod
rng=Random(8549)
for d in [2,3,4,5,6,8,10]:
 gam=F(d,d+1)**d
 for trial in range(50000):
  ts=[rng.randint(1,100) for _ in range(d+1)];ts=[F(t,sum(ts)) for t in ts];la=[(1-t)/d for t in ts]
  a=min(la);b=max(la);T=sum(1/x for x in la)-d*(d+1);E=1/a+1/b-T;c=F(d+1)/E
  for i in range(d+1):
   p=d**d*prod(la[j] for j in range(d+1) if j!=i);s=p*(d-sum(1/la[j] for j in range(d+1) if j!=i)/(d+1));v=p-c*s
   assert v>=gam
   if v>1-gam:
    print('UPPER FAILURE',d,la,'vertex',i,'corrected',v,'threshold',1-gam,'c',c,flush=True);raise SystemExit
 print(d,'no explicit correction failure 50000 exact samples',flush=True)
