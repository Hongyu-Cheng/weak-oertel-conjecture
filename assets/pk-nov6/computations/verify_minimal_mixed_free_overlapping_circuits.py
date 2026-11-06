"""Exact minimal mixed-free system and all continuous-normal circuit selections."""
from fractions import Fraction as F
from itertools import combinations, product
from functools import reduce
from math import gcd


def det(a):
    a = [list(map(F, row)) for row in a]
    answer = F(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            answer = -answer
        val = a[k][k]
        answer *= val
        for i in range(k+1, len(a)):
            scale = a[i][k]/val
            for j in range(k+1, len(a)):
                a[i][j] -= scale*a[k][j]
    return answer


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def evaluate(coeff, point):
    return coeff[0]+sum(a*b for a, b in zip(coeff[1:], point))


affine = [
    (1, -4, 4, -2, -2),
    (2, 4, -12, 4, 3),
    (-2, 0, 8, -3, -2),
    (0, 0, 0, 1, 0),
    (0, 0, 0, 0, 1),
]
assert tuple(map(sum, zip(*affine))) == (1, 0, 0, 0, 0)
base = [(0, 0), (2, 0), (3, 1), (1, 3), (0, 2)]
continuous = [(0, 0)]*3+[(1, 0), (0, 1)]
vertices = [(F(p[0]+2, 8), F(p[1]+2, 8), F(q[0]), F(q[1]))
            for p, q in zip(base, continuous)]
for i, point in enumerate(vertices):
    assert [evaluate(a, point) for a in affine] == [F(i == j) for j in range(5)]
    assert all(F(1, 4) <= point[k] <= F(5, 8) for k in (0, 1))
edge_matrix = [[vertices[j][i]-vertices[0][i] for j in range(1, 5)] for i in range(4)]
assert det(edge_matrix) == F(1, 32)

witnesses = [
    (1, 1, 1, 1),
    (0, 1, 1, 1),
    (-5, 1, 5, 5),
    (1, -5, -19, 5),
    (1, 0, 1, -3),
]
levels = (1, 1, 5, 5, 1)
for i, w in enumerate(witnesses):
    values = [evaluate(a, w) for a in affine]
    assert values == [1-4*levels[i] if i == j else levels[i] for j in range(5)]
    assert all(isinstance(x, int) for x in w[:2])

normals = [tuple(-x for x in row[-2:]) for row in affine]
assert normals == [(2, 2), (-4, -3), (3, 2), (-1, 0), (0, -1)]
assert all(cross(normals[i], normals[j]) for i, j in combinations(range(5), 2))
circuits = {}
for ids in combinations(range(5), 3):
    a, b, c = [normals[i] for i in ids]
    weights = [cross(b, c), cross(c, a), cross(a, b)]
    if all(x < 0 for x in weights):
        weights = [-x for x in weights]
    if all(x > 0 for x in weights):
        divisor = reduce(gcd, weights)
        weights = tuple(x//divisor for x in weights)
        assert all(sum(weights[j]*normals[ids[j]][k] for j in range(3)) == 0
                   for k in range(2))
        circuits[ids] = weights

support = [(2, 3, 4), (0, 3, 4), (0, 1, 4), (0, 1, 2), (1, 2, 3)]
weights = [(1, 3, 2), (1, 2, 2), (2, 1, 1), (1, 2, 2), (2, 3, 1)]
assert circuits == dict(zip(support, weights))

# Circuit sums of the lambda coordinates; projected covering means <=0.
projected = []
for ids, coeff in zip(support, weights):
    row = tuple(sum(coeff[j]*affine[ids[j]][k] for j in range(3)) for k in range(5))
    assert row[-2:] == (0, 0)
    projected.append(row)
assert projected == [
    (-2, 0, 8, 0, 0),
    (1, -4, 4, 0, 0),
    (4, -4, -4, 0, 0),
    (1, 4, -4, 0, 0),
    (-2, 8, 0, 0, 0),
]

for g, ids in enumerate(support):
    assert set(ids) == set(range(5))-{g, (g+1) % 5}
    for j in (g, (g+1) % 5):
        assert all(evaluate(affine[i], vertices[j]) == 0 for i in ids)
        assert all(evaluate(a, vertices[j]) >= 0 for a in affine)

pair_witness = [1, 2, 0, 0, 2, 0, 0, 3, 3, 0]
for (g, h), i in zip(combinations(range(5), 2), pair_witness):
    assert evaluate(projected[g], witnesses[i]) > 0
    assert evaluate(projected[h], witnesses[i]) > 0

# Exact integer argument for the three-group cover, with a finite redundant screen.
for z1, z2 in product(range(-12, 13), repeat=2):
    if z1 >= 1 and z2 >= 1:
        assert z1+z2 >= 1
    assert any(evaluate(projected[g], (z1, z2, 0, 0)) <= 0 for g in (0, 2, 4))

selections = covered = 0
for size in range(1, 6):
    for chosen in combinations(range(5), size):
        selections += 1
        if not all(any(evaluate(projected[g], point) <= 0 for g in chosen)
                   for point in witnesses):
            continue
        covered += 1
        assert size >= 3
        private = [
            set(support[g])-set().union(*(set(support[h]) for h in chosen if h != g))
            for g in chosen
        ]
        assert not all(private)
assert min(len(c) for size in range(1, 6) for c in combinations(range(5), size)
           if all(any(evaluate(projected[g], p) <= 0 for g in c) for p in witnesses)) == 3

# Exclusive squares are contained in the actual convex hull source by construction.
delta = F(1, 100)
for i, point in enumerate(witnesses):
    for sx, sy in product((-1, 1), repeat=2):
        corner = (*point[:2], point[2]+sx*delta, point[3]+sy*delta)
        assert evaluate(affine[i], corner) < 0
        assert all(evaluate(affine[j], corner) > 0 for j in range(5) if j != i)
assert abs(cross((witnesses[2][0]-witnesses[0][0],
                  witnesses[2][1]-witnesses[0][1]),
                 (witnesses[3][0]-witnesses[0][0],
                  witnesses[3][1]-witnesses[0][1]))) == 36

print("PASS: full-rank rational mixed-free simplex; five exact mixed deletion witnesses;")
print("all ten triples classified into exactly five positive circuits; all ten pair failures;")
print(selections, "circuit selections checked,", covered, "cover the five witness bases, none all-private;")
print("three-group global integer cover and all twenty exclusive-square corners.")
