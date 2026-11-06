"""Exact arithmetic certificates for the simplex cap/stability note."""
from fractions import Fraction as F
from itertools import product
from math import comb, prod

for d in range(1, 13):
    n = d + 1
    gamma = F(d, n) ** d
    assert 1 - F(3, 2*n) >= F(1, 2*n)
    assert sum(comb(d,k) for k in range(2,d+1)) == 2**d-d-1
    assert F((n+1)//2,n) > gamma/2

# Exact product remainders on representative extreme credit arrays.
for d in range(1, 9):
    n = d + 1
    gamma = F(d,n)**d
    a = gamma / 10
    for bits in product((0,1), repeat=n):
        cs = [a*b for b in bits]
        cb = sum(cs)/n
        bary = [F(1,n)+(c-cb)/(n*gamma) for c in cs]
        assert sum(bary) == 1 and min(bary) > 0
        for i in range(n):
            cap_bound = d**d * prod(bary[j] for j in range(n) if j != i)
            rhs = gamma+cb-F(2**d-d-1,1)/gamma*a*a
            assert cap_bound+cs[i] >= rhs

print("PASS: sign margins, normalization, finite remainder, and exact credit samples")
