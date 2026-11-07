"""Exact rational frustum counterexample; no numerical dependencies."""
from fractions import Fraction as F
from math import factorial

d=4;a=F(1,3);r=F(1);s=F(21,20)
m=F(d,d+1)*(1-a**(d+1))/(1-a**d)
assert m==F(121,150)
V=(1-a**d)/factorial(d);assert V==F(10,243)
assert m/4==F(121,600)
t=-s*(1-m);assert t==F(-203,1000)
b=m+t;assert b==F(1811,3000) and a<b<1
assert -t/s==1-m
cost=(1-b**d)/(1-a**d)
assert cost==F(70243430162159,80000000000000)
E0=1-((d-s)/(d+1))**d
V0=2*F(d,d+1)**d*((1+s)/2)**d
assert E0==F(87882639,100000000)
assert V0==F(2825761,3125000)>E0
assert E0-cost==F(62681037841,80000000000000)>0
# Fully proper perturbation with a simple exact Lipschitz certificate.
eps=F(1,10000)
assert t+eps==F(-2029,10000)
assert a<b+eps<1 and a<1-eps/s<1
cost_eps=(1-(b+eps)**d+s**d-(s-eps)**d)/(1-a**d)
inc=4*s**3*eps/(1-a**d)
assert inc==F(750141,1600000000)
assert cost_eps<=cost+inc
assert E0-cost-inc==F(25173987841,80000000000000)>0
# Exact dimension-three first nonzero Taylor coefficient.
d=3;lam=F(21,20);A=F(3,4);b0=(d-lam)/(d+1);E=1-b0**d
coef=E-d*(1+lam)*A*b0**(d-1)
assert b0==F(39,80) and coef==F(-13571,64000)<0
assert 2*A**d*((1+lam)/2)**d-E==F(50143,2048000)>0
print('PASS: actual4D frustum, exact below-cone gap, both-proper perturbation, and negative3D coefficient')
