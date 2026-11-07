"""Exact arithmetic certificate for facet padding; no numerical optimization."""
from fractions import Fraction as F

r = F(1, 10)
epsilon = r**4
V = F(1, 24)
gamma = F(4, 5)**4
old_mass = (1 + 2 * epsilon) * V
beta = (1 + epsilon) / (1 + 2 * epsilon)
added_mass = (3 + 2 * epsilon) * V
total = old_mass + added_mass
assert added_mass == old_mass * (4 * beta - 1)
assert total == 4 * (1 + epsilon) * V
assert old_mass / total * beta == F(1, 4)
assert F(3) + 2 * epsilon < 4

tau = gamma * (1 + epsilon)
assert tau == F(160016, 390625)
assert gamma * total / 4 == tau * V
assert 0 < tau - 2 * epsilon < tau < (1-r)**4

a = F(8000199, 10_000_000)
b = F(7999223, 10_000_000)
assert tau - a**4 == F(2032792963819263760799, 10**28) > 0
assert tau - 2*epsilon - b**4 == F(664183074753367294559, 10**28) > 0
assert 4*a + b - 4 == F(19, 10_000_000) > 0
assert gamma * added_mass / total > gamma / 4

# The projection 0<=u<=1, -1+u<=z<=1-u has these integer points only.
projection_integer_points = [
    (u, z) for u in range(-2, 4) for z in range(-3, 4)
    if 0 <= u <= 1 and -1 + u <= z <= 1-u
]
assert projection_integer_points == [(0, -1), (0, 0), (0, 1), (1, 0)]

print("PASS: exact facet-padding mass and five-cap contradiction certificate")
