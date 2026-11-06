"""Exact supplementary checks, not a substitute for the geometric proof."""
from fractions import Fraction as F
from itertools import product
import random

checks = 0
def check(p):
    global checks
    assert p
    checks += 1

def clip(x, a, b):
    return min(b, max(a, x))

def cap(l, h, threshold):
    return h - clip(threshold, l, h)

# Fubini's one-dimensional branches, retaining the derivative of |u|.
# These are single-fiber identity tests; no compatibility is claimed for
# independently generated rows.
rng = random.Random(73119)
dt = F(1, 100000)
buffer = F(1, 10)
for n in range(1, 4):
    for _ in range(150):
        z = [rng.randrange(-3, 4) for j in range(n)]
        a = [F(rng.randrange(-3, 4), 3) for j in range(n)]
        da = [F(rng.randrange(-3, 4), 2) for j in range(n)]
        v = F(rng.randrange(-3, 4), 2)
        az = sum(x*y for x,y in zip(a,z))
        daz = sum(x*y for x,y in zip(da,z))
        c = -az-buffer
        ell = daz+v*(c+buffer)
        cnew = -(az+dt*daz)/(1+dt*v)-buffer
        statuses = [
            (c-1,c+2,ell),
            (c,c+2,min(ell,0)),
            (c-1,c,max(ell,0)),
            (c+1,c+2,F(0)),
            (c-2,c-1,F(0)),
        ]
        for l,h,derivative in statuses:
            quotient=(cap(l,h,cnew)-cap(l,h,c))/dt
            check(quotient*(1+dt*v)==derivative)

# Actual rectangle example, all normal orientations represented by a.
s=F(1,10)
for denominator in range(1,18):
    for numerator in range(-80,81):
        a=F(numerator,denominator)
        up=sum(cap(F(-1),F(1),-a*z) for z in (-1,0,1))
        down=sum(clip(a*z+2*s,F(-1),F(1))+1 for z in (-1,0,1))
        check(up==3)
        check(down>=3+2*s)
        if abs(a)>=1+2*s:
            check(down==3+2*s)
check(F(4)>3+2*s)

# Exact actual contacts and the zonoid equality for a=1,u=1.
check(cap(F(-1),F(1),1)==0)
check(cap(F(-1),F(1),0)==1)
check(cap(F(-1),F(1),-1)==2)
for alpha,v in product(range(-5,6),repeat=2):
    inside=alpha-v
    outside=-alpha+v
    derivative=min(inside,0)+max(outside,0)
    check(derivative==0)
    check(abs(inside)==abs(outside))

# Complete-chain algebra: no unweighted interior integer has been omitted.
for r in range(-8,8):
    for end in range(r+2,10):
        N=end-r-1
        for p in range(r+1,end):
            c=F(r+end,2)-p
            proper=sum(z-p for z in range(r+1,end))
            check(proper==N*c)
            left_inside_plus=proper+(r-p)+(end-p)
            left_inside_minus=-proper
            right_inside_plus=proper
            right_inside_minus=-proper-(r-p)-(end-p)
            check(left_inside_plus==(N+2)*c)
            check(right_inside_minus==-(N+2)*c)
            check((left_inside_plus>=0 and left_inside_minus>=0)==(c==0))
            check((right_inside_plus>=0 and right_inside_minus>=0)==(c==0))

# Actual nonsymmetric convex interval family realizing the midpoint rule.
# Sheared equal intervals; the old cap has inside/outside endpoint contacts.
for slope in (F(-3,2),F(-1,3),F(0),F(7,5)):
    for h in (F(1,2),F(1),F(5,3)):
        for N in (1,2,3,4):
            # C fibers at z=-N,...,N, centered on slope*z.  The plane
            # x=(slope-h/N)z touches the bottom at N, top at -N.
            a=-slope+h/N
            def value(tilt):
                return sum(cap(slope*z-h,slope*z+h,-tilt*z)
                           for z in range(-N,N+1))
            check(value(a)==(2*N+1)*h)
            for j in range(1,6):
                movement=F(j,1000)
                # Either direction has constant mass for this symmetric
                # calibration; the increasing direction makes the old
                # full/empty endpoint traces strict.
                check(value(a-movement)==value(a))
                check(value(a+movement)==value(a))

print(f"PASS: {checks} exact checks")
