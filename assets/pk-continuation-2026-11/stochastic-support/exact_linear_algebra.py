"""Exact Gaussian-elimination utility shared by the portable checkers.

Extracted without algorithm changes from the earlier absorption-certificate
checker. Callers supply Fraction matrices; this module performs no I/O.
"""

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
