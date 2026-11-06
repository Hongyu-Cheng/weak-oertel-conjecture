"""Exact arithmetic/identity checks for the weighted three-tail proof."""
from fractions import Fraction as F
import sympy as s

assert F(16,27)>F(1,2)
assert 43**2>30**2*2
assert sum((F(1,s.factorial(j)) for j in range(5)),F(0))==F(65,24)
assert F(65,24)+F(1,120)/(1-F(1,6))==F(1631,600)
assert F(1631,600)<F(30,11)
assert F(15,11)*F(11,30)==F(1,2)
assert F(11,30)>F(1,3)

# g=I^(1/alpha), I'=alpha*A, I''=alpha*(alpha-1)*B.
al,I,A,B=s.symbols('al I A B',positive=True)
chain=s.diff(I**(1/al),I,2)*(al*A)**2+s.diff(I**(1/al),I)*al*(al-1)*B
expected=(1-al)*I**(1/al-2)*(A*A-I*B)
assert s.simplify(chain-expected)==0

# H(R)>=0 is exactly the critical triple-tail inequality.
R,g,Ga,C=s.symbols('R g Ga C')
H=(1+C)*g-(Ga+s.Rational(1,2))-(2-Ga)*R
gap=((1+C)*g-s.Rational(5,2)*R)/(1-R)-(Ga+s.Rational(1,2))
assert s.factor(gap-H/(1-R))==0

# Exact d=2 powered-mean concavity under R=r^2, checked directly.
r=s.symbols('r',positive=True)
mean=s.Rational(2,3)*(1+r+r*r)/(1+r)
powmean=s.factor(mean**2)
dR=s.diff(powmean,r)/(2*r)
ddR=s.factor(s.diff(dR,r)/(2*r))
assert s.factor(ddR+2/(3*r*(1+r)**4))==0

# Fixed-tail subset optimization: a=1-F(t) is always a minimizer.
for den in range(1,41):
    for num in range(den+1):
        f=F(num,den); a0=1-f
        val0=max(F(0),a0-1+f)-a0/2
        assert val0==(f-1)/2
        for a in [F(0),a0/2,a0,(1+a0)/2,F(1)]:
            assert max(F(0),a-1+f)-a/2>=val0

print('PASS: dimensional constant, concavity identity, critical branch, and subset optimization.')
