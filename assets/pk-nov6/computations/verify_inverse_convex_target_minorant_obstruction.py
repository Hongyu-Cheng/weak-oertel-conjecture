"""Exact arithmetic for the all-uniform-couplings minorant deficit."""
from fractions import Fraction as F

s = F(3, 128) + F(1, 2**20)
e = F(32, 125) * s**2
delta = F(128, 125) * F(1, 2**20)
c = F(1, 2)
a, b = c * (1 + e - delta), c * e
M, W = a + b + c, b + c
gamma = F(4, 9)
alpha, beta = 1 - s / 2, s / 2
a0, b0 = F(1, 3) - e / 16, F(1, 3) - F(41, 125) * e
u, v = F(5, 4) * a0, F(5, 4) * (a0 + b0)
U = (
    (1 - a0)**2 + e * ((1 - u) / alpha)**2,
    (1 - b0)**2,
    (a0 + b0)**2 + e * (1 - ((alpha - v) / alpha)**2 / F(3, 5)),
)
assert all(0 < mass < M / 2 for mass in (a, b, c))
assert a > b
assert W - M / 2 == F(1, 4096000)
for bound in U:
    assert gamma * M / 2 - c * bound > F(3, 10**7)
assert F(3, 10**7) / gamma == F(27, 40000000)
assert W - (M / 2 - F(27, 40000000)) == (
    F(1, 4096000) + F(27, 40000000)
)
print("PASS: nonheavy fibers, exact target slack, three uniform cap gaps,")
print("      retained-mass deficit 27/40000000, and strict loss budget.")
