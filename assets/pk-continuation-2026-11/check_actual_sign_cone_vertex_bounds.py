#!/usr/bin/env python3
"""Exact finite-vertex norm certificates for all two-hit cones of one matrix.

This proves actual retained-simplex upper bounds via the finite-vertex lemma.
It uses Fraction arithmetic and no numerical determinant or optimization.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import isqrt, prod
from pathlib import Path
import argparse
import hashlib
import json
from check_absorption_relaxation_certificate import solve


def vertices_and_bound(P, R):
    n = len(P)
    J = [i for i in range(n) if i not in R]
    H = solve([[Q(i == j) - P[i][j] for j in J] for i in J],
              [[P[i][r] for r in R] for i in J])
    m = [max(row) for row in H]
    scale = 10 ** 8
    t = [Q(scale, isqrt(q.numerator * scale * scale // q.denominator) + 1)
         for q in m]
    assert all(tj > 0 and tj * tj * mj < 1 for tj, mj in zip(t, m))
    determinant = prod(1 + tj for tj in t)
    vertices = []
    for r in R:
        for count in range(len(J) + 1):
            for A in combinations(J, count):
                h = ([row[0] for row in solve(
                    [[Q(i == j) - P[i][j] for j in A] for i in A],
                    [[P[i][r]] for i in A])] if A else [])
                denominator = 1 + sum(h)
                lam = [Q(0)] * n
                lam[r] = Q(1) / denominator
                for j, hj in zip(A, h):
                    lam[j] = hj / denominator
                assert all(isinstance(x, Q) for x in lam)
                assert sum(lam) == 1 and all(x >= 0 for x in lam)
                assert all(lam[j] <= sum(P[j][i] * lam[i] for i in range(n)) for j in J)
                assert all(lam[j] == sum(P[j][i] * lam[i] for i in range(n)) for j in A)
                transformed = [(1 + t[k]) * lam[j] for k, j in enumerate(J)] + [
                    lam[r0] - sum(H[k][ell] * t[k] * lam[j]
                                  for k, j in enumerate(J))
                    for ell, r0 in enumerate(R)]
                assert sum(transformed) == 1
                norm_squared = sum(x * x for x in transformed)
                assert isinstance(norm_squared, Q)
                assert 0 < norm_squared <= 1
                vertices.append((norm_squared, r, A, lam))
    assert len(vertices) == len(R) * 2 ** len(J)
    assert len({tuple(x[3]) for x in vertices}) == len(vertices)
    vertices.sort(key=lambda x: x[0], reverse=True)
    upper_squared = prod(x[0] for x in vertices[:n]) / determinant ** 2
    assert isinstance(upper_squared, Q)
    return t, determinant, vertices, upper_squared


def verify(path):
    raw = path.read_bytes()
    data = json.loads(raw)
    P = [[Q(x, data['denominator']) for x in row] for row in data['P_integer_rows']]
    n = len(P)
    assert n == 6 and all(len(row) == n and sum(row) == 1 for row in P)
    assert all(P[i][i] == 0 for i in range(n))
    assert all(P[i][j] > 0 for i in range(n) for j in range(n) if i != j)
    records = []
    for R in combinations(range(n), 2):
        t, determinant, vertices, upper_squared = vertices_and_bound(P, R)
        assert len(vertices) == 32 and upper_squared < Q(1, 1600)
        assert vertices[0][0] == vertices[1][0] == 1
        assert all(x[0] < 1 for x in vertices[2:])
        a = determinant.numerator * 1000 // determinant.denominator
        q = [(-((-x[0].numerator * 1000) // x[0].denominator)) for x in vertices[2:6]]
        assert Q(a, 1000) <= determinant
        assert all(x[0] <= Q(qj, 1000) for x, qj in zip(vertices[2:6], q))
        assert 1600 * prod(q) < 10 ** 6 * a * a
        records.append({
            'hit_indices_one_based': [r + 1 for r in R],
            'vertex_count': len(vertices),
            't': list(map(str, t)),
            'map_determinant': str(determinant),
            'top_six_vertex_norms_squared': [str(x[0]) for x in vertices[:6]],
            'top_six_vertex_root_and_active': [{'root': x[1] + 1, 'active': [i + 1 for i in x[2]]} for x in vertices[:6]],
            'exact_capacity_upper_squared': str(upper_squared),
            'coarse_determinant_lower_numerator_over_1000': a,
            'coarse_nonroot_norm_squared_upper_numerators_over_1000': q,
            'coarse_integer_comparison_gap': 10 ** 6 * a * a - 1600 * prod(q),
        })
    return {
        'verdict': 'PASS_ACTUAL_SIMPLEX_CAPACITY_UPPER_BOUNDS',
        'input_sha256': hashlib.sha256(raw).hexdigest(),
        'all_two_hit_cones': len(records),
        'vertices_examined': sum(x['vertex_count'] for x in records),
        'uniform_strict_relative_capacity_upper_bound': '1/40',
        'records': records,
        'scope': 'All source simplices of relative volume at least 1/32 must hit at least three rows for this particular rational matrix. No assertion is made for arbitrary stochastic matrices or arbitrary fans.',
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
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}, indent=2))
    for record in result['records']:
        print(record['hit_indices_one_based'], record['coarse_determinant_lower_numerator_over_1000'],
              record['coarse_nonroot_norm_squared_upper_numerators_over_1000'])
