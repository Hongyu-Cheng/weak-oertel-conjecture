#!/usr/bin/env python3
"""Exact checks of the explicit trim certificates and two-slope algebra."""
from fractions import Fraction as F
from math import factorial


def clip(poly, a, b, c):
    """Intersect a rational polygon with a*x+b*y<=c."""
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        vp, vq = a * p[0] + b * p[1] - c, a * q[0] + b * q[1] - c
        if vp <= 0:
            out.append(p)
        if (vp < 0 < vq) or (vq < 0 < vp):
            ratio = vp / (vp - vq)
            out.append((p[0] + ratio * (q[0] - p[0]), p[1] + ratio * (q[1] - p[1])))
    return out


def area(poly):
    return abs(sum(p[0] * q[1] - q[0] * p[1]
                   for p, q in zip(poly, poly[1:] + poly[:1]))) / 2


square = [(F(-1), F(-1)), (F(1), F(-1)), (F(1), F(1)), (F(-1), F(1))]
corner_checks = 0
layer_checks = 0
for den in range(2, 65):
    for num in {1, den // 2, den}:
        t = F(num, den)
        K = clip(square, F(1), F(1), 2 - t)
        mass = area(K)
        assert mass == 4 - t * t / 2
        caps = [clip(K, F(-1), F(0), t * t / 12),
                clip(K, F(0), F(-1), t * t / 12),
                clip(K, F(1), F(1), -t * t / 6)]
        expected = [2 - t * t / 3, 2 - t * t / 3,
                    2 - t * t / 3 + t ** 4 / 72]
        assert list(map(area, caps)) == expected
        loss = F(1, 2) - max(expected) / mass
        assert loss == t * t * (6 - t * t) / (72 * mass) > 0
        # Actual six-base source: the exposing form is z+eta+x+y.
        source_mass = F(0)
        changed = []
        for z in [-1, 0, 1]:
            for eta in [0, 1]:
                fiber = clip(square, F(1), F(1), 4 - t - z - eta)
                fiber_mass = area(fiber)
                source_mass += fiber_mass
                if fiber_mass != 4:
                    changed.append((z, eta))
        assert changed == [(1, 1)] and source_mass == 24 - t * t / 2
        assert 6 / source_mass > F(1, 4)
        corner_checks += 1

for d in range(2, 11):
    for n in range(2, 11):
        w = F(2 ** d)
        M = 3 * 2 ** (n - 1) * w
        beta = F(1, 2 ** n)
        assert w < M / 2 ** n
        for den in [2, 4, 16, 64]:
            t = F(1, den)
            epsilon = t ** d / factorial(d)
            assert (3 * w / 2) / M == beta
            assert (3 * w / 2) / (M - epsilon) > beta
            layer_checks += 1

algebra_checks = 0
for beta in [F(1, 8), F(2, 9), F(1, 3), F(1, 2)]:
    for mask in range(8):
        rho = [F(1, 3), F(2, 5), F(7, 11)]
        plus = [F(2), F(3, 2), F(5, 3)]
        minus = [F(4, 3), F(7, 4), F(9, 5)]
        A = sum(rho[j] / minus[j] for j in range(3) if mask & (1 << j))
        B = sum(rho[j] / plus[j] for j in range(3) if not mask & (1 << j))
        response = beta * B - (1 - beta) * A
        incidence = A / (A + B)
        assert response == (A + B) * (beta - incidence)
        assert (response < 0) == (incidence > beta)
        algebra_checks += 1

print(f"PASS: {corner_checks} exact corner-cap and six-base trims; "
      f"{layer_checks} all-dimensional no-heavy protected-layer cases; "
      f"{algebra_checks} nonsmooth incidence identities.")
