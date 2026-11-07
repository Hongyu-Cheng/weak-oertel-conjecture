"""Exact identities for the all-m functional proof; uniform signs are proved in its text."""
import sympy as s
m,E,x,h,T,C,q,So,r,y=s.symbols('m E x h T C q So r y')
checks=0
def eq(a,b=0):
 global checks
 assert s.factor(a-b)==0,(a,b)
 checks+=1
Ep=m*(E+1)/(1-x)
Z=E*((m+1)*x-1)+m*x
D=x*(m*h+(m+1)*E)-E*h
A=(E+x)**2-(E+1)*(E-m*x)
eq(A,Z+x*(E+x));eq(x*Ep-E,Z/(1-x))
logL=(Ep-m)/(E-m*x)+m*(Ep+1)/(E+x)-(m+1)*Ep/E
ell=m*(m+1)*x*Z/((1-x)*E*(E-m*x)*(E+x))
eq(logL,ell)
ratio=h*(h-x)/D
logR=Ep/(E+h)-Ep/(E+1)-ratio*(Ep/(E+h)-m/(h-x))
ellR=m*(m+1)*x*(1-h)/((1-x)*D)
eq(logR,ellR)
eq(ellR/ell,E*(E-m*x)*(E+x)*(1-h)/(D*Z))
eq(h*(h-x)+(E+h)*((m+1)*x-h),D)
eq(ratio*(1-h)/(h-x)**2,h*(1-h)/((h-x)*D))
Lt=C*(E-So-2+T)*((E+1)**2-(E+1)*T+q)
eq(s.diff(Lt,T,2),-2*C*(E+1))
eq(s.diff(Lt,T).subs({T:2*(1-x),q:(1-x)**2,So:(m-2)*x}),C*A)
eq(E*(h-x)*A-h*(E+x)*Z,x*(h*(E+1)*(E-m*x)-E*A))
hc=x+Z/E;hb=E*A/((E+1)*(E-m*x))
eq(hb-hc,Z**2/(E*(E+1)*(E-m*x)))
# General logarithmic differentiation of f(h) gives (10).
num=2*h*(h-x)+m*h*(E+h)-(m+1)*(E+h)*(h-x)
eq(num,h*h+((m-1)*x-E)*h+(m+1)*E*x)
# f'(1) after (1-x)^m(E+1)=1.
fp1=(1+((m-1)*x-E)+(m+1)*E*x)/(1-x)
eq(fp1-1,Z/(1-x))
# Exact transformed cubic, all m.
cubic=(r+(r+1)*y)*(r+((m+1)*r-1)*y+m*(r+1)*y*y)
p=s.Poly(cubic,y)
eq(p.coeff_monomial(1),r*r)
eq(p.coeff_monomial(y),(m+2)*r*r)
C2=-m*(m-1)*r*r/2+2*m*r-1
C3=m*(1+r)**2-m*(m+1)*(m+2)*r*r/6
eq(p.coeff_monomial(y*y)-(m+2)*(m+1)*r*r/2,C2)
eq(p.coeff_monomial(y**3)-(m+2)*(m+1)*m*r*r/6,C3)
# Endpoint polynomial identities determining B positivity.
end1=s.factor(cubic.subs({r:1/m,y:1/m}))
end2=s.factor(cubic.subs({r:1/m,y:2/(m+1)}))
eq(end1,2*(2*m+1)*(m+1)/m**4)
eq(end2,3*(5*m+3)/(m*m*(m+1)))
# Padé derivative, without logarithmic branch assumptions.
pade=(m-1)/(2+(m-1)*x)+(m+1)/(2-(m+1)*x)-m/(1-x)
eq(pade,m*(m-1)*(m+1)*x*x/((1-x)*(2+(m-1)*x)*(2-(m+1)*x)))
# Base dimension.
e1=x/(1-x);l1=x*(2-x);r1=(1-x)*(e1+h)*(1-(e1+h)*(h-x)/h**2)
eq(l1-r1,x*(h-x)*(2*h*(1-x)+x)/(h*h*(1-x)))
# Exact supplementary specializations of the ALL-m binomial identity.
for mm in range(2,31):
 B=C2.subs(m,mm)+C3.subs(m,mm)*y-r*r*sum(s.binomial(mm+2,k)*y**(k-2) for k in range(4,mm+3))
 eq(cubic.subs(m,mm)-r*r*(1+y)**(mm+2),y*y*B)
 assert s.Rational(2)*(2*mm+1)/(mm+1)>=s.Rational(10,3)
 assert s.Rational(3)*(5*mm+3)/(mm+1)>=13
 checks+=2
assert s.Rational(8,3)+s.Rational(5,96)==s.Rational(87,32)<s.Rational(11,4)<s.Rational(10,3)
assert s.Rational(121,16)*s.Rational(5,3)==s.Rational(605,48)<13
checks+=2
print('PASS:',checks,'exact differential, transformed-polynomial, endpoint, and supplementary specialization checks')
