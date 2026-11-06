"""Exact hinge integrals, concave mixtures, and affine comparison constants."""
from fractions import Fraction as Q
from math import comb
import random

def I(d,L,c):
    if c<=0:return Q(0)
    return c*L**(d-1)/(d-1)-(L**d-max(L-c,Q(0))**d)/(d*(d-1))

def hinge(d,c):
    b=Q(1,d+1);h=1-b;G=h**d
    return (d+1)*G*(d-1)*I(d,Q(1),c)-(d-1)*I(d,h,c-b)-(d-1)**2*I(d,h,c)

def integral_linear(d,L,lo,hi,u,v):
    p=d-2
    return sum(Q(comb(p,j))*(-1)**j*L**(p-j)*
               (u*(hi**(j+1)-lo**(j+1))/(j+1)
                +v*(hi**(j+2)-lo**(j+2))/(j+2)) for j in range(p+1))

checks=0
for d in range(2,31):
    m=d+1;b=Q(1,m);h=1-b;G=h**d
    k1=h**(d-2)/m
    k2=d*h**(d-1)-1-(d-1)*Q(d-1,d)**d
    kd=min(k1,k2)
    assert kd>0 and k2==d*hinge(d,b)/h**d
    for c in sorted({Q(j,100) for j in range(1,100)}|{b,h}):
        E=hinge(d,c)
        assert E>0
        if c>=b:
            assert E==(h**(d-1)-Q(1,d))*(1-c)**d-Q(d-1,d)*max(h-c,Q(0))**d
            err=(1-c)**d/d
            assert E>=k2*err
        else:
            err=(d-1)*I(d,Q(1),c)
            assert E>=k1*err
        assert E>=kd*err
        checks+=1

rng=random.Random(740811)
for d in range(2,10):
    m=d+1;b=Q(1,m);h=1-b;G=h**d
    kd=min(h**(d-2)/m,d*h**(d-1)-1-(d-1)*Q(d-1,d)**d)
    for k in range(15):
        v0=Q(rng.randrange(5),7);v1=Q(rng.randrange(5),7)
        atoms=[(Q(rng.randrange(1,30),30),Q(rng.randrange(1,10),7)) for _ in range(5)]
        def phi(x):
            return (1-x)*v0+x*v1+sum(w*(min(x,c)-c*x) for c,w in atoms)
        aa=v0;bb=v1-v0
        for c,w in atoms:
            if c<=b:aa+=w*c;bb-=w*c
            else:bb+=w*(1-c)
        knots=sorted({Q(0),Q(1),b,h,*(c for c,w in atoms)})
        assert all(aa+bb*x>=phi(x) for x in knots)
        own=Q(0);other=Q(0);ordinary=Q(0)
        for lo,hi in zip(knots,knots[1:]):
            slope=(phi(hi)-phi(lo))/(hi-lo)
            intercept=phi(lo)-slope*lo
            ordinary+=integral_linear(d,Q(1),lo,hi,intercept,slope)
            if lo>=b:
                own+=integral_linear(d,Q(1),lo,hi,intercept,slope)
            if hi<=h:
                other+=integral_linear(d,h,lo,hi,intercept,slope)
        deficit=(d-1)*own+(d-1)**2*other-m*G*(d-1)*ordinary
        assert deficit==sum(w*hinge(d,c) for c,w in atoms)>0
        err=aa+bb/d-(d-1)*ordinary
        assert deficit>=kd*err>=0
        # Exact first-order volume coefficient of the displayed simplex.
        assert d*(aa+bb/d)==d*aa+bb
        # The maximal-depth normalization subtracts Gamma times added mass.
        ENpsi=(deficit+m*G*(d-1)*ordinary)
        assert Q(d,m)*ENpsi-d*G*(d-1)*ordinary==Q(d,m)*deficit
        checks+=1

print(f"PASS {checks} exact hinge, curvature-mixture, and normalization checks")
