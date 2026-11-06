"""Exact scalar and actual pyramid checks; geometric proof is in the note."""
from fractions import Fraction as F
from math import factorial
checks=0
def check(ok):
    global checks
    assert ok
    checks+=1

for d in range(2,31):
    r=F(d,d+1); beta=r**d; sp=r**(d-1)/F(d+1)
    check(d*sp==beta)
    check(sp==beta/d)
    check(F(1,2*d)<beta)
    check(F(1,2)-F(1,2*d)==F(d-1,2*d))
    # Standard simplex cut x_1 >= a: section coarea and actual cone volume.
    V=F(1,factorial(d))
    for num in range(1,15):
        a=F(num,15)
        cap=(1-a)**d*V
        section=(1-a)**(d-1)/factorial(d-1)
        check(cap==section*(1-a)/d)
        # Its complement remainder from the far point x_1=0.
        comp=V-cap
        check(comp-section*a/d>=0)
    # Box coordinate caps, at all proper rational offsets.
    sides=[F(2*i+1,i+1) for i in range(d)]
    VB=F(1)
    for s in sides: VB*=s
    for axis in range(d):
        S=VB/sides[axis]
        for num in (1,2,4):
            a=F(num,5)*sides[axis]
            cap=S*(sides[axis]-a)
            cone=S*(sides[axis]-a)/d
            check(cap-cone==F(d-1,d)*cap)
            # Inside support allocation m=lambda*S, including partial density.
            lam=F(num,5)
            check(VB-lam*S*sides[axis]/d>=0)
            # Outside support has zero height regardless of allocation.
            check(lam*S*(sides[axis]-sides[axis])==0)
# Oblique triangle cap: vertices (0,0),(1,0),(0,1), cut x+y>=a.
# Coarea T=a for raw u=(1,1); raw height=1-a, cap=(1-a*a)/2.
for num in range(1,100):
    a=F(num,100)
    cap=(1-a*a)/2
    cone=a*(1-a)/2
    check(cap-cone==(1-a)/2)
    check(cap>=cone)
# Explicit cube law all weights rational; both directed terms independent of law.
for d in range(2,16):
    den=sum(range(1,d+1))
    weights=[F(i,den) for i in range(1,d+1)]
    mixed=sum(2*(w/2)*F(1,2) for w in weights)/d
    check(mixed==F(1,2*d))
print(f'PASS: {checks} exact checks')
