"""Exact checks for the simplex-frustum and diamond graph examples.

The inequalities and coupling existence are proved in the accompanying
centroid-graph-volume-surplus-and-dominated-mean.md, not by this verifier.
"""
from fractions import Fraction as F

count = 0
for d in range(1, 31):
    old_mean = F(d, d+1)
    for m in range(2, 51):
        t = F(1, m)
        delta = t**d
        a = 1-delta
        new_mean = old_mean*(1-t**(d+1))/a
        shift = new_mean-old_mean
        assert shift == old_mean*delta*(1-t)/(1-delta)
        assert 0 < shift <= delta
        assert shift <= old_mean*delta/(1-delta)
        assert shift <= old_mean
        # Residual is precisely the removed vertex simplex.
        residual_mean = old_mean*t
        assert a*new_mean+delta*residual_mean == old_mean
        count += 1

for m in range(2, 101):
    epsilon = F(1, m)
    mean_left = (1-epsilon)/2
    mean_right = (1+epsilon)/2
    assert mean_right-mean_left == epsilon
    assert epsilon <= epsilon/(1-epsilon)
    assert 1-(1-epsilon) == epsilon

print(f"PASS: {count} rational simplex shifts and 99 diamond graph widths.")
