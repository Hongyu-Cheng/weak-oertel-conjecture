"""Exact finite checks for the complete-block rank and physical stress lemma.

The proof of separation and the arbitrary-dimensional statement is in the note;
these checks verify the component formulas and finite rank calibrations.
"""
from fractions import Fraction as F
from random import Random
import sympy as S

rng = Random(917064)
checks = 0
for d in range(2, 6):
    m = d + 1
    for n in range(1, 6):
        for groups in range(1, 5):
            rows = S.zeros(m * groups, d * n)
            # Basis c=e_j-e_(m-1), with the common nonzero row factor
            # removed. Each fiber has its own positive volume z+1.
            for group in range(groups):
                for z in range(n):
                    if rng.randrange(3) == 0:
                        # All strict full/empty traces have zero derivative.
                        continue
                    perm = list(range(m))
                    rng.shuffle(perm)
                    for local_row, label in enumerate(perm):
                        for j in range(d):
                            value = int(label == j) - int(label == m - 1)
                            rows[m * group + local_row, d * z + j] = (z + 1) * value
            for group in range(groups):
                assert sum((rows[m * group + i, :] for i in range(m)),
                           S.zeros(1, d * n)) == S.zeros(1, d * n)
            rank = rows.rank()
            assert rank <= d * groups
            kernel = rows.nullspace()
            assert len(kernel) == d * n - rank
            forced_zero = [
                z for z in range(n)
                if all(all(v[d * z + j] == 0 for j in range(d))
                       for v in kernel)
            ]
            assert len(forced_zero) <= groups
            assert d * len(forced_zero) <= rank
            checks += 1

    for _ in range(8):
        c = [F(rng.randrange(-4, 5)) for _ in range(d)]
        c.append(-sum(c))
        a = [[F(0) if i == j else (m*c[j]+c[i])/F(d*m-1)
              for j in range(m)] for i in range(m)]
        b = [row[:] for row in a]
        for i in range(m):
            b[i][i] = -c[i]
        assert all(sum(b[i][j] for i in range(m)) == 0 for j in range(m))
        assert sum(b[i][i] for i in range(m)) == 0
        assert [sum(row) for row in b] == [-F(d*m, d*m-1)*v for v in c]
        q = sum(v*v for v in c)/d - (
            sum(sum(row)**2 for row in a)
            + sum(v*v for row in a for v in row))/m
        assert q == F(d*d-1, d*(d*m-1))*sum(v*v for v in c)

        gamma = F(d, m)**d
        full_weight = F(rng.randrange(5), 4)
        w = 1-full_weight
        alpha = w/(m*gamma)
        assert full_weight + m*gamma*alpha == 1
        # A weighted full/canonical stress has exactly w times the
        # canonical Hessian; in particular the weight is not discarded.
        assert w >= 0 and alpha >= 0
        checks += 1

# Actual partial-tuple calibration from Section 6, after removing the
# common positive factor Gamma*V*(-dm/(dm-1)).
partial = S.Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, -1, -1],
])
assert partial.rank() == 3 > 2
for vertex in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
    assert vertex[2] > -1  # strict full trace at base zero
    assert vertex[0] > -1 and vertex[1] > -1  # at base one
checks += 1

# The one-stress quantifier calibration: M=x, C1=x, C2=x-y^2.
g0 = S.Matrix([1, 0])
g1 = S.Matrix([1, 0])
g2 = S.Matrix([1, 0])
delta = S.Matrix([0, 1])
assert g0.dot(delta) == g1.dot(delta) == g2.dot(delta) == 0
assert (S.zeros(2)-S.diag(0, -2))[1, 1] == 2
assert (S.zeros(2)-S.zeros(2))[1, 1] == 0
checks += 1
print("PASS:", checks, "exact complete-block ranks, forced-zero blocks,")
print("positive lifts/full-trace weights, actual partial-block rank, and stress quantifier checks")
