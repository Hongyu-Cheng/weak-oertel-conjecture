#!/usr/bin/env python3
"""Exact algebra checks for the movable-diagonal note; no numeric optimization."""
from fractions import Fraction as Q
from itertools import product


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def swap(x, r, i):
    out = list(x)
    out[i] = r - sum(x)
    return out


checks = 0
for d in range(1, 6):
    rj = Q(3, 2)
    q = rj / (d + 1)
    for t in (Q(0), q / 2, q, (q + rj / d) / 2, rj / d):
        for p, rp, b in ((-1, Q(1), Q(1, 4)),
                         (0, rj, Q(1, 4)),
                         (1, Q(7, 4), Q(1, 4))):
            assert rp <= rj + b * p
            for raw in product((-2, 0, 1), repeat=d):
                u = tuple(map(Q, raw))
                if min(u) >= 0:
                    continue
                i = u.index(min(u))
                v = [-u[i] if k == i else u[k] - u[i]
                     for k in range(d)]
                S = sum(v)
                assert S > 0 and min(v) >= 0
                w = [x / S for x in v]
                a = Q(2, 7)
                x = [rp * Q(k + 1, d * (d + 1))
                     for k in range(d)]
                sx = swap(x, rp, i)
                candidate = [t] * d
                si = swap(candidate, rj, i)
                assert si[i] == rj - d * t
                L = a * p + dot(u, [v0 - t for v0 in sx])
                identity = a * p + dot(v, [x[k] - si[k]
                                          for k in range(d)])
                identity += u[i] * (rp - rj)
                assert L == identity
                lower = (a + u[i] * b) * p
                lower += dot(v, [x[k] - si[k] for k in range(d)])
                assert lower <= L
                roof = (a / S) * p + dot(w, x) - t
                roof -= w[i] * (rp - (d + 1) * t)
                assert roof == L / S
                inverse = [-w[i] if k == i else w[k] - w[i]
                           for k in range(d)]
                assert inverse == [u0 / S for u0 in u]
                same_point = (a / S - w[i] * b) * p + dot(w, x) - t
                remainder = w[i] * ((d + 1) * t - rj)
                assert same_point + remainder <= roof
                if t >= q:
                    assert min(candidate[k] - si[k]
                               for k in range(d)) >= 0
                    assert same_point <= roof
                else:
                    tp = rj - d * t
                    assert all(t <= z <= tp for z in si)
                checks += 1

# Uniform threshold bounds and converse normals, including distinguished weight zero.
threshold_checks = 0
for d in range(1, 6):
    rj = Q(3, 2)
    for t in (Q(0), rj / (2 * (d + 1)), rj / (d + 1), rj / d):
        for rp in (Q(1, 10), Q(1), Q(7, 4), Q(5)):
            C = max(rj, rp)
            for omega in (Q(0), Q(1, 5), Q(1, 2), Q(1)):
                tau = t + omega * (rp - (d + 1) * t)
                assert abs(tau) <= C and abs(tau - rp) <= C
                threshold_checks += 1
            for i in range(d):
                for k in range(d):
                    w = [Q(int(l == k)) for l in range(d)]
                    u = [-w[i] if l == i else w[l] - w[i]
                         for l in range(d)]
                    assert any(u)
                    x = [rp / (2 * d)] * d
                    a = Q(-3, 11)
                    p = Q(2)
                    margin = a * p + dot(u, [z - t for z in swap(x, rp, i)])
                    roof = a * p + dot(w, x) - t
                    roof -= w[i] * (rp - (d + 1) * t)
                    assert margin == roof


def clip(x):
    return min(Q(1), max(Q(0), x))


# This finite breakpoint calculation is exact for every real tilt in the interval example:
# all pieces are affine and the exterior pieces are constant.
for c in (Q(1), Q(2), Q(5, 2), Q(3), Q(4)):
    knots = {Q(0), 1 - c, -c, c - 1, c}
    knots.update((min(knots) - 1, max(knots) + 1))
    F = [5 - c + clip(1 - c - a) + clip(1 - c + a)
         for a in knots]
    assert min(F) == 5 - c
    assert max(F) == 6 - c
    depth = min(min(F), 7 - max(F), Q(6))
    assert depth == min(5 - c, 1 + c)
    if c == 2:
        assert depth == 3
    if c == 3:
        assert depth == 2

# The two-slope effective tilts share precisely the required gap.
for sm, sp, omega in product((Q(2), Q(1, 3)),
                             (Q(0), Q(-3)),
                             (Q(0), Q(1, 7), Q(1))):
    a = Q(4, 9)
    assert (a - omega * sp) - (a - omega * sm) == omega * (sm - sp) >= 0

print(f"PASS: {checks} exact swap/roof/sign cases; "
      f"{threshold_checks} uniform threshold cases; inverse normals; "
      "all real interval tilts via affine breakpoints; linked two-slope tilts.")
