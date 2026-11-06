"""Exact polygon and ordinary-depth certificate for the gluing counterexample.

The finite depth-candidate principle is proved in the companion audit.
Every coordinate, clipping operation, intersection, and area here is rational.
"""

from fractions import Fraction as F


checks = 0


def check(left, right):
    global checks
    assert left == right, (left, right)
    checks += 1


def positive(value):
    global checks
    assert value > 0, value
    checks += 1


def sub(a, b):
    return a[0]-b[0], a[1]-b[1]


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def det(o, a, b):
    return cross(sub(a, o), sub(b, o))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower, upper = [], []
    for point in points:
        while len(lower) >= 2 and det(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    for point in reversed(points):
        while len(upper) >= 2 and det(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1]+upper[:-1]


def area(poly):
    return abs(sum(cross(poly[i-1], poly[i]) for i in range(len(poly))))/2


def clip(poly, normal, threshold=F(0)):
    previous = poly[-1]
    old = sum(previous[j]*normal[j] for j in (0, 1))-threshold
    output = []
    for point in poly:
        new = sum(point[j]*normal[j] for j in (0, 1))-threshold
        if (old >= 0) != (new >= 0):
            t = old/(old-new)
            output.append(tuple(previous[j]+t*(point[j]-previous[j]) for j in (0, 1)))
        if new >= 0:
            output.append(point)
        previous, old = point, new
    return hull(output)


def affine(poly, scale, shift):
    return hull([tuple(scale*p[j]+shift[j] for j in (0, 1)) for p in poly])


def midpoint(left, right):
    return hull([tuple((p[j]+q[j])/2 for j in (0, 1)) for p in left for q in right])


def segment_intersections(a, b, c, d):
    r, s, q = sub(b, a), sub(d, c), sub(c, a)
    denominator = cross(r, s)
    if denominator:
        t, u = cross(q, s)/denominator, cross(q, r)/denominator
        return [tuple(a[j]+t*r[j] for j in (0, 1))] if 0 <= t <= 1 and 0 <= u <= 1 else []
    if cross(q, r):
        return []
    return list({p for p in (a, b, c, d)
                 if all(min(a[j], b[j]) <= p[j] <= max(a[j], b[j])
                        and min(c[j], d[j]) <= p[j] <= max(c[j], d[j]) for j in (0, 1))})


A = [(F(-1), F(2)), (F(-2), F(-1)), (F(2), F(-3)), (F(2), F(-1))]
B = [(F(-13, 8), F(17, 8)), (F(-5, 2), F(-1, 2)),
     (F(3, 2), F(-5, 2)), (F(3, 2), F(-1))]
K = [(F(-21, 16), F(33, 16)), (F(-9, 4), F(-3, 4)),
     (F(7, 4), F(-11, 4)), (F(7, 4), F(-1))]
check(midpoint(A, B), hull(K))
for poly, expected in ((A, F(10)), (B, F(271, 32)), (K, F(1183, 128))):
    check(area(poly), expected)
    for i in range(4):
        positive(det(poly[i-1], poly[i], (F(0), F(0))))

normals = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(-1))]
scales = [F(3, 4), F(17, 16), F(1)]
shifts = [(F(0), F(-1, 4)), (F(-9, 16), F(0)), (F(-1, 2), F(1, 2))]
area_table = [(F(5), F(45, 16), F(245, 64)),
              (F(8, 3), F(289, 96), F(363, 128)),
              (F(55, 8), F(55, 8), F(55, 8))]

for normal, scale, shift, expected in zip(normals, scales, shifts, area_table):
    ac, bc, kc = [clip(poly, normal) for poly in (A, B, K)]
    check(affine(ac, scale, shift), bc)
    check(affine(ac, (1+scale)/2, tuple(v/2 for v in shift)), kc)
    check(midpoint(ac, bc), kc)
    check(tuple(area(poly) for poly in (ac, bc, kc)), expected)
    check(area(bc), scale**2*area(ac))
    check(area(kc), ((1+scale)/2)**2*area(ac))
    check(sum(normal[j]*shift[j] for j in (0, 1)), F(0))
    for cap, whole in zip((ac, bc, kc), (A, B, K)):
        positive(area(cap))
        positive(area(whole)-area(cap))
    assert area(ac)/area(A) != area(bc)/area(B)
    checks += 1

