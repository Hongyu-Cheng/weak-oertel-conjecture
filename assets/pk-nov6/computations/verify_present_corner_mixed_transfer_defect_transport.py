"""Exact checks supporting the proved present-corner mixed transfer.

These finite checks supplement, and do not replace, the quantified proof.
No mixed criticality or realizability of an independently assigned menu is
inferred from the checks.
"""

from fractions import Fraction as F
from itertools import product

checks = 0


def require(condition):
    global checks
    assert condition
    checks += 1


def det(p, q):
    return p[0] * q[1] - p[1] * q[0]


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(det(poly[i], poly[(i + 1) % len(poly)])
                   for i in range(len(poly)))) / 2


def value(p, i):
    return [p[0], p[1], -p[0] - p[1]][i]


def clip(poly, i, threshold):
    result = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        a, b = value(p, i) - threshold, value(q, i) - threshold
        if a >= 0:
            result.append(p)
        if a * b < 0:
            t = a / (a - b)
            result.append(tuple(p[j] + t * (q[j] - p[j]) for j in range(2)))
    return result


def section(poly, i, threshold):
    result = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        a, b = value(p, i) - threshold, value(q, i) - threshold
        if a == 0:
            result.append(p)
        if a * b < 0:
            t = a / (a - b)
            result.append(tuple(p[j] + t * (q[j] - p[j]) for j in range(2)))
    if not result:
        return F(0)
    axis = 1 if i == 0 else 0
    return max(p[axis] for p in result) - min(p[axis] for p in result)


# Actual triangle scale, with canonical determinant D=1.
for aa, p, ix, iy, iz in product(
        [F(1, 4), F(1, 2), F(1), F(2)],
        [F(1, 4), F(1, 2), F(3, 4)],
        [F(1, 4), F(1, 2), F(3, 4)],
        [F(1, 4), F(1, 2), F(3, 4)],
        [F(1, 4), F(1, 2), F(3, 4)]):
    x, y, z = p * ix, (1 - p) * iy, aa * iz
    poly = [(aa, -z), (-x, p), (-y, -(1 - p - y))]
    heights = [aa, p, 1 - p]
    H = sum(heights)
    k = area(poly)
    fractions = [area(clip(poly, i, F(0))) / k for i in range(3)]
    f2 = [4 * (heights[i] / H) ** 2 / fractions[i] for i in range(3)]
    require(4 - sum(f2) == 8 * k / H ** 2 > 0)
    for i in range(3):
        require(section(poly, i, F(0)) * heights[i] == 2 * k * fractions[i])


# Actual proper A cuts and actual nonzero far tails, W=3 for canonical B=T.
for sx, sy, ox, oy in product(
        [F(3), F(4), F(6)], [F(3), F(5), F(7)],
        [F(-2), F(0), F(2)], [F(-2), F(0), F(2)]):
    A = [(ox, oy), (ox + sx, oy), (ox, oy + sy)]
    a = area(A)
    U = [area(clip(A, i, F(-1))) for i in range(3)]
    E = sum(U) - a
    require(E >= 0)
    for i in range(3):
        vals = [value(p, i) for p in A]
        T = area(clip(A, i, F(2)))
        if min(vals) < -1 < max(vals) and T > 0:
            sig = section(A, i, F(-1))
            remain = U[i] - F(3, 2) * sig
            require(remain >= 0 and remain ** 2 >= U[i] * T)
            delta = max(F(0), a - sum(U[j] for j in range(3) if j != i))
            require(T >= delta)
            # U-sqrt(U delta)<=E, with nonnegative squaring only.
            require(U[i] <= E or U[i] * delta >= (U[i] - E) ** 2)


c, lower, rho2 = F(128, 279), F(20, 49), F(119, 279)
delta_max = F(80, 4557)
m_lo, s_hi, rho_hi = F(63887, 100000), F(33867, 50000), F(65309, 100000)
L_lo = F(697, 1000)
require(F(125, 93) - F(65, 49) == delta_max)
require(F(30, 31) * F(201, 400) - L_lo ** 2 == F(14921, 31000000))
den = 1 - 4 * s_hi * delta_max / (3 * lower * L_lo)
require(den > 0)
x_bound = 2 * s_hi / (3 * m_lo * den)
require(x_bound == F(24392142300, 32586905977))
require(F(3, 4) - x_bound == F(192148731, 130347623908) > 0)
require(F(51, 25) * F(3, 4) == F(153, 100))
T = F(153, 100)
require(2 + T - T ** 2 / 4 == F(117791, 40000) < F(59, 20))
require(F(5, 4) * rho2 - c == F(83, 1116) > 0)
require(rho2 < F(2, 3) ** 2 < c)
require(F(133, 100) < F(7, 6) ** 2)
require(F(2, 21) < F(1, 10))
require(4 * rho_hi / (m_lo * L_lo) == F(261236000, 44529239) < 6)
require(m_lo + F(2, 3) > F(13, 10))
require(lower < F(2, 3) ** 2)
require(F(14, 5) ** 2 < 8)
require((2 - F(13, 10) * F(14, 5)) / F(3, 8) == -F(328, 75) < -4)
require(F(3, 4) - F(67, 100) == F(2, 25))
require(F(7, 2) - 4 * F(2, 25) > 0)
require(F(3, 5) * F(7, 2) - 4 == -F(19, 10))
require(-4 * F(3, 5) == -F(12, 5))

print(f"PASS: {checks} exact present-corner geometry and mixed-transfer checks")
