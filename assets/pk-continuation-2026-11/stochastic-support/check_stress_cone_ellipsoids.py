#!/usr/bin/env python3
"""Check exact rational ellipsoid certificates on five retained sign cones.
The checker needs no NumPy, SciPy, saved search arrays, or floating arithmetic.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import argparse
import json
from exact_linear_algebra import solve


def positive_determinant(matrix):
    M = [list(row) for row in matrix]
    determinant = Q(1)
    for i in range(len(M)):
        pivot = M[i][i]
        assert pivot > 0
        determinant *= pivot
        for j in range(i + 1, len(M)):
            for k in range(i + 1, len(M)):
                M[j][k] -= M[j][i] * M[i][k] / pivot
    return determinant


def verify(data):
    P = [[Q(x, data['P_denominator']) for x in row] for row in data['P_integer_rows']]
    Qmat = [[Q(x, data['Q_denominator']) for x in row] for row in data['Q_integer_rows']]
    n = len(P)
    d = n - 1
    R = [r - 1 for r in data['R_one_based']]
    J = [j for j in range(n) if j not in R]
    assert len(P) == len(Qmat) == n
    assert all(len(row) == n for row in P + Qmat)
    assert all(P[i][i] == 0 and sum(P[i]) == 1 for i in range(n))
    assert all(P[i][j] > 0 for i in range(n) for j in range(n) if i != j)
    assert all(Qmat[i][j] == Qmat[j][i] for i in range(n) for j in range(n))
    determinant = positive_determinant(Qmat)
    assert determinant > 4 ** d
    max_quadratic = Q(0)
    count = 0
    for r in R:
        for a in range(len(J) + 1):
            for A in combinations(J, a):
                h = ([row[0] for row in solve(
                    [[Q(i == j) - P[i][j] for j in A] for i in A],
                    [[P[i][r]] for i in A])] if A else [])
                v = [Q(0)] * n
                v[r] = 1 / (1 + sum(h))
                for j, hj in zip(A, h):
                    v[j] = hj * v[r]
                assert sum(v) == 1
                assert all(v[j] <= sum(P[j][i] * v[i] for i in range(n)) for j in J)
                norm = sum(v[i] * Qmat[i][j] * v[j] for i in range(n) for j in range(n))
                assert norm <= 1
                max_quadratic = max(max_quadratic, norm)
                count += 1
    assert count == len(R) * 2 ** len(J)
    return {
        'N': n,
        'R_one_based': data['R_one_based'],
        'vertices_checked': count,
        'positive_determinant': str(determinant),
        'determinant_threshold': 4 ** d,
        'max_vertex_quadratic': str(max_quadratic),
        'strict_capacity_upper_bound': '1/' + str(2 ** d),
        'verdict': 'PASS_EXACT_ELLIPSOID_CERTIFICATE',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', nargs='?', type=Path,
                        default=Path(__file__).with_name('stress-cone-rational-ellipsoids.json'))
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    records = [verify(record) for record in data['certificates']]
    report = {'verdict': 'PASS_ALL_EXACT_STRESS_CONE_CERTIFICATES',
              'matrices': len(records),
              'total_vertices_checked': sum(r['vertices_checked'] for r in records),
              'scope': 'Five explicitly rationalized matrices and their indicated retained cones only. Not the mean-cap bridge for arbitrary matrices.',
              'records': records}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + '\n')
    for record in records:
        print(record['N'], record['R_one_based'], record['vertices_checked'],
              record['strict_capacity_upper_bound'], record['verdict'])
