"""Exact rational certificate for the standalone scalar-profile counterexample."""
from fractions import Fraction as F
e=F(1,100000);tau=F(1,10000);eta=F(1,100);W=F(7,2)
a=W*e/2
capx=a*F(36,49)
capy=a*tau*tau/((eta+tau)*(eta+tau+e))
cap3=a*(1-tau*tau/(F(35101,10000)*(F(35101,10000)+e)))
profile=capy+capx+cap3/4
support=F(351011,100000)
sections=[F(6,7)*e,W*tau*e/((eta+tau)*(eta+tau+e)),W*tau*e/(F(35101,10000)*(F(35101,10000)+e))]
assert a==F(7,400000)
assert 0<capy<capx<cap3<a
assert capy/a<F(1,10000)
assert profile<min(a,F(9,2))
assert all(0<x<F(1,1000) for x in sections)
assert support+F(8,3)*profile-a-F(9,2)<0
assert F(1,10000)+F(36,49)+F(1,4)<1
print('PASS 7 exact rational checks')
