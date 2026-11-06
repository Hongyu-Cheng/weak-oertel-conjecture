"""Exact interval certificate at an algebraic projective-centroid parameter.

This checks explicit analytic boundary integrals on an archived actual
globally critical family. It does not replace that all-normal proof.
"""
from fractions import Fraction as F
import sympy as s

count=0
def check(x):
    global count
    assert x
    count+=1
class I:
    def __init__(self,x,y=None):
        self.lo=F(x); self.hi=F(x if y is None else y)
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+-asI(o)
    def __rsub__(self,o): return asI(o)+-self
    def __mul__(self,o):
        o=asI(o); vals=[x*y for x in [self.lo,self.hi] for y in [o.lo,o.hi]]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asI(o); check(o.lo*o.hi>0)
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return asI(o)/self
    def __pow__(self,n):
        assert n>=0
        ans=I(1)
        for _ in range(n): ans=ans*self
        return ans
def asI(x): return x if isinstance(x,I) else I(x)

t,h,e=F(100,291),F(20,97),F(1,100)
a,b=1-e,1+e
lo,hi=F(15957301,10**9),F(15957302,10**9)
P=lambda z:509600*z*z-1777040*z+28227
check(P(lo)>0);check(P(hi)<0);check(2*509600*hi<1777040)
check(1+lo*(h-2*t)>0);check(hi<1/(2*t-h))
c=I(lo,hi)
f=lambda u:1/(1+c*(u-2*t))**2
g=lambda u:1/(1+c*((u+h)/2-2*t))**2
integral=lambda l,r:(r-l)/((1+c*(l-2*t))*(1+c*(r-2*t)))
integral_g=lambda l,r:(r-l)/((1+c*((l+h)/2-2*t))*(1+c*((r+h)/2-2*t)))
D=lambda r:2*t*integral(h,r)+h*(2*t-h)*f(h)+r*(r-2*t)*f(1)
L1=lambda r:2*t*integral(h,2*t)+h*(2*t-h)*f(h)
L2=lambda r:t*integral(r-(2-4*t),r)+2*t*(r-2*t)*f(1)
DO=lambda r:4*t*integral_g(h,r)+2*h*(2*t-h)*g(h)+2*r*(1-2*t)*g(r)
O1=lambda r:4*t*integral_g(h,2*t)+2*h*(2*t-h)*g(h)
O2=lambda r:2*t*integral_g(r-(2-4*t),r)+4*t*(1-2*t)*g(r)
M=sum((r*r-h*h)/2 for r in [a,F(1),b]);Q=6*t*(1-2*t);beta=Q/M
theta1=(4*t-1)/(6*t-1);theta2=t/(6*t-1)
check(beta==F(182000000,405433227));check(theta1==F(109,309));check(theta2==F(100,309))
check(theta1+2*theta2==1)
for r in [a,F(1),b]:
    check(h<2*t<r);check(h<r-(2-4*t)<r)
    check((r*r-h*h)/2<Q)

result={}
for name,dd,l1,l2 in [
    ('old',sum(D(r) for r in [a,1,b]),sum(L1(r) for r in [a,1,b]),sum(L2(r) for r in [a,1,b])),
    ('oneA',D(1)+DO(a),L1(1)+O1(a),L2(1)+O2(a)),
    ('oneB',D(1)+DO(b),L1(1)+O1(b),L2(1)+O2(b))]:
    p1=l1-beta*dd;p2=l2-beta*dd;pw=theta1*p1+2*theta2*p2
    result[name]=(p1,p2,pw)
    print(name, 'payments enclosed in',[(float(x.lo),float(x.hi)) for x in (p1,p2,pw)])
check(result['old'][0].lo>F(12,1000))
check(result['old'][1].hi<-F(6,1000))
check(result['old'][2].lo>F(3,10000))
check(result['oneA'][0].lo>F(17,1000))
check(result['oneA'][1].lo>F(49,10000))
check(result['oneA'][2].lo>F(9,1000))
check(result['oneB'][0].hi<-F(1,2000))
check(result['oneB'][1].hi<-F(13,1000))
check(result['oneB'][2].hi<-F(8,1000))

# The centroid-normalization integral and the fixed-cap geometric lengths.
C,U=s.symbols('C U');tt=s.Rational(t.numerator,t.denominator);hh=s.Rational(h.numerator,h.denominator)
v=s.symbols('v')
primitive=s.integrate(s.expand((((v-1)/C+2*tt)*(v-1)/C)/C/v**4),v)
value=s.factor(primitive.subs(v,1+C*(1-2*tt))-primitive.subs(v,1+C*(hh-2*tt)))
expected=-29644461*(509600*C**2-1777040*C+28227)/((91*C+291)**3*(140*C-291)**3)
check(s.cancel(value-expected)==0)
check(s.factor(509600*((44426-1067*s.sqrt(1702))/25480)**2-1777040*((44426-1067*s.sqrt(1702))/25480)+28227)==0)
R=s.symbols('R',positive=True)
centroid=R/3+hh**2/(3*(R+hh))
check(s.simplify(s.diff(centroid,R,2)-2*hh**2/(3*(R+hh)**3))==0)
print(f'{count} exact checks PASS; printed decimals only display proven rational enclosures')
