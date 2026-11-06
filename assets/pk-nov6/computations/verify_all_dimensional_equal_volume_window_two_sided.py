"""Exact checks supplementary to the all-dimensional analytical proof."""
from fractions import Fraction as F

checks = 0
r = F(9409, 5184)
assert r == ((F(9, 4) + F(4, 9)) / 2) ** 2
checks += 1
assert (1 - F(27, 64)) * r == F(348133, 331776) > 1
checks += 1
assert F(27, 64) * (2 - r) == F(959, 12288)
checks += 1
assert F(27, 64) * (2 - r) - F(1, 32) == F(575, 12288)
checks += 1

for d in range(1, 501):
    gamma = F(d, d + 1) ** d
    delta = (-57 + 202 * gamma - 121 * gamma ** 2) / 64
    assert F(4, 11) < gamma <= F(1, 2)
    checks += 1
    assert F(55, 7744) <= delta <= F(55, 256)
    checks += 1
    assert delta < gamma * (1 - gamma)
    checks += 1
    constant = 2 * gamma + delta
    assert gamma * constant / (constant + 2 * gamma) > gamma / 2
    checks += 1
    for rr in (F(1), F(9, 8), F(5, 4), F(11, 8)):
        difference = 1 - (1 - gamma) ** 2 * rr ** 2 - gamma * (2 - rr)
        assert difference >= delta
        checks += 1
    if d >= 3:
        assert (1 - gamma) * r > 1
        checks += 1
        assert F(2, (d + 1) ** d) < gamma * (2 - r)
        checks += 1

print(f"PASS: {checks:,} exact window and realized-width-gap checks")
