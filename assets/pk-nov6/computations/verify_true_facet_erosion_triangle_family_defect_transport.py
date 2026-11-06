"""Exact arithmetic checks complementing, not replacing, the written proof."""
from fractions import Fraction as F

checks = 0


def check(statement):
    global checks
    assert statement
    checks += 1


def dot(u, x):
    return sum(a * b for a, b in zip(u, x))


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(x[0] * y[1] - x[1] * y[0]
                   for x, y in zip(poly, poly[1:] + poly[:1]))) / 2


def clip(poly, u, h):
    out = []
    for x, y in zip(poly, poly[1:] + poly[:1]):
        a, b = dot(u, x) - h, dot(u, y) - h
        if a >= 0:
            out.append(x)
        if a * b < 0:
            t = a / (a - b)
            out.append(tuple(x[j] + t * (y[j] - x[j]) for j in range(2)))
    return out


vs = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(-1))]
for denominator in range(2, 16):
    for numerator in range(1, 3 * denominator + 1):
        L = F(numerator, denominator)
        poly = [(F(2), F(-1)), (F(-1), (1 + L) / 2),
                (F(-1), (1 - L) / 2)]
        us = [(F(-1), F(0)), ((3 + L) / (2 * L), 3 / L),
              ((L - 3) / (2 * L), -3 / L)]
        check(all(sum(u[j] for u in us) == 0 for j in range(2)))
        check(all(max(dot(u, p) for p in poly) == 1 for u in us))
        check(all(min(dot(v, p) for p in poly) == -1 for v in vs))
        check(area(poly) == 3 * L / 2)
        for R in [F(1, 4), F(1, 2), F(2, 3), F(17, 25), F(3, 4)]:
            x = 2 - 3 * R
            source = (x, -x / 2)
            caps = [area(clip(poly, v, dot(v, source))) / area(poly)
                    for v in vs]
            check(caps[0] == R * R)
            check(caps[1] == caps[2])
            if R < 1 - L / 3:
                check(caps[1] == 1 - 9 * R * R / (9 - L * L))
            else:
                check(caps[1] == (L + 3 - 3 * R) ** 2 / (2 * L * (L + 3)))

c = F(128, 279)
check(c < F(17, 25) ** 2)
check(F(16, 33) > c)
check(2 * F(256, 575) + F(289, 2500) == F(57847, 57500))
check(F(57847, 57500) > 1)
check(F(1961, 2025) < F(32, 33))
check(F(551, 576) < F(32, 33))
check(F(25, 551) > F(1, 32))
s = F(5001, 5000)
rho = 2 * s - 1
f = rho ** 2 - (F(13, 8) * rho - 1) ** 2 / 9
check(f / s == F(127640941, 133360000))
check(F(32, 33) - f / s == F(55368947, 4400880000))
check(F(63, 64) ** 2 < F(32, 33))
check(F(65, 4097) < F(1, 63))
check(F(147, 200) ** 2 < F(151, 279))
check(F(9, 50) ** 2 > F(1, 33))
A0, B0, T0 = F(241, 800), F(347, 800), F(41, 100)
check(2 * A0 + T0 - B0 / 63 == 1 + F(283, 50400))
check(F(31329, 69300) > F(65, 144))
check((2 - F(23, 100)) ** 2 / (9 * (1 - F(23, 100)))
      == F(31329, 69300))
check(F(2, 9) * (1 + F(1, 32) + 1) == F(65, 144))


def G(x, y):
    return max(T0 * max(x, y), A0 * max(x, y) + B0 * min(x, y))


for i in range(21):
    for j in range(21):
        p, s = F(i, 20), F(j, 20)
        for r in [F(62, 63), F(125, 126), F(1)]:
            total = G(r, s) + G(p, 1 - s) + G(1 - p, 1 - r)
            check(total >= 2 * A0 + T0 - B0 * (1 - r))
            check(total > 1)
print(f"PASS: {checks} exact checks")
