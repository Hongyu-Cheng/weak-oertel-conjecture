from fractions import Fraction as F
from itertools import product

def pos(x): return max(x,F(0))
def cap_len(l,h,s): return pos(h-max(l,s))
def response(l,h,s,vl,vr,r):
    D=vl+vr
    if s<l: return D
    if s==l: return D+pos(r-vl)
    if s<h: return vr+r
    if s==h: return -pos(-r-vr)
    return F(0)
checks=0
t=F(1,100000)
# Actual affine endpoint paths, including all five statuses and both signs.
for s,vl,vr,r in product([F(-2),F(-1),F(0),F(1),F(2)],
                         [F(-3,2),F(-1,4),F(0),F(2,3),F(2)],
                         [F(-2),F(-1,3),F(0),F(3,4),F(1)],
                         [F(-3),F(-1),F(-1,4),F(0),F(2,3),F(2),F(4)]):
    l,h=F(-1),F(1)
    newl,newh=l+t*vl,h-t*vr
    exact=(cap_len(l,h,s)-cap_len(newl,newh,s+t*r))/t
    assert exact==response(l,h,s,vl,vr,r)
    checks+=1
# Exact inversion of the source's three-interval supporting calibration.
def Ri(r,h): return 3*h+r-pos(-h-r)
def inv(ell,h):
    # Breakpoint r=-h, loss 2h.
    return (ell-4*h)/2 if ell<2*h else ell-3*h
for h,ell in product([F(-2),F(-1,7),F(0),F(3,5),F(2)],
                     [F(j,3) for j in range(-15,16)]):
    r=inv(ell,h)
    assert Ri(r,h)==ell
    checks+=1
    # Recovered allocation, including exact ties.
    tau=F(1) if h+r<0 else F(0)
    for tie in ([F(0),F(1,3),F(1)] if h+r==0 else [tau]):
        assert (3+tie)*h+(1+tie)*r==ell
        checks+=1
# Two unlike supporting rows, common loss and exact weighted inverse equation.
for h1,h2,ell in product([F(-1),F(0),F(1)],repeat=3):
    rr1,rr2=inv(ell,h1),inv(ell,h2)
    alpha=(rr1+2*rr2)/3
    assert F(1,3)*inv(ell,h1)+F(2,3)*inv(ell,h2)==alpha
    assert Ri(rr1,h1)==Ri(rr2,h2)==ell
    checks+=1
print(f'{checks} exact actual-interval/branch checks PASS')
