"""Exact diagnostics for common-vertex simplex positive-normal reduction."""
from fractions import Fraction as Q
from itertools import combinations, product


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def vertices(d, radius):
    return [(Q(0),) * d] + [
        tuple(radius if i == k else Q(0) for i in range(d))
        for k in range(d)
    ]


swap_checks = 0
for d in range(1, 6):
    radii = {-1: Q(1, 2), 0: Q(3, 2), 1: Q(3, 4)}
    slopes = {-1: Q(1), 0: Q(0), 1: Q(-3, 4)}
    normals = [tuple(Q(i - d) for i in range(d)),
               tuple(Q((-1) ** i * (i + 1)) for i in range(d)),
               (Q(-1),) * d]
    for j, rj in radii.items():
        q = rj / (d + 1)
        b = slopes[j]
        assert all(rp <= rj + b * (p - j) for p, rp in radii.items())
        for normal in normals:
            if min(normal) >= 0:
                continue
            i = min(range(d), key=lambda k: normal[k])
            ui = normal[i]
            new_u = tuple(-ui if k == i else normal[k] - ui for k in range(d))
            assert min(new_u) >= 0 and sum(new_u) > 0
            for a in [Q(-7, 3), Q(0), Q(11, 5)]:
                new_a = a + ui * b
                for p, rp in radii.items():
                    for x in vertices(d, rp) + [(rp / (d + 1),) * d]:
                        sx = list(x)
                        sx[i] = rp - sum(x)
                        ssx = list(sx)
                        ssx[i] = rp - sum(sx)
                        assert tuple(ssx) == x
                        old_swapped = a * (p - j) + dot(
                            normal, tuple(c - q for c in sx))
                        new = new_a * (p - j) + dot(
                            new_u, tuple(c - q for c in x))
                        difference = ui * (rp - rj - b * (p - j))
                        assert old_swapped - new == difference >= 0
                        if p == j and x == (q,) * d:
                            assert tuple(sx) == x and new == 0
                        swap_checks += 1

# One-dimensional saturation is independent of the positive normal.
for d in range(1, 6):
    radii = {-2: Q(2), -1: Q(3), 0: Q(4), 1: Q(5, 2), 2: Q(1)}
    for j, rj in radii.items():
        q = rj / (d + 1)
        B = max(max(q, abs(q - rp)) / abs(p - j)
                for p, rp in radii.items() if p != j)
        for sign in [-1, 1]:
            a = sign * B
            for p, rp in radii.items():
                if p == j:
                    continue
                t = q - a * (p - j)
                if sign * (p - j) > 0:
                    assert t <= 0
                else:
                    assert t >= rp

# Two-dimensional finite-trace replacement via exact polyhedron vertices.
P = list(product(range(-1, 2), repeat=2))
r = {p: Q(3) - Q(abs(p[0]), 2) - Q(abs(p[1]), 3) for p in P}
q = Q(3, 4)
old = (Q(100), Q(-100))
constraints = []
for p in P:
    if p == (0, 0):
        continue
    value = dot(old, p)
    if q - r[p] <= value <= q:
        constraints.append((p, "eq", value))
    elif value > q:
        constraints.append((p, "ge", q))
    else:
        constraints.append((p, "le", q - r[p]))


def feasible(x):
    for row, sense, rhs in constraints:
        value = dot(row, x)
        if sense == "eq" and value != rhs:
            return False
        if sense == "ge" and value < rhs:
            return False
        if sense == "le" and value > rhs:
            return False
    return True


candidate_vertices = []
inverse_norms = []
for c1, c2 in combinations(constraints, 2):
    (a, b), _, e = c1
    (c, d), _, f = c2
    det = a * d - b * c
    if not det:
        continue
    inverse_norms.append(max(abs(d) + abs(b), abs(c) + abs(a)) / abs(det))
    x = ((e * d - b * f) / det, (a * f - e * c) / det)
    if feasible(x):
        candidate_vertices.append(x)
assert candidate_vertices
C = max(max(q, abs(q - rp)) for rp in r.values())
B = C * max(inverse_norms)
for x in candidate_vertices:
    assert max(abs(t) for t in x) <= B

print("PASS: {} exact swap/margin checks, one-dimensional saturation,"
      " and finite two-dimensional replacement vertices.".format(swap_checks))
