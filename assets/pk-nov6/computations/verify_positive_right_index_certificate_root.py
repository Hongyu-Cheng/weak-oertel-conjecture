"""Independent polynomial reconstruction for the all-index knot certificate."""
from fractions import Fraction as F
from math import comb
import sympy as s

v=s.symbols('v')
U=-v**2/4-v**3/3+v/(1+v)-s.Rational(1,2)+3*v/(4*(1+2*v))+v**2/(4*(1+2*v)**2)+1/(8*(1+2*v))
P=[F(9),F(9),F(-60),F(-52),F(88),F(88),F(32)]
assert s.cancel(-U*24*(1+v)*(1+2*v)**2-s.Add(*[s.Rational(c.numerator,c.denominator)*v**i for i,c in enumerate(P)]))==0
cases=[(F(0),F(1,2),[F(9),F(39,4),F(19,2),F(317,40),F(76,15),F(43,24),F(3,4)]),
       (F(1,2),F(3,5),[F(3,4),F(13,24),F(317,750),F(2071,5000),F(3377,6250),F(10353,12500),F(20448,15625)]),
       (F(3,5),F(1),[F(20448,15625),F(2019,625),F(25726,3125),F(457,25),F(13588,375),F(331,5),F(114)])]
for low,high,expected in cases:
    width=high-low
    power=[sum(P[i]*comb(i,j)*low**(i-j)*width**j for i in range(j,7)) for j in range(7)]
    bern=[sum(power[j]*F(comb(k,j),comb(6,j)) for j in range(k+1)) for k in range(7)]
    assert bern==expected
    assert min(bern)>=F(2,5)
    reverse=[sum(bern[k]*comb(6,k)*comb(6-k,j-k)*(-1)**(j-k) for k in range(j+1)) for j in range(7)]
    assert reverse==power
assert F(2,5)/432==F(1,1080)
print('PASS: rational identity, 21 reconstructed coefficients, 3 reverse identities, and final constant')
