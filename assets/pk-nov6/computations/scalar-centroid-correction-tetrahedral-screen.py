from fractions import Fraction as F
from random import Random
from math import prod
rng=Random(94119);gam=F(27,64)
for trial in range(50000):
 p,q,r,s=[F(rng.randint(1,40)) for _ in range(4)]
 aa=p*s/((p+r)*(p+s)*(q+s));bb=q*r/((p+r)*(q+s)*(q+r));tau=aa/(aa+bb)
 la=[(r/(p+r)+tau*s/(p+s))/3,(s/(q+s)+(1-tau)*r/(q+r))/3,(p/(p+r)+(1-tau)*q/(q+r))/3,(q/(q+s)+tau*p/(p+s))/3]
 caps=[('quad',p*(aa+bb)+q*q/((q+s)*(q+r)),3*(aa+bb)*(p+q-r-s)/4)]
 for i in range(4):
  if any(la[j]>F(1,3) for j in range(4) if j!=i):continue
  fp=27*prod(la[j] for j in range(4) if j!=i)
  sp=fp*(3-sum(1/la[j] for j in range(4) if j!=i)/4)
  caps.append(('vertex'+str(i),fp,sp))
 caps += [('complement-'+name,1-v,-c) for name,v,c in list(caps)]
 lower=max([(F(0),'nonnegative')]+[((gam-v)/(-c),name) for name,v,c in caps if c<0]);upper=min([((v-gam)/c,name) for name,v,c in caps if c>0],default=(F(10**10),'none'))
 if lower[0]>upper[0]:
  print('COUNTER',trial,'params',p,q,r,s,'lambda',la,'lower',lower,'upper',upper,'caps',caps,flush=True);break
else:print('No scalar correction obstruction in 50000 exact sampled quadrilateral-centroid configurations',flush=True)
