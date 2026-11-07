#!/usr/bin/env python3
"""Exact algebra and independent planar clipping for the truncation note."""
from fractions import Fraction as F

checks=0


def check(x):
    global checks
    assert x
    checks+=1


for d in range(2,21):
    c=F(d-1,2*d*(2*d-1))
    gamma=F(d,d+1)**d
    for denominator in (2*(d+1),4*(d+1),10*(d+1),100*(d+1)):
        eps=F(1,denominator)
        e=eps**d
        delta=e/(1-e)
        alpha_power=1/(1-e)
        check(delta<1)
        check(alpha_power<2**d)
        check((1+delta/d)**d>=alpha_power) # alpha-1 <= delta/d.
        check(F(2*d+1,d*(d+1))<=1) # centroid displacement coefficient.
        check(gamma/(1-e)-gamma==gamma*delta)
        check(alpha_power*e==delta)
        check(alpha_power-1==delta)
        rho_critical=c*eps
        check(rho_critical<F(1,2*d))
        check(rho_critical<=(1-eps)/F(2*d*(2*d-1)))
        for scale in (F(1,4),F(1,2),F(3,4),F(99,100)):
            rho=scale*rho_critical
            check(1-rho>(2*d-1)*rho)
            check(-1+(2*d-1)**2*rho < -eps-(2*d-1)*rho)
            lower=eps-d*rho
            upper=F(d,2*d-1)*eps+d*rho
            check(lower>upper)
        check(eps-d*rho_critical==F(d,2*d-1)*eps+d*rho_critical)
        a=1-F(d+1,d)*eps
        check(a>=F(1,2))
        check((1-a)*F(d,d+1)==eps)
        check(1/a-1<=F(2*(d+1),d)*eps)
        # Fixed endpoint homothet A lies strictly within every middle body.
        Amin=F(d,2*(d+1))
        Amax=F(2*d+1,2*(d+1))
        check((eps/Amin)**d*alpha_power<1)
        check(Amax<1)


def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(poly,poly[1:]+poly[:1])))/2


def clip(poly,normal,threshold):
    def margin(p):return sum(x*y for x,y in zip(normal,p))-threshold
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        mp,mq=margin(p),margin(q)
        if mp>=0:out.append(p)
        if mp*mq<0:
            s=mp/(mp-mq)
            out.append(tuple((1-s)*x+s*y for x,y in zip(p,q)))
    return out


def centroid(poly):
    cross=[p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])]
    den=3*sum(cross)
    return tuple(sum((p[i]+q[i])*c for p,q,c in zip(poly,poly[1:]+poly[:1],cross))/den
                 for i in range(2))


T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
V=F(1,2)
for q in (F(1,25),F(1,50),F(2,75),F(3,100)):
    eps=2*q/(1+q*q)
    alpha=(1+q*q)/(1-q*q)
    e=eps**2
    delta=e/(1-e)
    check(eps<=F(1,6))
    check(alpha**2*(1-e)==1)
    K=clip(T,(F(1),F(1)),eps)
    Ktilde=[tuple(alpha*x for x in p) for p in K]
    check(area(K)==(1-e)*V)
    check(area(Ktilde)==V)
    intersection=clip(T,(F(1),F(1)),alpha*eps)
    check((V-area(intersection))/V==delta)
    outer=clip(Ktilde,(F(1),F(1)),F(1))
    check(area(outer)/V==delta)
    check(centroid(Ktilde)==(alpha*(1-eps**3)/(3*(1-e)),)*2)
    cuts=[((F(1),F(0)),alpha/3),((F(0),F(1)),alpha/3),
          ((-F(1),-F(1)),-2*alpha/3)]
    fractions=[area(clip(Ktilde,n,t))/V for n,t in cuts]
    check(fractions[:2]==[F(4,9)/(1-e)]*2)
    check(fractions[2]==F(4,9)/(1-e)-delta)

print(f"PASS {checks} exact checks")
