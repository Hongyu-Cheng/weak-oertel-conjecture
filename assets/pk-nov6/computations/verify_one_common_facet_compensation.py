"""Exact symbolic/Fraction checks for one-common-facet-triangle-compensation.md."""
from fractions import Fraction as F
import sympy as sp

p = sp.symbols('p', positive=True)
gamma = sp.Rational(4, 9)
w = 1 - 2*p
w3 = 2*p**2/(1-p)
sigma = (1-3*p)/(1-p)
lam = (1-2*p)/(1-p)**2
lam3 = 1/(2*(1-p))
total = 2*lam+lam3
T = 2*w+w3-1
assert sp.factor(w-w3-sigma) == 0
assert sp.factor(T-sigma*(1-2*p)) == 0
assert sp.factor(2*w*p**2-w3*(1-2*p)*(1-p)) == 0
assert sp.factor(w*(1+2*p)+2*w3*(1-p)-1) == 0
assert sp.factor(T+w*(3*p-1)/(1-p)) == 0
# The k=3 vector coefficient is W=-sigma*u3 plus the displayed term.
assert sp.factor(-sigma+T+w3*(3*(1-2*p)-1)/(2*p)) == 0
assert sp.factor(2*lam*(1-p)-(1+sigma)) == 0
assert sp.factor(total-(5-9*p)/(2*(1-p)**2)) == 0
assert sp.factor(1-gamma*total+2*sigma
                 -(1-3*p)*(17-21*p)/(9*(1-p)**2)) == 0

def length_overlap(a, b, c, d):
    return max(F(0), min(b, d)-max(a, c))

for den in range(4, 60):
    for num in range(1, (den+2)//3):
        r = F(num, den)
        if not 0 < r < F(1, 3):
            continue
        l = (1-2*r)/(1-r)**2
        s = (1-3*r)/(1-r)
        L = 2*l+1/(2*(1-r))
        assert s > 0
        assert 1-F(4,9)*L+2*s > 0
        for left in [F(0), r/2, r, (r+F(1,2))/2, F(1,2)]:
            for right in [F(1,2), (F(3,2)-r)/2, 1-r, 1-r/2, F(1)]:
                if right <= left:
                    continue
                mass = l*(length_overlap(left,right,r,F(1))
                          +length_overlap(left,right,F(0),1-r))
                assert mass >= (right-left)*2*l*(1-r)
print('PASS: symbolic stress identities and exact interval-profile inequalities')
