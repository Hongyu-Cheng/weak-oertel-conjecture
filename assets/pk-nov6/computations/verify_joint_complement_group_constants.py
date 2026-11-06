from fractions import Fraction as F

# Exact planar-simplex joint-complement obstruction.
cap=F(4,9)
pair_cap=F(1,9)
single_remainder=1-cap
pair_remainder=1-2*cap+pair_cap
triple_remainder=1-3*cap+3*pair_cap
assert single_remainder==F(5,9)
assert pair_remainder==F(2,9)>0
assert triple_remainder==0

# Full overlap penalty calibration on interval groups.
# One fiber [-1,1], caps x>=-delta and x<=delta.
for delta in [F(0),F(1,10),F(1,2),F(1)]:
 B=1+delta
 overlap=2*delta
 assert 2*B-overlap==2
 assert B==F(2,2)+overlap/2
print('PASS: exact joint-remainder and overlap constants')
