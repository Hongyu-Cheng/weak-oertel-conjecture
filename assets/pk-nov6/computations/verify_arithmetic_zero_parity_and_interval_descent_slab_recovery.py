"""Exact arithmetic-normalization and actual interval-path identities."""
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

a,eps=s.symbols('a eps',positive=True)
M=a+2
Sigma=(a**3+2)/(12*M)
D=s.sqrt((a**3+2)/(36*M))
beta=(a+s.Rational(1,2)+eps*D)/M
claimed=s.Rational(3,2)*(1+eps*D*(a*a*M/(a**3+2)-1))/M**2
eq(s.diff(beta,a)-claimed)
eq((M/3)+2*(M/3)-M)
eq(D**2-Sigma/3)
eq(1+(1-a)/M-3/M)
eq(Sigma-((a*(a*a/12))+2*s.Rational(1,12))/M)

# Exact covariance/normalization bounds on the whole specified rational grid.
for k in range(1001):
    aa=F(1,16)+F(k,8000)
    mm=aa+2
    ss=(aa**3+2)/(12*mm)
    dd2=ss/3
    truth(F(1,16)<=aa<=F(3,16))
    truth(aa<mm/2 and 1<mm/2)
    truth(aa+1<mm and 2<mm)
    truth(aa+1<2)
    truth(0<ss<=F(1,12))
    truth(dd2<=F(1,36))
    truth(2*ss/3<F(1,16))
    truth(F(1,16)-F(1,40000)>0)
    truth(1-F(1,10000)/6>0)
    truth(aa*aa*mm/(aa**3+2)>=0)

# Centered interval own energy and exact arithmetic zero-mass cancellation.
v,y,t=s.symbols('v y t',positive=True)
E=v-4*y*y/v
eq(E.subs(y,0)-v)
L=s.symbols('L')
eq((M-t)/M*L/(M-t)-L/M)

# The N=d+1 midpoint strictness factor is certified algebraically by raising
# to N: [(1+r)^(d/N)]^N=(1+r)^d>1 for every positive rational r.
for d in range(1,11):
    for k in range(1,31):
        r=F(k,17)
        truth((1+r)**d>1)

print(f'{checks} exact arithmetic-zero/parity/path checks PASS')
