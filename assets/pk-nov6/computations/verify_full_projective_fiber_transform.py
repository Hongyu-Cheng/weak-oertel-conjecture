"""Exact chart, weight, incidence, and cap-transform arithmetic checks."""
from fractions import Fraction as F

def ell(z):return z+1
def image(z,x):return (z/ell(z),x/ell(z))
def inverse(u,y):return (u/(1-u),y/(1-u))

for z in [F(0),F(1),F(2),F(7,3)]:
    for x in [F(-2),F(0),F(5,7)]:
        u,y=image(z,x)
        assert inverse(u,y)==(z,x)
        assert 1-u==1/ell(z)
        for alpha,beta,c in [(F(2),F(-3),F(4)),(F(-1),F(1),F(1,2))]:
            # Numerator identity after multiplying the original signed value
            # by the positive inverse denominator.
            assert (alpha*z+beta*x-c)*(1-u)==(alpha+c)*u+beta*y-c

u0=F(0)
u1=F(2,3)
ordinary_mid=(u0+u1)/2
assert ordinary_mid==F(1,3)
assert inverse(ordinary_mid,F(0))[0]==F(1,2)  # Not integral.
L0,L1=F(1),F(3)
projective_mid=(L0*u0+L1*u1)/(L0+L1)
assert projective_mid==F(1,2)
assert inverse(projective_mid,F(0))[0]==1

# For d=1 and both image intervals [0,1], the weighted masses are1,3,2.
assert (1/(1-u0),1/(1-u1),1/(1-projective_mid))==(F(1),F(3),F(2))
assert 2==(1+3)/2

# The x-only map sends two rectangle points to a nonconvex image.
mid_y=(F(1)+F(1,3))/2
assert mid_y==F(2,3)>F(1,2)

# ell=z without translation is singular.
assert (F(1)/1,F(1)/1)==(F(2)/2,F(2)/2)

print("PASS: exact projective inverse, cap formula, weights, midpoint, and x-only obstruction")
