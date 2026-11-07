"""Exact arithmetic diagnostics; the linked note supplies the general proof."""
from fractions import Fraction as Q

def tail(length, threshold):
    return min(length, max(Q(0), length / 2 - threshold))

def g(a, b, x):
    return min(a, max(Q(0), (a + b) / 2 - 2 * x))

def pair_by_breakpoints(a, b, x):
    # All slope changes of f_a(t)+f_b(2x-t), plus both constant tails.
    pts = [-a / 2, a / 2, 2 * x - b / 2, 2 * x + b / 2]
    pts += [min(pts) - a - b - 1, max(pts) + a + b + 1]
    return min(tail(a, t) + tail(b, 2 * x - t) for t in pts)

def profile(a, b, U, s, x):
    return min(U / 2 + s - x + g(a, b, x),
               U / 2 - s + x + g(a, b, -x))

def maximizer(a, b, s):
    sigma = abs(s)
    if sigma <= (b - a) / 4:
        x = sigma
    elif sigma <= (b + 3 * a) / 4:
        x = sigma / 2 + (b - a) / 8
    else:
        x = sigma - a / 2
    return x if s >= 0 else -x

def formula(a, b, U, s):
    sigma = abs(s)
    if sigma <= (b - a) / 4:
        return U / 2 + a
    if sigma <= (b + 3 * a) / 4:
        return U / 2 - sigma / 2 + (b + 7 * a) / 8
    return (U + a) / 2

def minimum(r):
    if r <= Q(1, 5):
        return 1 / (4 - 2 * r), 1 - 2 * r
    if r <= Q(1, 3):
        return (1 + 5 * r) / (6 * (1 + r)), (1 + r) / 2
    return (1 + 3 * r) / (4 + 6 * r), 1 + 2 * r

checks = 0
for denominator in range(1, 17):
    for numerator in range(1, denominator + 1):
        a, b = Q(numerator, denominator), Q(1)
        target, U_opt = minimum(a)
        assert target > Q(1, 4)
        for U in {(a + b) / 2, b, b + 2 * a, 4 * b, U_opt}:
            if U < (a + b) / 2:
                continue
            S = U / 2 - (a + b) / 4
            for frac in [Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1)]:
                s = frac * S
                xstar = maximizer(a, b, s)
                lo, hi = s - U / 2, s + U / 2
                assert lo <= xstar <= hi
                F = formula(a, b, U, s)
                assert profile(a, b, U, s, xstar) == F
                points = {lo, hi, xstar, Q(0), (b - a) / 4,
                          -(b - a) / 4, (a + b) / 4, -(a + b) / 4}
                points.update(lo + Q(k, 12) * U for k in range(13))
                for x in points:
                    assert pair_by_breakpoints(a, b, x) == g(a, b, x)
                    if lo <= x <= hi:
                        assert profile(a, b, U, s, x) <= F
                        checks += 1
                beta = max(b / 2, F) / (a + b + U)
                assert beta >= target
                if U == U_opt and abs(frac) == 1:
                    assert beta == target
assert minimum(Q(1))[0] == Q(2, 5)
assert minimum(Q(1, 5))[0] == Q(5, 18)
assert minimum(Q(1, 3))[0] == Q(1, 3)
print(f"PASS: {checks} exact cap/profile checks and all extremizing parameters")
