#!/usr/bin/env python3
"""Exact scalar certificates for source-shaped outer fibers.

The geometric proof is dimension-reduction-exploration.md.  This script
checks its rational hypotheses; it does not enumerate the enormous body.
"""
from fractions import Fraction as F
import json

r = 9
d = 3 * r - 1
s = F(51, 52)
t = F(999, 26000)
eta = F(1999, 52000)
N = 6409 * 10**40
n = 3 * N
gamma = F(d, d + 1)**d
m = F(2**d, 6**r) * s**d
outer = t**d / 6**r
outside = 3 * N * outer

margins = {
    "s_greater_than_half": s - F(1, 2),
    "s_less_than_one": 1 - s,
    "t_positive": t,
    "eta_above_t": eta - t,
    "eta_below_twice_contraction_loss": 2 * (1 - s) - eta,
    "multi_outer_origin_margin": 3 - 2 * s - 11 * t,
    "multi_core_cut_margin": 3 - 2 * s - 4 * eta,
    "eta_less_than_one": 1 - eta,
    "total_mass_defect": 1 + outside - m,
    "origin_cut_deficit": gamma * m - F(1, 2) - N * outer,
    "outer_smaller_than_core": m - outer,
}
assert d == 26 and n == 19227 * 10**40
for name, margin in margins.items():
    assert margin > 0, (name, margin)

report = {
    "status": "all_exact_rational_checks_pass",
    "scope": "scalar hypotheses only; analytic construction is in the companion note",
    "integer_dimension": n,
    "continuous_dimension": d,
    "copies_per_type": N,
    "parameters": {"s": str(s), "t": str(t), "eta": str(eta)},
    "normalized_core_volume": str(m),
    "normalized_single_outer_volume": str(outer),
    "margins": {name: {"numerator": x.numerator, "denominator": x.denominator}
                for name, x in margins.items()},
}
print(json.dumps(report, indent=2))
