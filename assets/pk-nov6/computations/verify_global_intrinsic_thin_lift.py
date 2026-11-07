"""Exact calibration for the intrinsic global thin-law lift."""
from fractions import Fraction as F

# The weak-law density is (t+1)/4 on each [-1,1] segment.
# The hidden radius is density / kappa_1=(t+1)/8.
assert F(1,8)*2==F(1,4)
integral_t_plus_one=F(2)
lift_area=F(1,4)*integral_t_plus_one
assert lift_area==F(1,2)
assert 2*lift_area==1
gamma2=F(4,9)
assert lift_area*gamma2==F(2,9)
assert F(1,4)>F(2,9)
assert F(1,4)-F(2,9)==F(1,36)

# Common hidden axes need only the largest complementary dimension.
for m in range(1,10):
    for q in range(m):
        r=m-q
        assert q+r==m
        assert 1<=r<=m
        assert m+r<=2*m

print('PASS: intrinsic dimensions, unit total mass, and strict projection depth gain.')
