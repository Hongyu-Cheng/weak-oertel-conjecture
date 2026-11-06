"""Exact certificate for the all-k deterministic-negative gamma theorem.

No floating-point values or external special functions are used. The
infinite-dimensional ranges are covered analytically in the accompanying
note; this script checks its finite rational residual and cutoff constants.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial


def exp_unit_interval(x):
    """Rigorous rational bounds on exp(-x), 0<=x<=1.

    Degree 32 gives the upper Taylor bound; degree 33 gives the lower.
    """
    assert 0 <= x <= 1
    term = total = F(1)
    for j in range(1, 33):
        term *= -x / j
        total += term
    upper = total
    lower = total + term * (-x / 33)
    assert 0 < lower <= upper
    return lower, upper


E_LO, E_HI = exp_unit_interval(F(1))


@lru_cache(None)
def exp_interval(x):
    """Rigorous bounds on exp(-x) for nonnegative rational x."""
    assert x >= 0
    whole = x.numerator // x.denominator
    remainder = x - whole
    lo, hi = exp_unit_interval(remainder)
    return E_LO**whole * lo, E_HI**whole * hi


def tail_polynomial(k, s):
    return sum(s**j / factorial(j) * (1-F(1, 2**(k-j)))
               for j in range(k))


def scale_interval(coefficient, interval):
    lo, hi = interval
    return ((coefficient*lo, coefficient*hi) if coefficient >= 0
            else (coefficient*hi, coefficient*lo))


def exact_probability_interval(k, p):
    """Bounds G_{k,p} via its exact two-exponential representation."""
    assert k >= 1 and 0 <= p <= 1
    s = k-1+p
    if p == 0:
        return scale_interval(tail_polynomial(k, s), exp_interval(s))
    if p == 1:
        return scale_interval(tail_polynomial(k+1, s), exp_interval(s))
    c = (1-p)/p
    polynomial = F(1)/c
    constant = -F(1)/c
    A = tail_polynomial(k, s)
    B = p / (2**k*(1+p))
    for j in range(k):
        if j:
            polynomial = s**j/c - j*polynomial/c
            constant = -j*constant/c
        weight = F(1, factorial(j)*2**(k-j))
        A += weight*polynomial
        B += weight*constant
    lo_A, hi_A = scale_interval(A, exp_interval(s))
    lo_B, hi_B = scale_interval(B, exp_interval(s/p))
    return lo_A+lo_B, hi_A+hi_B


GRID_CERTIFICATE = {
    1: 459849, 2: 456756,
    3: 456756, 4: 457418, 5: 458844, 6: 460391, 7: 461880,
    8: 463263, 9: 464533, 10: 465695, 11: 466758,
}
grid_checks = 0
for k, certificate in GRID_CERTIFICATE.items():
    intervals = [exact_probability_interval(k, F(j,32)) for j in range(33)]
    for lo, hi in intervals:
        assert 0 < lo <= hi < 1
        assert hi-lo < F(1,10**12)
        # Exact cross-multiplication certificate on EVERY grid point.
        assert 10**6 * lo.numerator >= certificate * lo.denominator
        threshold = F(459,1000) if k == 1 else F(57,125)
        assert F(certificate,10**6) > threshold
        grid_checks += 1
    minimum = min(lo for lo,hi in intervals)
    assert minimum.numerator * 10**6 // minimum.denominator == certificate


def gamma_limit_lower(m):
    Z = sum((2**(m+1)-2**j)*(factorial(m)//factorial(j))*m**j
            for j in range(m+1))
    return F(Z*32**m, 2**(m+1)*factorial(m)*87**m)


TAIL_CERTIFICATE = {
    75: 47899, 76: 47900, 77: 47900, 78: 47900,
    79: 47901, 80: 47901, 81: 47901,
}
gamma_checks = 0
for m in range(11,82):
    lower = gamma_limit_lower(m)
    assert lower >= F(46684,100000)
    if m in TAIL_CERTIFICATE:
        certificate = TAIL_CERTIFICATE[m]
        assert lower.numerator * 100000 // lower.denominator == certificate
    gamma_checks += 1

# Rational gaps in the interval and Taylor steps.
assert F(459,1000)-F(1,128)-F(9,20) == F(19,16000) > 0
assert F(57,125)-F(1,256)-F(9,20) == F(67,32000) > 0
assert F(57,125)-F(1,192)-F(9,20) == F(19,24000) > 0
assert F(46684,100000)-F(1,60)-F(9,20) == F(13,75000) > 0
# Infinite range k>=83: each of the two decreasing error terms is
# bounded by its k=83 value, and the square root inequality is squared
# only after checking the positive right side.
right = F(1,20)-F(1,486)
assert right == F(233,4860) > 0
assert right**2-F(3,16*82) == F(23023,1936807200) > 0

print(f"PASS: {grid_checks} exact grid intervals, {gamma_checks} finite gamma bounds, "
      "all seven extended tail entries, and exact infinite-range gaps")
print("Grid lower certificates /10^6:", GRID_CERTIFICATE)
print("Extended gamma certificates /10^5:", TAIL_CERTIFICATE)
