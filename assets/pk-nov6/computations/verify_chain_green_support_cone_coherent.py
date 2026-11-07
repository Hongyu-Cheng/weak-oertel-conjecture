"""Exact rational calibrations for the discrete-base Green-cone theorem.

The all-N/all-d assertions are proved in the companion mathematical note.
This script independently checks kernel identities and actual polygon/cap
first variations, including closed coincident-cap branches.
"""
from fractions import Fraction as F
from itertools import combinations

checks = 0


def check(predicate):
    global checks
    assert predicate
    checks += 1


def green(N, j, i):
    return F(min(i, j) * (N - max(i, j)), N)


for N in range(2, 31):
    for i in range(1, N):
        check(green(N, 0, i) == green(N, N, i) == 0)
        for j in range(1, N):
            check(
                2 * green(N, j, i)
                - green(N, j - 1, i)
                - green(N, j + 1, i)
                == (j == i)
            )
        check(sum(green(N, j, i) for j in range(1, N)) == F(i * (N - i), 2))
        check(
            sum(j * green(N, j, i) for j in range(1, N))
            == F(i * (N - i) * (N + i), 6)
        )
        for a, b in ((F(0), F(1)), (F(1), F(0)), (F(2, 7), F(5, 3))):
            lhs = sum(
                green(N, j, i) * (F(N - j, N) * a + F(j, N) * b)
                for j in range(1, N)
            )
            rhs = F(i * (N - i), 6 * N) * ((2 * N - i) * a + (N + i) * b)
            check(lhs == rhs)
    # A signed endpoint/interior input checks the exact inverse, not positivity.
    e0, eN = F(-2, 5), F(7, 11)
    c = {i: F((-1) ** i * (i + 2), 2 * i + 1) for i in range(1, N)}
    delta = [
        F(N - j, N) * e0
        + F(j, N) * eN
        + sum(green(N, j, i) * c[i] for i in range(1, N))
        for j in range(N + 1)
    ]
    check(delta[0] == e0 and delta[N] == eN)
    for i in range(1, N):
        check(2 * delta[i] - delta[i - 1] - delta[i + 1] == c[i])
    # Positive stress reconstruction and summation by parts.
    s = [F(0)] + [F((i * i + 1) % 7, 5) for i in range(1, N)] + [F(0)]
    q = [-s[1]] + [2 * s[j] - s[j - 1] - s[j + 1] for j in range(1, N)] + [-s[-2]]
    check(sum(q) == 0)
    check(sum(j * q[j] for j in range(N + 1)) == 0)
    check(sum(q[j] * delta[j] for j in range(N + 1)) == sum(s[i] * c[i] for i in range(1, N)))
    for i in range(1, N):
        check(sum(green(N, j, i) * q[j] for j in range(1, N)) == s[i])


def dot(u, x):
    return sum(a * b for a, b in zip(u, x))


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


R = [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1)]


def polygon(offsets):
    pts = []
    for i, j in combinations(range(5), 2):
        a, b = R[i], R[j]
        det = a[0] * b[1] - a[1] * b[0]
        if not det:
            continue
        x = (
            F(offsets[i] * b[1] - offsets[j] * a[1], det),
            F(a[0] * offsets[j] - b[0] * offsets[i], det),
        )
        if all(dot(r, x) <= h for r, h in zip(R, offsets)):
            pts.append(x)
    return hull(pts)


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(poly[k][0] * poly[(k + 1) % len(poly)][1]
                   - poly[k][1] * poly[(k + 1) % len(poly)][0]
                   for k in range(len(poly)))) / 2


def clip(poly, u, b):
    # Closed halfspace u.x >= b.
    out = []
    if not poly:
        return out
    for a, c in zip(poly, poly[1:] + poly[:1]):
        fa, fc = dot(u, a) - b, dot(u, c) - b
        if fa >= 0:
            out.append(a)
        if (fa < 0 < fc) or (fc < 0 < fa):
            lam = fa / (fa - fc)
            out.append(tuple(a[k] + lam * (c[k] - a[k]) for k in range(2)))
    return hull(out)


base_offsets = [[F(0), F(0), F(1), F(1), 1 + F(j, 3)] for j in range(4)]
polys = [polygon(h) for h in base_offsets]
check([area(p) for p in polys] == [F(1, 2), F(7, 9), F(17, 18), F(1)])
check(sum(area(p) for p in polys) == F(29, 9))


def facet(poly, r, h):
    return sorted(x for x in poly if dot(r, x) == h)


def edge_measure_over_normal(edge, r):
    if len(edge) < 2:
        return F(0)
    a, b = edge[0], edge[-1]
    if r[0]:
        return abs((b[1] - a[1]) / r[0])
    return abs((b[0] - a[0]) / r[1])


def cap_edge_fraction(edge, r, j, alpha, u, b):
    a, c = edge[0], edge[-1]
    fa, fc = alpha * j + dot(u, a) - b, alpha * j + dot(u, c) - b
    if fa == fc == 0:
        # Actual outward trace, including a whole-fiber closed boundary.
        return F(dot(u, r) >= 0)
    if min(fa, fc) >= 0:
        return F(1)
    if max(fa, fc) <= 0:
        return F(0)
    positive, negative = (fa, fc) if fa > 0 else (fc, fa)
    return positive / (positive - negative)


