"""Exact numerical parts of the allocation-region certificates."""
from fractions import Fraction as F
r=F(4,3);y=F(5,6)
# Rational grid is a supplement; the source proves all real allocations.
for k in range(161):
 for a in range(161-k):
  t=r*F(k,160);p=r*F(a,160);q=r-t-p
  sets=[]
  if t<=1:sets.append((t,2-t))
  if p<=F(1,2) and q<=F(1,2):sets.append(((p+q)/2,1-(p+q)/2))
  assert sets and min(x[0] for x in sets)<=y<=max(x[1] for x in sets)
assert y+2*(1-y)==F(7,6)<r
assert (2-y)+2*(1-y)==F(3,2)>r
G=F(4,9);target=G*F(201,200)
pA=2*G/F(100);pK=G*F(197,200)
assert pA+pK==target
assert target>G and pA>G/F(100)
assert F(121,400)<F(197,450)
assert F(4,9)*F(197,200)>F(121,400)
assert F(41,75)-F(4,9)==F(23,225)
print('PASS: interval allocation bounds, strict pointwise gain, and two-allocation exact emptiness.')
