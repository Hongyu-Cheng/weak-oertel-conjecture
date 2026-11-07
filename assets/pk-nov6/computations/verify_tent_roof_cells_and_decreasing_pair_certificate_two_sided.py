"""Exact consistency checks for the proved axial formulas."""
from fractions import Fraction as F

checks = 0


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(points):
    pts = sorted(set(points))
    lo, hi = [], []
    for x in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], x) <= 0:
            lo.pop()
        lo.append(x)
    for x in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], x) <= 0:
            hi.pop()
        hi.append(x)
    return lo[:-1]+hi[:-1]


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                   -poly[i][1]*poly[(i+1) % len(poly)][0]
                   for i in range(len(poly))))/2


def cap(poly, threshold):
    out = []
    for i, x in enumerate(poly):
        y = poly[(i+1) % len(poly)]
        sx, sy = x[0]-threshold, y[0]-threshold
        if sx >= 0:
            out.append(x)
        if sx*sy < 0:
            ratio = sx/(sx-sy)
            out.append(tuple(x[j]+ratio*(y[j]-x[j]) for j in (0, 1)))
    return area(out)


def triangle(w):
    return [(-w/3, -1/w), (2*w/3, F(0)), (-w/3, 1/w)]



import sympy as sp
R,t,a,x,y=sp.symbols("R t a x y",positive=True)
S=(R+1+a*(1+t/R))/3
J=S/2-a/4+(S-a)**2/(4*a*t)+S**2/(a*(1+t))
C=(R+1)**2*(5*t+1)/(36*t*(t+1))
A=(-3*R**2*t**2+5*R**2*t+4*R**2+6*R*t**3+10*R*t**2-4*R*t+5*t**3+t**2)/(36*R**2*t*(t+1))
B=(R+1)*(3*R*t**2+5*R*t-2*R+5*t**2+t)/(18*R*t*(t+1))
N=(-3*x**3+33*x**2+8*x+52)*y**2+(-18*x**3+86*x**2-16*x+56)*y+96*x**2
assert sp.factor(J-A*a-B-C/a)==0
assert sp.factor(4*A*C-(sp.Rational(4,3)-B)**2-N.subs({x:R-1,y:t-1})/(108*R*t*(t+1)))==0
checks+=2

def kite(w,p):
    aa,bb,cc=-(1+p)*w/3,(2*p-1)*w/3,(2-p)*w/3
    return hull([(aa,F(0)),(bb,1/w),(cc,F(0)),(bb,-1/w)])

def own(r,p,q):
    aa,bb=1-p,1-q
    S=(1+r+aa+r*bb)/3
    H=(2*p-1+r*(2*q-1))/6
    mass=(r+1)/2
    if p>r*r*q:mass=(1+p/r+r*bb)/2
    if aa>r*r*bb:mass=(1+r*q+aa/r)/2
    if H>0:return mass-own(r,1-p,1-q)
    if aa<=r*r*bb:
        assert bb>0
        return S/2-aa/4+(S-aa)**2/(4*r*r*bb)
    assert aa>0
    return S/(2*r)-bb/4+(S-r*bb)**2/(4*aa)

for r in [F(j,6) for j in range(6,37)]:
    for p in [F(j,8) for j in range(9)]:
        for q in [F(j,8) for j in range(9)]:
            AA,BB=kite(F(1),p),kite(r,q)
            MM=hull([tuple((aa[j]+bb[j])/2 for j in (0,1)) for aa in AA for bb in BB])
            assert own(r,p,q)==cap(MM,F(0))
            checks+=1
            if r<=5:
                low=(2*p-1)/3
                high=-r*(2*q-1)/3
                if low<=high:
                    for alpha in [low,(low+high)/2,high]:
                        assert own(r,p,q)+cap(AA,alpha)+cap(BB,-alpha)>=F(4,3)
                        checks+=1
for r in [F(j,6) for j in range(27,37)]:
    lower=r/6+F(1,12)+(1-1/r)**2/9+F(4,9)
    assert lower>=F(4,3)+F(17,1458)
    checks+=1
