#!/usr/bin/env python3
"""Exact scalar checks for the 675-coordinate product construction.

All comparisons use fractions and integer powers.  The compact certificate
records rational enclosing intervals rather than expanding their enormous
power numerators. Geometry and the exponential bound are proved in the note.
"""
from fractions import Fraction as F
import json

epsilon = F(1, 10000)
s = q = F(501, 1000)
t = F(997, 1000)
eta = F(399, 400)
h, N, n, padding_bits = 1684, 225, 675, 14
u = 2 * (1-q)
kappa = (F(1, 3)+epsilon) / (F(1, 3)-epsilon)
m = (2*s)**2 * (2*q)**h / 6
alpha = t**2 * u**h / 6
mlo, mhi = F(483979, 100000), F(24199, 5000)
alo, ahi = F(113789, 20000000), F(284473, 50000000)

assert n == 3*N
assert mlo < m < mhi
assert alo < alpha < ahi

margins = {
    "epsilon_positive": epsilon,
    "epsilon_below_third": F(1, 3)-epsilon,
    "s_above_half": s-F(1, 2),
    "s_below_one": 1-s,
    "outer_scale_positive": t,
    "eta_above_outer_scale": eta-t,
    "eta_below_twice_loss": 2*(1-s)-eta,
    "mixed_type_origin_margin": 3-2*s-2*kappa*t,
    "q_above_half": q-F(1, 2),
    "q_below_one": 1-q,
    "relative_defect_interval_certificate":
        1+n*alo-mhi-mhi/F(2**padding_bits),
    "middle_cut_interval_certificate": F(32, 87)*mlo-F(1, 2)-N*ahi,
    "outer_mass_smaller_than_core": mlo-ahi,
    "exp_series_upper_margin": F(87, 32)-(F(65, 24)+F(1, 100)),
}
for name, value in margins.items():
    assert value > 0, (name, value)

# Check the resulting exact statements as well as their interval certificates.
assert (1+n*alpha-m)/m > F(1, 2**padding_bits)
assert F(1, 2)+N*alpha < F(32, 87)*m
assert alpha < m

report = {
    "status": "all_exact_rational_checks_pass",
    "scope": "scalar hypotheses; full geometry is proved in the companion note",
    "integer_dimension": n,
    "base_continuous_dimension": h+2,
    "padding_dimension": f"2^{n+padding_bits}",
    "final_continuous_dimension": f"{h+2}+2^{n+padding_bits}",
    "copies_per_type": N,
    "parameters": {"epsilon": str(epsilon), "s": str(s), "t": str(t),
                   "eta": str(eta), "q": str(q), "u": str(u), "h": h},
    "exact_power_intervals": {
        "core_ratio": {"expression": "(501/500)^1686/6",
                       "strict_lower": str(mlo), "strict_upper": str(mhi)},
        "outer_ratio": {"expression": "(997/1000)^2*(499/500)^1684/6",
                        "strict_lower": str(alo), "strict_upper": str(ahi)},
    },
    "positive_margins": {
        name: {"numerator": value.numerator, "denominator": value.denominator}
        for name, value in margins.items()
    },
}
print(json.dumps(report, indent=2))
