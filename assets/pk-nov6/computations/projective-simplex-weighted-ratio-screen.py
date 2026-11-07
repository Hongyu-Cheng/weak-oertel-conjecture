from fractions import Fraction as F
from random import Random
from math import prod
rng=Random(16354)
for d in [2,3,4,5,6,8]:
 for trial in range(20000):
  r=[rng.randint(1,30) for _ in range(d+1)];r=[F(v,sum(r)) for v in r];la=[(1-v)/d for v in r];D=1-d*sum(x*x for x in la);theta=[x*(1-d*x)/D for x in la]
  before=[d**d*prod(la[j] for j in range(d+1) if j!=i) for i in range(d+1)]
  after=[(d*la[i])**d/prod(1+d*(la[i]-la[j]) for j in range(d+1) if j!=i) for i in range(d+1)]
  b=sum(t*p for t,p in zip(theta,before));a=sum(t*p for t,p in zip(theta,after))
  if b<a:
   print('EXACT FAILURE',d,la,'theta',theta,'beforecaps',before,'aftercaps',after,'before',b,'after',a,'difference',a-b,flush=True);raise SystemExit
 print('dimension',d,'20000 exact no projective monotonicity failure',flush=True)
