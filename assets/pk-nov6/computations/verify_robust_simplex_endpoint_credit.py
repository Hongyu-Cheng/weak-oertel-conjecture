"""Exact arithmetic for the explicit robust endpoint-credit error budget.

The geometric proof is in robust-simplex-facet-neighborhood-endpoint-credits.md.
This verifier checks the rational coefficient bounds, not geometric sampling.
"""
from fractions import Fraction as F

# sigma,r <= delta/8, kappa <= delta/24, and r <= 1.
consumed = 2 * F(1, 8) + 2 * F(1, 8) + 6 * F(1, 24)
assert consumed == F(3, 4)
assert 1 - consumed == F(1, 4)

# Retaining the sharper 4*kappa+2*kappa*r error only helps.
for r in (F(0), F(1, 8), F(1)):
    assert 4 + 2 * r <= 6

# The corrected barycentric center sums to one exactly and lies inside
# whenever a/V < gamma; verify on arbitrary representative credit vectors.
for d in range(1, 31):
    n = d + 1
    gamma = F(d, n) ** d
    ratio = gamma / 1000
    credits = [ratio * F(i, n - 1) for i in range(n)]
    average = sum(credits) / n
    bary = [F(1, n) + (c - average) / (n * gamma) for c in credits]
    assert sum(bary) == 1
    assert min(bary) > 0
    assert all(abs(x - F(1, n)) <= ratio / (n * gamma) for x in bary)

print("PASS: robust margin, explicit slack, and barycentric normalization")
