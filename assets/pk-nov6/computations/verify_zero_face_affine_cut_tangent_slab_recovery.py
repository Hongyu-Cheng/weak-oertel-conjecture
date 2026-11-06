"""Exact cone/collar and normalization algebra for the analytic tangent note."""
import sympy as s
from fractions import Fraction as F
checks=0
def ck(q):
    global checks
    assert q
    checks+=1
c,t,r=s.symbols('c t r',positive=True)
I=((c-t)**2*s.log(c-t)/2-(c-t)**2/4+t*((c-t)*s.log(c-t)-(c-t)))/c**2
ck(s.simplify(s.diff(I,t).subs(t,0)+1/c)==0)
ck(s.simplify(I.subs(t,0)-(s.log(c)/2-s.Rational(1,4)))==0)
removed=t*t*s.log(t)/(2*c*c)-t*t/(4*c*c)
ck(s.simplify(s.diff(removed,t)-t*s.log(t)/c**2)==0)
eta,B=s.symbols('eta B',positive=True)
primitive=(r+eta)*s.log(r+eta)-r*s.log(r)-eta
ck(s.simplify(s.diff(primitive,r)-s.log(1+eta/r))==0)
# Exact projection multipliers for the cap-to-later-section construction.
for den in range(5,46):
    height=F(1,den)
    H=2*height
    for j in range(9):
        old_s=height*F(j,8)
        theta=(1-H)/(1-old_s)
        ck(F(1,2)<theta<=1)
        ck(theta*old_s+(1-theta)==H)
        ck(1/theta<=2)
# Uniform bulk logarithm derivative bound follows from denominator>=L/2.
for den in range(2,41):
    rr=F(1,den)
    ck(1-rr>=F(1,2))
    ck(1/(1-rr)<=2)
print(f'PASS: {checks} exact checks')
