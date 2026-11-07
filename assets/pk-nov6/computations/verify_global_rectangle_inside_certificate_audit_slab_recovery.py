"""Independent exact audit of the saved all-normal triangle certificate.

Unlike the producer, this does not clip polygons or reconstruct its fan.
It checks direct status-polynomials and proves triangle coverage by exact
containment, pairwise separating axes, and total area.
"""
import json
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def oriented(tri):
    return tri if cross(*tri) > 0 else [tri[0], tri[2], tri[1]]


def separated(a, b):
    for tri, other in [(a, b), (b, a)]:
        for p, q in zip(tri, tri[1:] + tri[:1]):
            if all(cross(p, q, v) <= 0 for v in other):
                return True
    return False


data = json.loads(Path(__file__).with_name(
    "globally_deepest_rectangle_inside_facets_certificate_two_sided.json").read_text())
z = [-2, -1, 0, 1, 2]
r = list(map(F, data["widths"]))
h = list(map(F, data["halfheights"]))
delta, Q, M = map(F, [data["delta"], data["Q"], data["M"]])
check(r == [F(1), F(51, 50), F(51, 50), F(203, 200), F(101, 100)])
check(h == [F(4001, 4000), F(8091, 8000), F(403, 400), F(8029, 8000), F(3999, 4000)])
check(delta == F(1, 4000))
check(M == 2 * sum(w * H for w, H in zip(r, h)))
check(2 * r[2] * h[2] == F(20553, 10000))
sx = sum(w**3 * H for w, H in zip(r, h)) / (12 * sum(w * H for w, H in zip(r, h)))
sy = sum(w * H**3 for w, H in zip(r, h)) / (3 * sum(w * H for w, H in zip(r, h)))
check(sx > 0 and sy > 0 and sx / sy > 0)

groups = {-1: [], 1: []}
labels = {-1: set(), 1: set()}
for entry in data["triangles"]:
    sign = entry["base_sign"]
    check(sign in groups)
    tri = [tuple(map(F, row)) for row in entry["vertices"]]
    check(all(sum(v) == 1 and min(v) >= 0 for v in tri))
    check(cross(*tri) != 0)
    terms = []
    for base, width, height in zip(z, r, h):
        for xsign, ysign in product([-1, 1], repeat=2):
            normal = (xsign * width / 2, ysign * height + delta, sign * base)
            # Inclusion-exclusion signs are positive when the two endpoint
            # signs agree, negative when they differ.
            factor = xsign * ysign
            vals = [dot(normal, v) for v in tri]
            check(min(vals) >= 0 or max(vals) <= 0)
            if max(vals) > 0:
                check(min(vals) >= 0)
                terms.append((factor, normal))
    # Independently expand the polynomial in the six power-basis monomials.
    powers = {}
    for i in range(3):
        for j in range(i, 3):
            powers[i, j] = sum(f * n[i] * n[j] * (1 if i == j else 2)
                               for f, n in terms)
    powers[0, 1] -= 2 * Q
    matrix = [[F(0) for _ in range(3)] for _ in range(3)]
    for (i, j), coefficient in powers.items():
        matrix[i][j] = matrix[j][i] = coefficient if i == j else coefficient / 2
    check(matrix == [list(map(F, row)) for row in entry["matrix"]])
    coefficients = [[sum(matrix[k][l] * a[k] * b[l]
                         for k in range(3) for l in range(3))
                     for b in tri] for a in tri]
    check([coefficients[i][j] for i in range(3) for j in range(i, 3)]
          == list(map(F, entry["bernstein"])))
    check(all(x >= 0 for row in coefficients for x in row))
    for size in [1, 2, 3]:
        for support in combinations(range(3), size):
            if all(coefficients[i][j] == 0 for i in support for j in support):
                check(all(tri[i][0] == 0 for i in support)
                      or all(tri[i][1] == 0 for i in support))
    groups[sign].append(oriented(tri))
    labels[sign].add(entry["cell"])

for sign in [-1, 1]:
    triangles = groups[sign]
    check(sum(cross(*tri) for tri in triangles) == 1)
    for a, b in combinations(triangles, 2):
        check(separated(a, b))
check(len(labels[-1]) == 54 and len(labels[1]) == 56)
check(len(groups[-1]) + len(groups[1]) == 193)


def clamp(x, top):
    return max(F(0), min(top, x))


def mass(a, horizontal):
    if horizontal:
        return sum(2 * H * clamp(w / 2 + a * base, w) for base, w, H in zip(z, r, h))
    return sum(w * clamp(H + a * base + delta, 2 * H) for base, w, H in zip(z, r, h))


for table in data["axis_tables"]:
    horizontal = table["horizontal"]
    knots = {F(0)}
    for base, w, H in zip(z, r, h):
        if base:
            knots.update([w / (2 * base), -w / (2 * base)] if horizontal else
                         [(H - delta) / base, (-H - delta) / base])
    knots = sorted(knots)
    check(knots == list(map(F, table["knots"])))
    values = [mass(a, horizontal) for a in knots]
    check(values == list(map(F, table["masses"])))
    check(min(values) == (Q + F(13, 20000) if horizontal else Q))
    if not horizontal:
        check([a for a, value in zip(knots, values) if value == Q] == [F(-1, 2)])
        j = knots.index(F(-1, 2))
        check((values[j - 1] - Q) / (knots[j] - knots[j - 1]) == F(1, 200))
        check((values[j + 1] - Q) / (knots[j + 1] - knots[j]) == F(3, 200))
    # Analytic tail status: beyond every knot, each nonzero-base interval
    # is full or empty. Verify that already at the extreme knots.
    for a in [knots[0], knots[-1]]:
        for base, w, H in zip(z, r, h):
            if base:
                value, top = (w / 2 + a * base, w) if horizontal else (H + a * base + delta, 2 * H)
                check(value <= 0 or value >= top)

check(h[0] - 1 - delta == 0)
check(h[4] - 1 + delta == 0)
check(2 * r[0] * h[0] + sum(r[i] * (h[i] - F(z[i], 2) + delta) for i in [1, 2, 3]) == Q)
check(all(-h[i] < F(z[i], 2) - delta < h[i] for i in [1, 2, 3]))
other = [2 * r[0] * h[0], 2 * sum(r[i] * h[i] for i in [0, 1]),
         2 * sum(r[i] * h[i] for i in [3, 4]), 2 * r[4] * h[4]]
check(other == [F(4001, 2000), F(812741, 200000), F(3245483, 800000), F(403899, 200000)])
check(all(value < Q for value in other))
check(Q / M == F(8130713, 16281374))
print(f"PASS: {checks:,} independent exact checks; 193 triangles cover both simplices with disjoint interiors")
