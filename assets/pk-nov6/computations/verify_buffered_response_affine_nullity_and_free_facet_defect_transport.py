from fractions import Fraction as F
import sympy as s

N,M,E,eps,f,B,beta,Q,tr,av,R = s.symbols('N M E eps f B beta Q tr av R', positive=True)
delta=eps*f/B
D=-M*tr
cap=-Q*tr-delta*(av-R)
C=-E*tr+N*E*av
J=-M*tr-2*M*R
correction=delta*(C/(N*E)+J/(2*M)-(N+2)*D/(2*N*M))
assert s.simplify(correction-delta*(av-R))==0
assert s.simplify((cap+correction-beta*D).subs(Q,beta*M))==0
x,a,y=s.symbols('x a y',real=True)
L=1+a*(x-y)
assert s.simplify(s.diff(L**(-N)/(N*E),x,2)-(N+1)*a*a/E*L**(-N-2))==0
checks=3
for d in range(2,50):
    assert s.integrate(x**(d-1)*(1-x),(x,0,1))==s.Rational(1,d*(d+1))
    checks+=1
Xi=x*x-s.Rational(1,3)
assert s.integrate(Xi,(x,-1,1))==0
assert 2*s.integrate((1-x)*Xi,(x,0,1))==-s.Rational(1,6)
assert -s.Rational(1,6)<-s.Rational(1,9)
checks+=3
# Many exact signed trace/translation/angular calibrations, not actual-body claims.
for d in range(1,10):
    n=d+1
    for j in range(-7,8):
        m=F(2*d+3,3)
        b=F(d+2,5*d+7)
        de=F(d+1,7*d+9)
        tt=F(j,3)
        aa=F(j*j-2,5)
        rr=F(2*j+1,7)
        dd=-m*tt
        cc=-tt+n*aa
        jj=-m*tt-2*m*rr
        qq=b*m
        first=-qq*tt-de*(aa-rr)
        rest=de*(cc/n+jj/(2*m)-F(n+2,2*n)*dd/m)
        assert first+rest-b*dd==0
        checks+=1
print(f'{checks} exact checks PASS')
