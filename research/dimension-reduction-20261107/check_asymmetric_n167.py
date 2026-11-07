#!/usr/bin/env python3
"""Exact geometry and scalar checks for the asymmetric (167,99) candidate.

All predicates use fractions or integers. The separate analytic proof is
responsible for the complete lattice census and the ambient all-points bound.
This script uses no data from the earlier symmetric construction's checker.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json


def det(u, v):
    return u[0]*v[1]-u[1]*v[0]


def dot(u, v):
    return sum((a*b for a, b in zip(u, v)), F(0))


def add(u, v):
    return tuple(a+b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a-b for a, b in zip(u, v))


def mul(a, u):
    return tuple(a*b for b in u)


def clip(poly, normal, p):
    result = []
    for a, b in zip(poly, poly[1:]+poly[:1]):
        fa, fb = dot(normal, sub(a, p)), dot(normal, sub(b, p))
        ina, inb = fa <= 0, fb <= 0
        if ina:
            result.append(a)
        if ina != inb:
            result.append(add(a, mul(fa/(fa-fb), sub(b, a))))
    return result


def area_ratio(poly):
    return abs(sum((det(a, b) for a, b in zip(poly, poly[1:]+poly[:1])), F(0)))


def solve_rows(matrix, rhs):
    a, b = matrix
    determinant = det(a, b)
    return (F(rhs[0]*b[1]-a[1]*rhs[1], determinant),
            F(a[0]*rhs[1]-rhs[0]*b[0], determinant))


def main():
    n, d, D = 167, 99, 100
    counts = [56, 56, 55]
    p = (F(334371, 10**6), F(332129, 10**6))
    p_bary = (1-sum(p), *p)
    normals = [tuple(F(v, 10**6) for v in row) for row in
               [(-599637, -800272), (971233, 238130), (-310548, 950558)]]
    weights = [F(1),
               det(mul(-1, normals[0]), normals[2])/det(normals[1], normals[2]),
               det(normals[1], mul(-1, normals[0]))/det(normals[1], normals[2])]
    frows = [mul(w, row) for w, row in zip(weights, normals)]
    assert min(weights) > 0
    assert add(add(frows[0], frows[1]), frows[2]) == (0, 0)
    tri = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
    m, gamma = F(3304235, 10**6), F(99, 100)**99
    deltas = [F(325903, 10**7), F(6517257, 200000000), F(50753, 1562500)]
    eps, C, R = F(1, 10**20), F(10), F(3*(n+1))
    origin = tuple(F(3, D)*v for v in p_bary) + (F(1, D),)*97
    assert len(origin) == D and sum(origin) == 1 and min(origin) > F(99, 10000)
    assert all(abs(dot(row, sub(vertex, p))) <= 1
               for row in frows for vertex in tri)
    assert min(origin) > C*eps
    rows = []
    for a in range(3):
        poly = tri
        for j in range(3):
            if j != a:
                poly = clip(poly, normals[j], p)
        vertex, q = max(combinations(poly, 2),
                        key=lambda pair: abs(det(sub(pair[0], p), sub(pair[1], p))))
        assert vertex == tri[a]
        theta_max = abs(det(sub(vertex, p), sub(q, p)))
        beta = area_ratio(clip(tri, mul(-1, normals[a]), p))
        delta, delta_prime = deltas[a], deltas[a]+F(1, 10**12)
        t = 1-delta_prime
        eta = 1-(delta+delta_prime)/2
        theta = m/(1+delta)**d
        kappa = theta/theta_max
        assert 0 < kappa < 1
        q_shrunk = add(p, mul(kappa, sub(q, p)))
        vertices = [p, vertex, q_shrunk]
        assert abs(det(sub(vertex, p), sub(q_shrunk, p))) == theta
        assert theta*(1+delta)**d == m
        assert all(min(1-x-y, x, y) >= 0 for x, y in vertices)
        for j in range(3):
            scores = [dot(frows[j], sub(v, p)) for v in vertices]
            assert max(scores) <= 1 and min(scores) >= -1
            if j == a:
                assert min(scores) == 0
            else:
                assert max(scores) == 0
        targets = [F(2 if a == j else -1) for j in range(3)]
        perturb_planar = solve_rows(frows[:2], targets[:2])
        perturb = (-sum(perturb_planar), *perturb_planar)
        assert all(dot(row, perturb_planar) == target
                   for row, target in zip(frows, targets))
        assert max(map(abs, perturb)) < 3 < C
        v_ray, q_ray = sub(vertex, p), sub(q_shrunk, p)
        coefficients = (det(perturb_planar, q_ray)/det(v_ray, q_ray),
                        det(v_ray, perturb_planar)/det(v_ray, q_ray))
        assert min(coefficients) > 0
        assert sum(coefficients) < 6
        assert F(3, D)-eps*sum(coefficients) > 0
        assert 0 < t < eta < 1-delta
        assert 1-30*delta_prime > 0
        assert 1-31*delta_prime < 0
        # Source simplex has zero minimum in every barycentric coordinate
        # after joining to the 97 free vertices. This validates the uniform
        # facet bounds used in the analytic origin-fiber argument.
        origin_gap = min((delta_prime-delta)*oj-(2-delta-delta_prime)*C*eps
                         for oj in origin)
        assert origin_gap > 0
        E = theta*sum((comb(counts[a], r)*(1-r*delta_prime)**d
                       for r in range(1, 31)), F(0))
        middle_margin = gamma*m-beta-E
        assert middle_margin > F(8, 100000)
        assert theta < m
        assert R > 2*t*eps
        rows.append({
            'a': a, 'N': counts[a], 'theta_max': str(theta_max),
            'theta': str(theta), 'beta': str(beta), 'delta': str(delta),
            'delta_prime': str(delta_prime), 'eta': str(eta), 't': str(t),
            'q_original': [str(v) for v in q],
            'vertex': [str(v) for v in vertex], 'kappa': str(kappa),
            'E': str(E), 'middle_margin': str(middle_margin),
            'center_perturbation': [str(v) for v in perturb],
            'center_source_coefficients_per_epsilon': [str(v) for v in coefficients],
            'origin_facet_gap_lower_bound': str(origin_gap),
        })
    E_total = sum((F(row['E']) for row in rows), F(0))
    surplus = 1+E_total-m
    assert surplus > F(8, 100000)
    W = (2**n-1)*m+1+E_total
    maximum_depth = gamma*m/W
    assert maximum_depth < gamma/F(2**n)
    assert F(65, 24)*gamma > 1+surplus/(2**n*m)
    report = {
        'status': 'PASS_EXACT_GEOMETRY_AND_SCALARS', 'n': n, 'd': d,
        'm': str(m), 'epsilon': str(eps), 'C': str(C), 'R': str(R),
        'p_planar': [str(v) for v in p],
        'p_barycentric': [str(v) for v in p_bary],
        'normal_rows': [[str(v) for v in row] for row in normals],
        'positive_row_weights': [str(v) for v in weights], 'rows': rows,
        'surplus': str(surplus), 'surplus_decimal': float(surplus),
        'middle_margins_decimal': [float(F(row['middle_margin'])) for row in rows],
        'scope': 'Exact geometry and scalar premises. The accompanying analytic proof must establish actual fibers and the all-points bound. Sharp-bound target only; not 1/e, not both dimensions below 100, and not Lean-formalized.',
    }
    output = Path(__file__).with_name('asymmetric-n167-candidate.json')
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(report['status'])
    print('n =', n, 'd =', d)
    print('surplus =', report['surplus_decimal'])
    print('middle margins =', report['middle_margins_decimal'])
    print('Saved', output.name)


if __name__ == '__main__':
    main()
