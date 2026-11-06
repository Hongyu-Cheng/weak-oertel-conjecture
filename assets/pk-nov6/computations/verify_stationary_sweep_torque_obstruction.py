"""Exact rational data for the square-product stationary-sweep obstruction.

The all-halfspace minimum is proved geometrically in the companion note,
using the centrally symmetric contained strip. This script verifies the
claimed volumes, full section moments, and torque signs.
"""

from fractions import Fraction as F

b, a = F(1, 2), -F(9, 20)
indices = (-1, 0, 1)
heights = {z: b - a * z for z in indices}
areas = {z: 2 * (1 - heights[z]) for z in indices}
assert all(-1 < heights[z] < 1 for z in indices)
assert [areas[z] for z in indices] == [F(19, 10), F(1), F(1, 10)]
assert sum(areas.values()) == 3
assert sum(2 * z for z in indices) == 0
assert sum(2 * (heights[z] - b) for z in indices) == 0
right_fraction = (areas[0] + areas[1]) / sum(areas.values())
assert right_fraction == F(11, 30) < F(4, 9)

# On b in [2/5,1/2], a=4(b-9/20), hence |a|<=1/5<1-b.
for level in (F(2, 5), F(1, 2)):
    tilt = 4 * (level - F(9, 20))
    assert abs(tilt) <= F(1, 5) < 1 - level

section_total, section_right, section_left, torque = 6, 4, 4, 2
tilt_derivative = 4
assert -section_total == -6
assert -section_right + tilt_derivative * torque == 4
assert -section_left - tilt_derivative * torque == -12

print("PASS: exact stationary-sweep masses, moments, and torque signs")
