"""Exact breakpoint certificate for the four-fiber reflection calculation."""
from fractions import Fraction as F

w = {0: F(2), 1: F(6), 2: F(10), 3: F(3)}
M = sum(w.values())

def overlap(a, c, y):
    return max(F(0), min(a, c, 2*y, a+c-2*y))

def retention(j, y):
    return sum(overlap(a, w[2*j-z], y)
               for z, a in w.items() if 2*j-z in w)

def scalar_bound(j):
    return w[j] + 2*sum(
        min(w[j-k], w[j+k], max(F(0), w[j-k]+w[j+k]-w[j]))
        for k in range(1, 4) if j-k in w and j+k in w)

assert M == 21
assert [scalar_bound(j) for j in w] == [2, 10, 10, 3]
assert all(retention(j, w[j]/2) == scalar_bound(j) for j in w)
assert max(scalar_bound(j) for j in w) < M/2

pieces = {
    1: [(F(0), F(1), 6, 0), (F(1), F(3), 2, 4),
        (F(3), F(5), -2, 16), (F(5), F(6), -6, 36)],
    2: [(F(0), F(3,2), 6, 0), (F(3,2), F(3), 2, 6),
        (F(3), F(9,2), -2, 18), (F(9,2), F(5), 2, 0),
        (F(5), F(10), -2, 20)]
}

# Every possible min/max switch of a summand occurs among these points.
def all_breakpoints(j):
    points = {F(0), w[j]}
    for z, a in w.items():
        if 2*j-z not in w:
            continue
        c = w[2*j-z]
        points.update({F(0), min(a,c)/2, max(a,c)/2, (a+c)/2})
    return sorted(p for p in points if 0 <= p <= w[j])

for j, blocks in pieces.items():
    declared = {b for lo, hi, _, _ in blocks for b in (lo, hi)}
    assert set(all_breakpoints(j)) <= declared
    for lo, hi, slope, intercept in blocks:
        # On this interval every summand is affine. Endpoint agreement
        # therefore proves the entire displayed piece; midpoint is redundant.
        for y in (lo, (lo+hi)/2, hi):
            assert retention(j, y) == slope*y+intercept

maxima = {j: max(retention(j, y) for y in all_breakpoints(j)) for j in w}
assert maxima == {0:F(2), 1:F(10), 2:F(12), 3:F(3)}
assert retention(2, F(3)) == 12
assert F(12, M) == F(4,7) > F(1,2)
print('PASS: midpoint bound fails; actual reflection maximum is 12/21=4/7.')
