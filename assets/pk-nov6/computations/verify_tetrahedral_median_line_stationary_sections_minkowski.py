#!/usr/bin/env python3
"""Exact symbolic and rational checks for the median-line section theorem."""
from fractions import Fraction as F
import sympy as s

checks = 0

def eq(a, b=0):
    global checks
    assert s.factor(s.together(a-b)) == 0, (a,b)
    checks += 1

# Complete diagonal centroid, difference, and one-sided centrality identities.
x,y,z = s.symbols('x y z')
w = 1-x-y-z
alpha,beta=x*y,z*w
D=(x+z)*(x+w)*(y+z)*(y+w)
l2=z*(1/(x+z)+1/(y+z)-1)/3
l3=w*(1/(x+w)+1/(y+w)-1)/3
eq(3*(l2-l3), (z-w)*(alpha-(alpha-beta)**2)/D)
eq((1-3*l2)*(x+z)*(y+z), alpha*(1+z)-beta*z)
eq((1-3*l3)*(x+w)*(y+w), alpha*(1+w)-beta*w)

# The conic and its COMPLETE rational parametrization.
A,B,t,h,r = s.symbols('A B t h r')
C=2-A-B
a=A*(3-2*A-B)/(3*C)
b=B*(3-A-2*B)/(3*C)
conic=A*A+2*A*B+3*B*B-3*A-6*B+3
eq((a+3*b-1)*3*C, -2*conic)
Ah=3*(h+1)**2/(2*(h*h+2*h+3))
Bh=(h*h+4*h+7)/(2*(h*h+2*h+3))
eq(conic.subs({A:Ah,B:Bh}))
eq(1-Ah, -(h+3)*(h-1)/(2*(h*h+2*h+3)))
eq(1-Bh, (h*h-1)/(2*(h*h+2*h+3)))
Ar=3*r*r/(2*(r*r+2))
Br=(r*r-2*r+4)/(2*(r*r+2))
eq(Ah.subs(h,-r-1),Ar)
eq(Bh.subs(h,-r-1),Br)
ar=r*r*(4-r)/(4*(r*r+2))
br=(r**3+8)/(12*(r*r+2))
eq(a.subs({A:Ar,B:Br}),ar)
eq(b.subs({A:Ar,B:Br}),br)
eq(ar+3*br,1)
eq(s.Rational(3,8)-ar,(2*r**3-5*r*r+6)/(8*(r*r+2)))
assert (2*r**3-5*r*r+6).subs(r,s.Rational(5,3))==s.Rational(37,27)
checks+=1

# Integrate the two-coordinate simplex density exactly.
z0,z1,threshold=s.symbols('z0 z1 threshold')
small=s.integrate(s.integrate(6*(1-z0-z1),(z1,0,B*(1-z0/A))),(z0,0,A))
eq(small,A*B*(3-A-B))
cap=1-A*B*(3*(1+threshold)**2-(A+B)*(1+threshold)**3)
coarea=3*A*B*(2-A-B)
eq(-s.diff(cap,threshold).subs(threshold,0),coarea)
scalar=s.Rational(3,4)*(2-A-B)*(A+B-4*A*B)
eq(coarea*((1/A+1/B)/4-1),scalar)

# Exact scalar correction, numerator identities, Bernstein certificates.
c=2*br/(6*br-1)
Q=(1-A*B*(3-A-B)-c*scalar).subs({A:Ar,B:Br})
hh=r**3-2*r*r+4
Qclosed=(r+2)**3*(r**4-4*r**3+7*r*r-6*r+4)/(4*(r*r+2)**2*hh)
eq(Q,Qclosed)
L=-11*r**7+86*r**6-188*r**5+44*r**4+212*r**3-88*r*r+80
U=21*r**7-106*r**6+228*r**5-84*r**4-172*r**3+168*r*r+80
eq(Qclosed-s.Rational(27,64),L/(64*(r*r+2)**2*hh))
eq(s.Rational(37,64)-Qclosed,U/(64*(r*r+2)**2*hh))
LC=[80,80,s.Rational(1328,21),s.Rational(2736,35),s.Rational(6768,35),s.Rational(4432,21),s.Rational(1168,7),208]
UC=[80,80,112,s.Rational(4784,35),s.Rational(2672,35),s.Rational(1136,7),s.Rational(2192,7),1232]
for P,cs in [(L,LC),(U,UC)]:
    eq(P.subs(r,2*t),sum(cs[j]*s.binomial(7,j)*t**j*(1-t)**(7-j) for j in range(8)))
    assert all(v>0 for v in cs)
    checks+=len(cs)
assert hh.subs(r,s.Rational(4,3))==s.Rational(76,27)
checks+=1

# Both vertex types have the same correction. No generic-case exclusion.
bb=s.symbols('bb',positive=True)
aa=1-3*bb
cc=2*bb/(6*bb-1)
VQ=27*bb**3/(2*(6*bb-1))
for pp,ss in [(27*bb**3,27*bb**3*(3-3/(4*bb))), (27*aa*bb**2,27*aa*bb**2*(3-(1/aa+2/bb)/4))]:
    eq(pp-cc*ss,VQ)
eq(VQ-s.Rational(27,64),27*(2*bb+1)*(4*bb-1)**2/(64*(6*bb-1)))
eq(s.diff(VQ,bb),81*bb**2*(4*bb-1)/(2*(6*bb-1)**2))
assert VQ.subs(bb,s.Rational(5,24))==s.Rational(125,256)
assert VQ.subs(bb,s.Rational(1,3))==s.Rational(1,2)
checks+=2

# Independent Fraction arithmetic for all geometric formulas, not used as proof.
for j in range(1,200):
    rr=F(j,100)
    dd=rr*rr+2
    aa=3*rr*rr/(2*dd)
    bb=(rr*rr-2*rr+4)/(2*dd)
    assert 0<aa<1 and 0<bb<1
    lam0=aa*(3-2*aa-bb)/(3*(2-aa-bb))
    lam1=bb*(3-aa-2*bb)/(3*(2-aa-bb))
    assert lam0+3*lam1==1
    assert 0<lam0<F(3,8) and F(5,24)<lam1<F(1,3)
    assert lam0/aa+lam1/bb==1
    cc=2*lam1/(6*lam1-1)
    pp=1-aa*bb*(3-aa-bb)
    ss=F(3,4)*(2-aa-bb)*(aa+bb-4*aa*bb)
    qq=pp-cc*ss
    assert F(27,64)<qq<F(37,64)
    assert F(27,64)<1-qq<F(37,64)
    pv=27*lam1**3
    sv=pv*(3-F(3,4)/lam1)
    assert pv-cc*sv==27*lam1**3/(2*(6*lam1-1))
    assert F(27,64)<=pv-cc*sv<=F(1,2)
    checks+=8

print(f'PASS {checks} exact symbolic identities, positive coefficients, and rational geometric checks')
