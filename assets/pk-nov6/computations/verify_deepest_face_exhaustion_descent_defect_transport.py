"""Exact all-breakpoint interval calibration of the actual hull expansion."""
from fractions import Fraction as F

checks = 0
def check(ok):
    global checks
    assert ok
    checks += 1

def clamp(x, lo, hi):
    return max(lo, min(x, hi))

A, B = F(8), F(1)
breakpoints = (-A/2, -B/2, B/2, A/2)
slopes = tuple(sorted(set(breakpoints + (-A-B, A+B))))
endpoint = [clamp(A/2-a, F(0), A)+clamp(B/2+a, F(0), B)
            for a in slopes]
check(min(endpoint) == B)
for a in slopes:
    check(clamp(A/2-a, F(0), A)+clamp(B/2+a, F(0), B) >= B)
    check(clamp(A/2+a, F(0), A)+clamp(B/2-a, F(0), B) >= B)

for numerator in range(0, 75):
    t = F(numerator, 100)
    K = F(9, 2)+2*t
    M = A+B+K
    q_middle = K/2+B
    check(K >= (A+B)/2)
    check(q_middle == F(13, 4)+t)
    check(q_middle < A/2)
    check(K+B > q_middle)  # least pure-base middle cap
    check(max(A/2, B/2, q_middle) == 4)
    check(M == F(27, 2)+2*t)
    if t:
        check(4/M < F(8, 27))
        check(M > F(27, 2))

# Rank-zero bound uses the two ACTUAL nonzero continuous normals.
for left in range(1, 13):
    for right in range(1, 13):
        length = F(left+right)
        depth = F(min(left, right))
        check(depth <= length/2)  # baseDepth - V/2, baseDepth=V

print(f"PASS: {checks} exact deepest-face descent calibration checks")
