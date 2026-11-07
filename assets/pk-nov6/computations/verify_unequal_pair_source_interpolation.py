"""Exact diagnostics for the universal unequal-copy interpolation theorem.

The analytic proof is in the companion Markdown note. This script uses only
Fraction arithmetic and rigorously enclosing integer-root calculations.
"""
from fractions import Fraction as Q


def clamp(x, a, b):
    return max(a, min(b, x))


def profile_min(d, a, r, s):
    """Exact minimum over shifts and both affine-power orientations."""
    m = Q(d, d + 1) * (1 - a ** (d + 1)) / (1 - a ** d)

    def tail(q):
        return (1 - clamp(m + q, a, Q(1)) ** d) / (1 - a ** d)

    def cost(t):
        return r ** d * tail(t / r) + s ** d * tail(-t / s)

    knots = [r * (a - m), r * (1 - m), s * (m - 1),
             s * (m - a), m * (s - r) / 2]
    values = [r ** d, s ** d] + [cost(t) for t in knots]
    return min(min(values), r ** d + s ** d - max(values))


def root_two_upper(d):
    """A strict rational upper bound on 2**(1/d), within 2**(-100)."""
    den = 2 ** 100
    target = 2 * den ** d
    lo, hi = den, 2 * den
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** d <= target:
            lo = mid
        else:
            hi = mid
    assert lo ** d <= target < hi ** d
    return Q(hi, den)


checks = 0
for d in range(2, 11):
    gamma = Q(d, d + 1) ** d
    assert 2 * gamma < 1
    c_upper = Q(d, d + 1) * root_two_upper(d)
    ratios = sorted(set([Q(1), Q(21, 20), Q(11, 10), Q(3, 2),
                         Q(2), Q(d), Q(d + 1)]))
    for r in [Q(1), Q(3, 2)]:
        for ratio in ratios:
            s = r * ratio
            if s <= d * r:
                alpha = (d * r - s) / (d - 1)
                beta = (s - r) / (d - 1)
                assert alpha >= 0 and beta >= 0
                assert alpha + beta == r
                assert alpha + d * beta == s
                upper = (alpha * c_upper + beta) ** d
                if s == r:
                    exact_endpoint = 2 * gamma * r ** d
                elif s == d * r:
                    exact_endpoint = r ** d
                else:
                    exact_endpoint = None
            else:
                upper = r ** d
                exact_endpoint = upper
            for a in [Q(0), Q(1, 10), Q(1, 3), Q(3, 4), Q(9, 10)]:
                actual = profile_min(d, a, r, s)
                if exact_endpoint is not None:
                    assert actual >= exact_endpoint, (d, a, r, s, actual)
                else:
                    # This is stronger than comparison with the desired bound:
                    # the bound uses c_d, which is strictly below c_upper.
                    assert actual >= upper, (d, a, r, s, actual, upper)
                if s >= d * r:
                    assert actual == r ** d
                checks += 1

for a in [Q(0), Q(1, 3), Q(9, 10)]:
    for r, s in [(Q(1), Q(1)), (Q(2), Q(3)), (Q(1), Q(100))]:
        assert profile_min(1, a, r, s) == r
        checks += 1

# The rational truncation counterexample remains above the new universal bound.
d, a, r, s = 4, Q(1, 3), Q(1), Q(21, 20)
c_upper = Q(4, 5) * root_two_upper(d)
alpha, beta = (4 - s) / 3, (s - 1) / 3
assert profile_min(d, a, r, s) > (alpha * c_upper + beta) ** d

print("PASS: {} exact finite-frustum diagnostics; coefficients, endpoint values,"
      " plateau, d=1, and truncation-counter compatibility.".format(checks))
