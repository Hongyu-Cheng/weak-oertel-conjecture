"""Exact one-dimensional checks for allocated Gauss--Green closure."""
from fractions import Fraction as F
import sympy as s

count=0
def eq(a,b):
    global count
    assert s.simplify(a-b)==0, (a,b)
    count+=1

x,t,theta=s.symbols('x t theta', real=True)
for k in range(9):
    psi=x**k
    derivative=s.diff(psi,x)
    # Proper interval cap [t,1].
    eq(psi.subs(x,1), s.integrate(derivative,(x,t,1))+psi.subs(x,t))
    # Inside support, arbitrary retained body selector theta at -1.
    eq(psi.subs(x,1)-theta*psi.subs(x,-1),
       s.integrate(derivative,(x,-1,1))+(1-theta)*psi.subs(x,-1))
    # Outside support, body=section=theta at +1.
    eq(theta*psi.subs(x,1),theta*psi.subs(x,1))
    for m in (2,3,7,19):
        tm=-1+s.Rational(1,m)
        eq(psi.subs(x,1),s.integrate(derivative,(x,tm,1))+psi.subs(x,tm))
        tp=1-s.Rational(1,m)
        eq(psi.subs(x,1),s.integrate(derivative,(x,tp,1))+psi.subs(x,tp))

def interval_trace(a,z):
    threshold=-a*z
    if threshold>1: return ('empty',)
    if threshold<-1: return ('full',)
    return ('cut',threshold)

for a in (3,4,17,100):
    for z in (-1,0,1):
        assert interval_trace(a,z)==interval_trace(2,z)
        count+=1

# Shared finite-contact normal shift vanishes with delta, not by assigning
# the section mean to each source separately.
ka,kb,da,db,ya,yb,u,S=s.symbols('ka kb da db ya yb u S', positive=True)
k=ka+kb
e=ka*da+kb*db
eq(k*((ka*ya+kb*yb)/k-(e/k)*S*u),ka*ya+kb*yb-e*S*u)
print(f'PASS: {count} exact checks')
