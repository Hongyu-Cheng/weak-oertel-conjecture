from fractions import Fraction as F
t=[F(96,100),F(97,100),F(98,100)]
c=[(1-x**5)/120 for x in t];sections=[x**4/24 for x in t]
M=F(1,40);a=F(5,6)**5/2
assert sum(c)/M==F(1406574933,10000000000)
assert a-sum(c)/M==F(146483541281,2430000000000)>0
h=[120*(cv+sv/2) for cv,sv in zip(c,sections)]
assert h[0]*h[2]-h[1]**2==F(13912864519608719,100000000000000000000)>0
for x in t:
 hx=1-x**5+F(5,2)*x**4
 dh=-5*x**4+10*x**3;ddh=-20*x**3+30*x**2
 assert hx*ddh-dh**2==5*x*x*(1-x)*(x+1)*((x-1)**4+5)>0
print('PASS: below-OC cap budget, actual section law, strict log-convexity certificate')
