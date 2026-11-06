"""Exact arithmetic checks for the rational all-multiplicity obstruction."""
from fractions import Fraction as F

for m in range(2,101):
    k=3*m*m-1
    a=F(m-1,k)
    total=1+k*a
    g=(F(1,2)+k*a*(1-a/2))/total
    s=1-g
    assert total==m and s==F(2*m-1,k) and s>=a
    cost=s+a
    assert cost==F(3*m-2,k)
    ratio=cost/(F(1,2)*(1+a))
    assert ratio==F(2*(3*m-2),3*m*m+m-2)<=F(2,m)
    assert 2*(1+k*a)*s == 1+k*(a*a+s*s-s*s)
    S=(1+k*a*a-2*k*a*a+2*k*a*a)/(2*(1+k*a))
    assert S==s
print('PASS: rational fibers, centroids, source/density distinction and ratios.')