def exact_derivative_of_quadratic(vals, h):
    # vals = f(0), f(h), f(2h), on one stable clipping chamber.
    return (4 * vals[1] - vals[2] - 3 * vals[0]) / (2 * h)


def certify_right_chamber(normals, offsets, velocities, endpoint):
    """No candidate-vertex slack changes sign in 0<t<=endpoint.

    Pair-intersection coordinates and all remaining slacks are affine
    in t. Thus this exact check certifies a fixed polygon chamber on
    that right interval, even when the t=0 polygon is degenerate.
    """
    for i, j in combinations(range(len(normals)), 2):
        a, b = normals[i], normals[j]
        det = a[0] * b[1] - a[1] * b[0]
        if not det:
            continue
        x0 = (
            F(offsets[i] * b[1] - offsets[j] * a[1], det),
            F(a[0] * offsets[j] - b[0] * offsets[i], det),
        )
        x1 = (
            F(velocities[i] * b[1] - velocities[j] * a[1], det),
            F(a[0] * velocities[j] - b[0] * velocities[i], det),
        )
        for r, h0, h1 in zip(normals, offsets, velocities):
            slack0, slack1 = h0 - dot(r, x0), h1 - dot(r, x1)
            if slack1:
                root = -slack0 / slack1
                check(not (0 < root <= endpoint))
            else:
                check(True)


caps = [
    (F(2, 7), (F(1), F(-1)), F(1, 9)),
    (F(-1, 5), (F(2), F(3)), F(7, 6)),
    (F(1, 4), (F(-3), F(2)), F(-2, 3)),
    (F(0), (F(1), F(0)), F(1)),      # outside coincident vertical cap
    (F(0), (F(-1), F(0)), F(-1)),    # inside coincident vertical cap
    (F(1), (F(0), F(0)), F(1)),      # closed integer boundary at j=1
    (F(-1), (F(0), F(0)), F(-2)),
]

mass_table = [[F(1), F(1)], [F(1), F(1)], [F(4, 9), F(5, 9)],
              [F(4, 9), F(5, 9)], [F(5, 9), F(4, 9)]]
h = F(1, 10000)
for i in (1, 2):
    for rindex, r in enumerate(R):
        delta = [[F(0)] * 5 for _ in range(4)]
        for j in (1, 2):
            delta[j][rindex] = green(3, j, i)
        for j in range(4):
            certify_right_chamber(R, base_offsets[j], delta[j], 2 * h)
        moved = []
        for t in (F(0), h, 2 * h):
            offsets = [
                [base_offsets[j][l] + t * delta[j][l] for l in range(5)]
                for j in range(4)
            ]
            pp = [polygon(oo) for oo in offsets]
            # Each listed support coordinate is the actual support.
            for j in range(4):
                for l in range(5):
                    check(max(dot(R[l], x) for x in pp[j]) == offsets[j][l])
            # Exact neighbor Minkowski inclusions certify actual fibers.
            for j in (1, 2):
                for x in pp[j - 1]:
                    for y in pp[j + 1]:
                        midpoint = tuple((x[k] + y[k]) / 2 for k in range(2))
                        check(all(dot(rr, midpoint) <= hh for rr, hh in zip(R, offsets[j])))
            moved.append(pp)
        masses = [sum(area(p) for p in pp) for pp in moved]
        slope = exact_derivative_of_quadratic(masses, h)
        check(slope == mass_table[rindex][i - 1])
        predicted_mass = sum(
            edge_measure_over_normal(facet(polys[j], r, base_offsets[j][rindex]), r)
            * delta[j][rindex]
            for j in (1, 2)
        )
        check(slope == predicted_mass)
        for alpha, u, b in caps:
            for j in range(4):
                certify_right_chamber(
                    R + [tuple(-x for x in u)],
                    base_offsets[j] + [alpha * j - b],
                    delta[j] + [F(0)],
                    2 * h,
                )
            vals = [sum(area(clip(pp[j], u, b - alpha * j)) for j in range(4))
                    for pp in moved]
            slope = exact_derivative_of_quadratic(vals, h)
            predicted = F(0)
            for j in (1, 2):
                edge = facet(polys[j], r, base_offsets[j][rindex])
                predicted += (
                    delta[j][rindex]
                    * edge_measure_over_normal(edge, r)
                    * cap_edge_fraction(edge, r, j, alpha, u, b)
                )
            check(slope == predicted)

# Endpoint tangent cone: deterministic feasible and infeasible samples.
endpoint_samples = [
    [F(0), F(0), F(0), F(0), F(1)],
    [F(0), F(0), F(1), F(0), F(0)],
    [F(0), F(0), F(1), F(1), F(1)],
    [F(1), F(2), F(-1), F(3), F(2)],
    [F(0), F(0), F(0), F(0), F(-1)],
    [F(-1), F(-2), F(1), F(-3), F(-2)],
]
for j in (0, 3):
    for eta in endpoint_samples:
        if j == 0:
            predicted = eta[4] - eta[2] + eta[1] >= 0 and eta[4] - eta[3] + eta[0] >= 0
        else:
            predicted = eta[2] + eta[3] - eta[4] >= 0
        offsets = [base_offsets[j][l] + h * eta[l] for l in range(5)]
        pp = polygon(offsets)
        realized = all(max(dot(R[l], x) for x in pp) == offsets[l] for l in range(5))
        check(realized == predicted)

print("PASS", checks, "exact rational checks")
