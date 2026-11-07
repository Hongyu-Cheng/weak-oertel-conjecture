"""Exact high-cardinality circuit obstruction, all 27 circuits, and actual masses."""
from fractions import Fraction as F
from itertools import product, combinations


u = [(1, 0), (0, 1), (-1, -1)]
b = [
    [(-1, 4, 4)]*3,
    [(3, -4, 14), (7, -8, -4), (3, -4, 0)],
    [(3, 14, -4), (3, 0, -4), (7, -4, -8)],
]
bases = [(0, 0), (1, 0), (0, 1), (1, 1)]
vertices = [(F(5, 2), -F(5, 4)), (-F(5, 4), F(5, 2)),
            (-F(5, 4), -F(5, 4))]


def threshold(g, i, z):
    c, a, q = b[g][i]
    return c+a*z[0]+q*z[1]


def margin(g, i, z, x):
    return sum(a*c for a, c in zip(u[i], x))-threshold(g, i, z)


expected = [
    [[-1, -1, -1], [3, 7, 3], [3, 3, 7]],
    [[3, 3, 3], [-1, -1, -1], [17, 3, 3]],
    [[3, 3, 3], [17, 3, 3], [-1, -1, -1]],
    [[7, 7, 7], [13, -5, -1], [13, -1, -5]],
]
for z, table in zip(bases, expected):
    assert [[threshold(g, i, z) for i in range(3)] for g in range(3)] == table

labels = list(product(range(3), repeat=2))
for g, i in labels:
    z, x = bases[g], vertices[i]
    assert margin(g, i, z, x) > 0
    assert all(margin(h, j, z, x) < 0 for h, j in labels if (h, j) != (g, i))

# All normal triples: exactly one of each direction is a minimal positive circuit.
def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


circuits = []
for ids in combinations(labels, 3):
    a, q, c = [u[i] for _, i in ids]
    coeff = [cross(q, c), cross(c, a), cross(a, q)]
    positive = all(v > 0 for v in coeff) or all(v < 0 for v in coeff)
    if positive:
        assert sorted(i for _, i in ids) == [0, 1, 2]
        circuits.append(tuple(sorted(ids, key=lambda t: t[1])))
assert len(circuits) == 27
assert set(circuits) == {
    ((g0, 0), (g1, 1), (g2, 2)) for g0, g1, g2 in product(range(3), repeat=3)}
assert all(u[i][0]*u[j][1] != u[i][1]*u[j][0] or
           sum(a*q for a, q in zip(u[i], u[j])) > 0
           for (_, i), (_, j) in combinations(labels, 2))


def circuit_sum(circuit, z):
    return sum(threshold(g, i, z) for g, i in circuit)


required = [tuple((g, i) for i in range(3)) for g in range(3)]
required += [((0, 0), (1, 1), (2, 2))]
for z, wanted in zip(bases, required):
    covering = [c for c in circuits if circuit_sum(c, z) <= 0]
    assert covering == [wanted]
    assert circuit_sum(wanted, z) == -3
    assert all(circuit_sum(c, z) >= 1 for c in circuits if c != wanted)

sums = [tuple(sum(b[g][i][k] for g, i in c) for k in range(3)) for c in required]
assert sums == [(-3, 12, 12), (13, -16, 10), (13, 10, -16), (13, -8, -8)]
assert F(1, 4) < 1 < F(13, 8)
assert 0 < F(3, 26) < F(23, 26) < 1
for z in product(range(-15, 16), repeat=2):
    assert min(circuit_sum(c, z) for c in required) < 0
assert all(threshold(g, i, (F(1, 2), F(1, 2))) >= 1 for g, i in labels)

occurrences = {label: sum(label in c for c in required) for label in labels}
assert all(count >= 1 for count in occurrences.values())
assert sum(count-1 for count in occurrences.values()) == 3
assert all(occurrences[label] == 2 for label in required[3])
assert not set(required[3])-set().union(*(set(c) for c in required[:3]))
assert 4*3-9 == sum(3-len(c) for c in required)+sum(v-1 for v in occurrences.values())

# Exhaustive small abstract incidence check of the general counting identity/bounds.
incidence_cases = 0
ground = set(range(5))
possible = [set(c) for k in (1, 2, 3) for c in combinations(range(5), k)]
for groups in combinations(possible, 3):
    union = set().union(*groups)
    n, s, h, d = len(union), len(groups), 3, 2
    degree = {j: sum(j in g for g in groups) for j in union}
    delta = h*(d+1)-n
    assert delta == ((h-s)*(d+1)+sum(d+1-len(g) for g in groups)
                     +sum(v-1 for v in degree.values()))
    for index, g in enumerate(groups):
        private = g-set().union(*(q for j, q in enumerate(groups) if j != index))
        assert len(private) >= n-(s-1)*(d+1)
    assert sum(v > 1 for v in degree.values()) <= delta
    assert sum(any(degree[j] > 1 for j in g) for g in groups) <= 2*delta
    incidence_cases += 1


def area(poly):
    if not poly:
        return F(0)
    return abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                   -poly[i][1]*poly[(i+1) % len(poly)][0] for i in range(len(poly))))/2


def clip(poly, normal, cut):
    out = []
    for i, p in enumerate(poly):
        q = poly[(i+1) % len(poly)]
        a = sum(x*y for x, y in zip(normal, p))-cut
        c = sum(x*y for x, y in zip(normal, q))-cut
        if a >= 0:
            out.append(p)
        if a < 0 < c or c < 0 < a:
            t = a/(a-c)
            out.append(tuple(p[j]+t*(q[j]-p[j]) for j in range(2)))
    return out


delta = F(1, 100)
square = [(-delta, -delta), (delta, -delta), (delta, delta), (-delta, delta)]
fibers = [vertices]*3+[square]
assert area(vertices) == F(225, 32)
assert area(square) == F(1, 2500)
total = sum(area(k) for k in fibers)
assert total == F(675, 32)+F(1, 2500)
for g, i in labels:
    mass = sum(area(clip(k, u[i], threshold(g, i, z))) for z, k in zip(bases, fibers))
    expected_mass = F(49, 8)+(F(1, 2500) if g in (1, 2) and i in (1, 2) else 0)
    assert mass == expected_mass
    assert 0 < mass < total
    assert mass > F(25, 8)  # These are not critical-depth budgets.
assert F(4, 9)*area(vertices) == F(25, 8)
assert F(25, 8) > total/9

print("PASS: nine strict mixed deletion witnesses, all 27 positive circuits,")
print("four unique forced circuit choices, bounded mixed-free projection inequalities,")
print(incidence_cases, "incidence identities, and all nine exact actual-source cap masses.")
