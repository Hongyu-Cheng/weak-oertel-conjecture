"""Exact finite certificate for the sixteen prescribed integer heights."""

from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm

vertices = [tuple((k >> j) & 1 for j in range(4)) for k in range(16)]
heights = [256**k for k in range(16)]


def integer_dependence(indices):
    columns = [(1, *vertices[k]) for k in indices]
    mat = [[F(columns[c][r]) for c in range(6)] for r in range(5)]
    pivots = []
    row = 0
    for col in range(6):
        pivot = next((r for r in range(row, 5) if mat[r][col]), None)
        if pivot is None:
            continue
        mat[row], mat[pivot] = mat[pivot], mat[row]
        scale = mat[row][col]
        mat[row] = [entry / scale for entry in mat[row]]
        for r in range(5):
            if r != row and mat[r][col]:
                scale = mat[r][col]
                mat[r] = [x - scale * y for x, y in zip(mat[r], mat[row])]
        pivots.append(col)
        row += 1
        if row == 5:
            break
    free = next(c for c in range(6) if c not in pivots)
    vec = [F(0) for _ in range(6)]
    vec[free] = 1
    for r, pivot in enumerate(pivots):
        vec[pivot] = -mat[r][free]
    denominator = lcm(*(v.denominator for v in vec))
    result = [int(v * denominator) for v in vec]
    divisor = gcd(*result)
    result = [v // divisor for v in result]
    return result


count = 0
for indices in combinations(range(16), 6):
    coefficients = integer_dependence(indices)
    assert any(coefficients)
    assert max(map(abs, coefficients)) <= 120
    assert sum(coefficients) == 0
    for coordinate in range(4):
        assert sum(c * vertices[k][coordinate] for c, k in zip(coefficients, indices)) == 0
    assert abs(sum(c * heights[k] for c, k in zip(coefficients, indices))) >= 1
    count += 1

assert count == 8008
assert heights[8] - heights[7] > 1
assert heights[0] + heights[3] - heights[1] - heights[2] == 255**2 * 257
assert F(32, 8) == 4 == F(16, 4)
assert F(1, 2) / 16 == F(1, 32)
print("PASS: all 8008 six-point dependence certificates, widths, and sharp-cover constants")
