"""Exact algebra for the all-normal triangle-frustum certificate.

The global paired-tail input is an archived theorem.  Its use, all gap
partitions and uniform comparison arguments are proved in the source.
"""
from fractions import Fraction as F
import sympy as S

checks=0
def check(c):
    global checks
    assert c
    checks+=1

Delta=F(4,1287)
delta=Delta**2/192
check(delta==F(1,12*1287**2))
check(delta==F(1,19876428))
check(F(64,143)-F(4,9)==Delta)
check(F(1,124416)>delta)
check(F(1,36)>delta)
check(8*F(1,10**9)<delta)
check(F(17,3)+F(7,3)==8)
check(F(7,24)<F(3,8))
check(F(1,4)*(1+F(1,6)+F(1,48))<F(3,8))

t,e,b,s,h=S.symbols('t e b s h',real=True)
r=1+e*t
tstar=e/3
I2=S.integrate(r**2,(t,-1,1))
check(S.expand(I2-2*(1+e**2/3))==0)
check(S.integrate(r*(t-tstar),(t,-1,1))==0)
check(S.expand(S.integrate((t-tstar)**2,(t,-1,1))-I2/3)==0)
P=S.integrate((2*r+b*(t-tstar))**2,(t,-1,1))/((9-s*s)*I2)
check(S.factor(P-(4+b*b/3)/(9-s*s))==0)
t0=tstar+h
J2=2*(S.Rational(1,3)+t0*t0)
P_h=S.integrate((2*r+b*(t-t0))**2,(t,-1,1))/((9-s*s)*I2)
check(S.factor(P_h-(4*I2-8*b*h+b*b*J2)/((9-s*s)*I2))==0)
bstar=4*h/J2
expected=S.Rational(4,9)-4*h*h/(9*(1+e*e/3)*(S.Rational(1,3)+t0*t0))
check(S.factor(P_h.subs({s:0,b:bstar})-expected)==0)
check(S.factor(S.diff(P_h,b).subs({s:0,b:bstar}))==0)
gt=S.integrate(t*r*r,(t,-1,1))/I2
check(S.factor(gt-(2*e/3)/(1+e*e/3))==0)
R=S.symbols('R',positive=True)
check(S.factor(1-R*R/((R+2)*(2*R-2))-S.Rational(1,2)
               -(R-2)/((R+2)*(2*R-2)))==0)

# Rational actual slice-incidence checks and integrated cap identities.
for eps in (F(1,10**9),F(1,10**10),F(1,10**12),F(1,2)):
    for ss in (F(0),F(1,8),F(1,4)):
        for beta in (F(-1,4),F(-1,8),F(0),F(1,8),F(1,4)):
            for tt in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
                rr=1+eps*tt
                threshold=-beta*(tt-eps/3)
                check(rr*(-1+ss)<threshold<2*rr)
            val=(4+beta*beta/3)/(9-ss*ss)
            check(val>=F(4,9))
            check((val==F(4,9))==(ss==0 and beta==0))
    check((2*eps/3)/(1+eps*eps/3)>eps/3)

for B in (F(0),F(1,4),F(3,4),F(1),F(4),F(72),F(1000)):
    multiplier=F(4,3) if B==0 else min(F(4,3),1/B)
    check((4+B/3)*multiplier<=F(17,3))

print(f'{checks} exact checks PASS')
