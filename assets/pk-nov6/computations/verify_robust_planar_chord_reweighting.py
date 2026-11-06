import sys

import sympy as S
x,y,z,t,s,v=S.symbols('x y z t s v', nonnegative=True)
b=S.Rational(4,3)
T=S.symbols('t0:3'); e=sum(T[i]*T[j] for i in range(3) for j in range(i+1,3)); A=[T[i]*(sum(T)-T[i]) for i in range(3)]
def E(card,q,subs):
 Q=sum(q[i]*A[i] for i in range(3))
 out=(b-1)*e*Q+sum(((1+b)*q[i]*A[i]-Q)*T[i]**2 for i in range(card))
 return S.expand(9*out.subs(dict(zip(T,subs)),simultaneous=True))
# Singleton: substitute t0=t,t1=x,t2=y, then s=x+y,v=xy.
assert S.expand(E(1,[1,b,b],[t,x,y])-(7*t*t*(x+y)**2+15*t*(x+y)*x*y+8*x*x*y*y-24*x*y*t*t))==0
# Two corners, both possible ordered minimizing patterns.
assert S.expand(E(2,[1,1,b],[x,x+y,z])-(2*x+y)*(3*x*(x+y)*(2*x+y)-8*x*(x+y)*z+7*(2*x+y)*z*z))==0
assert S.expand(E(2,[b,1,b],[x,x+y,z])-(2*x+y)*(7*x*x*(x+y)-(6*x*x+10*x*y)*z+(15*x+7*y)*z*z))==0
assert S.expand((6*x*x+10*x*y)**2-28*x*x*(x+y)*(15*x+7*y)+x*x*(384*x*x+496*x*y+96*y*y))==0
# All corners: both threshold patterns, exact positive coefficient tables.
P1=20*x**4+34*x**3*y+17*x**3*z+34*x*x*y*y+34*x*x*y*z+14*x*x*z*z+32*x*y**3+48*x*y*y*z+22*x*y*z*z+3*x*z**3+12*y**4+24*y**3*z+15*y*y*z*z+3*y*z**3
P2=22*x**4+49*x**3*y+10*x**3*z+57*x*x*y*y+19*x*x*y*z+4*x*x*z*z+44*x*y**3+37*x*y*y*z+4*x*y*z*z+14*y**4+21*y**3*z+7*y*y*z*z
assert S.expand(E(3,[b,1,1],[x,x+y,x+y+z])-P1)==0
assert S.expand(E(3,[b,b,1],[x,x+y,x+y+z])-P2)==0
for P in [P1,P2]:assert all(c>=0 for _,c in S.Poly(P,x,y,z).terms())
# Further reweighting gives exactly 1/(1+B).
B=S.symbols('B',positive=True)
assert S.simplify(S.Rational(3,7)/(S.Rational(3,7)+3*B*S.Rational(4,7)/4)-1/(1+B))==0
assert S.Rational(3,7)>S.Rational(27,64)
assert 5*6**6<2*7**6
print('PASS: every finite identity, positive-coefficient certificate, and dimension comparison.')
