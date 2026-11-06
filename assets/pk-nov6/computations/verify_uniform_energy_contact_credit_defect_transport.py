"""Exact identities supplementary to the uniform analytic proof."""
import sympy as s
from fractions import Fraction as F

checks=0
def ck(x):
    global checks
    assert x
    checks+=1

t,h,eps=s.symbols('t h eps', real=True)
R=1-h*t
q=R+eps*s.sqrt(2*R)
alpha=eps*s.sqrt(2)*(1-s.sqrt(R))
ck(s.simplify(s.diff(alpha,t).subs(t,0)-eps*h/s.sqrt(2))==0)
ck(s.simplify(s.diff(q,t).subs(t,0)+h+eps*h/s.sqrt(2))==0)
ck(s.simplify(s.diff(q/(2*R),t).subs(t,0)-eps*h/(2*s.sqrt(2)))==0)
ck(s.simplify(R-q+eps*s.sqrt(2)-alpha)==0)
invariant=R+eps*R/s.sqrt(3)
ck(s.simplify(s.diff(invariant/(2*R),t))==0)

# Uniform marked homothety scaling of every fixed energy power.
for d in range(1,20):
    for power in [s.Rational(1,d),s.Rational(1,d+1),s.Rational(2,3)]:
        ck(s.simplify(s.diff((1-h*t)**(d*power),t).subs(t,0)
                      +h*d*power)==0)

# Exact finite quantile response: arbitrary rational coareas, losses,
# positive weights and signed contact derivative.
for j in range(1,30):
    rho=[F(1,6),F(1,3),F(1,2)]
    S=[F(j+1,3),F(j+2,4),F(j+3,5)]
    loss=[F(j-8,7),F(j+2,9),F(11-j,6)]
    ad=F(j-15,13)
    H=sum(r/z for r,z in zip(rho,S))
    theta=[r/z/H for r,z in zip(rho,S)]
    tau=-sum(w*l for w,l in zip(theta,loss))-ad/H
    threshold_derivatives=[-(tau+l)/z for l,z in zip(loss,S)]
    ck(sum(r*c for r,c in zip(rho,threshold_derivatives))==ad)
    ck(sum(theta)==1)
    ck(all(w>0 for w in theta))

print(f'{checks} exact checks PASS')
