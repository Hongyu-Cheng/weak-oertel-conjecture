"""Exact certificate: midpoint components need not be lattice-complete.

Only Python standard-library integer and Fraction arithmetic is used.
The 13-point configuration is a five-generator subconfiguration of the
larger candidate found independently by coherent_obstruction.
"""

from fractions import Fraction
from itertools import combinations, product


V = [
    (2, 0, 1),
    (0, -2, 0),
    (2, -2, -1),
    (-1, 3, 0),
    (1, 2, 2),
]

# Every row means n.x <= b.
FACETS = [
    (-10, -2, 9, 4),
    (-5, -1, -10, 2),
    (0, -1, 2, 2),
    (1, -2, 2, 4),
    (4, 3, -3, 5),
    (5, 4, -3, 7),
]

P = [
    (-1, 3, 0),
    (0, -2, 0),
    (0, -1, 0),
    (0, 0, 0),
    (0, 1, 0),
    (1, -1, 0),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 1),
    (1, 2, 2),
    (2, -2, -1),
    (2, -1, 0),
    (2, 0, 1),
]
Q = (1, 0, 1)
C = [p for p in P if p != Q]

# Convex coefficients on the five listed generators, in the order of P.
COEFFICIENTS = [
    ("0", "0", "0", "1", "0"),
    ("0", "1", "0", "0", "0"),
    ("1/22", "8/11", "1/22", "2/11", "0"),
    ("1/11", "5/11", "1/11", "4/11", "0"),
    ("3/22", "2/11", "3/22", "6/11", "0"),
    ("3/11", "4/11", "3/11", "1/11", "0"),
    ("7/22", "1/11", "7/22", "3/11", "0"),
    ("1/3", "1/3", "0", "0", "1/3"),
    ("7/15", "1/15", "0", "1/5", "4/15"),
    ("0", "0", "0", "0", "1"),
    ("0", "0", "1", "0", "0"),
    ("1/2", "0", "1/2", "0", "0"),
    ("1", "0", "0", "0", "0"),
]

EXPECTED_TRIPLES = [
    ((-1, 3, 0), (1, -1, 0), (0, 1, 0)),
    ((0, -2, 0), (0, 0, 0), (0, -1, 0)),
    ((0, -1, 0), (0, 1, 0), (0, 0, 0)),
    ((0, -1, 0), (2, -1, 0), (1, -1, 0)),
    ((0, 1, 0), (2, -1, 0), (1, 0, 0)),
    ((1, 0, 0), (1, 2, 2), (1, 1, 1)),
    ((2, -2, -1), (2, 0, 1), (2, -1, 0)),
]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def determinant(a, b, c):
    return dot(a, cross(b, c))


def parity(p):
    return tuple(x % 2 for x in p)


def main():
    # The hull is three-dimensional and contained in the integer box
    # used below, directly from its generator coordinates.
    assert determinant(*(sub(V[i], V[0]) for i in (1, 2, 3))) != 0
    assert all(-1 <= p[0] <= 2 and -2 <= p[1] <= 3 and -1 <= p[2] <= 2 for p in V)

    # Each inequality is a valid actual supporting facet of the hull.
    for f in FACETS:
        assert all(dot(f[:3], p) <= f[3] for p in V)
        face = [p for p in V if dot(f[:3], p) == f[3]]
        assert any(cross(sub(b, a), sub(c, a)) != (0, 0, 0)
                   for a, b, c in combinations(face, 3))

    # These valid inequalities exclude every unlisted integer point of
    # the containing box. Convex witnesses below prove the reverse
    # inclusion without relying on a floating hull implementation.
    feasible = [
        p for p in product(range(-1, 3), range(-2, 4), range(-1, 3))
        if all(dot(f[:3], p) <= f[3] for f in FACETS)
    ]
    assert feasible == P
    assert len(P) == 13
    for p, row in zip(P, COEFFICIENTS):
        weights = [Fraction(t) for t in row]
        assert min(weights) >= 0 and sum(weights) == 1
        assert all(sum(weights[j] * V[j][i] for j in range(5)) == p[i]
                   for i in range(3))

    # Enumerate ALL unordered pairs of distinct endpoints, not just a
    # hand-selected list of connecting triples.
    triples = []
    for a, b in combinations(P, 2):
        if parity(a) == parity(b):
            middle = tuple((a[i] + b[i]) // 2 for i in range(3))
            assert middle in P
            triples.append((a, b, middle))
    assert triples == EXPECTED_TRIPLES
    assert len(triples) == 7

    parent = {p: p for p in P}

    def find(p):
        while parent[p] != p:
            p = parent[p]
        return p

    def union(a, b):
        parent[find(b)] = find(a)

    for a, b, middle in triples:
        union(a, b)
        union(a, middle)
    components = {}
    for p in P:
        components.setdefault(find(p), set()).add(p)
    assert {frozenset(s) for s in components.values()} == {
        frozenset(C), frozenset([Q])
    }

    # The omitted point is a boundary point, strictly inside a triangular
    # facet. Its vertex-average certificate is particularly simple.
    assert all(Q[i] == Fraction(V[0][i] + V[1][i] + V[4][i], 3)
               for i in range(3))
    slacks = [f[3] - dot(f[:3], Q) for f in FACETS]
    assert slacks == [5, 17, 0, 1, 4, 5]
    assert [p for p in P if dot(FACETS[2][:3], p) == FACETS[2][3]] == [
        (0, -2, 0), Q, (1, 2, 2), (2, 0, 1)
    ]
    assert [p for p in P if parity(p) == parity(Q)] == [Q]
    assert not any(tuple(a[i] + b[i] for i in range(3)) == tuple(2*x for x in Q)
                   for a, b in combinations(P, 2))

    # The component's ordinary difference lattice is already Z^3.
    origin = (0, 0, 0)
    basis = [(1, 0, 0), (0, -1, 0), (1, 1, 1)]
    assert origin in C and all(p in C for p in basis)
    assert determinant(*basis) == -1
    assert Q == tuple(basis[1][i] + basis[2][i] for i in range(3))
    assert all(v in C for v in V)
    assert len({parity(p) for p in C}) == 6
    assert len({parity(p) for p in P}) == 7
    print("PASS: exact five-vertex, 13-point complete lattice base")
    print("PASS: all seven midpoint triples; components of sizes 12 and 1")
    print("PASS: omitted facet centroid; component difference determinant -1")
    print("PASS: no coarser affine lattice or 2-saturation repair can exclude q")


if __name__ == "__main__":
    main()
