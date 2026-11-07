"""Exact checks for the direct rational sharp-OC counterexample.

The proof handles all exponentially many fibers symbolically; this file checks
the source vertex matrices and the fixed rational inequalities, not the entire
mathematical proof. It uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import chain
import json
from pathlib import Path

D = 23
N = D + 1
L = 10000
eps = F(1, L)
beta = F(103, 104)
m = L ** D
n = 3 * m
gamma = F(D, N) ** D
q = F(8192, 6561) * beta ** D  # M / V


def det(matrix):
    mat = [list(row) for row in matrix]
    ans = F(1)
    for k in range(len(mat)):
        r = next(r for r in range(k, len(mat)) if mat[r][k])
        if r != k:
            mat[r], mat[k] = mat[k], mat[r]
            ans = -ans
        pivot = mat[k][k]
        ans *= pivot
        for r in range(k + 1, len(mat)):
            mul = mat[r][k] / pivot
            for c in range(k + 1, len(mat)):
                mat[r][c] -= mul * mat[k][c]
    return ans


def fj(x, j):
    return x[j] - x[(j + 1) % N]


sources = []
for a in range(3):
    roots = set(range(a, N, 3))
    cols = []
    for r in sorted(roots):
        for length in (1, 2, 3):
            col = [F(0) for _ in range(N)]
            for k in range(length):
                col[(r - k) % N] = F(1, length)
            cols.append(col)
    centroid = [sum(col[j] for col in cols) / N for j in range(N)]
    vertices = [[beta * col[j] + (1 - beta) * centroid[j]
                 for j in range(N)] for col in cols]
    determinant = abs(det(list(zip(*cols))))
    assert determinant == F(1, 6 ** 8)
    assert abs(det(list(zip(*vertices)))) == beta ** D * determinant
    for r in roots:
        assert [centroid[(r - 2) % N], centroid[(r - 1) % N], centroid[r]] == [F(2, 144), F(5, 144), F(11, 144)]
    assert min(chain.from_iterable(vertices)) == (1 - beta) / 72
    hit = []
    for j in range(N):
        h = max(fj(col, j) for col in vertices)
        if j in roots:
            assert h == beta + (1 - beta) / 16 > 0
            hit.append(j)
        else:
            assert h <= -(1 - beta) / 48 < 0
            assert fj(centroid, j) <= -F(1, 48)
        assert h <= 1
        assert fj(centroid, j) <= F(1, 16)
    sources.append({"type": a, "roots": hit, "determinant": str(determinant)})

# Scalar obligations for the exact body, origin fiber, and ambient exclusions.
checks = {
    "M_over_V_less_than_one": 1 - q,
    "Gamma_M_over_V_minus_3_over_8": gamma * q - F(3, 8),
    "M_over_b_greater_than_one": 4 * q - 1,
    "P_plus_A_half_barycentric_margin": (1 - beta) / 72 - eps / 48,
    "centroid_plus_two_A_f_margin": beta / 48 - 2 * eps,
    "centroid_plus_two_A_lambda_margin": beta / 72 - eps / 12,
    "g_minus_delta": (1-beta)/48 - 2*eps,
    "unpaid_support_negative_at_k_one": (1 - beta) / 24 - 2 * eps,
    "unpaid_support_decreases_in_k": F(1, 48) - 2 * eps,
    "paid_support_negative_at_k_n": 3*(n+1) - (n+1) - (n-1)*2*eps,
    "negative_fiber_volume_below_M_in_V_units": q - F(1, 4 * m),
}
assert all(value > 0 for value in checks.values())
assert n * eps ** D == 3
assert F(1, 8) + F(1, 4) == F(3, 8)
report = {
    "verdict": "PASS_EXACT_DIRECT_RATIONAL_CONSTRUCTION_SCALAR_AND_SOURCE_CHECKS",
    "d": D, "L": L, "m": str(m), "n": str(n),
    "beta": str(beta), "epsilon": str(eps), "Gamma": str(gamma),
    "M_over_V": str(q),
    "positive_exact_margins": {key: str(value) for key, value in checks.items()},
    "source_geometry": sources,
    "proof_scope": "The note proves the finite fiber census, exact origin fiber, all-subset support formulas, and exposed-fiber isolation analytically; this checker certifies every fixed scalar and continuous source calculation used there.",
}
assert 6561*104**23-8192*103**23 == 33779795573668127344976093026519051930525573120
assert 8*8192*(23*103)**23-3*6561*(24*104)**23 == 47199574894061329600561263464623691938213399093856004046633146585892726610395136
assert (1-beta)/48-2*eps == F(1,3120000)
out = Path(__file__).with_name("audit-direct-rational-sharp-oc-counterexample-exact.json")
out.write_text(json.dumps(report, indent=2) + "\n")
print(report["verdict"])
print(f"Three 24-vertex sources and all {len(checks)} exact positive scalar margins passed.")
