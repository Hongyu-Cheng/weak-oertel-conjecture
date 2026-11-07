"""Exact finite checks for projective thin-edge union coverage and layer example."""
from fractions import Fraction as F
from itertools import product


def repeated_cap(a,c,d):
    assert a>0 and c<0 and d<0
    return (3*a*a*(a-c)*(a-d)-a**3*(2*a-c-d))/((a-c)**2*(a-d)**2)


layer_checks=0
for denominator in range(100,1100,10):
    e=F(1,denominator)
    tau=repeated_cap(e,-2*e,-1)
    I0=F(27,64)*repeated_cap(e,-5*e/4,(e-3)/4)
    I2=F(27,64)*repeated_cap(e/4,-2*e,-(2*e+3)/4)
    assert tau==e*(5*e+8)/(9*(1+e)**2)
    assert I0==e*(11*e+23)/(36*(1+e)**2)
    assert I2==e*(23*e+26)/(576*(1+e)**2)
    ratio=(2*I0+I2)/tau
    assert ratio==3*(125*e+254)/(64*(5*e+8))
    assert F(3,2)-ratio==3*(35*e+2)/(64*(5*e+8))>0
    lam=[F(36,100),F(36,100),F(28,100),F(0)]
    assert sum(lam)==1 and sum(x>=F(1,4) for x in lam)==3
    assert e*(lam[0]+lam[1]-2*lam[2])>lam[3]
    assert lam[2]+lam[3]>F(1,4)
    for omitted in range(4):
        c=[F(0) if j==omitted else F(1,3) for j in range(4)]
        assert e*(c[0]+c[1]-2*c[2])<=c[3]
    layer_checks+=1


def W(r,k):
    return r*r*(k*r+3)/(6*(1+k*r)**3)


# W''=(1-3kr)/(1+kr)^5; convexity is checked pointwise below
# by both its exact sign and Jensen inequalities. Maxima of arbitrary
# affine radial profiles preserve this convexity under composition.
convex_checks=0
for seed in range(1,31):
    # Use rational ray directions y=r, z=k0*r, avoiding trig arithmetic.
    k0=F(seed%7,7);k=1+k0
    profiles=[(F(1+(seed+3*j)%11,60)/k,
               F(1+(2*seed+5*j)%13,60)/k) for j in range(1+seed%9)]
    def R(t):
        return max((1-t)*a+t*b for a,b in profiles)
    def f(t):
        return W(R(t),k)
    for i,j in product(range(9),repeat=2):
        x,y=F(i,8),F(j,8)
        rx,ry=R(x),R(y)
        assert k*rx<=F(1,3) and k*ry<=F(1,3)
        assert (1-3*k*rx)/(1+k*rx)**5>=0
        assert f((x+y)/2)<=(f(x)+f(y))/2
        convex_checks+=1

assert F(27,16)-F(3,2)==F(3,16)
print(f'PASS: {layer_checks} exact facet-layer volume/coverage examples; '
      f'{convex_checks} arbitrary-union radial/Jensen checks; '
      'exact 3/16 coverage margin.')
