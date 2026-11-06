#!/usr/bin/env python3
"""Exact algebra checks supplementing the functional all-m proof; no finite screen substitutes for it."""
from fractions import Fraction as F
from math import prod
import sympy as s
checks=0

def zero(expr):
    global checks
    assert s.factor(expr)==0, s.factor(expr)
    checks+=1

def ok(value):
    global checks
    assert value
    checks+=1

x,h,E,m,T,q,S=s.symbols('x h E m T q S')
U=E-m*x
Z=E*((m+1)*x-1)+m*x
A=(E+x)**2-(E+1)*U
D=x*(m*h+(m+1)*E)-E*h
Ep=m*(E+1)/(1-x)
hb=E*A/((E+1)*U)
hv=(E*U*(E+x)-(m+1)*E*x*Z)/((E+1)*U**2)
zero(A-Z-x*(E+x))
zero((1-x)*(x*Ep-E)-Z)
zero(E*U*(E+x)*(1-h)-D*Z-(E+1)*U**2*(hv-h))
zero(E*(h-x)*A-h*(E+x)*Z-x*(h*(E+1)*U-E*A))
zero(hv-hb-E*(E+x)*(1-x)*(2*E-x*(Ep+m))/((E+1)*U**2))
zero(U*(1-x)-Z-(1-x)*(2*E-x*(Ep+m)))
L=(1-m*x/E)*(1+x/E)**m
# Differentiate logarithm without symbolic powers.
Llog=s.diff(s.log(U/E),x)+Ep*s.diff(s.log(U/E),E)
Llog+=m*((1+Ep)/(E+x)-Ep/E)
zero(Llog-m*(m+1)*x*Z/((1-x)*E*U*(E+x)))
# R=rho(E+h)(1-F), F=(E+h)(h-x)^m/h^(m+1).
# At h stationarity F/(1-F)=h(h-x)/D.
Rlog=-Ep/(E+1)+Ep/(E+h)-h*(h-x)/D*(Ep/(E+h)-m/(h-x))
zero(Rlog-m*(m+1)*x*(1-h)/((1-x)*D))
Flogh=1/(E+h)+m/(h-x)-(m+1)/h
zero((E+h)*Flogh-D/(h*(h-x)))
Lpair=(E-S-2+T)*((E+1)**2-(E+1)*T+q)
zero(s.diff(Lpair,T,2)+2*(E+1))
LTratio=(s.diff(Lpair,T)/Lpair).subs({S:(m-2)*x,T:2*(1-x),q:(1-x)**2})
zero(LTratio-A/(U*(E+x)**2))
# F_T/F=(h-1)/(h-x)^2 with fixed E,h.
RTratio=-h*(h-x)/D*(h-1)/(h-x)**2
zero(RTratio-h*(1-h)/((h-x)*D))
# Original positive pair-factor strict quadratic.
pairW=(S+(T/q-2)/(1-1/(E+1)))*((E+1)**2-(E+1)*T+q)
zero(s.diff(pairW,T,2)+2*(E+1)/(q*(1-1/(E+1))))

# m=1 factorization and exact removable-h=1 limits.
e=x/(1-x);rho=1-x
C=x/((1-x)*(1-rho))-1
Q=1+x/e
W=(1-h)*C*Q
R=rho*(e+h)*(1-(e+h)*(h-x)/h**2)
zero(W-R-x*(h-x)*(1-h)*(2*h+x-h*x)/(h**2*(1-x)))
for k in range(1,9):
    e=(1-x)**(-k)-1;rho=(1-x)**k
    C=k*x/((1-x)*(1-rho))-1
    Q=(1+x/e)**k
    R=rho*(e+h)*(1-(e+h)*(h-x)**k/h**(k+1))
    zero(-s.diff(R,h).subs(h,1)-(1-rho)*C)
    zero(s.limit(C/x,x,0)-s.Rational(k+1,2))
    zero(s.limit((1-k*x/e)/x,x,0)-s.Rational(k+1,2))
    zero(R.subs(x,0))
    zero(s.diff(R,x).subs(x,0))

# Exact arbitrary-vector transformations and positive-domain inequalities.
def quantities(xs,hh):
    rr=prod(1-v for v in xs); ee=1/rr-1
    qq=prod(1+v/ee for v in xs)
    ll=(1-sum(xs)/ee)*qq
    ff=(ee+hh)*prod(hh-v for v in xs)/hh**(len(xs)+1)
    rt=rr*(ee+hh)*(1-ff)
    return rr,ee,qq,ll,ff,rt

for k in range(1,11):
    for seed in range(1,21):
        hh=F(seed+2,seed+5)
        xs=[hh*F(1+(seed*(j+3))%17,19) for j in range(k)]
        rr,ee,qq,ll,ff,rt=quantities(xs,hh)
        cc=sum(v/(1-v) for v in xs)/(1-rr)-1
        ww=(1-hh)*cc*qq
        nx=[-v/(1-v) for v in xs];nh=-hh/(1-hh)
        rn,en,qn,ln,fn,rt_n=quantities(nx,nh)
        ok(ln==-cc*qq/rr)
        ok(rt_n==-rt/(rr*(1-hh)))
        ok(fn==ff)
        ok(rt_n/ln==rt/ww)
        ok(0<rt<ww)
        ok(ln<0 and rt_n<0 and 0<ff<1)
        # Verify zero deletion exactly, even though quantities uses changed m.
        zvals=quantities(xs+[F(0)],hh)
        ok(zvals==quantities(xs,hh))

# Negative-domain stationary algebra has the claimed strict remainder.
for k in range(2,16):
    for xx in [F(-1,20),F(-1,3),F(-1),F(-7,2)]:
        ee=(1-xx)**(-k)-1
        ep=k*(ee+1)/(1-xx);uu=ee-k*xx
        zz=ee*((k+1)*xx-1)+k*xx
        aa=(ee+xx)**2-(ee+1)*uu
        hvv=(ee*uu*(ee+xx)-(k+1)*ee*xx*zz)/((ee+1)*uu**2)
        hbb=ee*aa/((ee+1)*uu)
        ok(uu>0 and zz>0 and aa>0)
        ok(2*ee-xx*(ep+k)>0)
        ok(hvv>hbb)

print(f'PASS: {checks} exact checks; general symbolic stationarity, pair stability, ratio transforms, and boundary identities.')
