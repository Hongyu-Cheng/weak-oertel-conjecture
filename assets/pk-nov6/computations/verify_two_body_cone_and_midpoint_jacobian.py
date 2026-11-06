"""Exact checks for the planar cone calibration and midpoint defect split."""
from fractions import Fraction as F

for k in [F(1),F(3,2),F(2),F(3),F(10)]:
    a=F(2,3)
    shift=a*k*(k-1)/(1+k*k)
    cost=(a-shift)**2+(a+shift/k)**2
    target=F(4,9)*(k+1)**2/(k*k+1)
    assert cost==target
    excess=(k-1)/2
    shortfall=F(8,9)-cost
    if k>1: assert shortfall/excess==F(8,9)*(k-1)/(k*k+1)
    b=(k-1)/(k+1)
    eta=1-b*b
    image=(k+1)**2/(4*k)
    minkowski=(k+1)/2
    assert eta*image==1
    assert minkowski-image==(k*k-1)/(4*k)
    assert image-1==(k-1)**2/(4*k)
    assert (minkowski-image)+(image-1)==excess
    assert 1-eta==(b*b+b*b)/2

# All-d rational t gives rational k=t^(d-1), exact cone formulas.
for d in range(2,12):
    a=F(d,d+1);gamma=a**d
    for t in [F(1),F(3,2),F(2),F(3)]:
        k=t**(d-1)
        shift=a*k*(t-1)/(1+t**d)
        assert 0<=shift<a
        assert shift<k/F(d+1)
        cost=(a-shift)**d+(a+shift/k)**d
        assert cost==gamma*(1+t**(d-1))**d/(1+t**d)**(d-1)
        assert cost<=2*gamma
        rho=1/t
        integral_ratio=F(1,2**d)*(1+k/rho*((1+rho)**d-1))
        assert integral_ratio==F(1,2**d)*(1+(1+t)**d-t**d)
        assert integral_ratio>=1

assert F(4,9)*F(3)**2/F(5)==F(4,5)
assert (F(8,9)-F(4,5))/F(1,2)==F(8,45)
print('PASS: exact two-body cone and midpoint-Jacobian certificates')
