#!/usr/bin/env python3
"""Exact scalar certificate for the 76-integer-coordinate construction.

Large rational powers are enclosed by directed integer rounding at each
operation. All checks use integers or Fraction; no floating arithmetic is
used to establish any inequality. Run with --output PATH to save JSON.
"""

from fractions import Fraction as F
from math import factorial
import argparse
import json


def ceildiv(a, b):
    assert a >= 0 and b > 0
    return (a + b - 1) // b


def power_interval(base, exponent, scale=10**35):
    """Return integer L,U with L/scale <= base**exponent <= U/scale.

    The loop invariant is enclosure of the exact accumulated power and
    exact remaining squared base. Positivity makes every multiplication
    monotone; floor for lower endpoints and ceil for upper endpoints
    preserve that invariant.
    """
    assert base >= 0 and exponent >= 0
    lower = base.numerator * scale // base.denominator
    upper = ceildiv(base.numerator * scale, base.denominator)
    acc_lower = acc_upper = scale
    remaining = exponent
    trace = []
    while remaining:
        if remaining & 1:
            acc_lower = acc_lower * lower // scale
            acc_upper = ceildiv(acc_upper * upper, scale)
        trace.append({
            "remaining": remaining,
            "base_lower": str(lower),
            "base_upper": str(upper),
            "acc_lower": str(acc_lower),
            "acc_upper": str(acc_upper),
        })
        remaining //= 2
        if remaining:
            lower = lower * lower // scale
            upper = ceildiv(upper * upper, scale)
    return F(acc_lower, scale), F(acc_upper, scale), trace


def encode_fraction(value):
    return {"numerator": str(value.numerator),
            "denominator": str(value.denominator)}


def certificate():
    D, N, n, h = 4, 19, 76, 1372126
    epsilon = F(1, 10**10)
    s = q = F(500001, 1000000)
    t = F(999997, 1000000)
    eta = F(399999, 400000)
    u = 2 * (1 - q)
    theta, v = F(3, 32), F(27, 64)
    cmin, cmax = F(1, D) - epsilon, F(1, D) + (D - 1) * epsilon
    kappa = cmax / cmin

    geometric_margins = {
        "epsilon": epsilon,
        "one_over_D_minus_epsilon": F(1, D) - epsilon,
        "s_minus_half": s - F(1, 2),
        "one_minus_s": 1 - s,
        "q_minus_half": q - F(1, 2),
        "one_minus_q": 1 - q,
        "t": t,
        "eta_minus_t": eta - t,
        "two_one_minus_s_minus_eta": 2 * (1 - s) - eta,
        "origin_mixed_type_margin": 3 - 2 * s - 2 * kappa * t,
    }
    assert all(value > 0 for value in geometric_margins.values())
    assert u == 2 * (1 - q)
    assert n == D * N

    m_power_lower, m_power_upper, m_trace = power_interval(2 * q, h + 3)
    a_power_lower, a_power_upper, a_trace = power_interval(u, h)
    m_lower, m_upper = theta * m_power_lower, theta * m_power_upper
    a_lower = theta * t**3 * a_power_lower
    a_upper = theta * t**3 * a_power_upper

    # Short bounds for a human-readable proof; the directed-power bounds
    # above certify these strict rational enclosures.
    mlo = F(1458096242880, 10**12)
    mhi = F(1458096242881, 10**12)
    alo = F(6027714519577, 10**15)
    ahi = F(6027714519578, 10**15)
    assert mlo < m_lower <= m_upper < mhi
    assert alo < a_lower <= a_upper < ahi

    e_upper = F(1359141, 500000)
    e_series_bound = sum((F(1, factorial(j)) for j in range(9)), F(0))
    e_series_bound += F(10, 9 * factorial(9))
    assert e_series_bound < e_upper

    scalar_margins = {
        "mass_defect": 1 + n * alo - mhi,
        "relative_mass_defect_2_pow_18": 1 + n * alo - mhi - mhi / 2**18,
        "middle_cut_below_M_over_e": mlo / e_upper - v - N * ahi,
        "outer_volume_below_core": mlo - ahi,
        "e_upper_minus_series_bound": e_upper - e_series_bound,
    }
    assert all(value > 0 for value in scalar_margins.values())

    return {
        "statement": "Exact scalar certificate for n=76, d=1372129+2^94",
        "parameters": {
            "D": D, "N": N, "n": n, "h": h,
            "base_continuous_dimension": h + D - 1,
            "padding_dimension_power_of_two": n + 18,
            "epsilon": encode_fraction(epsilon),
            "s": encode_fraction(s), "q": encode_fraction(q),
            "t": encode_fraction(t), "eta": encode_fraction(eta),
        },
        "short_bounds": {
            name: encode_fraction(value) for name, value in {
                "m_lower": mlo, "m_upper": mhi,
                "alpha_lower": alo, "alpha_upper": ahi,
                "e_upper": e_upper,
            }.items()
        },
        "geometric_positive_margins": {
            name: encode_fraction(value) for name, value in geometric_margins.items()
        },
        "scalar_positive_margins": {
            name: encode_fraction(value) for name, value in scalar_margins.items()
        },
        "directed_rounding_scale": str(10**35),
        "m_power_trace": m_trace,
        "alpha_power_trace": a_trace,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output")
    args = parser.parse_args()
    result = certificate()
    if args.output:
        with open(args.output, "w", encoding="utf-8") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
    print("PASS: all geometric and scalar inequalities certified by rational arithmetic.")
    print("n=76; d=1372129+2^94; no floating arithmetic in any certificate.")


if __name__ == "__main__":
    main()
