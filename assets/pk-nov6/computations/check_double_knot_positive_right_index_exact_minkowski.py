"""Exact finite falsification test for D(H,J)<=0 when J>=1.

The tested range is finite. Passing does not establish the sublemma.
"""

from fractions import Fraction as F
import json


def deficit(d, H, J):
    t = F(1, d + 1)
    B = F(H - J, d * H * (2 * J + 1))
    a = t * F(H + J + 1, H * (2 * J + 1))
    A = F(J * (2 * H + 1), H * (2 * J + 1))
    m = 1 // a
    mass = sum((1 - a * h) ** d for h in range(m + 1))
    left = sum((1 - B * h) ** (d - 1) * (1 - F(h, H))
               for h in range(H))
    right = A * sum((1 + B * (h + 1)) ** (d - 1) *
                    (1 - F(h, J)) for h in range(J))
    return mass - left - right


rows = []
checked = 0
for d in range(2, 11):
    best = F(-10**10)
    indices = None
    for J in range(1, 11):
        for H in range(J, (2 * d + 1) * J + d + 1):
            value = deficit(d, H, J)
            checked += 1
            if value > best:
                best, indices = value, [H, J]
            if value > 0:
                print('EXACT COUNTEREXAMPLE', d, H, J, str(value), flush=True)
                raise SystemExit(1)
    rows.append(dict(d=d, maximum_normalized_deficit=str(best),
                     approximate=float(best), indices=indices))
    print(d, str(best), indices, flush=True)

with open('./double_knot_positive_right_index_exact_minkowski.json', 'w') as f:
    json.dump(dict(status='no counterexample; not a proof', checked=checked,
                   J_max=10, rows=rows), f, indent=2)
print(f'PASS {checked} exact finite double-knot checks; no proof inferred.')
