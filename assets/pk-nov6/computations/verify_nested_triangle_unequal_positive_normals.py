from fractions import Fraction as F

radii = [F(1,2), F(3,2), F(3,4)]
bases = [-1, 0, 1]
a, beta = F(6,7), F(-3,28)
assert (radii[0]+radii[2])/2 <= radii[1]
thresholds = [F(1,2)-beta*z for z in bases]
assert thresholds == [F(11,28),F(1,2),F(17,28)]
for r,t in zip(radii,thresholds):
    assert (1-a)*r < t < a*r
differences = [a*r-t for r,t in zip(radii,thresholds)]
assert differences == [F(1,28),F(11,14),F(1,28)]
candidate = sum(x*x for x in differences)/(a*(2*a-1))
assert candidate == F(81,80)
coordinate_min = F(1) + F(1,8)**2 + F(1,8)**2
assert coordinate_min == F(33,32)
assert coordinate_min-candidate == F(3,160)
assert F(1)+F(1,16) > coordinate_min
equal_min = radii[1]**2-4*F(1,2)**2
assert equal_min == F(5,4)
# The whole indicated interval makes both equal-normal endpoint caps zero.
for b in [F(-1,4), F(1,8)]:
    assert F(1,2)+b >= radii[0]/2
    assert F(1,2)-b >= radii[2]/2
mass = sum(r*r for r in radii)
assert mass == F(49,16)
assert 2*radii[1]**2 > mass
assert F(4,9)*radii[1]**2 == 1 > F(2,9)*mass
print('PASS: actual triangle family, all exact cap branches, unequal-normal improvement, restricted minima, and OC safety')
