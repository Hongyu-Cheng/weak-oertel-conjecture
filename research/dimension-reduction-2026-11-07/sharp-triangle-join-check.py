"""Exact rational certificate for the n=132, d=99 sharp-bound example."""

from fractions import Fraction as F
from math import comb
import json
from pathlib import Path


d, N, n, cutoff = 99, 44, 132, 30
D = d + 1
a, delta, epsilon = F(63, 100), F(329, 10000), F(1, 10**13)
Q = 1 - a + a * a
eta = (1 - delta) / 2
v = delta / D + (1 - delta) * a * epsilon / Q
theta_p = a / (3 * (1 + a))
theta_a = (a / (1 + a) + (1 - a) / (2 - a)) / 3
beta = 1 / ((1 + a) * (2 - a))
gamma = F(d, D) ** d
m = theta_p * (1 + delta) ** d
alpha = [theta_a * (1 - r * D * v) ** d for r in range(1, cutoff + 1)]
E = 3 * sum(comb(N, r) * alpha[r - 1] for r in range(1, cutoff + 1))

assert n == 3 * N and 1 <= cutoff <= N
assert F(1, 2) < a < 1 and 0 < delta < 1 and 0 < eta < 1 - delta
margins = {
    "center_root_weight": epsilon / a,
    "center_edge_weight": epsilon * (2 * a - 1) * (1 + a) / (a * Q),
    "center_common_weight": F(3, D) - 3 * a * epsilon / Q,
    "center_free_weight": F(1, D),
    "center_min_coordinate": F(1, D) - a * epsilon / Q,
    "largest_negative_scale": 1 - cutoff * D * v,
    "unpaid_positive_cut_gap_coefficient": 1 - eta - delta,
    "volume_surplus": 1 + E - m,
    "origin_cut": gamma * m - beta - E / 3,
    "whole_negative_fiber": gamma * m - alpha[0],
}
assert all(value > 0 for value in margins.values())
assert 2 * epsilon < 1 and eta * epsilon < 1
assert all(0 < alpha[r] <= alpha[0] for r in range(cutoff))


def rational(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


report = {
    "status": "Exact rational inequalities passed; geometry is proved in the companion note.",
    "dimensions": {"n": n, "d": d, "N": N, "negative_subset_cutoff": cutoff},
    "parameters": {name: rational(value) for name, value in {
        "a": a, "delta": delta, "epsilon": epsilon, "eta": eta, "Q": Q, "v": v,
    }.items()},
    "quantities": {name: rational(value) for name, value in {
        "theta_positive": theta_p, "theta_negative": theta_a, "beta": beta,
        "Gamma_d": gamma, "m": m, "E": E,
    }.items()},
    "strict_positive_margins": {name: rational(value) for name, value in margins.items()},
    "negative_fiber_ratios": [rational(value) for value in alpha],
    "decimal_orientation_only": {
        "m": float(m), "E": float(E),
        **{name: float(value) for name, value in margins.items()},
    },
}
destination = Path(__file__).with_name("sharp-triangle-join-certificate.json")
destination.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"dimensions": report["dimensions"], **report["decimal_orientation_only"]}, indent=2))
