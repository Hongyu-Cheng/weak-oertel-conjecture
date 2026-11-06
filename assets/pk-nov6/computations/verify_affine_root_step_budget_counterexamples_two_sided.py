"""Exact Fraction certificates for both strengthened numerical examples."""
from fractions import Fraction as F
from math import comb

def evalpoly(coeff,x):
    return sum(F(c)*x**j for j,c in enumerate(coeff))

gam=F(6,7)**6
coeff=[-11805,9195,8670,2550,375,35]
for r in range(6):
    assert sum((j-8)*comb(5,r)*j**(5-r) for j in range(10))==-coeff[r]
assert evalpoly(coeff,F(2,3))==-F(239945,243)
assert evalpoly(coeff,F(3,4))==F(1198965,1024)
assert all(x>0 for x in coeff[1:])
Bupper=sum((F(6,7)*(j+F(2,3))/(8+F(2,3)))**6 for j in range(10))
assert Bupper==F(837979292565,567869252041)
assert Bupper<F(369,250)
assert gam>F(79,200)
assert F(79,200)+1+F(6,75)+F(15,75**2)-F(369,250)==F(1,600)
assert F(67,75)**6>F(1,2)
assert F(18,245)<F(67,75) and F(87,91)<F(76,75)
assert F(76,75)<F(11,10) and F(11,10)**6<2
v=[F(67+j,75) for j in range(10)]
M=sum(x**6 for x in v)
assert M==F(273705308393,35595703125)
assert M>F(23,3) and gam>F(9,23)
assert gam*M>3>2*Bupper
assert gam+v[-1]**6>Bupper
assert gam+sum(x**6 for x in v[:8])>Bupper
assert 9*gam*v[0]**6>F(711,400)>F(369,250)>Bupper

assert M-2*sum(x**6 for x in v[:6])==F(3911779367,177978515625)
assert M-2*sum(x**6 for x in v[7:])==F(99585557737,59326171875)
assert gam*M/2>F(3,2)>Bupper

coeff71=[-24348077,6155485,626878,23450,455,5]
for r in range(6):
    assert sum((j-60)*comb(5,r)*j**(5-r) for j in range(71))==-355*coeff71[r]
assert evalpoly(coeff71,F(2))==-9334555
assert evalpoly(coeff71,F(3))==431500
assert all(x>0 for x in coeff71[1:])
B71=sum(F(j+3,73)**6 for j in range(71))
assert B71==F(1654903372484,151334226289)<F(219,20)
assert F(31,36)**6>F(2,5)
v71=[F(540+j,600) for j in range(71)]
M71=sum(x**6 for x in v71)
assert M71==F(523011847458152767,9331200000000000)>56
assert gam>F(11,28)
assert gam*M71>22>2*B71
assert F(31,36)**6+sum(x**6 for x in v71[61:])>B71
assert sum(x**6 for x in v71[:60])>B71
assert gam*max(v71)**6==F(61,70)**6<1
print('PASS: both step budgets, maximal-fiber comparison, strict moment failure, and competing-center margin.')
