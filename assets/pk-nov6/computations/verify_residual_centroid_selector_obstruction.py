"""Exact rational arithmetic for the residual-selector obstruction."""
from fractions import Fraction as F

r = F(497,3000)
big_r = F(9,2)
ell = F(11,12)-big_r*r
t = F(3979,6000)
assert t == 1-r-ell
m = r*t**4
assert m == F(124581095445185057,3888000000000000000)
assert F(1,32)<m<F(11,20)**5<1
g_d_1 = 5*r/6
assert g_d_1 == F(497,3600)
y_res_1 = (F(1,6)-m*g_d_1)/(1-m)
assert y_res_1-F(1,6) == F(103,3600)*m/(1-m)>0

# The algebraic a=(2*m**(1/5)-1)**5 obeys 0<a<10^-5
# by the exactly verified interval 1/32<m<(11/20)^5.
assert F(2,25)*F(1,10**5)<F(1,6)-r
derivative_bound = F(12,25)*(1+F(12,125)*F(1,100))**4
assert derivative_bound == F(1148810043113472,2384185791015625)
assert derivative_bound<F(1,2)

# All residual means of a measure supported in D obey this stronger bound.
for j in range(1,101):
    mass = m*F(j,100)
    lowest_residual_x = (F(1,6)-mass*r)/(1-mass)
    assert lowest_residual_x>F(1,6)

print("PASS: exact BM mass, D centroid, residual direction and strict cap budget.")
