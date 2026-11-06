"""Exact rational certificate for the all-uniform-couplings obstruction."""

from fractions import Fraction as F

epsilon = F(1, 2**20)
s = F(3, 128) + epsilon
e = F(32, 125) * s**2
delta = F(128, 125) * epsilon
alpha, beta = 1 - s / 2, s / 2
a0 = F(1, 3) - e / 16
b0 = F(1, 3) - F(41, 125) * e
u, v = F(5, 4) * a0, F(5, 4) * (a0 + b0)

# Areas divided by c=area(T).
a, b, central = 1 + e - delta, e, F(1)
total = a + b + central
assert e == F(604028929, 4294967296000)
assert a == F(32, 125) * (2 - s) ** 2
assert all(w < total / 2 for w in (a, b, central))
assert a > b > 0
assert b + central > total / 2 and a + central > total / 2

# Threshold branches, including the strict event for a possible atom on
# the sum-cap boundary.
assert beta < u < 1
assert 0 < (u - beta) / alpha < 1
assert F(2, 5) < v / alpha < 1
assert F(8, 25) < b0 < 1
assert 0 < a0 < a0 + b0 < 1
assert F(9, 64000) < e < F(1, 6250)
assert F(3, 128) < s < F(1, 40)

tau = F(2, 9) * total
upper_bounds = (
    (1 - a0) ** 2 + e * ((1 - u) / alpha) ** 2,
    (1 - b0) ** 2,
    (a0 + b0) ** 2 + e * (1 - ((alpha - v) / alpha) ** 2 / F(3, 5)),
)
expected_gaps = (
    F(1432514278136662974050522862997520267,
      912835900916101579792855125196800000000000),
    F(2025814712493388791956711,
      2594073385365405696000000000000),
    F(5478570717192890979361486970803017356213,
      8557836571088452310558016798720000000000000000),
)
for i, (bound, expected) in enumerate(zip(upper_bounds, expected_gaps), 1):
    gap = tau - bound
    assert gap == expected
    assert gap > F(6, 10**7)
    print(f"Cap {i}: exact strict gap = {gap}")

print("All area, median, branch, and strict-cap assertions passed exactly.")
