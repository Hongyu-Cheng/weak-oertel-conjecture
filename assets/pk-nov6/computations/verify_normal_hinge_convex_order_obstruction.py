"""Exact data checks for the actual minimizer convex-order obstruction."""
from fractions import Fraction as F

points = [(0,0),(0,1),(1,0),(1,1)]
eps = {z:(-1)**sum(z) for z in points}
h = {z:F(eps[z],4) for z in points}
assert sum(h.values()) == 0
assert all(sum(z[k]*h[z] for z in points)==0 for k in (0,1))
assert sum((1+h[z]) for z in points) == 4
assert sum((1-h[z]) for z in points) == 4
hinge = sum((1+h[z])**2/2 for z in points)
assert hinge == F(17,8)
assert sum((1-h[z])**2/2 for z in points) == hinge
assert 2*hinge == 4+sum(h[z]**2 for z in points) == F(17,4) < 5
for k in (0,1):
    assert sum(z[k]*(1+h[z]) for z in points) == 2
    assert sum(z[k]*(1-h[z]) for z in points) == 2
for p in points:
    for z in points:
        q = sum((1-p[k])*z[k]+p[k]*(1-z[k]) for k in (0,1))
        assert max(0,1-q) == int(p==z)
assert sum(1-abs(h[z]) for z in points) == 3
print('PASS: exact fibers, cap budgets, hinge value, moments, and convex tests.')
