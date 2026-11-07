"""Exact arithmetic checks for the two unrestricted-depth notes."""
from fractions import Fraction as F
from itertools import product

n, d = 4, 8
N = n + d + 1
eps = F(1, 1000)
V = [(1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1),
     (0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1),
     (1, 1, 1, 0), (1, 1, 0, 1)]
P = [(0,) * n] + [tuple(int(i == j) for i in range(n))
                          for j in range(n)] + V
assert len(set(P)) == N and all(p in set(product((0, 1), repeat=n)) for p in P)
assert eps < min(F(1, N*d*(n-1)), F(1, 2*n*d*(N-1)))
assert sum(sum(v)-1 for v in V) == 10
assert [sum(v[i] for v in V) for i in range(n)] == [5, 5, 4, 4]
assert [F(sum(p[i] for p in P), N) for i in range(n)] == [F(6,13),F(6,13),F(5,13),F(5,13)]
gap = F(8, 9)**8/5 - F(1, 13)
assert gap == F(2870203, 2798036865) > 0

eps = F(1, 10)
fiber_area = 4*eps
total = 2*fiber_area
cap_area = 2*eps*(1+eps)
assert cap_area/total == F(11,40)
assert F(4,13)-cap_area/total == F(17,520) > 0
assert F(2,9) < cap_area/total
assert F(1,3)-F(1,4) == F(1,12)
print('PASS: exact unrestricted binary-lift and mixture obstruction arithmetic')
