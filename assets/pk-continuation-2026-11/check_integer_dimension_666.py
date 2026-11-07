#!/usr/bin/env python3
"""Exact compact certificate for the earlier three-type n=666 refinement."""
from fractions import Fraction as F
import json

s, t = F(500001, 10**6), F(999997, 10**6)
eta, epsilon = F(399999, 400000), F(1, 10**8)
q, h, N, n = F(10001, 20000), 33666, 222, 666
kappa = (F(1, 3) + epsilon) / (F(1, 3) - epsilon)

# Unreduced integer numerators and denominators: only compact enclosing
# rational intervals, never these large integers, are printed.
m_num, m_den = 2 * 500001**2 * 10001**h, 3 * 10**12 * 10000**h
E_num, E_den = 111 * 999997**2 * 9999**h, 10**12 * 10000**h
mlo, mhi = F(4829177735, 10**9), F(4829177736, 10**9)
Elo, Ehi = F(3829582770, 10**9), F(3829582771, 10**9)
for numerator, denominator, lo, hi in [
    (m_num, m_den, mlo, mhi), (E_num, E_den, Elo, Ehi)
]:
    assert lo.numerator * denominator < numerator * lo.denominator
    assert numerator * hi.denominator < hi.numerator * denominator
assert n == 3 * N

margins = {
    "epsilon_positive": epsilon,
    "epsilon_below_third": F(1, 3) - epsilon,
    "s_above_half": s - F(1, 2),
    "s_below_one": 1 - s,
    "q_above_half": q - F(1, 2),
    "q_below_one": 1 - q,
    "t_positive": t,
    "eta_above_t": eta - t,
    "eta_below_two_times_loss": 2 * (1 - s) - eta,
    "singleton_origin_margin": 2 - 2 * s - t,
    "mixed_type_origin_margin": 3 - 2 * s - 2 * kappa * t,
    "exp_series_margin": F(193, 71) - F(1957, 720) - F(1, 4410),
    "middle_cut_margin": F(71, 193) * mlo - F(1, 2) - Ehi / 3,
    "relative_mass_defect_above_two_to_minus_14": 1 + Elo - mhi - mhi / 2**14,
    "outer_volume_below_core": mlo - Ehi / n,
}
for name, margin in margins.items():
    assert margin > 0, (name, margin)

print(json.dumps({
    "status": "all_exact_rational_checks_pass",
    "scope": "three-source parameter refinement; not Lean-formalized",
    "integer_dimension": n,
    "copies_per_type": N,
    "free_box_dimension": h,
    "padding_dimension": "2^680",
    "continuous_dimension": "33668+2^680",
    "parameters": {key: str(value) for key, value in {
        "s": s, "t": t, "eta": eta, "epsilon": epsilon, "q": q,
    }.items()},
    "core_volume_ratio_strict_interval": [str(mlo), str(mhi)],
    "total_outer_volume_ratio_strict_interval": [str(Elo), str(Ehi)],
    "margins": {name: str(value) for name, value in margins.items()},
}, indent=2))