a, b, k = area(A), area(B), area(K)
check(4*k-a-b, F(37, 2))
check((4*k-a-b)**2-4*a*b, F(7, 2))
check(37**2-1355, 14)

depth_data = [
    (A, (F(-3, 2), F(1, 2)), F(5, 2), F(1, 4), (F(1), F(3)),
     [F(25, 6), F(10, 3), F(34, 9), F(18, 7)]),
    (B, (F(-3, 2), F(2)), F(3, 2), F(48, 271), (F(4), F(3)),
     [F(625, 416), F(343, 96), F(27, 16), F(625, 352)]),
    (K, (F(-27, 16), F(15, 16)), F(9, 4), F(288, 1183), (F(5), F(9)),
     [F(343, 128), F(225, 64), F(343, 128), F(7203, 3200)])]

for poly, chord, raw_depth, normalized, min_normal, vertex_values in depth_data:
    intersections = set()
    for i in range(4):
        for j in range(4):
            intersections.update(segment_intersections(
                poly[i-1], poly[i], tuple(-v for v in poly[j-1]), tuple(-v for v in poly[j])))
    check(intersections, {chord, tuple(-v for v in chord)})
    vertex_areas = []
    for vertex in poly:
        cap_area = area(clip(poly, (-vertex[1], vertex[0])))
        vertex_areas.append(min(cap_area, area(poly)-cap_area))
    check(vertex_areas, vertex_values)
    for value in vertex_values:
        positive(value-raw_depth)
    candidates = set(poly) | intersections
    candidate_areas = [area(clip(poly, (sign*(-p[1]), sign*p[0])))
                       for p in candidates for sign in (F(-1), F(1))]
    check(min(candidate_areas), raw_depth)
    check(area(clip(poly, min_normal)), raw_depth)
    check(raw_depth/area(poly), normalized)
    positive(F(4, 9)-normalized)
    for normal in normals:
        positive(area(clip(poly, normal))-raw_depth)

check(area(A)+area(B)+area(K), F(3547, 128))
positive((area(A)+area(B)+area(K))/2-area(A))
for normal, expected in zip(normals, (F(745, 64), F(3269, 384), F(165, 8))):
    check(sum(area(clip(poly, normal)) for poly in (A, B, K)), expected)

# Affine-roof lift: all-dimensional maps are checked by exact coefficient
# identities, while these polygons are the actual truncated projections.
roof_constants = [F(19), F(14), F(33, 2)]
projected_expected = [
    [A[0], A[1], A[2], (F(9, 5), F(-4, 5))],
    [B[0], B[1], B[2], (F(27, 20), F(-17, 20))],
    [K[0], K[1], K[2], (F(63, 40), F(-33, 40))]]
projected = []
for poly, constant, expected in zip((A, B, K), roof_constants, projected_expected):
    projection = clip(poly, (F(-11), F(-1)), -constant)
    projected.append(projection)
    check(projection, hull(expected))
    positive(constant-1)
    positive(11*poly[-1][0]+poly[-1][1]-constant)
    for p in projection:
        assert constant-11*p[0]-p[1] >= 0
        checks += 1
check(midpoint(projected[0], projected[1]), projected[2])

for normal, scale, shift in zip(normals, scales, shifts):
    check(F(14)-11*shift[0]-shift[1], 19*scale)
    check(F(33, 2)-(11*shift[0]+shift[1])/2, 19*(1+scale)/2)
    ac, bc, kc = [clip(poly, normal) for poly in projected]
    check(affine(ac, scale, shift), bc)
    check(affine(ac, (1+scale)/2, tuple(v/2 for v in shift)), kc)
    check(midpoint(ac, bc), kc)
    for cap in (ac, bc, kc):
        positive(area(cap))

ap, bp = projected_expected[:2]
check(sub(ap[2], ap[1]), (F(4), F(-2)))
check(sub(bp[2], bp[1]), (F(4), F(-2)))
check(sub(bp[3], bp[2]), tuple(F(3, 4)*v for v in sub(ap[3], ap[2])))

print(f"PASS: {checks} exact rational checks, including exhaustive polygon-depth candidates and roof lifts")
