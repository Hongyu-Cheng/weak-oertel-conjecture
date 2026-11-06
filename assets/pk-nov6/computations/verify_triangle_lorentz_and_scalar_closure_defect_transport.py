"""Exact rational geometry and constant checks for the triangle theorem.

These checks supplement the general proof in
triangle-cap-chord-lorentz-inequality-and-exact-deficit-defect-transport.md.
They do not replace its quantified scalar argument.
"""

from fractions import Fraction as F
from itertools import product

checks = 0


def require(statement):
    global checks
    assert statement
    checks += 1


def det(p, q):
    return p[0] * q[1] - p[1] * q[0]


def area(poly):
    return abs(sum(det(poly[i], poly[(i + 1) % len(poly)])
                   for i in range(len(poly)))) / 2


def margin(point, i):
    return [point[0], point[1], -point[0] - point[1]][i]


def clip(poly, i):
    result = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        a, b = margin(p, i), margin(q, i)
        if a >= 0:
            result.append(p)
        if (a < 0 < b) or (b < 0 < a):
            t = a / (a - b)
            result.append(tuple(p[j] + t * (q[j] - p[j]) for j in range(2)))
    return result


def chord(poly, i):
    points = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        a, b = margin(p, i), margin(q, i)
        if a == 0:
            points.append(p)
        if a * b < 0:
            t = a / (a - b)
            points.append(tuple(p[j] + t * (q[j] - p[j]) for j in range(2)))
    axis = 1 if i == 0 else 0
    return max(p[axis] for p in points) - min(p[axis] for p in points)


for a, p, ix, iy, iz in product(
        [F(1, 5), F(1, 3), F(1, 2), F(1), F(3, 2)],
        [F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(3, 4)],
        [F(1, 4), F(1, 2), F(3, 4)],
        [F(1, 4), F(1, 2), F(3, 4)],
        [F(1, 4), F(1, 2), F(3, 4)]):
    x, y, z = p * ix, (1 - p) * iy, a * iz
    poly = [(a, -z), (-x, p), (-y, -(1 - p - y))]
    require(all(det(poly[i], poly[(i + 1) % 3]) > 0 for i in range(3)))
    k = area(poly)
    heights = [a, p, 1 - p]
    off = [[F(0), x, y], [z, F(0), 1 - p - y],
           [a - z, p - x, F(0)]]
    q = [area(clip(poly, i)) / k for i in range(3)]
    sigma = [chord(poly, i) for i in range(3)]
    for i in range(3):
        j, l = (i + 1) % 3, (i + 2) % 3
        require(q[i] == heights[i] ** 2 /
                ((heights[i] + off[i][j]) * (heights[i] + off[i][l])))
        require(sigma[i] * heights[i] == 2 * k * q[i])
    total = 1 + a
    aa = [u / total for u in heights]
    bb = [[u / total for u in row] for row in off]
    d = [bb[i][(i + 1) % 3] - bb[i][(i + 2) % 3] for i in range(3)]
    g = [2 * aa[i] + sum(bb[i]) for i in range(3)]
    f2 = [4 * aa[i] ** 2 / q[i] for i in range(3)]
    require(sum(g) == 3)
    for i in range(3):
        j, l = (i + 1) % 3, (i + 2) % 3
        require(g[i] == 1 - d[j] + d[l])
        require(g[i] > abs(d[i]))
        require(f2[i] == g[i] ** 2 - d[i] ** 2)
        require(0 < g[i] < 2)
        require((g[j] + g[l]) ** 2 - (d[j] - d[l]) ** 2 == 8 - 4 * g[i])
        B = g[j] * g[l] + d[j] * d[l]
        require(B > 0)
        require(B ** 2 - f2[j] * f2[l] == (g[j] * d[l] + g[l] * d[j]) ** 2)


c, q0, lower = F(128, 279), F(119, 279), F(20, 49)
require(q0 + 2 * c == F(125, 93))
require(F(4) / c - F(59, 20) ** 2 == F(13, 800))
require(F(71, 100) ** 2 - F(4, 9) * c / lower == F(113951, 25110000))
require(c / q0 < F(26, 25) ** 2)
require(F(51, 25) * F(71, 100) == F(3621, 2500) < F(29, 20))
require(F(2) + F(29, 20) - F(29, 20) ** 2 / 4 == F(4679, 1600) < F(59, 20))
require(F(129, 100) * q0 - c == F(2551, 27900))
rho_upper, s_upper, h_upper = F(65309, 100000), F(33867, 50000), F(57663, 50000)
m_lower, x = F(63887, 100000), F(67, 100)
require(rho_upper ** 2 - q0 == F(9069199, 2790000000000))
require(s_upper ** 2 - c == F(5659231, 697500000000))
require(h_upper ** 2 - F(133, 100) == F(21569, 2500000000))
require(lower - m_lower ** 2 == F(4110319, 490000000000))
require(2 - x * rho_upper - 2 * s_upper * h_upper == F(10269, 78125000))
require(7 * x - 4 * h_upper > 0)
require(4 + m_lower * (7 * x - 4 * h_upper)
        - s_upper * (2 * x + 4 * h_upper) == F(165384, 9765625))
require(7 * m_lower - 2 * s_upper > 0)
require(F(23, 279) > F(4, 49))

theta = F(223, 1000)
coefficient = 2 / theta - 2
require(F(71, 100) ** 2 - 9 * theta ** 2 * c / lower == F(40107, 38750000))
require(coefficient == F(1554, 223))
require(coefficient * x - 4 * h_upper == F(155901, 2787500))
require(4 + m_lower * (coefficient * x - 4 * h_upper)
        - s_upper * (2 * x + 4 * h_upper) == F(975345521, 278750000000))
require(coefficient * m_lower - 2 * s_upper > 0)
require(theta - F(2, 9) == F(7, 9000))

print(f"PASS: {checks} exact actual-triangle and scalar-constant checks")
