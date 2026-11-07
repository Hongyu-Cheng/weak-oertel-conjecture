#!/usr/bin/env python3
"""Exact arithmetic for the continuous-simplex padding counterexample.

The factor dimension ell=2^(n+8) is symbolic: no giant integer is expanded.
The companion note proves the geometric and transcendental inequalities.
"""
from fractions import Fraction as F
import json

r, d0 = 9, 26
s, t, eta = F(100, 101), F(1, 51), F(203, 10302)
N = 25 * (6**9 // 18) * 51**26
n = 3 * N
m = F(2**26, 6**9) * s**26
alpha = t**26 / 6**9
E = 3 * N * alpha
assert E == F(25, 6)
assert n == 25 * 6**8 * 51**26

margins = {
    "s_above_half": s - F(1, 2),
    "s_below_one": 1 - s,
    "outer_scale_positive": t,
    "eta_above_t": eta - t,
    "eta_below_two_times_loss": 2 * (1 - s) - eta,
    "eta_below_one": 1 - eta,
    "origin_group_margin": 3 - 2 * s - 11 * t,
    "cube_cut_margin": 3 - 2 * s - 4 * eta,
    "core_ratio_above_493_over_96": m - F(493, 96),
    "core_ratio_below_3968_over_771": F(3968, 771) - m,
    "middle_cut_deficit_using_32_over_87": F(32, 87) * m - F(17, 9),
    "relative_mass_defect_above_1_over_256": (1 + E - m) / m - F(1, 256),
    "exp_series_bound_below_87_over_32": F(87, 32) - (F(65, 24) + F(1, 100)),
    "outer_volume_below_core_volume": m - alpha,
}
for name, margin in margins.items():
    assert margin > 0, (name, margin)

print(json.dumps({
    "status": "all_exact_rational_checks_pass",
    "scope": "exact rational inputs; padding and exp inequalities are proved in companion note",
    "base_continuous_dimension": d0,
    "integer_dimension": n,
    "copies_per_type": N,
    "padding_dimension": "2^(n+8)",
    "final_continuous_dimension": "26+2^(n+8)",
    "normalized_outside_volume": str(E),
    "normalized_core_volume": str(m),
    "margins": {name: {"numerator": x.numerator, "denominator": x.denominator}
                for name, x in margins.items()},
}, indent=2))
