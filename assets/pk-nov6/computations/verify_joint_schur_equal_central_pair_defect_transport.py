"""Exact identities for the joint funding theorem; no numerical proof."""
import sympy as s
checks=0
def check(x):
    global checks
    assert x
    checks+=1

A,B,C,al,be=s.symbols('A B C al be',positive=True)
Q=-A*al**2+B*be**2-C*(al+be)**2
check(s.factor(Q.subs(al,-C*be/(A+C))-(B-A*C/(A+C))*be**2)==0)

# Raw-units common-shift correction contains the square of the threshold.
t,P,d,e,Hvv,Br,k=s.symbols('t P d e Hvv Br k',positive=True)
raw=-Hvv-e**2/Br+2*k*e*d*P/(t**2*Br)-k**2*d**2*P**2/(t**4*Br)
check(s.factor(raw.subs(k,t**2*e/(d*P))+Hvv)==0)

p,q,r,z,U,V,bb,TT=s.symbols('p q r z U V bb TT',positive=True)
prob=s.cancel((p**3/((p+r)*(p+z))-q**3/((q+r)*(q+z)))/(p-q))
h=s.diff(prob,r,2)+s.diff(prob,z,2)-2*s.diff(prob,r,z)
Juv=s.factor(h.subs({r:1,z:1,p:1/U-1,q:1/V-1})/(3*U*V*(2-U-V)))
expected=2*((U+V-1)**3+U*V*(3-2*U-2*V))/(3*(2-U-V))
check(s.factor(Juv-expected)==0)
prod=TT**2-(1+3*bb)*TT+1
J=2*((1-TT)**3+prod*(2*TT-1))/(3*TT)
check(s.factor(J-(2*bb-4*bb*TT+s.Rational(2,3)*TT**2))==0)

u,zz=s.symbols('u zz')
v=(zz**2/3-u)/(1+u)
tx=(1+u)/2; tq=(1+v)/2
b0=(3*u**2+zz**2)*(zz**2+3)/(24*zz**2*(u+1))
diff=u*v/zz; c0=(1-2*b0-diff)/2
VV=lambda T:s.factor((2-T-3*diff*T/(2*T-1))/2)
qq=lambda T:s.factor(1/VV(T)-1)
JJ=lambda T:s.factor(2*b0-4*b0*T+s.Rational(2,3)*T*T)
R=s.factor((1/c0-3+(1/b0-3)*qq(tq))/(qq(tx)-qq(tq)))
E=s.factor(1/(2*b0*b0)-((R+1/b0-3)/JJ(tq)-R/JJ(tx)))
formula=-(3*u+zz)**2*(3*u*u-2*u*zz+zz**2-2*zz)*(u*zz-3*u+zz**2+zz)**2/(36*zz*(u+1)*(3*u*u+zz**2)**2*JJ(tx)*JJ(tq))
check(s.factor(E-formula)==0)

# Verify the two cubic-root identities used to reduce to u,zeta.
check(s.factor(b0-tx*tq*(tx+tq-1)/(4*tx*tq-1))==0)
check(s.factor((4*b0-tx)*(2*tx-1)**2-3*diff**2*tx)==0)
check(s.factor((4*b0-tq)*(2*tq-1)**2-3*diff**2*tq)==0)
check(s.factor(9*(u+1)**2-4*(3+6*u)-3*(3*u+1)*(u-1))==0)

print(f'PASS: {checks} exact symbolic identities.')
