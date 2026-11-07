"""Exact constant checks for the independently audited scoped theorem."""
from fractions import Fraction as F
from math import comb

# Endpoint perturbation budget.
assert 2*F(1,8)+2*F(1,8)+6*F(1,24) == F(3,4)

# sqrt(2)/8+1/4 < 1/2 follows exactly from 2 < 2^2.
assert 2 < 2**2
# sqrt(2-sqrt(2)) > 1/2: sqrt(2) < 7/4.
assert 2 < F(7,4)**2

for d in range(2,101):
    n = d+1
    j = (n+1)//2
    gamma = F(d,n)**d
    ed = 2**d-d-1
    kd = F(j,n)-gamma/2
    assert 0 < gamma < F(1,2)
    assert ed > 0 and kd > 0
    assert sum(comb(d,k) for k in range(2,d+1)) == ed
    r = gamma*kd/(2*ed)
    assert F(j,n)-ed*r/gamma == gamma/2+kd/2
    assert gamma/(4*d) < gamma

    # Both closed vertical caps, for every r<=1, dominate the target.
    for r_vertical in (F(0),F(1)):
        target = gamma*(1+r_vertical/2)
        assert 2 >= target
        assert 1+r_vertical >= target

print("PASS: robust budget, sign bounds, finite remainder, and vertical caps")
