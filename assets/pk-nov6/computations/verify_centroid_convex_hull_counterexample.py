"""Exact verification of the full fiber-centroid convex hull obstruction.

All operations use Fraction. This verifies a selector counterexample,
not a counterexample to Oertel's conjecture.
"""
from fractions import Fraction as F


def area_centroid(poly):
    twice_area = cx = cy = F(0)
    for p, q in zip(poly, poly[1:] + poly[:1]):
        det = p[0] * q[1] - p[1] * q[0]
        twice_area += det
        cx += (p[0] + q[0]) * det
        cy += (p[1] + q[1]) * det
    if twice_area == 0:
        return F(0), (F(0), F(0))
    return twice_area / 2, (cx / (3 * twice_area), cy / (3 * twice_area))


def clip(poly, normal, threshold):
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        sp = sum(a * b for a, b in zip(normal, p)) - threshold
        sq = sum(a * b for a, b in zip(normal, q)) - threshold
        if sp >= 0:
            out.append(p)
        if sp * sq < 0:
            ratio = sp / (sp - sq)
            out.append(tuple(a + ratio * (b - a) for a, b in zip(p, q)))
    return out


def scale(poly, factor):
    return [tuple(factor * a for a in p) for p in poly]


eta = F(1, 2**20)
s = F(3, 128) + eta
A = [(F(0), F(0)), (F(4, 5), F(0)), (F(0), F(8, 25))]
T = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
fibers = {-1: scale(A, 2 - s), 0: T, 1: scale(A, s)}
areas = {z: area_centroid(poly)[0] for z, poly in fibers.items()}
centroids = {z: area_centroid(poly)[1] for z, poly in fibers.items()}
a, c, b = areas[-1], areas[0], areas[1]
M = a + b + c
target = F(2, 9) * M
e = F(32, 125) * s**2
delta = F(128, 125) * eta

assert all(area > 0 for area in areas.values())
assert c == F(1, 2)
assert b / c == e
assert (a - b) / c == 1 - delta
assert M / c == 2 + 2 * e - delta
assert all(area < M / 2 for area in areas.values())
assert M / 2 - a == F(1, 4096000)
assert F(9, 64000) <= e < F(1, 6250)
assert F(3, 128) < s < F(1, 40)

# Exact middle-fiber containment. The endpoint Minkowski average equals A
# by homothety; direct generator checks independently verify its inclusion in T.
for left in fibers[-1]:
    for right in fibers[1]:
        p = tuple((u + v) / 2 for u, v in zip(left, right))
        assert p[0] >= 0 and p[1] >= 0 and sum(p) <= 1

gA = area_centroid(A)[1]
assert gA == (F(4, 15), F(8, 75))
assert centroids[0] == (F(1, 3), F(1, 3))
assert tuple((u + v) / 2 for u, v in zip(centroids[-1], centroids[1])) == gA
for p in (gA, centroids[0]):
    assert p[0] + p[1] == (22 * p[1] + 4) / 17

h = F(1, 3) - F(17, 52) * e
k = (22 * h + 4) / 17
B = F(8, 25) * (1 - s)
assert F(8, 25) < h < F(1, 3)
assert 0 < k < F(2, 3)
assert gA[1] < h < centroids[0][1]


def full_cap(integer_normal, continuous_normal, threshold):
    return sum(
        area_centroid(clip(poly, continuous_normal, threshold - integer_normal * z))[0]
        for z, poly in fibers.items()
    )


# H_A: y+Bz>=h. H_B: -x-y+2z>=-k.
cap_A = full_cap(B, (F(0), F(1)), h)
cap_B = full_cap(F(2), (F(-1), F(-1)), -k)
assert cap_A == c * (1 - h) ** 2
assert cap_B == c * k**2 + b
assert cap_A < cap_B < target
gap = e / 117 - F(256, 1125) * eta - F(121, 676) * e**2
assert (target - cap_B) / c == gap > F(74, 100000000)

# The segment coverage uses its exact affine equation, not sampled points:
# y>=h places a point in H_A; y<=h and x+y=(22y+4)/17 places it in H_B.
assert k == (22 * h + 4) / 17

# H_-: y-2(z+1)>=(2-s)*8/75.
threshold_minus = F(2) + (2 - s) * F(8, 75)
cap_minus = full_cap(F(-2), (F(0), F(1)), threshold_minus)
assert -2 * (-1) + centroids[-1][1] == threshold_minus
assert cap_minus == F(4, 9) * a < target

# H_+: y+2(z-1)>=s*8/75.
threshold_plus = F(2) + s * F(8, 75)
cap_plus = full_cap(F(2), (F(0), F(1)), threshold_plus)
assert 2 * 1 + centroids[1][1] == threshold_plus
assert cap_plus == F(4, 9) * b < target

print("All exact centroid-convex-hull selector checks passed.")
print("Largest endpoint's area below M/2:", M / 2 - a)
print("Target minus larger middle cap, divided by area(T):", gap)
