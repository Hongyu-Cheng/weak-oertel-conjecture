"""Exact arithmetic checks for the unequal transport and planar window."""
from fractions import Fraction as F
from random import Random
from math import prod
import sympy as s

checks=0
def check(x):
    global checks
    assert x
    checks+=1
c=F(6144,22745)
check(c>F(2,9))
check(c/4-F(5,18)<0)
check(F(19,6)*c-F(23,27)==F(2177,614115))
a,b,k,C=s.symbols('a b k C',positive=True)
gap=C*(k+2*a)-s.Rational(2,9)*(k+a+b)
check(s.factor(gap.subs(k,(b+3*a)/4)-((C/4-s.Rational(5,18))*b+(11*C/4-s.Rational(7,18))*a))==0)
check(s.factor(s.Rational(3,4)*(k+a)-(k+a+b)/2-(k+a-2*b)/4)==0)
theta,AA,eps,al,U,Q,E=s.symbols('theta AA eps al U Q E',positive=True)
XX=1+AA/3-eps
check(s.expand(AA+theta*XX-(theta+4*AA/3-((1-theta)*AA/3+theta*eps)))==0)
L=4*AA/3-1
check(s.expand(U+theta*Q+theta*E-theta-(U+theta*Q-theta*L*E+theta*(L+1)*E-theta))==0)
for d in range(1,31):
    AA0=F(d+1,d)**d
    PP=(1+F(1,2*d))**(d+1)
    RR=max(F(0),1-(4*AA0/3-1)/(2*d))**(d+1)
    ee=1+AA0/3-F(2*d,d+1)*(PP+RR-1)
    check(0<ee<=AA0/3)
    for tt in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
        margin=(1-tt)*AA0/3+tt*ee
        check(0<margin<=AA0/3)

rng=Random(154917)
for d in range(1,13):
    for it in range(100):
        roots=[F(rng.randint(1,20),rng.randint(1,20)) for _ in range(d)]
        ts=[r**d for r in roots]
        check(prod(1+t for t in ts)>=(1+prod(roots))**d)
for den in range(1,31):
    for num in range(den,(5*den)//3+1):
        R=F(num,den)
        for extra in [F(0),F(1,10),F(1),F(10)]:
            K=(R+3)/4+extra
            check(c*(K+2)-F(2,9)*(K+1+R)>=F(2177,614115))
print(f'PASS: {checks:,} exact transport and original-mass checks')
