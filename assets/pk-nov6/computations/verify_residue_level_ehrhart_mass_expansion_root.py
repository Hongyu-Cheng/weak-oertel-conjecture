"""Exact finite calibrations of the residue-level theorem; not an OC proof."""
from fractions import Fraction as F
from itertools import product
from math import comb


def affine_dim(points):
    if len(points) <= 1:
        return 0
    p = points[0]
    vectors = [(q[0] - p[0], q[1] - p[1]) for q in points[1:]]
    v = next(q for q in vectors if q != (0, 0))
    return 2 if any(v[0] * q[1] != v[1] * q[0] for q in vectors) else 1


def bound(m, dim, count):
    return comb(m + dim, dim) + (count - dim - 1) * comb(m + dim - 1, dim)


def stratified_bound(weights, m, residue):
    source = {p: w for p, w in weights.items()
              if w > 0 and tuple(q % m for q in p) == residue}
    levels = sorted(set([F(0)] + list(source.values())))
    ans = F(0)
    for lo, hi in zip(levels, levels[1:]):
        points = [p for p, w in source.items() if w >= hi]
        ans += (hi - lo) * bound(m, affine_dim(points), len(points))
    mass = sum(source.values(), F(0))
    peak = max(source.values(), default=F(0))
    return ans, m * mass - (m - 1) * peak


def area(poly):
    if not poly:
        return F(0)
    return abs(sum(p[0] * q[1] - p[1] * q[0]
                   for p, q in zip(poly, poly[1:] + poly[:1]))) / 2


def cap_area(z, radius, cap):
    az, bz, ux, uy, threshold = cap
    poly = [(F(0), F(0)), (radius, F(0)), (F(0), radius)]

    def value(p):
        return az * z[0] + bz * z[1] + ux * p[0] + uy * p[1] - threshold

    clipped = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        v, w = value(p), value(q)
        if v >= 0:
            clipped.append(p)
        if (v < 0 < w) or (w < 0 < v):
            t = v / (v - w)
            clipped.append(tuple(a + t * (b - a) for a, b in zip(p, q)))
    return area(clipped)


# C has projection 4 Delta_2 and continuous triangular fibers
# (12-z_1-2z_2) Delta_2. The radius is positive and affine, so this
# is an actual full-dimensional convex body with precisely these bases.
bases = [(x, y) for x in range(5) for y in range(5 - x)]
normals = [(1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (0, 0)]
checks = 0
for az, bz, (ux, uy), threshold in product(
        range(-2, 3), range(-2, 3), normals, [F(0), F(3, 2), F(7), F(13)]):
    if az == bz == ux == uy == 0:
        continue
    cap = (az, bz, ux, uy, threshold)
    weights = {p: cap_area(p, F(12 - p[0] - 2 * p[1]), cap) for p in bases}
    total = sum(weights.values(), F(0))
    for m in (2, 3):
        for residue in product(range(m), repeat=2):
            refined, linear = stratified_bound(weights, m, residue)
            assert total >= refined >= linear, (cap, m, residue, total, refined, linear)
            if m == 2:
                source = {p: w for p, w in weights.items()
                          if w > 0 and tuple(q % 2 for q in p) == residue}
                if source and affine_dim(list(source)) >= 2:
                    # d=2, s=2 specialization of the NEW triangulation bound.
                    assert total >= 2 * sum(source.values()) - max(source.values()) / 2
            checks += 1

# Exact rank-one and unimodular-simplex equalities.
for m in range(2, 9):
    for n in range(1, 15):
        assert bound(m, 1, n + 1) == m * n + 1
    for dim in range(0, 9):
        assert bound(m, dim, dim + 1) == comb(m + dim, dim)

# A strict improvement over the scalar peak correction.
base2 = [(x, y) for x in range(3) for y in range(3 - x)]
weights = {p: F(6 - p[0] - 2 * p[1]) for p in base2}
refined, linear = stratified_bound(weights, 2, (0, 0))
assert sum(weights.values()) == 24 and refined == 20 and linear == 18

# The sharp limiting family for the rank-sensitive triangulation bound.
for d in range(1, 11):
    delta = F(1, 2 ** d)
    for rank in range(2, 13):
        for epsilon in (F(1, 100), F(1, 5), F(1, 2), F(9, 10), F(1)):
            b = epsilon ** d
            c = ((1 + epsilon) / 2) ** d
            source_mass = 1 + rank * b
            total = source_mass + rank * c + comb(rank, 2) * b
            lower = (2 + (rank - 2) * delta) * source_mass - (1 - 2 * delta)
            assert total >= lower

print("PASS:", checks, "exact cap/residue inequalities, including vertical boundary caps")
print("PASS: rank-one and simplex equality formulas; strict profile refinement 20 > 18")
print("PASS: cap triangulation bounds and exact rank-sensitive limiting families")
print("Finite checks only; the general proof is in residue-level-ehrhart-mass-expansion-root.md")
