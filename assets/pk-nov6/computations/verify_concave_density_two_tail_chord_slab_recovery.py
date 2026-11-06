"""Exact identities and rational checks supplementing the all-real proof."""
from fractions import Fraction as F
import sympy as s

checks=0
def eq(a,b):
    global checks
    assert s.simplify(a-b)==0,(a,b)
    checks+=1
def yes(p):
    global checks
    assert p
    checks+=1
def tail(p,t):
    return (1-t)**2/(1-p) if p<=t else 1-t*t/p
def tent(p,t):
    if p==0:return 2*(1-t)
    if p==1:return 2*t
    return 2*t/p if t<=p else 2*(1-t)/(1-p)

x,y,p,B,t=s.symbols('x y p B t',positive=True)
c=x*(1-x)/(y*(1-y));a0=(1-x)**2;b0=(1-y)**2
eq((a0-c*b0)*p/(1-p),(1-x)*(y-x)*p/(y*(1-p)))
eq((1-x*x/p)-a0-c*((1-y*y/p)-b0),x*(y-x)*(1-p)/((1-y)*p))
middle=1-x*x-x*x*b0/(B-b0)
eq(middle.subs(B,b0/(1-p)),1-x*x/p)
eq(s.diff(middle,B,2),-2*x*x*b0/(B-b0)**3)
eq(s.diff(middle,B).subs(B,b0/(1-x)),a0/b0)
eq(s.diff(middle,B).subs(B,1-y),x*x/(y*y))
eq(((1-x*x)-a0)/((1-y*y)-b0),c)
H,tt=s.symbols('H tt',real=True)
eq(c.subs({x:(1-tt)/H,y:3/H}),(1-tt)*(H-1+tt)/(3*(H-3)))

for den in range(3,13):
    for ix in range(1,den-1):
        for iy in range(ix+1,den):
            xx=F(ix,den);yy=F(iy,den)
            cc=xx*(1-xx)/(yy*(1-yy))
            bmin=(1-yy)**2;bmax=1-yy*yy
            for ip in range(21):
                pp=F(ip,20);aa=tail(pp,xx);bb=tail(pp,yy)
                yes(bmin<=bb<=bmax)
                gap=aa-(1-xx)**2-cc*(bb-bmin)
                yes(gap>=0)
                yes((gap==0)==(ip in [0,20]))
            for il in range(9):
                lam=F(il,8)
                aa=(1-lam)*(1-xx)**2+lam*(1-xx*xx)
                bb=(1-lam)*bmin+lam*bmax
                eq(aa,(1-xx)**2+cc*(bb-bmin))

# Exact finite polygonal tent representation, including endpoint components.
knots=[F(0),F(1,5),F(1,2),F(4,5),F(1)]
vals=[F(1,3),F(4,5),F(6,5),F(1),F(1,2)]
slopes=[(vals[i+1]-vals[i])/(knots[i+1]-knots[i]) for i in range(4)]
yes(all(slopes[i]>=slopes[i+1] for i in range(3)))
weights=[(F(0),vals[0]/2),(F(1),vals[-1]/2)]
for i in range(1,4):
    weights.append((knots[i],knots[i]*(1-knots[i])*(slopes[i-1]-slopes[i])/2))
integral=sum((knots[i+1]-knots[i])*(vals[i+1]+vals[i])/2 for i in range(4))
eq(sum(w for p,w in weights),integral)
for it in range(101):
    tt=F(it,100)
    j=min(3,next((i for i in range(4) if tt<=knots[i+1]),3))
    interpolant=vals[j]+slopes[j]*(tt-knots[j])
    eq(sum(w*tent(p,tt) for p,w in weights),interpolant)

# Root/Defect's actual affine one-direction witness lies exactly on the chord.
xx=F(6,17);yy=F(12,17)
R=lambda z:1-z/F(120)-F(119,120)*z*z
eq(R(yy),F(1,2));eq(R(xx),F(297,340))
eq(R(xx),(1-xx)**2+xx*(1-xx)/(yy*(1-yy))*(R(yy)-(1-yy)**2))
# Exact full-region check for nontrivial positive tent mixtures.
for xx,yy in [(F(1,4),F(3,4)),(F(1,3),F(2,3)),(F(6,17),F(12,17))]:
    for peaks in [(F(0),F(1)),(F(1,5),F(4,5)),(F(1,2),F(3,5)),(F(0),F(2,3))]:
        for mix in [F(1,5),F(1,2),F(4,5)]:
            bb=mix*tail(peaks[0],yy)+(1-mix)*tail(peaks[1],yy)
            aa=mix*tail(peaks[0],xx)+(1-mix)*tail(peaks[1],xx)
            b0=(1-yy)**2;bx=b0/(1-xx);by=1-yy
            if bb<=bx:upper=(1-xx)**2*bb/b0
            elif bb>=by:upper=1-xx*xx*(1-bb)/(yy*yy)
            else:upper=1-xx*xx-xx*xx*b0/(bb-b0)
            lower=(1-xx)**2+xx*(1-xx)/(yy*(1-yy))*(bb-b0)
            yes(lower<=aa<=upper)
print(f'PASS {checks} exact checks')
