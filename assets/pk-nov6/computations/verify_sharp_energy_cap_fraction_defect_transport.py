"""Exact identities and cone calibrations for the energy/cap theorem.

The general actual-section one-crossing proof is analytic in the source.
"""
from fractions import Fraction as F
from math import factorial
import sympy as S

checks=0
def check(c):
    global checks
    assert c
    checks+=1

s,A,B=S.symbols('s A B',positive=True)
for d in range(1,13):
    primitive=s**d/(A*(A+(B-A)*s)**d)
    check(S.factor(S.diff(primitive,s)-d*s**(d-1)/(A+(B-A)*s)**(d+1))==0)
    N=d+1
    Gamma=F(d,N)**d
    C=F(N**N,d**d)
    check(C*Gamma*(1-F(d,N))==1)
    cd=F(N,d)**(2*d+1)
    check(cd*Gamma**2==F(N,d))
    for j in range(1,10):
        r=F(d*j,N*10)
        alpha=r**d
        b=F(2*j+3,j+1)
        a=b*(1-1/r)
        c=(N*r-d)/(N*b*(1-r))
        Lb=1+c*b
        La=1+c*a
        check(a<0<b)
        check(c<0)
        check(Lb==1/(N*(1-r)))
        check(La==F(d,N)/r)
        check(b/Lb+d*a/La==0)
        energy=1/(Lb*La**d)
        check(energy==C*alpha*(1-r))
        # Integrate the actual cone section law with integer polynomial powers.
        t=S.symbols('t')
        ar=S.Rational(a.numerator,a.denominator)
        br=S.Rational(b.numerator,b.denominator)
        pos=S.integrate((1-t/br)**(d-1),(t,0,br))
        total=S.integrate((1-t/br)**(d-1),(t,ar,br))
        check(pos/total==S.Rational(alpha.numerator,alpha.denominator))
        check(0<alpha<Gamma)
    rr=S.symbols('rr',positive=True)
    aa=S.symbols('aa',positive=True)
    fd=S.Rational(N**N,d**d)*aa*(1-aa**S.Rational(1,d))
    value=S.diff(fd,aa,2).subs(aa,S.Rational(d,N)**d)
    check(S.simplify(value+S.Rational(cd.numerator,cd.denominator))==0)

# Direct simplex energy and cone-cap equality, including the centroid endpoint.
for d in range(1,21):
    N=d+1
    for j in (1,2,5,10):
        eps=F(j,10*N)
        alpha=(d*eps)**d
        E=F(N**N)*(1-d*eps)*eps**d
        check(E==F(N**N,d**d)*alpha*(1-d*eps))
        check(alpha<=F(d,N)**d)
        # The auxiliary centroidal retained cap is correctly distinguished.
        T=(N*eps)**d
        check(E/T==N*(1-d*eps))

print(f'{checks} exact checks PASS')
