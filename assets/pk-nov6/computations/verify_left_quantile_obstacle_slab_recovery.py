"""Exact calibration checks for the left-quantile obstacle source.

These finite checks supplement the analytic status-clamping and convexity
proofs; no tilt grid is represented as an all-normal proof.
"""
from fractions import Fraction as F
from itertools import product

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


def interval_mass(margin, h, delta):
    return min(2 * h, max(F(0), h + margin + delta))


vertices = [(0, 0), (1, 0), (0, 1), (1, 1)]
centers = [0, 0, 0, 1]
source = (F(1, 2), F(1, 2), F(1, 4))

for h in [F(1, 16), F(1, 12), F(1, 8), F(1, 6), F(3, 16)]:
    mass = 8 * h
    q = 2 * h
    radius = F(1, 4) - h
    energy = F(1, 2) + 2 * h
    obstacle = mass * radius**2 / energy
    check(radius > 0 and obstacle > 0)
    # The explicit u=1, a=0 tail has Q-plateau [h,1-h].
    for threshold in [h, F(1, 2), 1 - h]:
        raw = sum(interval_mass(F(c) - threshold, h, F(0)) for c in centers)
        check(raw == q)
    check(F(1, 4) - h == radius)
    check(F(1, 4) - (1 - h) < 0)
    for delta in [F(0), radius / 2, radius, radius + h / 4]:
        raw = sum(interval_mass(F(c) - F(1, 4), h, delta) for c in centers)
        check((raw == q) == (delta <= radius))
    # Clipping at all these actual rational tilts confirms the exact pair
    # identities and their analytic full-interval lower bound.
    for a1, a2, u in product([F(i, 8) for i in range(-16, 17)],
                             [F(i, 8) for i in range(-16, 17)], [-1, 1]):
        margins = [a1 * (z[0] - source[0]) + a2 * (z[1] - source[1])
                   + u * (F(c) - source[2])
                   for z, c in zip(vertices, centers)]
        check(margins[0] + margins[3] == F(u, 2))
        check(margins[1] + margins[2] == -F(u, 2))
        check(max(margins) >= F(1, 4))
        for delta in [F(0), radius / 2, radius, radius + h / 4]:
            raw = sum(interval_mass(m, h, delta) for m in margins)
            check(raw >= q)
            check(delta <= radius or raw > q)

# The perspective Hessian is a nonnegative rank-one quadratic form.
for d, x, s, vx, vs in product(range(1, 9), [F(1, 3), F(1), F(5, 2)],
                               [F(1, 4), F(1), F(3)],
                               [F(-2), F(0), F(3, 2)],
                               [F(-1), F(0), F(4)]):
    gxx = d * (d + 1) * x ** (d - 1) / s**d
    gxs = -d * (d + 1) * x**d / s ** (d + 1)
    gss = d * (d + 1) * x ** (d + 1) / s ** (d + 2)
    quadratic = gxx * vx**2 + 2 * gxs * vx * vs + gss * vs**2
    rank_one = d * (d + 1) * x ** (d - 1) / s ** (d + 2) * (s * vx - x * vs)**2
    check(quadratic == rank_one and quadratic >= 0)

check(F(1) * F(1, 8)**2 / F(3, 4) == F(1, 48))
print(f"PASS: {checks:,} exact left-quantile obstacle calibration checks")
