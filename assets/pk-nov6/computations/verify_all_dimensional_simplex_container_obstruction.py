#!/usr/bin/env python3
"""Exact-rational regression checks for the all-dimensional container note.

The proof is in the companion Markdown note. Finite checks are not its
replacement: these check the displayed constants, determinant factors,
vertex estimates, and arbitrary small perturbations of enclosing simplices.
"""
from fractions import Fraction as Q
from math import factorial
from random import Random


def solve(matrix, rhs):
    n = len(rhs)
    rows = [list(map(Q, row)) + [Q(value)] for row, value in zip(matrix, rhs)]
    for j in range(n):
        k = next(k for k in range(j, n) if rows[k][j])
        rows[j], rows[k] = rows[k], rows[j]
        pivot = rows[j][j]
        rows[j] = [v / pivot for v in rows[j]]
        for k in range(n):
            if k != j:
                scale = rows[k][j]
                rows[k] = [v - scale * w for v, w in zip(rows[k], rows[j])]
    return [row[-1] for row in rows]


def determinant(matrix):
    rows = [list(map(Q, row)) for row in matrix]
    result = Q(1)
    for j in range(len(rows)):
        candidates = [k for k in range(j, len(rows)) if rows[k][j]]
        if not candidates:
            return Q(0)
        k = candidates[0]
        if k != j:
            rows[j], rows[k] = rows[k], rows[j]
            result = -result
        pivot = rows[j][j]
        result *= pivot
        for k in range(j + 1, len(rows)):
            scale = rows[k][j] / pivot
            for l in range(j + 1, len(rows)):
                rows[k][l] -= scale * rows[j][l]
    return result


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def volume(vertices):
    d = len(vertices) - 1
    return abs(determinant([[vertices[j + 1][i] - vertices[0][i]
                             for j in range(d)] for i in range(d)])) / factorial(d)


def barycentric(vertices, point):
    d = len(point)
    return solve([[vertices[j][i] for j in range(d + 1)] for i in range(d)]
                 + [[Q(1)] * (d + 1)], list(point) + [Q(1)])


rng = Random(267093)
source_checks = 0
simplex_checks = 0
small_branch_checks = 0
for d in range(2, 11):
    V, gamma, c = Q(1, factorial(d)), Q(d, d + 1) ** d, Q(1, 16 * d * d)
    unit = [tuple(Q(i == j) for i in range(d)) for j in range(d)]
    for power in range(4, 12):
        e = Q(1, 2 ** power)
        a, b, h = 1 + e * e, e * e, d * (1 + e * e) - e
        A_vertices = unit + [tuple(e * x for x in v) for v in unit]
        B_vertices = [tuple(Q(0) for _ in range(d))] + [tuple(b * x for x in v) for v in unit]
        P_vertices = [tuple(a - (h if i == j else 0) for i in range(d)) for j in range(d)]
        assert volume([tuple([a] * d)] + P_vertices) == V * h ** d
        for u in A_vertices:
            for v in B_vertices:
                w = tuple(x + y for x, y in zip(u, v))
                assert all(x <= a for x in w) and sum(w) >= e
        masses = [V * (1 - e ** d), V * h ** d / 2 ** d, V * e ** (2 * d)]
        F = max(masses)
        W = 3 * F + sum(masses)
        assert min(masses) > 0 and W > 4 * F
        for n in range(2, 9):
            assert F < (2 ** (n - 2) * W) / 2 ** n
        # Worst allowed eta and delta; strict hypotheses only improve these.
        eta = c * e
        delta = eta / (1 - e ** (d - 1))
        assert delta <= 2 * eta and d * delta <= e / 16
        assert 1 - e - d * delta > Q(1, 2)
        assert d * delta * (e + d * delta) / (1 - e - d * delta) < e / 2
        assert h ** (d - 1) / 2 ** (d + 1) >= Q(1, 8) > c
        source_checks += 1
        if d > 6 or power > 7:
            continue
        # Each orientation and each facet height is independently perturbed.
        for sample in range(6):
            perturb = e ** (d + 2) / 16
            normals = [[-Q(i == j) + perturb * rng.randint(-2, 2)
                        for i in range(d)] for j in range(d)]
            normals.append([Q(1) + perturb * rng.randint(-2, 2) for _ in range(d)])
            heights = [max(dot(normal, v) for v in A_vertices)
                       + perturb * rng.randint(0, 2) for normal in normals]
            vertices = [tuple(solve([normal for k, normal in enumerate(normals) if k != j],
                                    [height for k, height in enumerate(heights) if k != j]))
                        for j in range(d + 1)]
            for vertex in vertices:
                assert all(dot(normal, vertex) <= height for normal, height in zip(normals, heights))
            for point in A_vertices:
                assert min(barycentric(vertices, point)) >= 0
            Delta = volume(vertices) - masses[0]
            assert Delta >= 0
            simplex_checks += 1
            if Delta >= c * e * V:
                continue
            eta, delta = Delta / V, Delta / (V * (1 - e ** (d - 1)))
            assert all(min(v) >= -delta and sum(v) <= 1 + eta for v in vertices)
            chosen = [max(range(d + 1), key=lambda k: vertices[k][i]) for i in range(d)]
            assert len(set(chosen)) == d
            assert all(vertices[chosen[i]][i] >= 1 for i in range(d))
            k0 = min(range(d + 1), key=lambda k: sum(vertices[k]))
            assert k0 not in chosen and sum(vertices[k0]) <= e
            v0 = vertices[k0]
            upper = delta * (e + d * delta) / (1 - e - d * delta)
            for i in range(d):
                weights = barycentric(vertices, tuple(e * x for x in unit[i]))
                alpha = weights[k0]
                assert alpha > 0
                assert (1 - alpha) / alpha <= (e + d * delta) / (1 - e - (d - 1) * delta)
            assert all(x <= upper for x in v0)
            assert sum(v0) <= d * upper < e / 2
            pyramid = volume([v0] + P_vertices)
            assert pyramid == V * h ** (d - 1) * (e - sum(v0))
            assert pyramid / 2 ** d > c * e * V
            small_branch_checks += 1

assert small_branch_checks > 50
print(f"PASS: {source_checks} exact source/constant/no-heavy cases; "
      f"{simplex_checks} independently perturbed enclosing simplices; "
      f"{small_branch_checks} small-volume vertex and pyramid certificates.")
