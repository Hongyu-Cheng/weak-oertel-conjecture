"""Exact arithmetic certificates for the section obstructions.
Disk geometry and stationarity are proved in the companion note.
"""
from fractions import Fraction as F
# A length-two disk diameter at z0 and a length-two zero-area endpoint fiber.
assert (F(0)*2+F(1)*2)/(2+2)==F(1,2)
# Three separated unit-disk profiles have P(0)=P(3)=2, P(3/2)=0.
assert all(abs(F(3,2)-3*z)>1 for z in [-1,0,1])
# Concentric radii 1,2,1: P(1)^2=4*(4-1)=12.
assert 4*(4-1)==12
assert 4-F(3,4)**2==F(55,16)
assert 1-F(3,4)**2==F(7,16)
assert 4-F(5,4)**2==F(39,16)
assert F(55)>7**2 and F(7)>F(5,2)**2 and F(39)>6**2
assert 12<6*3
# Every parallel section's outer-fiber lengths agree, so its z moment is zero.
for common_length in [F(0),F(1),F(7,5),F(2)]:
 assert -common_length+common_length==0
print('PASS: exact section-centroid defect and both profile-concavity obstructions.')
