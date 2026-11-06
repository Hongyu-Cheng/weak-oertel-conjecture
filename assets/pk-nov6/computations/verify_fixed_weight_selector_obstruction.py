"""Exact rational certificates; algebraic parameters are bounded by powers."""
from fractions import Fraction as F

alpha=F(17,100)
beta=F(199999,1000000)
m=(1-alpha)**4-(1-beta)**4
assert m-F(1,16)==F(2481161996159996799999,10**24)
assert F(101,200)**4-m==F(56588628840003200001,10**24)
assert F(1,16)<m<F(101,200)**4
# Thus 0 < 2*m**(1/4)-1 < 1/100 and 0<a<10^-8.
assert F(1,5)-beta==F(1,10**6)
assert 2*(F(1,5)-alpha)==F(3,50)
assert F(3,50)*F(1,10**8)<F(1,5)-beta
assert (F(3,50)/(1-F(1,5)))==F(3,40)
derivative_bound=F(3,10)*F(43,40)**3
assert derivative_bound==F(238521,640000)<F(1,2)
print('PASS: exact slab volumes, algebraic-root bounds, endpoint separation, and strict cap bound.')
