"""Exact arithmetic accompanying the current classical audit, not a proof by sampling."""
from fractions import Fraction as F
import sympy as s

checks = 0
def eq(a,b):
    global checks
    assert s.simplify(a-b)==0, (a,b)
    checks += 1
def yes(p):
    global checks
    assert p
    checks += 1

eta,w,H=s.symbols('eta w H', real=True)
qlo=(1+(1-eta/3)**2/4)*w+3*(1-eta)*(3-eta)/4
gap=(s.Rational(2,3)+(1-eta/3)**2/4)*w+s.Rational(1,4)-3*eta+3*eta**2/4
eq(qlo-(2+w/3),gap)
root=2-s.sqrt(33)/3
eq((s.Rational(1,4)-3*eta+3*eta**2/4).subs(eta,root),0)
eq((s.Rational(1,4)-3*eta+3*eta**2/4).subs(eta,s.Rational(1,12)),s.Rational(1,192))
yes(23**2>16*33)
yes(33>9)
eq(s.Rational(4,9)*s.Rational(1,12)**2,s.Rational(1,324))
eq((H-1)+(1-eta/H)*(-1-(H-1)),-1+eta)
for r in range(13):
    e=F(r,144)
    yes(F(1,4)-3*e+F(3,4)*e*e>=F(1,192))
    yes(F(2,3)+(1-e/3)**2/4>0)
    for hh in [F(3),F(7,2),F(10)]:
        yes((1-e/hh)**2>=(1-e/3)**2)
eq(F(259200,49*65536),F(2025,25088))
yes(F(2025,25088)<F(1,9))
for d in range(2,31):
    gamma=F(d,d+1)**d
    yes(1-2*gamma>0)
    # X<=2Q+E, Q<=Gamma(X+b)/2, b<=X imply the exact deficit.
    X,b=s.symbols('X b',real=True)
    eq(X-gamma*(X+b)-(1-2*gamma)*X,gamma*(X-b))
for gamma,rho,C,expected in [
    (F(4,9),F(2,3),F(1,2),F(6,7)),
    (F(27,64),F(1,2),F(88,81),F(12,13)),
    (F(256,625),F(46,125),F(4,3),F(690,851)),
]:
    yes(1-gamma*C>0)
    eq(rho/(1-gamma*C),expected)
print(f'PASS {checks} exact checks')
