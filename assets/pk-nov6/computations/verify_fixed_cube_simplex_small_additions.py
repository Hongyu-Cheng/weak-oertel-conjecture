"""Exact checks for fixed cube–simplex core additions.

The all-n projection classification and cap proof are analytic in the note;
finite checks below verify the coordinate maps and rational error constants.
"""
from fractions import Fraction as F
from itertools import product

for n in range(1,7):
    core = set(product((0,1), repeat=n))
    groups = {w:[] for w in core}
    for p in product((-1,0,1,2), repeat=n):
        if p in core:
            continue
        partner = tuple(x % 2 for x in p)
        center = tuple((x+y)//2 for x,y in zip(p,partner))
        assert center in core
        assert partner != center
        assert tuple(2*x-y for x,y in zip(center,partner)) == p
        groups[center].append(partner)
    assert all(len(vs) == len(set(vs)) for vs in groups.values())
    assert sum(map(len,groups.values())) == 4**n-2**n
    # Every core center has precisely 2^n-1 possible distinct partners.
    assert all(len(vs) == 2**n-1 for vs in groups.values())

for x in range(-100,101):
    if x < -1 or x > 2:
        y = (x+x%2)//2
        assert y < 0 or y > 1
        assert y != x

for d in range(2,101):
    nvert = d+1
    tau = 1-F(2,nvert)
    gamma = F(d,nvert)**d
    eps = tau/16
    r = tau/4
    exact_slack = tau-4*eps-(1+2*eps)*r
    assert exact_slack >= F(15,32)*tau > 0
    assert 0 < gamma < F(1,2)
    assert F(1,2**(d+1)) < F(1,2**d)

print("PASS: parity grouping, far-coordinate midpoint, and full-credit constants")
