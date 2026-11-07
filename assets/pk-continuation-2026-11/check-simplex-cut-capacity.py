#!/usr/bin/env python3
"""Exact arithmetic certificates; determinant extremality is proved in the note."""
from fractions import Fraction as F
from math import comb


def retained(d, k, t):
    return sum((F(comb(d, r)) * t**r * (1-t)**(d-r)
                for r in range(k)), F(0))


d, k, t = 5, 3, F(1, 2)
h, s = retained(d, k, t), (1-t)**(d+1-k)
assert h == F(1, 2) and s == F(1, 8)
assert (1-s)**d - (1-h) == F(423, 32768) > 0
assert t == F(k, d+1)  # actual centroid cut

d, k, t = 7, 4, F(2, 5)
h, s = retained(d, k, t), (1-t)**(d+1-k)
q = 1-F(d, d+1)**d
assert h == F(11097, 15625) and s == F(81, 625)
assert h-q == F(3371955119, 32768000000) > 0
assert (1-s)**d - (1-h) == F(3303536184833555664, 37252902984619140625) > 0
print('All exact simplex-cut capacity certificates passed.')
