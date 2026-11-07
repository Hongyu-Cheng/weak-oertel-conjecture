"""Exact certificates for signed simplex shell transport and the planar loss."""
from fractions import Fraction as F
import sympy as s

checks=0
for d in range(1,101):
    gamma=F(d,d+1)**d
    assert gamma>F(1,3)
    for r in (F(1), F(2*d+1,2*d), F(d+1,d)):
        assert 1<=r<=F(d+1,d)
        own=(1-gamma)*r**d
        endpoint=1-gamma*r**d
        total=own+2*endpoint
        old=3*(1-gamma)
        added=r**d-1
        assert endpoint>=0
        assert total==2+(1-3*gamma)*r**d
        assert total-old==(1-3*gamma)*added
        assert (2+r**d-total)-(3-old)==3*gamma*added
        checks+=4
    checks+=1

r=F(141,100)
assert r*r<2 and 2*r/3<1
middle=r*r-F(47,50)**2
last=1-F(22,25)**2
assert middle==F(2209,2000)
assert last==F(141,625)
assert middle+last==F(13301,10000)
assert F(4,3)-middle-last==F(97,30000)
assert (2+r*r)/2-r*r==F(119,20000)
checks+=6

p,h=s.symbols('p h', real=True)
m=(1+p)/3
mixed=(m-h)**2/p+1-(1-m-h)**2/(1-p)
assert s.factor(s.diff(mixed,h)-2*(1-2*p)*(h-s.Rational(1,3))/(p*(1-p)))==0
assert s.factor(mixed.subs(h,s.Rational(1,3))-(8+2*p)/9)==0
gm=1-(2-p)**2/(9*(1-p))
assert s.factor(s.Rational(5,9)-gm-p*p/(9*(1-p)))==0
assert s.factor(gm-s.Rational(1,2)-(1-2*p)*(p+1)/(18*(1-p)))==0
checks+=4
print(f'PASS: {checks} exact shell, planar source, and projected-tail checks')
