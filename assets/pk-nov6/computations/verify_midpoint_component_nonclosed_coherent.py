"""Exact obstruction to closedness of midpoint components; not an OC counterexample."""
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd

V = [(0, -1, -1), (-1, 3, 3), (1, 0, -2), (-2, 2, -2), (-2, 2, 0)]
expected = [
    (-2, 2, -2), (-2, 2, -1), (-2, 2, 0),
    (-1, 1, -1), (-1, 1, 0), (-1, 2, 0), (-1, 2, 1), (-1, 3, 3),
    (0, -1, -1), (0, 0, -1), (0, 1, -1), (0, 1, 0), (1, 0, -2),
]
isolated = {(-1, 1, 0), (0, 1, 0)}


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def solve(matrix, rhs):
    a = [[F(x) for x in row] + [F(y)] for row, y in zip(matrix, rhs)]
    n = len(a)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return None
        a[j], a[pivot] = a[pivot], a[j]
        z = a[j][j]
        a[j] = [x/z for x in a[j]]
        for i in range(n):
            if i == j:
                continue
            z = a[i][j]
            a[i] = [x-z*y for x, y in zip(a[i], a[j])]
    return [row[-1] for row in a]


# Supporting facets are exact integer inequalities f[:3] . p <= f[3].
facets = set()
for a, b, c in combinations(V, 3):
    u = cross(sub(b, a), sub(c, a))
    if not any(u):
        continue
    t = dot(u, a)
    values = [dot(u, p)-t for p in V]
    if min(values) < 0 < max(values):
        continue
    if max(values) > 0:
        u, t = tuple(-x for x in u), -t
    common = gcd(*u, t)
    facets.add(tuple(x//common for x in u) + (t//common,))
assert facets == {
    (-8, -7, 5, 2), (-3, -2, 0, 2), (-2, -3, -5, 8),
    (-1, 1, 0, 4), (2, 3, -1, 4), (8, -3, 5, -2),
}

# Every point of conv(V) is in this coordinate box. All candidates in
# the supporting halfspaces are subsequently proved to belong to conv(V)
# by explicit nonnegative rational barycentric representations.
P = [p for p in product(range(-2, 2), range(-1, 4), range(-2, 4))
     if all(dot(f[:3], p) <= f[3] for f in facets)]
assert P == expected
for p in P:
    found = False
    for ids in combinations(range(len(V)), 4):
        matrix = [[1]*4] + [[V[i][j] for i in ids] for j in range(3)]
        weights = solve(matrix, (1,) + p)
        if weights is not None and min(weights) >= 0:
            assert sum(weights) == 1
            assert tuple(sum(w*V[i][j] for w, i in zip(weights, ids))
                         for j in range(3)) == p
            found = True
            break
    assert found, p

parent = {p: p for p in P}


def find(p):
    while parent[p] != p:
        p = parent[p]
    return p


triples = []
for p, q in combinations(P, 2):
    if any((x-y) % 2 for x, y in zip(p, q)):
        continue
    midpoint = tuple((x+y)//2 for x, y in zip(p, q))
    assert midpoint in parent
    root = find(p)
    parent[find(q)] = root
    parent[find(midpoint)] = root
    triples.append((p, q, midpoint))
assert len(triples) == 5
components = {}
for p in P:
    components.setdefault(find(p), set()).add(p)
assert sorted(map(len, components.values())) == [1, 1, 11]
C = next(c for c in components.values() if len(c) == 11)
assert C == set(P) - isolated
assert set(V) <= C
for p in isolated:
    assert components[find(p)] == {p}

# These strictly positive tetrahedral combinations also prove that the
# omitted points are genuine interior points of the common hull.
for p, ids, weights in [
    ((-1, 1, 0), (0, 1, 2, 4), (F(7,20), F(3,20), F(1,20), F(9,20))),
    ((0, 1, 0), (0, 1, 2, 3), (F(1,6), F(11,30), F(13,30), F(1,30))),
]:
    assert sum(weights) == 1 and min(weights) > 0
    matrix = [[1]*4] + [[V[i][j] for i in ids] for j in range(3)]
    assert solve(matrix, (1,) + p) == list(weights)
    assert tuple(sum(w*V[i][j] for w, i in zip(weights, ids))
                 for j in range(3)) == p

parities = [{tuple(x % 2 for x in p) for p in component}
            for component in components.values()]
assert sorted(map(len, parities)) == [1, 1, 6]
assert all(not (a & b) for a, b in combinations(parities, 2))
assert len(set.union(*parities)) == 8
print("PASS: exactly 13 integer points, all with rational hull certificates")
print("PASS: exactly 5 midpoint triples; component sizes 11, 1, 1")
print("PASS: the 11-point component contains all hull vertices but omits two interior integer points")
print("PASS: disjoint parity budgets 6, 1, 1 do not make components closed")
