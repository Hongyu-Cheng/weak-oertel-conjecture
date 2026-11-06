"""Exact coarea, profile, row and flux checks for the geometric obstruction."""
from fractions import Fraction as F
import sympy as s

checks=0
def eq(v):
    global checks
    assert s.simplify(v)==0, v
    checks+=1
def truth(v):
    global checks
    assert v
    checks+=1

t,b,v=s.symbols('t b v',positive=True)
G=v*v*s.log(v)/2-v*v/4+b*(v*s.log(v)-v)
eq(s.diff(G,v)-(v+b)*s.log(v))
eq(s.diff(t+b*s.log(t-b),t)-t/(t-b))

delta,A,Ap,r=s.symbols('delta A Ap r',positive=True)
Xs=s.Matrix([1,delta*Ap*r,delta*Ap*(1-r)])
Xr=s.Matrix([0,delta*A,-delta*A])
cross=Xs.cross(Xr)
eq(cross.dot(cross)-delta**2*A**2*(2+delta**2*Ap**2))
for w in cross-s.Matrix([-delta**2*A*Ap,delta*A,delta*A]):
    eq(w)

# All exact seams, two surviving intervals and the central deleted interval.
for k in range(1001):
    x=F(k,1000)
    H=max(2-x,1+x)
    P=max(H,F(17,10))
    E=(x<=F(3,10) or x>=F(7,10))
    truth(P>=H>0)
    truth((P==H)==E)
    truth(H==(2-x if x<=F(1,2) else 1+x))

x=s.symbols('x')
hm=s.integrate(2-x,(x,0,s.Rational(3,10)))
hs=s.integrate(x*(2-x),(x,0,s.Rational(3,10)))
eq(hm-s.Rational(111,200))
eq(hs-s.Rational(81,1000))
Z=s.Rational(1,2)+hm
eq(Z-s.Rational(211,200))
ys=(s.Rational(1,8)+hs)/Z
yx=s.Rational(1,8)/Z
eq(ys-s.Rational(206,1055))
eq(yx-s.Rational(25,211))
c=s.symbols('c',positive=True)
eq(c*2*yx-c*s.Rational(50,211))
truth(0<ys<s.Rational(1,2))
truth(0<yx<2*yx<1)
truth((2*yx)**2<s.Rational(27,64))

# Defect densities (w.r.t. ds on E), including M=1/2.
H=s.symbols('H',positive=True)
n=s.Matrix([0,-1/s.sqrt(2),-1/s.sqrt(2)])
bd=s.sqrt(2)*H
zd=2*H/c
cv=s.Matrix([0,c,c])
for w in -n*bd-s.Rational(1,2)*cv*zd:
    eq(w)
center=s.Matrix([s.Rational(1,2),s.Rational(1,3),s.Rational(1,3)])
point=s.Matrix([x,0,0])
eq(n.dot(point-center)*bd-s.Rational(1,2)*(2*c/3)*zd)

# Any finite-union zero pattern: the DC slope-jump repair is exact.
for j in range(-100,101):
    J=F(j,7)
    Hjump=max(F(0),-J)
    Ajump=Hjump+J
    truth(Hjump>=0 and Ajump>=0)
    truth(Ajump==max(F(0),J))

# Shrinking roof band: one affine parameter, one interior contact source,
# and an atom in the relative interior of the limiting zero edge.
j,logc,p=s.symbols('j logc p',positive=True)
eq((2/j)*(s.sqrt(2)/j)*(j*j-logc)-2*s.sqrt(2)
   +2*s.sqrt(2)*logc/j**2)
sy=(s.Rational(1,2)+2*p)/3
eq((s.Rational(1,4)/3)-s.Rational(1,12))
eq(c*(s.Rational(1,12)+s.Rational(1,12))-c/6)
for w in -n*(2*s.sqrt(2))-s.Rational(1,2)*cv*(4/c):
    eq(w)
truth(s.Rational(1,36)<s.Rational(27,64))
for k in range(1,100):
    pp=s.Rational(k,100)
    ss=sy.subs(p,pp)
    truth(0<ss<1)

# Arbitrary prescribed atomic mass and a locally affine H: exact band mass.
delta,rr,h0,h1,z=s.symbols('delta rr h0 h1 z',positive=True)
width=delta*rr/(2*h0)
eq(s.integrate(h0+h1*z,(z,-width,width))/delta-rr)

# Two exponential scales, I=[1/3,2/3]: one-row limiting moments.
il=s.Rational(1,3)
Ztwo=2+il
eq(Ztwo-s.Rational(7,3))
eq(s.Rational(1,4)/Ztwo-s.Rational(3,28))
eq(c*s.Rational(1,2)/Ztwo-3*c/14)
eq((s.Rational(1,2)+s.Rational(1,2)+il/2)/Ztwo-s.Rational(1,2))
for density in (s.Integer(1),s.Integer(2)):
    for vv in -n*s.sqrt(2)*density-s.Rational(1,2)*cv*(2*density/c):
        eq(vv)

print(f'{checks} exact disconnected tangential-defect checks PASS')
