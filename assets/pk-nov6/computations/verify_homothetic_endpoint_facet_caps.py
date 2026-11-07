"""Exact checks of all-dimensional raw-tail minimization and constants."""
from fractions import Fraction as F

def clamp(x,a):return min(a,max(F(0),x))
for d in range(1,14):
 gamma=F(d,d+1)**d
 assert 2*gamma<=1
 for alpha,beta in [(F(1),F(1,10)),(F(1),F(3,4)),(F(5,4),F(3,4)),(F(2),F(3,2))]:
  assert alpha>=max(1,beta)
  assert (d+1)*alpha>=2+(d-1)*beta
  h0=(alpha+beta)/2-F(1,d+1)
  assert h0>=F(d,d+1)*beta
  for hn in range(-10,21):
   h=F(hn,10);answer=min(beta**d,2*max(h,0)**d)
   for rn in range(-30,31):
    r=F(rn,7);s=2*h-r
    assert clamp(r,alpha)**d+clamp(s,beta)**d>=answer
   if h<=0:r=s=h
   elif 2*h**d<=beta**d:r=s=h
   else:r=min(F(0),2*h-beta)-1;s=2*h-r
   assert clamp(r,alpha)**d+clamp(s,beta)**d==answer
  assert min(beta**d,2*h0**d)>=2*gamma*beta**d
print('PASS: exact tail saturation, attained minimum, and dimension-dependent constants.')
