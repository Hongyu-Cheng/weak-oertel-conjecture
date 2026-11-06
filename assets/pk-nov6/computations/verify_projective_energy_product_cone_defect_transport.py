from fractions import Fraction as F
from math import factorial
import sympy as s
checks=0
def ck(q):
    global checks
    assert q
    checks+=1
for d in range(1,21):
    for k in range(1,d+1):
        m=d-k; N=d+1
        beta=F(k,N); tangent=1-beta
        C=F(factorial(m),factorial(d))*F(N**N,k**k*(m+1)**(m+1))
        ck(C==F(factorial(m),factorial(d))/(beta**k*tangent**(m+1)))
        ck(F(m+1,N)/tangent==1)
        ck(F(k,1)/beta*tangent/(m+1)==1)
        telescoped=F(1)
        for r in range(m+1,d+1):telescoped*=F(r+1,r)**(r+1)
        ck(C*k**k==telescoped)
        # Actual standard-simplex face limit, with noncentral tangent mark.
        tangent_bary=[F(2*j,(m+1)*(m+2)) for j in range(1,m+2)]
        normal_v=[F(j,k+1) for j in range(1,k+1)]
        EF=F((m+1)**(m+1),factorial(m))*s.prod(tangent_bary)
        simplex_limit=F(N**N,factorial(d))*s.prod(tangent_bary)*s.prod(normal_v)
        ck(simplex_limit==C*k**k*s.prod(normal_v)*EF)
        for vj in normal_v:ck(F(1,N)/vj==beta/(k*vj))
        if k==1:ck(C==F(d+1,d)**(d+1))
        for z in [F(1,4),F(1,2),F(3,4)]:
            ck(z**k*(1-z)**(m+1)<=beta**k*(1-beta)**(m+1))
a,b,t,ss=s.symbols('a b t ss',positive=True)
ck(s.simplify(2/b*((a-b)**-2-(a+b)**-2)-8*a/(a*a-b*b)**2)==0)
expr=8*(1+ss*t)**3/(1-t*t)**2
ck(s.simplify(s.diff(s.log(expr),t)-(ss*t*t+4*t+3*ss)/((1+ss*t)*(1-t*t)))==0)
sv=F(8,13);tv=F(-1,2)
ck(sv*tv**2+4*tv+3*sv==0)
J=8*(1+sv*tv)**3/(1-tv*tv)**2
ck(J==F(10368,2197))
ck(J/8==F(1296,2197))
ck(all(J/8!=q for q in [1-sv*sv,1-sv,1+sv]))
print(f'{checks} exact checks PASS')
