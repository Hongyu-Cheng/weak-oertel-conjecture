"""Exact rational verifier; no optimization or approximate algebraic root."""
from fractions import Fraction as F
from math import comb

# Polynomial coefficients in increasing order.
coeff = [-11805, 9195, 8670, 2550, 375, 35]

def P(c):
    return sum(F(v)*c**r for r,v in enumerate(coeff))

# Check the entire finite-sum identity by coefficient comparison.
for r in range(6):
    lhs = sum((j-8)*comb(5,r)*j**(5-r) for j in range(10))
    assert lhs == -coeff[r], (r,lhs,coeff[r])
assert all(coeff[r]>0 for r in range(1,6))
assert P(F(2,3)) == -F(239945,243)
assert P(F(3,4)) == F(1198965,1024)

B_upper = sum(((F(j)+F(3,4))/(9+F(3,4)))**6 for j in range(10))
assert B_upper == F(2280098630,1172914587)
assert F(39,20)-B_upper == F(141696293,23458291740)
assert 100*6**6-39*7**6 == 77289
assert B_upper < F(39,20) < 5*F(6,7)**6
print('PASS: exact balance polynomial, positive-root interval, and strict moment-bound failure.')
