"""Exact rational checks for the actual three-interval hypograph example."""
from fractions import Fraction as F

fibers = {-1: (F(-1, 2), F(1, 2)),
           0: (F(-11, 20), F(19, 20)),
           1: (F(-1, 2), F(1, 2))}
x0 = F(1, 10)


def lower_length(interval, threshold):
    lo, hi = interval
    return min(hi-lo, max(F(0), threshold-lo))


def lower_tent(interval, threshold):
    lo, hi = interval
    center = (lo+hi)/2
    if threshold <= lo:
        return F(0)
    if threshold >= hi:
        return (hi-lo)**2/4
    if threshold <= center:
        return (threshold-lo)**2/2
    return (hi-lo)**2/4-(hi-threshold)**2/2


M = sum(hi-lo for lo, hi in fibers.values())
Mh = sum((hi-lo)**2/4 for lo, hi in fibers.values())
plus = sum(hi-lo-lower_length((lo, hi), x0) for lo, hi in fibers.values())
minus = sum(lower_length(interval, x0+2*z) for z, interval in fibers.items())
plus_h = sum((hi-lo)**2/4-lower_tent((lo, hi), x0) for lo, hi in fibers.values())
minus_h = sum(lower_tent(interval, x0+2*z) for z, interval in fibers.items())
assert M == F(7, 2) and Mh == F(17, 16)
assert max(hi-lo for lo, hi in fibers.values()) < M/2
assert plus == minus == F(33, 20)
assert plus/M == F(33, 70)
assert plus_h == F(409, 800) and minus_h == F(369, 800)
assert plus_h-minus_h == F(1, 20)
lam_plus, lam_minus = F(35, 66), F(35, 22)
assert lam_plus+lam_minus == F(70, 33)
assert lam_plus*plus+lam_minus*minus == M
assert lam_plus*plus_h+lam_minus*minus_h == F(2653, 2640)
assert Mh-(lam_plus*plus_h+lam_minus*minus_h) == F(19, 330)

# Enumerate every affine-cut breakpoint: on each intervening tilt interval
# the original interval cap mass is affine, and both outside tails are
# constant. Thus the finite minimum is the exact all-tilt minimum.
for orientation in (1, -1):
    tilts = {F(0)}
    for z, interval in fibers.items():
        if z:
            tilts.update((endpoint-x0)/z for endpoint in interval)
    tilts = sorted(tilts)
    probes = tilts+[tilts[0]-1, tilts[-1]+1]
    def mass(a):
        lower = sum(lower_length(interval, x0+a*z)
                    for z, interval in fibers.items())
        return lower if orientation == -1 else M-lower
    assert min(mass(a) for a in probes) == F(33, 20)

# The proper-cut section measures and their full ambient centroids.
sections_plus = [(F(z), x0) for z, (lo, hi) in fibers.items() if lo < x0 < hi]
sections_minus = [(F(z), x0+2*z) for z, (lo, hi) in fibers.items()
                  if lo < x0+2*z < hi]
assert len(sections_plus) == 3 and len(sections_minus) == 1
for sections in (sections_plus, sections_minus):
    assert tuple(sum(p[i] for p in sections)/len(sections) for i in range(2)) == (F(0), x0)

print("PASS: all exact cap budgets, all-tilt minima, section centroids, and hypograph errors")
