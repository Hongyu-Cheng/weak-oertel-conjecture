"""Exact moment and cap certificate using only rational arithmetic."""
from fractions import Fraction as F

a=F(2,9)
r=2*a-a*a
mx=a*a-F(2,3)*a**3
my=a-a*a+a**3/3
assert r==F(32,81)
assert mx==F(92,2187)
assert my==F(386,2187)
M=1+2*r
gx=(F(1,3)+2*mx)/M
gy=(F(1,3)+2*my)/M
assert gx==F(913,3915)
assert gy==F(1501,3915)
assert gx-a==F(43,3915)>0
assert gx>0 and gy>0 and gx+gy<1
cap=(1-gx)**2/M
assert cap==F(9012004,27437625)
assert F(2,9)<cap<F(1,3)
print('Exact actual-centroid cap certificate passed:',cap)
