#!/usr/bin/env python3
"""Independent exact check of an absorption-only necessary-condition obstruction.

No optimization, floating-point arithmetic, SymPy, or numerical source file is used.
This does NOT establish actual feasibility of any geometric source pattern.
"""
from fractions import Fraction as Q
from math import isqrt, prod
from pathlib import Path
import argparse
import hashlib
import json


def solve(A, B):
    """Exact Gaussian elimination of a square rational A against matrix B."""
    n = len(A)
    width = len(B[0])
    rows = [list(A[i]) + list(B[i]) for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if rows[i][k])
        rows[k], rows[pivot] = rows[pivot], rows[k]
        value = rows[k][k]
        rows[k] = [x / value for x in rows[k]]
        for i in range(n):
            if i != k:
                value = rows[i][k]
                rows[i] = [a - value * b for a, b in zip(rows[i], rows[k])]
    assert all(rows[i][j] == (i == j) for i in range(n) for j in range(n))
    answer = [row[n:] for row in rows]
    assert all(sum(A[i][k] * answer[k][j] for k in range(n)) == B[i][j]
               for i in range(n) for j in range(width))
    return answer


def verify(path):
    raw = path.read_bytes()
    data = json.loads(raw)
    n = len(data['P_integer_rows'])
    d = n - 1
    assert n == 6 and data['denominator'] == 1000
    P = [[Q(x, data['denominator']) for x in row]
         for row in data['P_integer_rows']]
    assert all(len(row) == n and sum(row) == 1 for row in P)
    assert all(P[i][i] == 0 for i in range(n))
    assert all(P[i][j] > 0 for i in range(n) for j in range(n) if i != j)
    v, gamma = Q(data['v']), Q(data['gamma'])
    assert v == Q(9, 10) and gamma == Q(d, n) ** d
    threshold = Q(1, 2 ** d) / v
    own_caps = [1 / prod(1 + p for p in row) for row in P]

    # An exact strictly positive dependence of the six centroid-cut normals.
    stationary_A = [[Q(i == j) - P[j][i] for j in range(n)] for i in range(n - 1)]
    stationary_A.append([Q(1)] * n)
    stationary = [row[0] for row in solve(stationary_A, [[Q(0)]] * (n - 1) + [[Q(1)]])]
    assert all(x > 0 for x in stationary) and sum(stationary) == 1
    assert all(sum(stationary[i] * P[i][j] for i in range(n)) == stationary[j]
               for j in range(n))

    scale = 10 ** 8
    total_weight = Q(0)
    credits = [Q(0)] * n
    pattern_results = []
    for pattern in data['patterns']:
        hits = pattern['hits']
        assert len(hits) == n and set(hits) <= {0, 1}
        R = [j for j, hit in enumerate(hits) if hit]
        J = [j for j, hit in enumerate(hits) if not hit]
        assert J and R
        A = [[Q(i == j) - P[i][j] for j in J] for i in J]
        B = [[P[i][r] for r in R] for i in J]
        H = solve(A, B)
        assert all(all(x > 0 for x in row) and sum(row) == 1 for row in H)
        maxima = [max(row) for row in H]
        assert maxima == list(map(Q, pattern['absorption_maxima']))
        lower = Q(1)
        roots = []
        for m in maxima:
            root = Q(isqrt((m.numerator * scale * scale) // m.denominator), scale)
            assert root * root <= m < (root + Q(1, scale)) ** 2
            roots.append(root)
            lower *= root / (1 + root)
        assert lower == Q(pattern['capacity_lower'])
        assert lower > Q(87, 2500) > threshold
        weight = Q(pattern['weight'])
        assert weight > 0
        total_weight += weight
        for j in R:
            credits[j] += weight
        pattern_results.append({
            'hit_indices_one_based': [j + 1 for j in R],
            'weight': str(weight),
            'rational_lower_bound_on_capacity_upper_bound': str(lower),
            'required_relative_source_volume': str(threshold),
            'positive_capacity_bound_margin': str(lower - threshold),
            'root_lower_bounds': list(map(str, roots)),
        })
    assert total_weight == 1 - v == Q(1, 10)
    scores = [v * p + credit for p, credit in zip(own_caps, credits)]
    assert scores == list(map(Q, data['scores']))
    gaps = [gamma - score for score in scores]
    assert all(score < Q(2007, 5000) < gamma for score in scores)
    assert all(gap > 0 for gap in gaps)
    assert min(gaps) == Q(data['minimum_gap'])
    return {
        'verdict': 'PASS_EXACT_NECESSARY_CONDITION_OBSTRUCTION_ONLY',
        'certificate_path': path.name,
        'certificate_sha256': hashlib.sha256(raw).hexdigest(),
        'dimension': d,
        'volume_ratio': str(v),
        'gamma': str(gamma),
        'stationary_positive_dependence': list(map(str, stationary)),
        'own_cap_fractions': list(map(str, own_caps)),
        'patterns': pattern_results,
        'sum_weights': str(total_weight),
        'scores': list(map(str, scores)),
        'minimum_gap': str(min(gaps)),
        'scope': 'Only the absorption-sensitive necessary capacity test is checked; no inscribed simplex realization and no Oertel counterexample is asserted.',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', nargs='?', type=Path,
                        default=Path(__file__).with_name('absorption-relaxation-rational-certificate.json'))
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = verify(args.certificate)
    rendered = json.dumps(result, indent=2) + '\n'
    if args.report:
        args.report.write_text(rendered)
    print(rendered, end='')
