"""Exact arithmetic audit of the sampled projection volume constants."""

from fractions import Fraction as F
from math import factorial, comb


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


for r in range(1, 7):
    for s in range(1, 7):
        sharp = F(factorial(s), factorial(r + s))
        base_volume = F(1, factorial(r))
        barycentric_moment = (
            base_volume * factorial(r) * factorial(s) / factorial(r + s)
        )
        assert barycentric_moment == sharp
        assert sharp == base_volume / comb(r + s, r)

        # All-positive homothetic vertex fibers on a unimodular simplex.
        for epsilon in [F(0), F(1, 100), F(1, 7), F(1)]:
            integrated = F(0)
            homogeneous = F(0)
            for beta in compositions(s, r + 1):
                monomial = epsilon ** sum(beta[1:])
                homogeneous += monomial
                coefficient = factorial(s)
                for b in beta:
                    coefficient = F(coefficient, factorial(b))
                simplex_integral = F(1, factorial(r + s))
                for b in beta:
                    simplex_integral *= factorial(b)
                integrated += coefficient * simplex_integral * monomial
            assert integrated == sharp * homogeneous
            sampled_mass = 1 + r * epsilon**s
            assert integrated >= sharp * sampled_mass
            if epsilon == 0:
                assert integrated == sharp
            if epsilon == 1:
                assert integrated == base_volume

        c = F(1, sharp)
        for k in range(0, 5):
            for J in range(1, 2**k + 1):
                for eta in [F(0), F(1, 4) / c, F(1, 2) / c]:
                    retained_fraction = 1 - c * eta
                    # Divide out the common positive Gamma_s.
                    depth_factor = retained_fraction / J / 2 ** (r - 1)
                    assert depth_factor >= F(1, 2 ** (k + r))

# Why the s=0 continuation of the displayed formula fails.
for N in range(1, 20):
    h = F(1, N + 3)
    assert N * h < (N + 1) * h

print("PASS: exact Dirichlet coefficients, sharp simplex family, and depth factors.")
