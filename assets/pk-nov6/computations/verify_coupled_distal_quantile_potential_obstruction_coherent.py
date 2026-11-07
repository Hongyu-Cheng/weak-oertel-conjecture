#!/usr/bin/env python3
"""Exact calibration of actual simultaneous distal cuts; no floating point."""
from fractions import Fraction as F

checks = 0
R = {-1: F(1), 0: F(3, 2), 1: F(1)}
B = F(7, 2)
k = F(5, 4)

def check(condition):
    global checks
    assert condition
    checks += 1

def cap_length(lo, hi, u, c, z, threshold):
    if hi < lo:
        return F(0)
    if u == 1:
        return max(F(0), hi-max(lo, threshold-c*z))
    assert u == -1
    return max(F(0), min(hi, c*z-threshold)-lo)

caps = [(1, k), (1, -k), (-1, F(0))]
for u, c in caps:
    check(sum(cap_length(-r, r, u, c, z, F(0)) for z, r in R.items()) == B)
check(sum(2*r for r in R.values()) == 7)
check(all(2*r < B for r in R.values()))
check(caps[0][0]+caps[1][0]+2*caps[2][0] == 0)
check(caps[0][1]+caps[1][1]+2*caps[2][1] == 0)
for j, (z, x) in enumerate([(1, F(1,2)), (-1, F(1,2)), (0, F(-1,2))]):
    check([i for i,(u,c) in enumerate(caps) if u*x+c*z >= 0] == [j])

def quantiles(a):
    if a <= F(1,4):
        t = a
    elif a <= F(11,4):
        t = (a+F(1,4))/2
    else:
        t = a-F(5,4)
    s = a/3 if a <= 3 else a-2
    return t, s

pieces = [
    (F(0), F(1,4), F(4,3), F(0)),
    (F(1,4), F(27,20), F(5,6), F(1,8)),
    (F(27,20), F(11,4), F(5,2), F(-17,8)),
    (F(11,4), B, F(3), F(-7,2)),
]

def mass_formula(a):
    for lo, hi, slope, intercept in pieces:
        if lo <= a <= hi:
            return slope*a+intercept
    raise AssertionError(a)

for left, right in zip(pieces, pieces[1:]):
    knot = left[1]
    check(knot == right[0])
    check(left[2]*knot+left[3] == right[2]*knot+right[3])
check(mass_formula(F(0)) == 0)
check(mass_formula(B) == 7)
check(mass_formula(F(27,20)) == F(5,4))
check(pieces[1][2] < pieces[2][2])
check(pieces[0][2] > pieces[1][2])
check(F(5,4)/F(27,20) == F(25,27))

parameters = {F(0), B, F(1,4), F(27,20), F(11,4), F(3)}
for den in range(1, 51):
    parameters.update(F(num, den) for num in range(0, int(B*den)+1))

for a in sorted(parameters):
    t, s = quantiles(a)
    thresholds = [t, t, s]
    for (u,c), threshold in zip(caps, thresholds):
        tail = sum(cap_length(-r, r, u, c, z, threshold) for z,r in R.items())
        check(tail == B-a)
    fibers = {}
    for z,r in R.items():
        lo = max(-r, -s)
        hi = min(r, t-k*z, t+k*z)
        fibers[z] = (lo, hi)
    mass = sum(max(F(0), hi-lo) for lo,hi in fibers.values())
    check(mass == mass_formula(a))
    for u,c in caps:
        new_cap_mass = sum(cap_length(lo,hi,u,c,z,F(0)) for z,(lo,hi) in fibers.items())
        check(new_cap_mass <= a)
    positive = {z for z,(lo,hi) in fibers.items() if hi>lo}
    check(positive == (set() if a == 0 else {0} if a <= F(27,20) else {-1,0,1}))
    if a > 0:
        check(fibers[0][0] < 0 < fibers[0][1])
        check(mass > 0)
    removed_excess = 3*(B-a)-(7-mass)
    check(removed_excess >= 0)
    check(mass == 3*a-((3*B-7)-removed_excess))

# Explicit ratio witnesses falsify either monotonicity direction.
check(mass_formula(F(1,4))/F(1,4) > mass_formula(F(1))/F(1))
check(mass_formula(F(2))/F(2) < mass_formula(B)/B)

print(f"PASS {checks} exact checks at {len(parameters)} rational parameters")
