"""Exact planar-union tests of peak-Bonnesen; no numerical optimization."""
from fractions import Fraction as F
from itertools import product
from random import Random


def cross(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def hull(points):
    points = sorted(set(points))
    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def area(poly):
    return abs(sum(p[0] * q[1] - p[1] * q[0]
                   for p, q in zip(poly, poly[1:] + poly[:1]))) / 2


def edges(poly):
    result = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        if p[0] == q[0]:
            continue
        slope = (q[1] - p[1]) / (q[0] - p[0])
        result.append((min(p[0], q[0]), max(p[0], q[0]), slope, p[1] - slope * p[0]))
    return result


def union_length(intervals):
    if not intervals:
        return F(0)
    intervals.sort()
    lo, hi = intervals[0]
    total = F(0)
    for left, right in intervals[1:]:
        if left > hi:
            total += hi - lo
            lo, hi = left, right
        else:
            hi = max(hi, right)
    return total + hi - lo


def union_area(polygons):
    # Between all vertex and edge-crossing abscissas, every vertical
    # boundary ordering is fixed. The interval-union length is affine,
    # and its midpoint integral is therefore exact on that slab.
    edge_lists = [edges(poly) for poly in polygons]
    all_edges = [edge for elist in edge_lists for edge in elist]
    breaks = {p[0] for poly in polygons for p in poly}
    for i, (a, b, slope, offset) in enumerate(all_edges):
        for c, d, slope2, offset2 in all_edges[i + 1:]:
            if slope == slope2:
                continue
            x = (offset2 - offset) / (slope - slope2)
            if max(a, c) < x < min(b, d):
                breaks.add(x)
    breaks = sorted(breaks)
    answer = F(0)
    for left, right in zip(breaks, breaks[1:]):
        x = (left + right) / 2
        intervals = []
        for elist in edge_lists:
            ys = [slope * x + offset for a, b, slope, offset in elist if a < x < b]
            if ys:
                intervals.append((min(ys), max(ys)))
        answer += (right - left) * union_length(intervals)
    return answer


square = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]
shifted = [(x + F(1, 2), y + F(1, 2)) for x, y in square]
assert union_area([square, square]) == 1
assert union_area([square, shifted]) == F(7, 4)
assert union_area([square, [(x + 3, y) for x, y in square]]) == 2

rng = Random(641829)
checks = 0
collision_outputs = 0
for base_dim in (1, 2):
    pool = list(product(range(4), repeat=base_dim))
    for modulus, lam in ((2, F(1, 2)), (3, F(1, 3))):
        for trial in range(24):
            sources = []
            for ignored in range(2):
                source = {}
                for base in rng.sample(pool, rng.randint(1, 4)):
                    while True:
                        poly = hull([(F(rng.randint(-7, 7)), F(rng.randint(-7, 7)))
                                     for ignored2 in range(5)])
                        if len(poly) >= 3 and area(poly) > 0:
                            break
                    source[tuple(modulus * z for z in base)] = poly
                sources.append(source)
            a_source, b_source = sources
            a_volumes = [area(poly) for poly in a_source.values()]
            b_volumes = [area(poly) for poly in b_source.values()]
            a, b = max(a_volumes), max(b_volumes)
            effective = sum(a_volumes) / a + sum(b_volumes) / b - 1
            outputs = {}
            for p, ppoly in a_source.items():
                for q, qpoly in b_source.items():
                    base = tuple((1 - lam) * z + lam * w for z, w in zip(p, q))
                    assert all(z.denominator == 1 for z in base)
                    poly = hull([tuple((1 - lam) * z + lam * w for z, w in zip(x, y))
                                 for x in ppoly for y in qpoly])
                    outputs.setdefault(base, []).append(poly)
            collision_outputs += sum(len(polys) > 1 for polys in outputs.values())
            total = sum((union_area(polys) for polys in outputs.values()), F(0))
            gap = total / effective - (1 - lam) ** 2 * a - lam ** 2 * b
            assert gap >= 0 and gap * gap >= 4 * lam ** 2 * (1 - lam) ** 2 * a * b
            checks += 1

print("PASS:", checks, "exact planar peak-Bonnesen inequalities")
print("Distinct output fibers with multiple overlapping polygon inputs:", collision_outputs)
print("Union areas use exact edge arrangements; no input-area overlap was double counted.")
print("The general proof, not these checks, establishes the arithmetic mass lemma.")
