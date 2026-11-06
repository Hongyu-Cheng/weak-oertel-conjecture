#!/usr/bin/env python3
"""Exact mass/cap certificates and independent finite minimax checks."""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial
from random import Random


def clip(poly, a, b, c):
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        vp, vq = a * p[0] + b * p[1] - c, a * q[0] + b * q[1] - c
        if vp <= 0:
            out.append(p)
        if vp * vq < 0:
            ratio = vp / (vp - vq)
            out.append(tuple(p[i] + ratio * (q[i] - p[i]) for i in range(2)))
    return out


def area(poly):
    return abs(sum((p[0] * q[1] - p[1] * q[0]
                    for p, q in zip(poly, poly[1:] + poly[:1])), F(0))) / 2


def solve(matrix, rhs):
    rows = [list(row) + [value] for row, value in zip(matrix, rhs)]
    n = len(rhs)
    for j in range(n):
        choices = [i for i in range(j, n) if rows[i][j]]
        if not choices:
            return None
        i = choices[0]
        rows[i], rows[j] = rows[j], rows[i]
        pivot = rows[j][j]
        rows[j] = [x / pivot for x in rows[j]]
        for i in range(n):
            if i != j:
                coeff = rows[i][j]
                rows[i] = [x - coeff * y for x, y in zip(rows[i], rows[j])]
    return [row[-1] for row in rows]


def game_vertices(A):
    k, m = len(A), len(A[0])
    equal = [[F(1)] * m + [F(0)]]
    inequalities = [list(row) + [F(-1)] for row in A]
    inequalities += [[F(i == j) for i in range(m)] + [F(0)] for j in range(m)]
    feasible = []
    for active in combinations(range(k + m), m):
        sol = solve(equal + [inequalities[i] for i in active], [F(1)] + [F(0)] * m)
        if sol is not None and all(sum(x * y for x, y in zip(row, sol)) >= 0
                                   for row in inequalities):
            feasible.append(sol)
    optimum = max(sol[-1] for sol in feasible)
    winners = [sol for sol in feasible if sol[-1] == optimum]
    return optimum, min(winners, key=lambda sol: sum(x > 0 for x in sol[:-1]))


square = [(F(-1), F(-1)), (F(1), F(-1)), (F(1), F(1)), (F(-1), F(1))]
cap_cases = 0
for n in range(2, 6):
    layers = list(product([0, 1], repeat=n - 1))
    L, q = len(layers), F(6)
    for t in [F(1), F(1, 2), F(1, 4), F(2, 7), F(1, 16)]:
        delta = t * t / 2
        fibers = {}
        for z in [-1, 0, 1]:
            for k in layers:
                poly = square
                for eta in layers:
                    base_eval = z + sum((2 * e - 1) * x for e, x in zip(eta, k))
                    poly = clip(poly, F(1), F(1), F(3 + sum(eta)) - t - base_eval)
                assert area(poly) == (4 - delta if z == 1 else 4)
                fibers[z, k] = poly
        M = sum(map(area, fibers.values()))
        assert M == L * (12 - delta)
        budgets = []
        for eta in layers:
            masses = [F(0), F(0), F(0)]
            for (z, k), poly in fibers.items():
                margin = sum((2 * e - 1) * (x - e) for e, x in zip(eta, k))
                assert margin == -sum(x != e for e, x in zip(eta, k))
                masses[0] += area(clip(poly, F(-1), F(0), 8 * margin + delta / (3 * q)))
                masses[1] += area(clip(poly, F(0), F(-1), 8 * margin + delta / (3 * q)))
                masses[2] += area(clip(poly, F(1), F(1), 8 * margin - 2 * delta / (3 * q)))
            expected = [q - 2 * delta / 3, q - 2 * delta / 3,
                        q - 2 * delta / 3 + delta * delta / (9 * q)]
            assert masses == expected
            budgets += masses
        beta = F(1, 2 * L)
        loss = beta - max(budgets) / M
        assert loss == delta * (3 * q - 2 * delta) / (18 * q * L * (2 * q - delta)) > 0
        assert 4 < M / 2 ** n
        cap_cases += 1

dimension_cases = 0
for d in range(2, 11):
    for n in range(2, 11):
        L, w = 2 ** (n - 1), F(2 ** d)
        q = 3 * w / 2
        for den in [2, 3, 8, 16]:
            t = F(1, den)
            delta = t ** d / factorial(d)
            M = L * (2 * q - delta)
            budget = q - 2 * delta / 3 + delta * delta / (9 * q)
            loss = F(1, 2 * L) - budget / M
            assert loss == delta * (3 * q - 2 * delta) / (18 * q * L * (2 * q - delta)) > 0
            assert w < M / 2 ** n
            assert F(2, 3 * L) > F(1, 2 * L)
            # One isolated deletion instead has the exact unchanged-layer budget.
            assert q / (2 * q * L - delta) > F(1, 2 * L)
            dimension_cases += 1

rng = Random(741531)
game_cases = 0
for k in range(1, 5):
    for m in range(1, 5):
        for sample in range(8):
            A = [[F(rng.randrange(7), 6) for _ in range(m)] for _ in range(k)]
            primal, lam = game_vertices(A)
            # max_pi min_v(-A^T pi) is minus the desired dual minimum.
            negative_transpose = [[-A[p][v] for p in range(k)] for v in range(m)]
            negative_dual, pi_sol = game_vertices(negative_transpose)
            pi = pi_sol[:-1]
            assert primal == -negative_dual
            assert sum(x > 0 for x in lam[:-1]) <= k
            assert all(sum(pi[p] * A[p][v] for p in range(k)) <= primal for v in range(m))
            assert all(sum(lam[v] * A[p][v] for v in range(m)) >= primal for p in range(k))
            game_cases += 1

print(f"PASS: {cap_cases} actual multi-plane source/cap certificates; "
      f"{dimension_cases} all-dimensional strict-decrement/no-heavy identities; "
      f"{game_cases} exact primal-dual/support game checks.")
