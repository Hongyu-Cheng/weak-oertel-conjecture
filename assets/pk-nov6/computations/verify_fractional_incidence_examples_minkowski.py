"""Independent rational checks of the two fractional-cover examples.

These verify the displayed examples, not the general projection/Helly theorem.
"""
from fractions import Fraction as F

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


# A cap is (orientation, slope, intercept): orientation*(x-slope*z-intercept)>=0.
def margin(cap, z, x):
    orientation, slope, intercept = cap
    return orientation * (x - slope * z - intercept)


def cap_length(cap, z, interval):
    orientation, slope, intercept = cap
    left, right = interval
    threshold = slope * z + intercept
    if orientation == 1:
        return max(F(0), right - max(left, threshold))
    return max(F(0), min(right, threshold) - left)


partition_caps = [(1, 6, 6), (-1, -2, -2), (1, -1, 1), (-1, 3, 1)]
partition_fibers = {-1: (F(-1), F(1)), 0: (F(-1), F(5)), 1: (F(5), F(7))}
expected_lengths = {-1: (1, 1, 0, 0), 0: (0, 0, 4, 2), 1: (0, 0, 2, 0)}
for z, interval in partition_fibers.items():
    lengths = tuple(cap_length(cap, z, interval) for cap in partition_caps)
    check(lengths == expected_lengths[z])
    check(sum(lengths) == interval[1] - interval[0])
    for cap, length in zip(partition_caps, lengths):
        if length == 0:
            check(max(margin(cap, z, x) for x in interval) < 0)
check(tuple(sum(cap_length(cap, z, interval) for z, interval in partition_fibers.items())
            for cap in partition_caps) == (1, 1, 6, 2))
check((partition_fibers[-1][0] + partition_fibers[1][0]) / 2 == 2)
check((partition_fibers[-1][1] + partition_fibers[1][1]) / 2 == 4)
check(len({z % 2 for z in partition_fibers}) == 2)

upper_thresholds = [(0, 0), (2, -1), (2, 1), (2, 0)]
lower_thresholds = [(1, 0), (1, -1), (1, 1), (3, 0)]
fractional_caps = [(1, a, b) for a, b in upper_thresholds]
fractional_caps += [(-1, a, b) for a, b in lower_thresholds]
expected_knots = {-1: [-3, -2, -1, 0], 0: [-1, 0, 0, 1], 1: [0, 1, 2, 3]}
for z in (-1, 0, 1):
    upper = sorted(a*z+b for a, b in upper_thresholds)
    lower = sorted(a*z+b for a, b in lower_thresholds)
    check(upper == lower == expected_knots[z])
    knots = sorted({F(-4), F(4), *map(F, upper)})
    for left, right in zip(knots, knots[1:]):
        x = (left + right) / 2
        check(sum(F(1, 4) for cap in fractional_caps if margin(cap, z, x) >= 0) == 1)
    for x in knots:
        check(any(margin(cap, z, x) >= 0 for cap in fractional_caps))
    for cap in fractional_caps:
        check(0 < cap_length(cap, z, (F(-4), F(4))) < 8)
check(set(upper_thresholds).isdisjoint(lower_thresholds))
masses = tuple(sum(cap_length(cap, z, (F(-4), F(4))) for z in (-1, 0, 1))
               for cap in fractional_caps)
check(masses == (12, 15, 9, 12, 12, 9, 15, 12))
check(sum(masses) / 4 == 24)
# An incidental two-cap global cover exists; no claim of minimal size four is made.
check(all(2*z-1 <= z+1 for z in (-1, 0, 1)))
print(f"PASS: {checks} independent exact example checks")
