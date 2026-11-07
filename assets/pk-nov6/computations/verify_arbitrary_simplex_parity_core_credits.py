"""Exact checks of the new arbitrary-simplex parity-core credit mechanism.
The complete all-direction proof is in the companion Markdown note.
"""
from fractions import Fraction as F
from itertools import product


def val(f, p):
    return f[0]+f[1]*p[0]+f[2]*p[1]


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                   - poly[i][1]*poly[(i+1) % len(poly)][0]
                   for i in range(len(poly))))/2


def cap(poly, f, threshold):
    out = []
    for p, q in zip(poly, poly[1:]+poly[:1]):
        a, b = val(f, p)-threshold, val(f, q)-threshold
        if a >= 0:
            out.append(p)
        if (a < 0 < b) or (b < 0 < a):
            alpha = a/(a-b)
            out.append(tuple(p[j]+alpha*(q[j]-p[j]) for j in range(2)))
    return area(out)


T = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
C = [(F(0), F(0)), (F(7, 4), F(0)), (F(0), F(4, 7))]
t = F(1, 10000)
A = [(t*p[0], t*p[1]) for p in T]
V, a, gamma = area(T), area(A), F(4, 9)
assert area(C) == V
assert all(min((p[j]+q[j])/2 for j in range(2)) >= 0
           and sum((p[j]+q[j])/2 for j in range(2)) <= 1
           for p in A for q in C)

# At every point of A, facets 0 and 1 have a fixed strictly positive
# endpoint margin; facet 2 does not. This is an unequal-shape partner.
facets = [(F(1), F(-1), F(-1)), (F(0), F(1), F(0)), (F(0), F(0), F(1))]
for i in (0, 1):
    margin = min(val(facets[i], p) for p in A)+max(val(facets[i], q) for q in C)-F(2, 3)
    assert margin > F(1, 10)
assert max(val(facets[2], p) for p in A)+max(val(facets[2], q) for q in C) < F(2, 3)

cbar = 2*a/3
shift = (a/(9*gamma*V), -2*a/(9*gamma*V))
y = (F(1, 3)+shift[0], F(1, 3)+shift[1])
assert all(val(f, y) > 0 for f in facets)
for f, credit in zip(facets, (a, a, F(0))):
    assert val(f, shift)-f[0] == (credit-cbar)/(3*gamma*V)


def all_tilt_minimum(f):
    center = val(f, y)
    # At base -1 use threshold center+beta; at +1 use center-beta.
    def mass(beta):
        return cap(A, f, center+beta)+cap(C, f, center-beta)
    breaks = sorted(set([val(f, p)-center for p in A]
                        + [center-val(f, q) for q in C]))
    minimum = min(mass(x) for x in breaks)
    # On both unbounded tails every cap is constant. Between consecutive
    # vertex levels the triangular cap areas are quadratic polynomials.
    minimum = min(minimum, mass(breaks[0]-1), mass(breaks[-1]+1))
    for lo, hi in zip(breaks, breaks[1:]):
        mid, h = (lo+hi)/2, (hi-lo)/2
        fm, f0, fp = mass(lo), mass(mid), mass(hi)
        quadratic = (fp+fm-2*f0)/(2*h*h)
        linear = (fp-fm)/(2*h)
        # Independent extra sample checks the polynomial fit exactly.
        for u in (-h/3, h/3):
            assert mass(mid+u) == f0+linear*u+quadratic*u*u
        if quadratic > 0:
            u = -linear/(2*quadratic)
            if -h <= u <= h:
                minimum = min(minimum, mass(mid+u))
    return cap(T, f, center)+minimum

for f in facets:
    assert all_tilt_minimum(f) >= gamma*(V+a)

# Every first-reflection group has distinct partner vertices, independently
# of geometric cube structure. Use a nonvertex complete parity transversal.
P = [(0, 0), (2, 1), (1, 2), (1, 1)]
assert len({tuple(x % 2 for x in p) for p in P}) == 4
for w in P:
    reflected = [(2*w[0]-v[0], 2*w[1]-v[1]) for v in P if v != w]
    assert len(set(reflected)) == 3
    for p, v in zip(reflected, [v for v in P if v != w]):
        assert tuple(x % 2 for x in p) == tuple(x % 2 for x in v)
        assert tuple((p[j]+v[j])//2 for j in range(2)) == w

print('PASS: unequal-shape exact midpoint compatibility, fixed facet credits,')
print('balanced true-centroid displacement, ALL real facet tilts, and nonvertex parity core')