# Mixed stationary branch, increasing tent no wider than decreasing.
R,t,x,y=sp.symbols("R t x y",positive=True)
T=2-R-t/R
Sr=R+T/3
P=1-T*T/(9*(1-t))
Qr1=Sr/2-sp.Rational(1,4)+(Sr-1)**2/(4*(R*R-t))
Qr2=Sr/(2*R)-(1-t/(R*R))/4+(Sr-R+t/R)**2/4
N1=(-6*x-11)*y**3+(3*x*x+4*x+15)*y*y+(6*x**5+33*x**4+76*x**3+66*x*x+30*x)*y-4*x**6-8*x**5
N2=-4*y**3-(4*x*x+18*x+7)*y*y+(-x**4+17*x*x+30*x+15)*y-4*x**4
assert sp.factor((R+1)/2-Qr1+P-sp.Rational(4,3)-N1.subs({x:R-1,y:1-t})/(36*R*R*(R*R-t)*(1-t)))==0
assert sp.factor((1+(1+t)/R)/2-Qr2+P-sp.Rational(4,3)-N2.subs({x:R-1,y:1-t})/(36*R*R*(1-t)))==0
checks+=2
for r in [F(j,8) for j in range(8,16)]:
    for a in [F(j,12) for j in range(1,13)]:
        for t in [F(j,12) for j in range(12)]:
            TT=1-r+a*(1-t/r)
            if TT<=0:continue
            b=a*t/(r*r);q=1-b
            alpha=-(1+a)/3+TT/(3*(1-t))
            AA,BB=kite(F(1),a),kite(r,q)
            pair_mass=1-TT*TT/(9*a*(1-t))
            assert cap(AA,alpha)+cap(BB,-alpha)==pair_mass
            assert own(r,a,q)+pair_mass>=F(4,3)
            checks+=2
# Wider-increasing H>=0 domain: exact cap realization and special edges.
for r in [F(j,16) for j in range(1,16)]:
    for a in [F(j,24) for j in range(1,25)]:
        for b in [F(j,24) for j in range(25)]:
            V=r*r*b;D=a-V;TT=1-r+a-V/r
            if D<=0 or TT>3*D or 2*TT<3*(1-r):continue
            q=1-b
            alpha=-(1+a)/3+a*TT/(3*D)
            AA,BB=kite(F(1),a),kite(r,q)
            MM=hull([tuple((aa[j]+bb[j])/2 for j in (0,1))for aa in AA for bb in BB])
            pair_mass=1-TT*TT/(9*D)
            assert cap(AA,alpha)+cap(BB,-alpha)==pair_mass
            assert cap(MM,F(0))+pair_mass>=F(4,3)
            checks+=2
R,z=sp.symbols('R z',positive=True)
poly=6*R**6+18*R**5-29*R**4-15*R**3+42*R**2-26*R+6
bs=[6,sp.Rational(23,6),sp.Rational(71,30),sp.Rational(241,160),sp.Rational(83,80),sp.Rational(23,32),sp.Rational(15,32)]
assert sp.expand(poly.subs(R,z/2)-sum(bs[j]*sp.binomial(6,j)*z**j*(1-z)**(6-j)for j in range(7)))==0
checks+=1
# Every finite tilt cell, including all facet/mode boundary parameters.
for r in [F(j,4) for j in range(4,25)]:
    for p in [F(j,6) for j in range(7)]:
        for q in [F(j,6) for j in range(7)]:
            AA,BB=kite(F(1),p),kite(r,q)
            MM=hull([tuple((aa[j]+bb[j])/2 for j in (0,1))for aa in AA for bb in BB])
            QQ=cap(MM,F(0))
            br=sorted(set([-(1+p)/3,(2*p-1)/3,(2-p)/3,(1+q)*r/3,-(2*q-1)*r/3,-(2-q)*r/3]))
            def PP(alpha):return cap(AA,alpha)+cap(BB,-alpha)
            candidates=[PP(alpha) for alpha in br]+[F(1)]
            for lo,hi in zip(br,br[1:]):
                mid=(lo+hi)/2
                flo,fhi,fmid=PP(lo),PP(hi),PP(mid)
                quadratic=2*(flo+fhi-2*fmid)/(hi-lo)**2
                if quadratic>0:
                    stationary=mid-(fhi-flo)/(2*quadratic*(hi-lo))
                    if lo<stationary<hi:candidates.append(PP(stationary))
            assert QQ+min(candidates)>=F(4,3)
            checks+=1
print(f"PASS: {checks:,} exact checks")
