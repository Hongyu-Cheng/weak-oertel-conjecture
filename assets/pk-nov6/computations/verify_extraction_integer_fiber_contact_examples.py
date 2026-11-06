"""Exact arithmetic checks for the affine-contact note's cube example."""
from fractions import Fraction as F
from itertools import product

corners = list(product((-1, 1), repeat=3))
chi = lambda z: z[0]*z[1]*z[2]
assert sum(chi(z) for z in corners) == 0
for j in range(3):
    assert sum(chi(z)*z[j] for z in corners) == 0
L = F(2)
vertices = {(z, L*chi(z)+e) for z in corners for e in (-1, 1)}
assert all((tuple(-t for t in z), -x) in vertices for z, x in vertices)
for z in corners:
    contacts = [(F(1, 2), F(1), L*chi(z)+1),
                (F(1, 2), F(-1), L*chi(z)-1)]
    assert sum(w*u*x for w, u, x in contacts) == 1
    assert sum(w*u for w, u, x in contacts) == 0
    for j in range(3):
        assert sum(w*u*z[j] for w, u, x in contacts) == 0
print('PASS: cube orthogonality, central symmetry, and exact normal contact stress')
