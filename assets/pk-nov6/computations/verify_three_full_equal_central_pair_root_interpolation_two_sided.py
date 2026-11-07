"""Exact symbolic verification of actual-root reciprocal stiffness interpolation."""
import sympy as S
from fractions import Fraction
p,B,D=S.symbols('p B D')
a=(1-2*B+D)/2;c=(1-2*B-D)/2
q=(2*B-a*p)/c;U=1/(1+p);V=1/(1+q);T=2-U-V
F=3*(2*B-D-1)**2*p**3+6*(6*B**2-5*B*D-3*B+D**2+D)*p**2+(36*B**2-24*B*D-8*B+3*D**2+1)*p+2*B*(6*B-3*D-1)
E=432*B**2*D**2-216*B*D**2-8*B+27*D**4+18*D**2+3
L=2*B-D-1
N2=-9*L**2*(4*B-3*D**2-1)
N1=-18*L*(24*B**2*D+8*B**2-6*B*D**2-12*B*D-2*B+3*D**3+D)
N0=-3*(288*B**3*D+48*B**3-180*B**2*D**2-144*B**2*D-12*B**2+36*B*D**3+96*B*D**2+12*B*D-9*D**4-6*D**2-1)
J=2*B-4*B*T+S.Rational(2,3)*T**2
G=(N2*p**2+N1*p+N0)/(2*B*E)
checks=0
def check(x):
 global checks
 assert x
 checks+=1
def zero(x):check(S.cancel(x)==0)
# Cubic comes from an ACTUAL captured-coordinate equation, not the weaker central coordinate.
num=S.together(U*(1+T-U)/(3*T)-a).as_numer_denom()[0]
zero(num-2*F)
zero(a*p+c*q-2*B)
zero(E-(27*D**4+18*(24*B**2-12*B+1)*D**2+3-8*B))
# Explicit modular identity. No inference is made from a numerical root.
num=S.together(J*G-1).as_numer_denom()[0]
zero(S.rem(num,F,p))
# Raw negative-pair differentiation and the stationary simplification.
r,w=S.symbols('r w', positive=True)
P=(p**2*q**2+p*q*(p+q)*(r+w)+(p**2+p*q+q**2)*r*w)/((p+r)*(p+w)*(q+r)*(q+w))
H=S.diff(P,r,2)-2*S.diff(P,r,w)+S.diff(P,w,2)
H=S.cancel(H.subs({r:1,w:1}))
Jraw=S.cancel(H/(3*U*V*T))
num=S.together(Jraw-J).as_numer_denom()[0]
zero(S.rem(num,F,p))
# The exact divided difference and the actual optimal funding formula.
x,y,z,K0,K1,K2=S.symbols('x y z K0 K1 K2')
theta=(z-y)/(z-x)
poly=lambda v:K2*v*v+K1*v+K0
zero(theta*poly(x)+(1-theta)*poly(z)-poly(y)-K2*(y-x)*(z-y))
A,C=S.symbols('A C', positive=True);u=C/(A+C)
zero(A*u*u+C*(1-u)**2-A*C/(A+C))
# Rational positivity checks reinforce, but do not replace, the displayed exact range proof.
for bi in range(1,30):
 b=S.Rational(bi,180)
 for di in range(-9,10):
  d=S.Rational(di,30)*(1-6*b)
  if abs(d)>=S.Rational(1,3)-2*b:continue
  check(E.subs({B:b,D:d})>1)
  check(N2.subs({B:b,D:d})>0)
# Actual nonsymmetric example: isolate all three positive roots using exact rational intervals.
bs=S.Rational(7,54);ds=S.Rational(1,1000)
fs=S.Poly(F.subs({B:bs,D:ds}),p)
intervals=S.polys.polytools.intervals(fs,eps=S.Rational(1,10**12))
check(len(intervals)==3)
for ((lo,hi),mult) in intervals:
 check(mult==1 and lo>0)
 check(q.subs({B:bs,D:ds,p:hi})>0)
check(a.subs({B:bs,D:ds})>S.Rational(1,3))
check(c.subs({B:bs,D:ds})>S.Rational(1,3))
print('PASS:',checks,'exact checks')
print('Nonsymmetric common b=',tuple(S.simplify(v.subs({B:bs,D:ds})) for v in (a,c,B,B)))
print('Actual stationary p intervals:',intervals)
