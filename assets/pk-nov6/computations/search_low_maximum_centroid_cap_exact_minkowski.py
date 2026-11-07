"""Exact falsification search for the proposed low-maximum 4/9 cap floor.

All cap fractions use rational confluent divided differences. Failure
would be an exact counterexample; a passing search is not a proof.
"""

from fractions import Fraction as F
from math import comb
import json
import random


def cap_from_centered_nodes(nodes):
    nodes = sorted(nodes)
    d = len(nodes) - 1
    values = [F(max(0, x) ** d) for x in nodes]
    for order in range(1, d + 1):
        nxt = []
        for i in range(d + 1 - order):
            if nodes[i] == nodes[i + order]:
                nxt.append(F(comb(d, order) * nodes[i] ** (d - order))
                           if nodes[i] > 0 else F(0))
            else:
                nxt.append((values[i + 1] - values[i]) /
                           (nodes[i + order] - nodes[i]))
        values = nxt
    return values[0]


rng = random.Random(413729)
results = []
checked = 0
floor = F(4, 9)
for d in range(2, 26):
    scale = 24
    coefficients = [scale // d + (i < scale % d) for i in range(d)]
    best = F(1)
    best_nodes = None
    for sample in range(180):
        for _ in range(12 * d):
            i, j = rng.sample(range(d), 2)
            lower = max(-scale - coefficients[i], coefficients[j] - scale)
            upper = min(scale - coefficients[i], coefficients[j] + scale)
            transfer = rng.randint(lower, upper)
            coefficients[i] += transfer
            coefficients[j] -= transfer
        assert sum(coefficients) == scale
        assert all(-scale <= x <= scale for x in coefficients)
        nodes = [-scale] + coefficients
        p = cap_from_centered_nodes(nodes)
        checked += 1
        if p < best:
            best, best_nodes = p, list(nodes)
        if p < floor:
            print('EXACT COUNTEREXAMPLE', d, nodes, str(p), flush=True)
            raise SystemExit(1)
    results.append(dict(d=d, probability=str(best), approximate=float(best),
                        centered_nodes=best_nodes))
    print(d, float(best), flush=True)

# Concentrated positive coefficients and many tiny negative coefficients.
# Nodes are [-1, +1 (k copies), -(k-1)/(d-k) (d-k copies)].
calibrations = []
for d in [5, 10, 20, 40, 80, 120]:
    for k in range(1, min(12, (d + 1) // 2) + 1):
        denom = d - k
        nodes = [-denom] + [denom] * k + [-(k - 1)] * (d - k)
        p = cap_from_centered_nodes(nodes)
        checked += 1
        assert p >= floor
        calibrations.append(dict(d=d, k=k, probability=str(p),
                                 approximate=float(p)))

out = dict(status='no counterexample found; not a proof', checked=checked,
           proposed_floor=str(floor), random_minima=results,
           concentrated_family=calibrations)
with open('./low_maximum_centroid_cap_exact_search_minkowski.json', 'w') as f:
    json.dump(out, f, indent=2)
print(f'Completed {checked} exact cap calculations; no proof inferred.')
