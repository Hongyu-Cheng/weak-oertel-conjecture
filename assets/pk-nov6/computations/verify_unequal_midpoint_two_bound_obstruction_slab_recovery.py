"""Exact arithmetic for two scalar-certificate obstructions and their families."""
from fractions import Fraction as F
import sympy as s
checks=0
def check(v):
    global checks
    assert v
    checks+=1
x=s.symbols('x')
a=x*x;v=(1+x)**2/4;g=s.Rational(4,9)
check(s.factor(4*(v*(1+a-2*g)-a*(1-a))-(x+1)*(3*x-1)*(15*x*x-4*x-1)/9)==0)
a=s.symbols('a');k=(1-2*a)*(1+a)/(1-a);v=(1+a)/2
check(s.factor(k-v-(1+a)*(1-3*a)/(2*(1-a)))==0)
check(s.factor(2*v-k-a*(1+a)/(1-a))==0)
check(s.factor(k-(1-a)-a*(1-3*a)/(1-a))==0)
for d,a,k,v,g,gap,reserve in [
    (1,F(1,4),F(5,6),F(5,8),F(1,2),F(1,48),F(7,48)),
    (2,F(4,25),F(6272,7425),F(49,100),F(4,9),F(14,13365),F(9146,66825)),
]:
    check(v<k<2*v)
    check(k/2+a*(1-k/(2*v))==g)
    check(g*(k+a+1)/2-g==gap)
    check(k/2+a-g*(k+a+1)/2==reserve)
    check(max(2*g,k,2*a+(1-a/v)*k)==2*g)
for j in range(1,100):
    a=F(j,300);v=(1+a)/2;k=(1-2*a)*(1+a)/(1-a)
    check(v<k<2*v);check(k/2+a*(1-k/(2*v))==F(1,2));check(k+a+1>2)
for num in range(101,128):
    x=F(num,300)
    if 15*x*x-4*x-1>=0:continue
    a=x*x;v=(1+x)**2/4;g=F(4,9);k=2*(g-a)/(1-a/v)
    check(v<k<2*v);check(k/2+a*(1-k/(2*v))==g);check(k+a+1>2)
    check(k/2+a>g*(k+a+1)/2)
print(f'PASS: {checks} exact identities and inequalities')
