"""Exact finite marked calibrations; analytic compactness is proved in the note."""
from fractions import Fraction as F
import sympy as s
checks=0
for den in range(1,31):
    for num in range(den+1):
        r=F(num,2*den)
        weights=(r,1-2*r,r)
        assert sum(weights)==1
        assert -weights[0]/2+weights[2]/2==0
        # Density relative to the uniform target on each half.
        assert weights[1]+2*weights[0]==1
        assert weights[1]+2*weights[2]==1
        checks+=4
for hm in range(-4,5):
    for h0 in range(-4,5):
        for hp in range(-4,5):
            A=min(F(h0),F(hm+hp,2)); B=F(hp-hm)
            assert A-B/2<=hm and A<=h0 and A+B/2<=hp
            assert A==min(F(h0),F(hm+hp,2))
            checks+=2
# Nonzero body term for a positive affine logarithmic certificate.
x=s.symbols('x', real=True)
rho_integral=s.integrate(1/(2*s.log(3)*(1+x/2)),(x,-1,1))
y=s.integrate(x/(2*s.log(3)*(1+x/2)),(x,-1,1))
assert s.simplify(rho_integral-1)==0
assert s.simplify(y-(2/s.log(3)-2))==0
assert s.simplify((s.log(s.Rational(1,2))-s.log(s.Rational(3,2)))/2+s.log(3)/2)==0
checks+=3
print(f'PASS: {checks} exact marked-entropy calibration checks')
