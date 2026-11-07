"""Exact certificates for shared-roof slab examples and anchored bounds."""
from fractions import Fraction as F
import sympy as s

checks=0
def check(a,b):
    global checks
    assert s.simplify(a-b)==0,(a,b)
    checks+=1

def clamp(x): return min(F(1),max(F(0),x))
for x,t1,t2 in [(F(-1),F(1),F(0)),(F(0),F(1),F(1)),(F(1),F(1),F(0))]:
    check(clamp(-x*x+2),t1)
    check(clamp(-x*x+1),t2)

x,L=s.symbols('x L',positive=True)
g=s.Rational(1,2)+2*L*x
check(s.integrate(g,(x,-1/(4*L),0))+s.Rational(1,2),
      s.Rational(1,2)+1/(16*L))
check(s.integrate(g*(1-g),(x,-1/(4*L),0))+s.Rational(1,4),
      s.Rational(1,4)+1/(24*L))
check(-s.Rational(1,4)/2-s.Rational(1,2)/2,-s.Rational(3,8))

# Midpoint defect is unchanged by an arbitrary affine subtraction.
a,b=s.symbols('a b',real=True)
check(-b-((-L+a-b)+(-L-a-b))/2,L)

# The exact anchored decomposition, with a nonuniform interior anchor.
lam=[F(1,7),F(2,7),F(4,7)]
for i in range(11):
    for j in range(11-i):
        mu=[F(i,10),F(j,10),F(10-i-j,10)]
        theta=min(li/mi for li,mi in zip(lam,mu) if mi)
        assert theta>=min(lam)
        if theta<1:
            residual=[(li-theta*mi)/(1-theta) for li,mi in zip(lam,mu)]
            assert all(t>=0 for t in residual)
            check(sum(residual),1)
            for li,mi,ri in zip(lam,mu,residual):check(theta*mi+(1-theta)*ri,li)

# Facet incidence lambda(p)=sign*alpha*own_slack+buffer.
alpha,slack,buffer=s.symbols('alpha slack buffer',positive=True)
for sign in [-1,1]:
    aFp,nFy,ap=s.symbols('aFp nFy ap',real=True)
    bF=aFp+nFy+slack
    c=ap+sign*alpha*nFy-buffer
    lp=ap-sign*alpha*aFp+sign*alpha*bF-c
    check(lp,sign*alpha*slack+buffer)
print(f'PASS: {checks} exact slab, anchor, transition-cost, and incidence certificates')
