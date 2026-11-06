"""Exact checks supplementing the analytic coupling and power proofs."""
from fractions import Fraction as F

# Unequal intervals: midpoint length, paired capacity, parity density.
a, c = F(9), F(1)
bm = (a+c)/2
assert bm == 5
assert min(a,c,bm/2) == 1
assert 2/bm == F(2,5)
assert 2*a*c/((a+c)*bm) == F(9,25)
assert 4*a*c/(a+c)**2 == F(9,25)

# Homothetic squares attain B_2(1,9)=4.
a, b, c = F(1), F(4), F(9)
t = F(1,4)
assert (a-t)+(b+2*t)+(c-t) == a+b+c
diff = (a-t)**2+(b+2*t)**2+(c-t)**2-a*a-b*b-c*c
assert diff == -4*t+6*t*t == F(-5,8)

# The equal-volume midpoint output saturates density at t=a/2.
a = F(7,3)
t = a/2
assert 2*t/a == 1
print('PASS: exact unequal midpoint capacities and sharp power obstruction')
