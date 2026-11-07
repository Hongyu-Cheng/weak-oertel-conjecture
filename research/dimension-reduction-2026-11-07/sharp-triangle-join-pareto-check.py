"""Exact checks for three dimension tradeoffs of the same geometric proof."""

from fractions import Fraction as F
from math import comb
import json
from pathlib import Path


results = []
for n, d, delta_numerator, cutoff in [
    (153, 34, 95483588829, 10),
    (132, 82, 39567853350, 25),
    (129, 104, 31193387251, 32),
]:
    N, D = n // 3, d + 1
    a, delta, epsilon = F(159, 250), F(delta_numerator, 10**12), F(1, 10**13)
    Q = 1 - a + a * a
    eta = (1 - delta) / 2
    v = delta / D + (1 - delta) * a * epsilon / Q
    theta_p = a / (3 * (1 + a))
    theta_a = (a / (1 + a) + (1 - a) / (2 - a)) / 3
    beta, gamma = 1 / ((1 + a) * (2 - a)), F(d, D) ** d
    m = theta_p * (1 + delta) ** d
    alpha = [theta_a * (1 - r * D * v) ** d for r in range(1, cutoff + 1)]
    E = 3 * sum(comb(N, r) * alpha[r - 1] for r in range(1, cutoff + 1))
    assert n == 3 * N and 1 <= cutoff <= N and d >= 3
    assert F(1, 2) < a < 1 and 0 < delta < 1 and 0 < eta < 1 - delta
    assert epsilon < Q / (a * D) and 2 * epsilon < 1 and eta * epsilon < 1
    margins = {
        "negative_scale": 1 - cutoff * D * v,
        "volume_surplus": 1 + E - m,
        "origin_cut": gamma * m - beta - E / 3,
        "whole_negative_fiber": gamma * m - alpha[0],
    }
    assert all(value > 0 for value in margins.values())
    results.append({
        "n": n, "d": d, "N": N, "cutoff": cutoff,
        "a": str(a), "delta": str(delta), "epsilon": str(epsilon),
        "exact_positive_margins": {name: str(value) for name, value in margins.items()},
        "decimal_orientation_only": {name: float(value) for name, value in margins.items()},
    })

Path(__file__).with_name("sharp-triangle-join-pareto-certificate.json").write_text(
    json.dumps(results, indent=2) + "\n"
)
print(json.dumps([{key: row[key] for key in ["n", "d", "a", "delta", "decimal_orientation_only"]}
                  for row in results], indent=2))
