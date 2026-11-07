#!/usr/bin/env python3
"""Exact scalar certificate for the 52-integer-variable Boolean-code body.

The construction is in integer-dimension-52-counterexample.md; its complete
geometric proof is accepted fact df488edae05a1702. This script uses rational and
integer arithmetic only; every outward-rounded power step is recorded.
"""

from fractions import Fraction as F
from math import comb, factorial
import json


def power_interval(base, exponent, digits=40):
    assert base > 0 and isinstance(exponent, int) and exponent >= 0
    scale = 10**digits
    lower = base.numerator * scale // base.denominator
    upper = (base.numerator * scale + base.denominator - 1) // base.denominator
    result_lower = result_upper = scale
    trace = []
    initial_exponent = exponent
    while exponent:
        row = {
            "remaining_exponent": exponent,
            "power_interval_scaled": [str(lower), str(upper)],
            "accumulator_before_scaled": [str(result_lower), str(result_upper)],
        }
        if exponent & 1:
            result_lower = result_lower * lower // scale
            result_upper = (result_upper * upper + scale - 1) // scale
        row["accumulator_after_scaled"] = [str(result_lower), str(result_upper)]
        trace.append(row)
        exponent //= 2
        if exponent:
            lower = lower * lower // scale
            upper = (upper * upper + scale - 1) // scale
    return (F(result_lower, scale), F(result_upper, scale)), {
        "base": str(base), "exponent": initial_exponent,
        "scale": str(scale), "trace": trace,
        "result_interval": [str(F(result_lower, scale)), str(F(result_upper, scale))],
    }


def main():
    N, n, h, ell = 13, 52, 274781, 2**61
    theta, beta = F(3, 32), F(27, 64)
    s, t = F(500000001, 10**9), F(999999997, 10**9)
    eta, epsilon, q = F(399999999, 400000000), F(1, 10**12), F(100001, 200000)
    ds, dt, dq = 2*s-1, 1-t, 2*q-1
    e_upper = F(1359141, 500000)
    e_series_upper = sum((F(1, factorial(i)) for i in range(9)), F(0)) + F(10, 9*factorial(9))

    core_interval, core_certificate = power_interval(2*q, h)
    m_interval = tuple(theta*(2*s)**3*x for x in core_interval)
    outer_certificates = []
    E_lower = E_upper = F(0)
    for r in range(1, N+1):
        tr, ur = 1-r*dt, 1-r*dq
        assert tr > 0 and ur > 0
        interval, certificate = power_interval(ur, h)
        alpha_interval = tuple(theta*tr**3*x for x in interval)
        E_lower += 4*comb(N, r)*alpha_interval[0]
        E_upper += 4*comb(N, r)*alpha_interval[1]
        outer_certificates.append({
            "cardinality": r, "multiplicity_per_type": comb(N, r),
            "tetrahedron_scale": str(tr), "free_scale": str(ur),
            "alpha_interval": list(map(str, alpha_interval)),
            "power_certificate": certificate,
        })

    mlo, mhi = F(1463268, 10**6), F(1463269, 10**6)
    Elo, Ehi = F(465669, 10**6), F(465670, 10**6)
    assert mlo < m_interval[0] <= m_interval[1] < mhi
    assert Elo < E_lower <= E_upper < Ehi

    margins = {
        "epsilon_positive": epsilon,
        "epsilon_below_quarter": F(1, 4)-epsilon,
        "s_above_half": s-F(1, 2), "s_below_one": 1-s,
        "q_above_half": q-F(1, 2), "q_below_one": 1-q,
        "t_positive": t, "eta_above_t": eta-t,
        "eta_below_two_times_loss": 2*(1-s)-eta,
        "all_outer_tetrahedron_scales_positive": 1-N*dt,
        "all_outer_free_scales_positive": 1-N*dq,
        "paid_origin_facet_margin": 1-N*(ds+4*epsilon*(3*t+1-ds)),
        "series_upper_below_e_upper": e_upper-e_series_upper,
        "middle_cut_margin": mlo/e_upper-beta-Ehi/4,
        "mass_surplus": 1+Elo-mhi,
        "padding_margin": 1+Elo-mhi-2**n*mhi/(2*ell-1),
        "all_outer_masses_below_core": mlo-theta,
    }
    assert n == 4*N
    assert margins["mass_surplus"] == F(3, 1250)
    for name, value in margins.items():
        assert value > 0, (name, value)

    print(json.dumps({
        "status": "all_exact_interval_and_rational_checks_pass",
        "scope": "Intermediate dimension improvement; above the billion-scale target; not Lean-formalized.",
        "integer_dimension": n, "copies_per_type": N,
        "source_dimension": 3, "free_box_dimension": h,
        "padding_dimension": str(ell),
        "continuous_dimension": str(3+h+ell),
        "parameters": {name: str(value) for name, value in {
            "s": s, "t": t, "eta": eta, "epsilon": epsilon,
            "q": q, "theta": theta, "origin_cap_fraction": beta,
            "delta_s": ds, "delta_t": dt, "delta_q": dq,
            "e_upper": e_upper,
        }.items()},
        "strict_m_interval": list(map(str, (mlo, mhi))),
        "strict_E_interval": list(map(str, (Elo, Ehi))),
        "margins": {name: str(value) for name, value in margins.items()},
        "core_power_certificate": core_certificate,
        "outer_power_certificates": outer_certificates,
    }, indent=2))


if __name__ == "__main__":
    main()
