from fractions import Fraction as F
from itertools import product

checks = 0
def check(p):
    global checks
    assert p
    checks += 1

def prod(xs):
    r=F(1)
    for x in xs: r*=x
    return r

def G(a,b,s):
    d=len(a)
    return (s**d+2)*prod(min(x,y,(x+y)/(2*s)) for x,y in zip(a,b))

a=[F(2)]*3+[F(1,2)]*3
b=[F(1)]*6
k=prod((x+y)/2 for x,y in zip(a,b))
t=prod(min(x,y) for x,y in zip(a,b))
gamma=F(6,7)**6
check(k==F(729,512))
check(t==F(1,8))
check(G(a,b,F(3,2))==F(857,512))
check((k+2)/2-G(a,b,F(3,2))==F(39,1024))
check(k/2-gamma*(k+2)/2==F(3978153,120472576))

# Exact finite breakpoint maxima dominate every sampled rational parameter.
# The analytic log-convex-cell proof, not this finite check, proves universality.
for d in range(1,5):
    for aa in product([F(1,2),F(1),F(2)],repeat=d):
        bb=[F(1)]*d
        breaks=[(x+y)/(2*min(x,y)) for x,y in zip(aa,bb)]
        best=max(G(aa,bb,s) for s in breaks)
        for s in [F(1,4),F(1,2),F(1),F(5,4),F(3,2),F(2),F(3),F(4)]:
            check(G(aa,bb,s)<=best)
for numerator in range(1,101):
    R=F(numerator,10)
    if R<1: continue
    k=(R+2+1/R)/4
    check(k+2/R-(k+2)/2==((R-3)**2+8)/(8*R))
    check(k+2/R>(k+2)/2)

print(f"PASS: {checks} exact checks")
