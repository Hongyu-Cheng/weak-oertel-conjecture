from fractions import Fraction as F
from math import prod

P = [(F(-19), F(-18)), (F(19), F(-3)), (F(-4), F(7))]
U = [(1, 0), (0, 1), (-1, -1)]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def clip(poly, normal):
    result = []
    for a, b in zip(poly, poly[1:] + poly[:1]):
        fa = sum(x * u for x, u in zip(a, normal))
        fb = sum(x * u for x, u in zip(b, normal))
        if fa >= 0:
            result.append(a)
        if fa * fb < 0:
            t = fa / (fa - fb)
            result.append(tuple(a[j] + t * (b[j] - a[j]) for j in range(2)))
    return result


def area(poly):
    return abs(sum(cross(a, b) for a, b in zip(poly, poly[1:] + poly[:1]))) / 2


for a, b in zip(P, P[1:] + P[:1]):
    assert cross((b[0] - a[0], b[1] - a[1]), (-a[0], -a[1])) > 0
assert area(P) == F(725, 2)
A = [area(clip(P, u)) for u in U]
T = [area(clip(clip(P, U[(i + 1) % 3]), U[(i + 2) % 3])) for i in range(3)]
S = [A[i] - sum(T) + T[i] for i in range(3)]
assert A == [F(13775, 92), F(1421, 20), F(198505, 848)]
assert T == [F(1681, 80), F(8379, 212), F(14641, 460)]
assert S == [F(83079, 1060), F(6701, 368), F(3471, 20)]
assert min(S + T) > 0
assert sum(S) + sum(T) == area(P)
assert prod(S) / prod(T) == F(214705407501, 22913326051) > 8
assert prod(S) - 8 * prod(T) == F(282589191837, 7801600) > 0
assert sum(T) / min(A) == F(310599, 238924) > 1
print("PASS: exact triangle, all six sectors, product violation, and overlap comparison")
