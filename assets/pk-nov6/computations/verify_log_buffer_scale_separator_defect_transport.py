"""Exact scalar and actual interval checks; no value derivative assumption."""
import sympy as s
checks=0
def eq(a,b):
    global checks
    assert s.simplify(a-b)==0,(a,b)
    checks+=1

eps,tau,M,D,Q,ell,ds=s.symbols('eps tau M D Q ell ds', positive=True)
t=s.symbols('t',real=True)
beta=Q/M
upper=(Q-t*ell)/(M-t*D)-tau*s.log(eps*s.exp(ds*t))
eq(s.diff(upper,t).subs(t,0),(beta*D-ell)/M-tau*ds)
eq(-M*s.diff(upper,t).subs(t,0),ell-beta*D+M*tau*ds)

ka,kb,da,db=s.symbols('ka kb da db',nonnegative=True)
Delta=ka*da+kb*db
eq(ka*(-ds*da)+kb*(-ds*db)+M*tau*ds,(M*tau-Delta)*ds)
f,eps0=s.symbols('f eps0',positive=True)
eq(s.diff(-eps0*s.exp(ds*t)*f,t).subs(t,0),-ds*eps0*f)

# Scale comparison and tangent bound algebra.
c,C,st=s.symbols('c C st',positive=True)
eq(c*tau*st-tau*s.log(tau*st)
   -tau*(1+s.log(C)-s.log(tau)),tau*(c*st-s.log(st)-1-s.log(C)))
tangent=c*st/2+s.log(2/c)-1-s.log(st)
eq(s.diff(tangent,st).subs(st,2/c),0)
eq(tangent.subs(st,2/c),0)
eq(s.diff(tangent,st,2),1/st**2)

# Actual invariant-buffer interval optimum and force.
J=s.Rational(1,2)+eps/(2*s.sqrt(3))-tau*s.log(eps)
estar=2*s.sqrt(3)*tau
eq(s.diff(J,eps).subs(eps,estar),0)
eq(s.diff(J,eps,2),tau/eps**2)
eq(estar/s.sqrt(3),2*tau)
eq((s.Rational(1,2)+eps/(2*s.sqrt(3))).subs(eps,estar),s.Rational(1,2)+tau)

for den in range(5,31):
    tv=s.Rational(1,den)
    ev=2*s.sqrt(3)*tv
    assert ev<s.sqrt(3)
    checks+=1
    eq(ev/s.sqrt(3),2*tv)

print(f'PASS: {checks} exact checks')
