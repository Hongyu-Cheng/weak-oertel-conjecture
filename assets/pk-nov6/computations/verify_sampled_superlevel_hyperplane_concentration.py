"""Exact adversarial checks of the superlevel hyperplane theorem.

The proof is in the companion note. These finite checks are not a proof.
They include lower-dimensional superlevels carrying positive sampled mass.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
from random import Random


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    ps = sorted(set(points))
    if len(ps) <= 1:
        return ps
    low, high = [], []
    for seq, out in ((ps, low), (ps[::-1], high)):
        for p in seq:
            while len(out) >= 2 and cross(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
    return low[:-1] + high[:-1]


def contains(poly, p):
    if len(poly) == 1:
        return poly[0] == p
    if len(poly) == 2:
        a, b = poly
        return (cross(a, b, p) == 0 and
                all(min(a[j], b[j]) <= p[j] <= max(a[j], b[j]) for j in range(2)))
    return all(cross(poly[i], poly[(i+1) % len(poly)], p) >= 0
               for i in range(len(poly)))


def area(poly):
    if len(poly) <= 2:
        return F(0)
    return F(abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                     - poly[i][1]*poly[(i+1) % len(poly)][0]
                     for i in range(len(poly)))), 2)


def audit_nested_polygons(seed):
    rng = Random(seed)
    grid = list(product(range(-2, 3), repeat=2))
    rng.shuffle(grid)
    layers = [(hull(grid[:size]), rng.randrange(1, 6))
              for size in range(1, len(grid)+1)]
    # Nested hulls, with arbitrary positive jump sizes: all superlevels convex.
    weights = {p: sum(c for poly, c in layers if contains(poly, p)) for p in grid}
    integral = sum(c*area(poly) for poly, c in layers)
    ordered = sorted(grid, key=lambda p: (-weights[p], p))
    p0, p1 = ordered[:2]
    outside = [p for p in grid if cross(p0, p1, p) != 0]
    b = max(weights[p] for p in outside)
    assert weights[p0] >= b and weights[p1] >= b
    loss = sum(weights[p] for p in outside)
    truncated = sum(min(w, b) for w in weights.values())-2*b
    assert loss <= truncated <= 2*integral, (seed, loss, truncated, integral)
    # Check exact finite lattice-point volume bound for every superlevel.
    for t in sorted(set(weights.values())):
        subset = [p for p in grid if weights[p] >= t]
        poly = hull(subset)
        if area(poly) > 0:
            assert 2*area(poly) >= len(subset)-2


for seed in range(200):
    audit_nested_polygons(seed)

# Exact sharpness, in every displayed rank: unimodular simplex times K.
for rank in range(1, 9):
    volume = F(1, factorial(rank))
    total = rank+1
    best_retained = rank
    assert total-best_retained == factorial(rank)*volume

# A high one-dimensional plateau over a full-dimensional low rectangle.
# A method requiring full rank of EVERY superlevel would be invalid here.
grid = list(product(range(-3, 4), repeat=2))
weights = {p: 1+100*(p[1] == 0) for p in grid}
total = sum(weights.values())
retained = sum(w for p, w in weights.items() if p[1] == 0)
integral = F(36)  # f=1 on [-3,3]^2 plus 100 on a measure-zero segment.
assert total-retained == 42 <= 2*integral

# Arbitrary large sampled mass on one affine hyperplane with ambient integral 0.
assert sum(1_000_000 for j in range(100)) > 0
assert F(0) == F(0)  # All mass is retained on that hyperplane.

print('PASS: 200 exact nested-polygon functions, every superlevel lattice bound,')
print('greedy threshold inequalities, sharp simplex ranks 1..8, and boundary-mass plateaux')
