"""Exact shear and depth constants; geometry is the audited diamond source."""
from fractions import Fraction as F

P = [(0,0,1),(1,0,0),(1,0,1),(1,0,2),(1,1,0),(1,1,1),
     (2,0,1),(2,1,0),(2,1,1),(2,1,2),(2,2,0)]
g = [F(1),F(1),F(1,2),F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(0)]
W = [0,1,3,4,5,6,7,8,10]
height = lambda i: g[i] + 100*P[i][0] + 10*P[i][1] + P[i][2]
assert [height(i) for i in W] == [2,101,102,110,111,201,210,211,220]
assert len({height(i) for i in W}) == 9
assert height(2) == F(203,2)
assert all(height(i).denominator == 1 for i in W)
assert F(1,9) < F(1,2)
for s in range(1,101):
    gamma = F(s,s+1)**s
    gamma_next = F(s+1,s+2)**(s+1)
    assert gamma/9 > gamma/16
    if s == 1:
        assert gamma/9 == gamma_next/8
    else:
        assert gamma/9 < gamma_next/8
    assert (gamma/9)/(gamma/2) == F(2,9)
print("PASS: integral shear, distinct fine levels, eta=1/9, and exact depth comparison.")
