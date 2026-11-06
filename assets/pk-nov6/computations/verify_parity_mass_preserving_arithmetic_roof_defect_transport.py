"""Exact checks for the parity-preserving arithmetic-buffer roof path."""
from fractions import Fraction as F
import sympy as sp

checks=0


def check(x):
    global checks
    assert x
    checks+=1


def cap(v,h):
    return min(v,max(v/2-h,F(0)))


a,b=sp.symbols('a b',positive=True)
M=sp.Rational(17,8)
D2=(a**3+1+b**3)/(12*M*(1+2*b))
dD2=-sp.diff(D2,a)+sp.diff(D2,b)
logfactor=sp.Rational(1,2)*(3*(b*b-a*a)/(a**3+1+b**3)-2/(1+2*b))
check(sp.factor(dD2-2*D2*logfactor)==0)
z,t=sp.symbols('z t')
check(sp.expand((1+(1-(a-t))*z)-(1+(1-a)*z)-t*z)==0)
check(sp.expand((1+((b+t)-1)*z)-(1+(b-1)*z)-t*z)==0)

eps=F(1,10000)
mass=F(17,8)
for k in range(101):
    aa=F(1,16)+F(k,1600)
    bb=F(9,8)-aa
    vv={-1:aa,0:F(1),1:bb}
    sig=(aa**3+1+bb**3)/(12*mass)
    dd2=sig/(1+2*bb)
    fac=F(1,2)*(3*(bb**2-aa**2)/(aa**3+1+bb**3)-2/(1+2*bb))
    ell={zz:mass*(1+zz)/(1+2*bb) for zz in vv}
    check(sum(vv.values())==mass)
    check(vv[-1]+vv[1]==F(9,8))
    check(vv[0]==1)
    check(aa+bb<2)
    check(sum(vv[zz]*ell[zz] for zz in vv)==mass)
    check(ell[-1]==0 and ell[0]>0 and ell[1]>0)
    check(sig<F(1,9))
    check(2*sig<F(1,4))
    check(dd2<F(1,25))
    check(fac<F(3,2))
    check(F(1,32)-eps/3>0)
    check(F(9,16)/mass>F(1,4))
    check(-1+3*eps/10<0)
    if aa>F(1,16):
        check(all(v<mass/2 for v in vv.values()))
    check(aa+1<mass and 1+bb<mass)
    # Both unchanged steep base slopes strictly separate the two endpoints.
    check(-aa/2+2>0)
    check(bb/2-2<-eps/2)
    # Full exact all-slope check. The function is affine between these
    # saturation thresholds, so their values certify its global minimum.
    for delta in [F(0),eps/10,eps/5,eps/2]:
        h=-delta
        breaks=sorted(set([aa/2-h,-aa/2-h,h-bb/2,h+bb/2]))
        slopes=breaks+[breaks[0]-2,breaks[-1]+2]
        vals=[cap(aa,h+s)+cap(bb,h-s) for s in slopes]
        check(min(vals)==aa)
        check(all(v>=aa for v in vals))
        for lo,hi in zip(breaks,breaks[1:]):
            check(cap(aa,h+(lo+hi)/2)+cap(bb,h-(lo+hi)/2)>=aa)

# An exact positive decrement while all parity masses and statuses stay fixed.
check(F(1,32)-eps/5>0)
print(f'PASS: {checks} exact parity-mass-preserving arithmetic roof checks')
