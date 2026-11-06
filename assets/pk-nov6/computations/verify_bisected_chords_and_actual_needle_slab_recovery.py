"""Exact polygon checks for the bisected-chord and actual needle notes.

These certify stated examples and independently clip actual polygons.
They are not substitutes for the arbitrary-body proofs.
"""
from fractions import Fraction as F

checks = 0


def check(value):
    global checks
    assert value
    checks += 1


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def area(poly):
    return abs(sum(a[0]*b[1]-a[1]*b[0]
                   for a, b in zip(poly, poly[1:]+poly[:1])))/2


def clip(poly, normal, threshold):
    out = []
    for a, b in zip(poly, poly[1:]+poly[:1]):
        da, db = dot(a, normal)-threshold, dot(b, normal)-threshold
        if da >= 0:
            out.append(a)
        if da*db < 0:
            t = da/(da-db)
            out.append(tuple(a[j]+t*(b[j]-a[j]) for j in (0, 1)))
    return out


def section(poly, normal, threshold=F(0)):
    pts = []
    for a, b in zip(poly, poly[1:]+poly[:1]):
        da, db = dot(a, normal)-threshold, dot(b, normal)-threshold
        if da == 0:
            pts.append(a)
        if da*db < 0:
            t = da/(da-db)
            pts.append(tuple(a[j]+t*(b[j]-a[j]) for j in (0, 1)))
    coordinate = 1 if normal == (1, 0) else 0
    lo = min(p[coordinate] for p in pts)
    hi = max(p[coordinate] for p in pts)
    return lo, hi


normals = ((1, 0), (0, 1), (-1, -1))
c, eps = F(128, 279), F(23, 279)
check(1+1/(2*eps) == F(325, 46))
check(1+3*c/(4*eps) == F(119, 23))
check(F(325, 46) < F(49, 4))
check(F(119, 23) < F(49, 9))

# Noncentrally symmetric triangles with ALL three chords bisected.
# Their centroid need not be zero. Distal truncations preserve the six rays.
feasible = 0
for j in range(0, 31):
    B = 1+F(j, 100)
    tri = [(F(-1), 1-2*B), (2*B/(2*B-1), -B/(2*B-1)),
           (F(-1), 2*B)]
    for denominator in (0, 20, 40, 80):
        poly = tri
        if denominator:
            poly = clip(poly, (-1, 0), -(2*B/(2*B-1)-F(1, denominator)))
        ss = [section(poly, v) for v in normals]
        check(ss == [(-B, B), (F(-1), F(1)), (F(-1), F(1))])
        k = area(poly)
        q = [area(clip(poly, v, F(0))) for v in normals]
        z = clip(clip(poly, (0, -1), F(0)), (1, 1), F(0))
        d = clip(clip(poly, (0, 1), F(0)), (-1, -1), F(0))
        check(q[1]+q[2] == k-area(z)+area(d))
        check(area(d) >= F(1, 2))
        check(area(z) <= B/(2*B-1))
        check(k >= 2*B+1)
        if max(q) <= c*k:
            feasible += 1
            check((2*B)**2 <= 1+1/(2*eps))
            x, y, zz = sorted(q)
            if x+y+zz/4 <= k:
                check((2*B)**2 <= 1+3*c/(4*eps))
check(feasible > 0)

# A collapsing proper-cut family whose selected first chord tends to two,
# while its whole Hausdorff limiting segment has length three.
for denominator in range(5, 106):
    e = F(1, denominator)
    tri = [(-1-e, -1-2*e), (-1+2*e, F(1, 2)), (-1-e, 2+2*e)]
    check(area(tri) == F(9, 2)*e+6*e*e)
    expected = [2+F(8, 3)*e, 12*e*e/(3+4*e), 6*e*e/(3-2*e)]
    for v, length in zip(normals, expected):
        values = [dot(v, x) for x in tri]
        check(min(values) < -1 < max(values))
        lo, hi = section(tri, v, F(-1))
        check(hi-lo == length)

# Actual rational equal-cap needle: every cap is exactly 15/16 of A.
H, e = F(375000, 80987), F(711, 80987)
tri = [(-1-e/3, F(1, 2)+e/6),
       (-1+e, F(1, 2)-e/2-H/2),
       (-1+e, F(1, 2)-e/2+H/2)]
a = area(tri)
check(a == F(177750000, 6558894169))
check((H+e-3)**2 == (H/8)*(H+4*e/3))
for v in normals:
    check(area(clip(tri, v, F(-1))) == F(15, 16)*a)
    values = [dot(v, x) for x in tri]
    check(min(values) < -1 < max(values))
lengths = [hi-lo for lo, hi in [section(tri, v, F(-1)) for v in normals]]
check(lengths == [F(93750, 80987), F(19750, 4778233), F(19750, 4778233)])
weights = [1/(2+2*x) for x in lengths]
p1 = weights[0]/sum(weights)
check(p1 == F(4797983, 25416949))
check(F(2, 9)-p1 == F(7652051, 228752541))
check(2+F(15, 16)*a-F(2, 9)*(9+a) == F(103, 144)*a)
check((tri[0][0]-2)/2 == F(-121599, 80987) < -1)

print(f'PASS: {checks:,} exact actual-polygon and rational checks')
