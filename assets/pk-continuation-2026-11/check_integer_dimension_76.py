#!/usr/bin/env python3
"""Exact compact arithmetic certificate for the n=76 construction.

The only arithmetic used is integer arithmetic and fractions.Fraction.
Positive rational powers are enclosed by outward-rounded fixed-denominator
intervals. The companion note proves the geometry and explains the interval
induction. No floating-point or transcendental evaluation is used.
"""
from fractions import Fraction as F
from math import factorial
import json


def power_interval(base, exponent, digits=40):
    """Return rational lower/upper bounds enclosing base**exponent."""
    assert base > 0 and isinstance(exponent, int) and exponent >= 0
    scale = 10**digits
    lower = base.numerator * scale // base.denominator
    upper = (base.numerator * scale + base.denominator - 1) // base.denominator
    result_lower = result_upper = scale
    while exponent:
        if exponent & 1:
            result_lower = result_lower * lower // scale
            result_upper = (result_upper * upper + scale - 1) // scale
        exponent //= 2
        if exponent:
            lower = lower * lower // scale
            upper = (upper * upper + scale - 1) // scale
    return F(result_lower, scale), F(result_upper, scale)


s, t = F(5000001, 10**7), F(9999997, 10**7)
eta, epsilon = F(3999999, 4000000), F(1, 10**10)
q = F(500001, 10**6)
u = 2 * (1 - q)
h, N, n = 1372128, 19, 76
theta, cap_fraction = F(3, 32), F(27, 64)
kappa = (F(1, 4) + 3 * epsilon) / (F(1, 4) - epsilon)
e_upper = F(27182819, 10**7)
e_series_upper = sum((F(1, factorial(k)) for k in range(11)), F(0)) + F(12, 11 * factorial(11))

free_core = power_interval(2 * q, h)
free_outer = power_interval(u, h)
certified_m = tuple((2 * s)**3 * theta * x for x in free_core)
certified_alpha = tuple(t**3 * theta * x for x in free_outer)

# Intentionally print short enclosures rather than gigantic exact powers.
mlo, mhi = F(1458094201550, 10**12), F(1458094201551, 10**12)
alo, ahi = F(6027739233, 10**12), F(6027739234, 10**12)
assert mlo < certified_m[0] <= certified_m[1] < mhi
assert alo < certified_alpha[0] <= certified_alpha[1] < ahi
assert n == 4 * N

margins = {
    "epsilon_positive": epsilon,
    "epsilon_below_quarter": F(1, 4) - epsilon,
    "s_above_half": s - F(1, 2),
    "s_below_one": 1 - s,
    "q_above_half": q - F(1, 2),
    "q_below_one": 1 - q,
    "t_positive": t,
    "eta_above_t": eta - t,
    "eta_below_two_times_loss": 2 * (1 - s) - eta,
    "singleton_origin_margin": 2 - 2 * s - t,
    "mixed_type_origin_margin": 3 - 2 * s - 2 * kappa * t,
    "exp_series_upper_below_selected_bound": e_upper - e_series_upper,
    "middle_cut_margin_from_enclosures": mlo / e_upper - cap_fraction - N * ahi,
    "mass_defect_from_enclosures": 1 + n * alo - mhi,
    "relative_mass_defect_above_two_to_minus_17": 1 + n * alo - mhi - mhi / 2**17,
    "outer_volume_below_core_from_enclosures": mlo - ahi,
}
for name, value in margins.items():
    assert value > 0, (name, value)

print(json.dumps({
    "status": "all_exact_interval_and_rational_checks_pass",
    "scope": "scalar certificate; analytic geometry is proved in the companion note; not Lean-formalized",
    "integer_dimension": n,
    "copies_per_type": N,
    "source_dimension": 3,
    "free_box_dimension": h,
    "padding_dimension": "2^93",
    "continuous_dimension": "1372131+2^93",
    "parameters": {key: str(value) for key, value in {
        "s": s, "t": t, "eta": eta, "epsilon": epsilon,
        "q": q, "u": u, "theta": theta, "origin_cap_fraction": cap_fraction,
        "e_upper": e_upper,
    }.items()},
    "power_enclosure_decimal_digits": 40,
    "core_volume_ratio_strict_interval": [str(mlo), str(mhi)],
    "outer_volume_ratio_strict_interval": [str(alo), str(ahi)],
    "margins": {name: str(value) for name, value in margins.items()},
}, indent=2))
