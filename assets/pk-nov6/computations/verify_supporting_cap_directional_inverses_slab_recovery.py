"""Exact actual-parallelogram clipping audit of supporting cap responses."""
import sympy as s
from fractions import Fraction as F

t = s.symbols('t', positive=True)
checks = 0

def check(a, b):
    global checks
    assert s.cancel(a-b) == 0, (a, b)
    checks += 1

def initial_sign(expr):
    poly = s.Poly(s.expand(expr), t)
    for (power,), coef in sorted(poly.terms(), key=lambda term: term[0][0]):
        if coef:
            return s.sign(coef)
    return 0

def clip(poly, level):
    ans=[]
    for p,q in zip(poly, poly[1:]+poly[:1]):
        vp=p[0]-level; vq=q[0]-level
        ip=initial_sign(vp)>=0; iq=initial_sign(vq)>=0
        if ip: ans.append(p)
        if ip != iq:
            lam=s.cancel(vp/(vp-vq))
            ans.append(tuple(s.cancel(p[i]+lam*(q[i]-p[i])) for i in (0,1)))
    return ans

def area(poly):
    if len(poly)<3: return s.S(0)
    return s.cancel(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly, poly[1:]+poly[:1]))/2)

def hinge_integral(intercept,slope):
    # Exact integral from -1 to 1 of (intercept+slope*y)_+.
    if slope<0: slope=-slope
    if slope==0: return 2*max(intercept,0)
    if intercept>=slope: return 2*intercept
    if intercept<=-slope: return F(0)
    return (intercept+slope)**2/(2*slope)

square=[(-1,-1),(1,-1),(1,1),(-1,1)]
paths=[(F(1,3),F(2,3),F(1,4),F(-1,5),F(1,7),F(-1,6)),
       (F(-1,4),F(3,5),F(-2,7),F(1,2),F(-1,3),F(2,5)),
       (F(0),F(1),F(-1,3),F(0),F(0),F(1,4)),
       (F(2,3),F(-1,2),F(1,5),F(1,4),F(2,5),F(0))]
for a11,a12,a21,a22,b1,b2 in paths:
    poly=[(s.Rational(x)+t*s.Rational(b1-a11*x-a12*y),
           s.Rational(y)+t*s.Rational(b2-a21*x-a22*y)) for x,y in square]
    D=4*(a11+a22)
    check(-s.diff(area(poly),t).subs(t,0),s.Rational(D))
    for level in [F(-3,2),F(-1),F(-1,3),F(0),F(2,5),F(1),F(3,2)]:
        for r in [F(-2),F(-3,5),F(0),F(2,7),F(1),F(2)]:
            cut=clip(poly,s.Rational(level)+s.Rational(r)*t)
            actual=-s.limit(s.diff(area(cut),t),t,0,dir='+')
            if level < -1: expected=D
            elif level == -1:
                expected=D+hinge_integral(r-a11-b1,a12)
            elif level < 1:
                expected=2*a11-2*b1+2*a22*(1-level)+2*r
            elif level == 1:
                expected=-hinge_integral(-r-a11+b1,-a12)
            else: expected=F(0)
            check(actual,s.Rational(expected))

# An actual three-interval supporting cap, for both signs and hinge branches.
for h in [F(-2),F(-1,3),F(0),F(1,4),F(2)]:
    for r in [F(-3),F(-1),F(0),F(1,2),F(3)]:
        R=3*h+r-max(-h-r,0)
        inverse=(R-4*h)/2 if R<2*h else R-3*h
        check(s.Rational(inverse),s.Rational(r))
print(f'{checks} exact checks PASS (168 actual clipped parallelograms, all cap statuses)')
