from fractions import Fraction as F
import sympy as s

count = 0
def check(v):
    global count
    assert v
    count += 1

a,b,V=F(19,20),F(21,20),F(9,2)
rs=[a,F(1),b]; qs=[F(17,57),F(1,3),F(23,63)]
S=sum(r*r for r in rs); M=V*S; beta=F(6)/M
check(M==F(5409,400)); check(beta==F(800,1803))
check(sum(r*r*(1-q) for r,q in zip(rs,qs))==2)
check(F(4)/(3*S)==beta)
for q in qs: check(0<q<F(1,2))
# Exact reversed covariance on polynomial convex calibrations. The proof
# in the source covers every convex function, not just these tests.
for n in range(2,20):
    weighted=sum(r*r*(F(1,3*(n+1))+
        ((1-q)**(n+1)-q**(n+1))/(3*(n+1))) for r,q in zip(rs,qs))/S
    check(weighted<=beta/F(n+1))
check(F(12)/F(261,10)==F(40,87)); check(F(40,87)>F(4,9))
check(-12+beta*F(261,10)==-F(252,601))
e=F(1,1000); ae=a-2*e; ce=1-e
M1=V*(ae*ae+ce*ce+b*b); qo=6*ce*ce; qf=qo+4*e*e
check(M1==F(5398569,400000)); check(qo==F(2994003,500000))
check(qf==F(598801,100000)); check(qo/M1==F(147852,333245))
check(qf/M1==F(2395204,5398569)); check(qf/M1<beta)
check((ae+b)**2<F(9,2)*ae*ae); check((ae+b)**2<F(9,2)*b*b)
check(qo>2*ae*ae); check(qo>2*b*b)
for d in range(1,30):
    g=F(d,d+1)**d
    aa=s.Rational(2*d+1,2*(d+1)); bb=2-aa
    check(aa>s.Rational(d,d+1)); check(aa<=1)
    check(3*g/(1+2*aa**(d-1))>=g)
    e0=s.symbols('e')
    alpha=d*(aa-1)
    qfixed=((d*(aa-2*e0)-alpha)/(d+1))**d+((d*(1-e0))/(d+1))**d+((d*bb+alpha)/(d+1))**d
    check(s.diff(qfixed,e0).subs(e0,0)==-3*d*s.Rational(d,d+1)**d)
print(f'{count} exact checks PASS')
