"""Exact certificate for the simultaneous localization obstruction."""
from fractions import Fraction as F

V=F(1,2)
threshold=F(1,3)
cap_area=(1-threshold)**2*V
total=3*V
cap_probability=cap_area/total
assert cap_area == F(2,9)
assert cap_probability == F(4,27)
oc_threshold=F(2,3)**2/2
assert oc_threshold == F(2,9)
assert oc_threshold-cap_probability == F(2,27) > 0
assert F(1,3)*F(1,2)-cap_probability == F(1,54) > 0

# Homothety about vertex (1,0), respectively (0,1), gives these centroids.
centroid=(F(1,3),F(1,3))
cap1=(threshold+(1-threshold)*centroid[0],(1-threshold)*centroid[1])
cap2=((1-threshold)*centroid[0],threshold+(1-threshold)*centroid[1])
assert cap1==(F(5,9),F(2,9))
assert cap2==(F(2,9),F(5,9))
assert (cap1[0]-centroid[0],cap1[1]-centroid[1]) == (F(2,9),F(-1,9))
assert (cap2[0]-centroid[0],cap2[1]-centroid[1]) == (F(-1,9),F(2,9))
assert 2*2-(-1)*(-1)==3

print("PASS: exact bad-cap masses, median obstruction, and affine-variation rank")
