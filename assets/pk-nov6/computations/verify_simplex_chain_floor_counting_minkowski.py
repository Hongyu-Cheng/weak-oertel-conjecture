"""Exact checks for the analytic two-list counting proof.

No numerical optimization is used. The theorem is proved in the notes;
this script checks integer endpoints and full finite-list event sets.
"""

from fractions import Fraction as F


def floor(x):
    return x.numerator // x.denominator


checks = 0
for k in range(1, 81):
    for denominator in range(1, 41):
        for numerator in range(denominator // 2 + 1):
            b = F(numerator, denominator)
            assert floor(F(k, 2) / (1 - b)) + floor(
                (F(k, 2) - b) / (1 + b)) >= k - 1
            checks += 1

for theta in [F(1, 2), F(3, 5), F(2, 3), F(3, 4), F(9, 10)]:
    for frac in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
        b = (1 - theta) * frac
        for m in range(1, 11):
            for radius_frac in [F(1, 3), F(2, 3), F(1)]:
                a = radius_frac / m
                radii = [1 - a * h for h in range(m + 1)]
                left = [max(F(0), 1 - a * (1 - b) * h / theta)
                        for h in range(m + 1)]
                right = [max(F(0), 1 - a * b / theta -
                             a * (1 + b) * h / theta)
                         for h in range(m + 1)]
                events = sorted(set([F(0), F(1)] + radii + left + right))
                levels = events[1:] + [(x + y) / 2 for x, y in
                                       zip(events, events[1:])]
                for level in levels:
                    assert sum(x >= level for x in left + right) >= \
                        sum(x >= level for x in radii)
                    checks += 1
                for p in range(1, 8):
                    assert sum(x ** p for x in left + right) >= \
                        sum(x ** p for x in radii)
                    checks += 1
                # This is the clipping step with a deterministic C.
                for C in [F(1, 3), F(1), F(3, 2), F(7)]:
                    for p in [1, 2, 3, 5]:
                        total = sum(min(r ** p, (C * x) ** p)
                                    for r, x in zip(radii, left))
                        total += sum(min(r ** p, (C * x) ** p)
                                     for r, x in zip(radii, right))
                        assert total >= min(F(1), C ** p) * \
                            sum(r ** p for r in radii)
                        checks += 1


def poly_integral(coefficients, left, right):
    return sum(c * (right ** (i + 1) - left ** (i + 1)) / (i + 1)
               for i, c in enumerate(coefficients))


# Direct polynomial certificate for the separate low-maximum obstruction.
first = poly_integral([0, -36, 168, -180], F(1, 3), F(1, 2))
second = poly_integral([0, 12, -24, 12], F(1, 2), F(1))
assert first == F(73, 432)
assert second == F(5, 16)
assert first + second == F(13, 27) < F(1, 2)
checks += 3
print(f"PASS: {checks} exact counting, layer-cake, clipping, and integral checks")
