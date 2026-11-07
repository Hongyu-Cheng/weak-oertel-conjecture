"""Exact certificates for the all-d three-quarter source-cost bound."""
from fractions import Fraction as F
from math import factorial

lower = [388,234,173,140,120,106,96,89,83,78,74,71,68,66,64,62,61,59,58]
for d, ell in enumerate(lower, 1):
    k = F(d+1,d)**d
    h = F(4,3)*k-1
    a = (1+F(1,2*d))**(d+1)
    b = max(F(0),1-h/F(2*d))**(d+1)
    gap = 1+F(d+1,2*d)*(1+k/3)-a-b
    assert 1000*gap > ell > 0
    n, p, big_d = d**d, (d+1)**d, d+1
    r = 3*(2*d+1)*n-4*p
    assert r > 0
    numerator = (1000*(6*d*n+(d+1)*(3*n+p))*(2*d)**(big_d-1)*(3*n)**d
                 -1000*(2*d+1)**big_d*(3*n)**big_d-1000*r**big_d)
    denominator = (2*d)**big_d*(3*n)**big_d
    assert numerator > ell*denominator
    assert F(numerator,denominator) == 1000*gap

assert 21**20 > 53*20**19
assert F(87,32) < F(33,20)**2
exp_lower = sum(F(19,15)**j/factorial(j) for j in range(6))
assert exp_lower == F(161384087,45562500)
assert exp_lower > F(60,17)
assert F(33,20)+F(17,60) == F(29,15)
assert (1+F(53,60))/2 == F(113,120)
assert F(233,120)-F(29,15) == F(1,120)
assert F(113,120)-F(33,40) == F(14,120)
print('PASS: 19 exact integer certificates and every all-d constant.')
