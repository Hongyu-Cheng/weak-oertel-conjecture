"""Exact identities underlying the all-interval elimination proof."""
from fractions import Fraction as F
import sympy as sy

checks=0
def eq(a,b):
    global checks
    assert sy.simplify(a-b)==0,(a,b)
    checks+=1
def yes(p):
    global checks
    assert p
    checks+=1
s,r,theta,z=sy.symbols('s r theta z',real=True)
N=1+4*theta/3-r/3
eq(sy.diff(N/(sy.Rational(5,2)-r),r),(sy.Rational(1,6)+4*theta/3)/(sy.Rational(5,2)-r)**2)
D=sy.Rational(5,2)+sy.Rational(9,16)*theta-r
eq(sy.diff(N/D,r),(sy.Rational(1,6)+sy.Rational(55,48)*theta)/D**2)
g=(2-s*s)*(1-sy.Rational(9,16)/s)/(sy.Rational(3,2)+s*s)
C=96*s**3-45*s*s-136*s+90
eq(sy.Rational(1,5)-g,C/(40*s*(2*s*s+3)))
eq(C.subs(s,z+sy.Rational(7,8)),z*z*(207+96*z)+sy.Rational(23,4)*z+sy.Rational(55,64))
eq(sy.Rational(23,4)**2-4*177*sy.Rational(55,64),sy.Rational(-9206,16))
G=(2-s*s)*(16*s-9)/(s*(33+7*s*s))
P=63*s**4+1504*s**3-675*s*s-594
eq(sy.diff(G,s),-P/(s*s*(7*s*s+33)**2))
eq(sy.diff(P,s),s*(252*s*s+4512*s-1350))
eq((252*s*s+4512*s-1350).subs(s,sy.Rational(9,16)),sy.Rational(81135,64))
eq(P.subs(s,sy.sqrt(3)/2),564*sy.sqrt(3)-sy.Rational(17037,16))
eq(G.subs(s,sy.sqrt(3)/2),(80-30*sy.sqrt(3))/153)
yes(821**2==674041);yes(3*480**2==691200);yes(674041<691200)
for numerator in range(563,867):
    ss=F(numerator,1000)
    if ss<=F(9,16) or 4*ss*ss>3:continue
    pp=63*ss**4+1504*ss**3-675*ss*ss-594
    yes(pp<0)
    gg=(2-ss*ss)*(16*ss-9)/(ss*(33+7*ss*ss))
    yes(0<gg<F(3,16))
    old=(2-ss*ss)*(1-F(9,16)/ss)/(F(3,2)+ss*ss)
    yes(gg<old<F(1,5))
# Whole-A height derivatives and exact interval endpoints.
ee,th=sy.symbols('ee th',positive=True)
XX=sy.sqrt(ee*ee+1);YY=sy.sqrt(ee*ee+1-th)
J=3*(YY+ee)/((1-th)*(XX+ee))
eq(sy.diff(J,ee)/(2*ee*J),(1/YY-1/XX)/(2*ee))
eq(sy.diff(J,th)/J,(1+ee/YY)/(2*(1-th)))
eq(J.subs({ee:sy.sqrt(sy.Rational(1,8)),th:sy.Rational(1,4)}),1+sy.sqrt(7))
eq(sy.Rational(9,8)*(1-3*sy.sqrt(3)/8)/sy.Rational(153,64),(8-3*sy.sqrt(3))/17)
eq(sy.Rational(5,4)*(1-sy.Rational(3,16)*(1+sy.sqrt(7)))/sy.Rational(153,64),(65-15*sy.sqrt(7))/153)
yes(31**2<3*18**2);yes(79**2<7*30**2)
eq(sy.Rational(477,512)-sy.Rational(9,64)*sy.Rational(5,4)*3*sy.Rational(9,4),sy.Rational(-261,1024))
xx,yy=sy.symbols('xx yy',real=True)
eq(sy.diff((r+xx+yy)/(7-10*r+18*yy),yy),(7-28*r-18*xx)/(7-10*r+18*yy)**2)
eq(((r+xx+yy)/(7-10*r+18*yy)).subs(yy,1-r),(1+xx)/(25-28*r))
eq(28*r+9*sy.Rational(4,3)*(theta-r),16*r+12*theta)
eq(G.subs(s,sy.sqrt(sy.Rational(3,7))),(176-99/sy.sqrt(sy.Rational(3,7)))/252)
yes(3*148**2<7*99**2)
# The disjoint missed-body reserve and the new one-twelfth bound.
ratio12=(r+xx+yy)/(7-sy.Rational(11,2)*r+sy.Rational(45,2)*yy)
eq(sy.diff(ratio12,yy),(7-28*r-sy.Rational(45,2)*xx)/(7-sy.Rational(11,2)*r+sy.Rational(45,2)*yy)**2)
eq(ratio12.subs(yy,1-r),(1+xx)/(sy.Rational(59,2)-28*r))
eq(28*r+12*sy.Rational(4,3)*(theta-r),12*r+16*theta)
eq(28*sy.Rational(5,8),sy.Rational(35,2))
eq(G.subs(s,sy.sqrt(sy.Rational(3,8))),(208-117/sy.sqrt(sy.Rational(3,8)))/285)
yes(3*737**2==1629507)
yes(8*468**2==1752192)
yes(3*737**2<8*468**2)
aa,bb,uu,vv,ww=sy.symbols('aa bb uu vv ww',real=True)
upper=aa+bb-2*(uu+vv+ww/4)
lower=sy.Rational(9,10)*bb+sy.Rational(9,20)*aa-sy.Rational(29,20)*uu+sy.Rational(4,5)*vv+ww/5
eq(10*(upper-lower).subs(aa,uu+vv+r*ww),bb-(7-sy.Rational(11,2)*r)*ww-sy.Rational(45,2)*vv)
print(f'PASS {checks} exact checks')
