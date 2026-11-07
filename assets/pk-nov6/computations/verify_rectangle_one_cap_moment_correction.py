"""Exact identities for the one-cap rectangle base-moment correction."""
from fractions import Fraction as F


def verify(t):
    assert 0 <= t <= 1
    left = 1 + 3*t
    middle = F(9, 2)
    right = (1+t)**2
    total = left + middle + right
    error = right-left
    removal = t-t*t
    retained = total-removal
    assert total == F(13, 2)+5*t+t*t
    assert error == -removal
    assert 0 <= removal <= F(1, 4)
    assert min(left, middle, right) >= 1
    # Primal removal at z=-1 and the gauge dual a=-1 match.
    masses = {-1: left, 0: middle, 1: right}
    primal = {-1: removal, 0: F(0), 1: F(0)}
    assert all(0 <= primal[z] <= masses[z] for z in masses)
    assert sum(z*primal[z] for z in masses) == error
    dual = -error - sum(w*max(F(0), -z-1) for z, w in masses.items())
    assert sum(primal.values()) == dual == removal
    # One removal cap x1-3(z+1) >= (1+t)^2.
    assert left-right == removal
    assert right+3 > 3
    assert right+6 > 1+t
    assert right >= 1
    assert retained == middle+2*right == F(13, 2)+4*t+2*t*t
    assert sum(z*(masses[z]-primal[z]) for z in masses) == 0
    # Centered version: the same one-sided left strip.
    threshold = F(1, 2)+t/2+t*t
    left_min = -left/2
    assert left/2-threshold == removal
    assert threshold-left_min == right
    assert (threshold+left_min)/2 == -removal/2
    assert threshold+3 > F(3, 2)
    assert threshold+6 > (1+t)/2
    # The old left unit square remains inside the retained fiber.
    assert left_min <= F(-1, 2) and threshold >= F(1, 2)
    cx = -right*removal/(2*retained)
    assert cx == -(1+t)**2*t*(1-t)/(2*retained)
    return retained, cx


for denominator in range(1, 51):
    for numerator in range(denominator+1):
        verify(F(numerator, denominator))

mass, cx = verify(F(1, 10))
assert mass == F(173, 25)
assert cx == F(-1089, 138400)
lower_cap = F(13, 4)-7*abs(cx)
target = F(4, 9)*mass
assert lower_cap == F(442177, 138400)
assert target == F(692, 225)
assert lower_cap-target > 0
# Rational bounds show 2 sqrt(2)+(3/2)sqrt(5)<7.
assert F(3, 2)**2 > 2 and F(7, 3)**2 > 5
assert 2*F(3, 2)+F(3, 2)*F(7, 3) < 7
assert F(13, 2) > F(1, 2)*F(25, 2)
print('PASS: one-cap correction, primal/dual masses, centroid, and depth slack.')
print('Exact certified depth surplus:', lower_cap-target)
