"""Independent exact algebra/status checks for the nonsimplex cap audit.
The finite checks supplement the classical proof; they are not its basis.
"""
from fractions import Fraction as F
from math import factorial, comb

checks=0
def check(p):
    global checks
    assert p
    checks+=1

def power_integral_shift(lo,hi,shift,p):
    return sum(F(comb(p,j))*shift**(p-j)*(hi**(j+1)-lo**(j+1))/F(j+1)
               for j in range(p+1))
def cap_integrated(p,r,h):
    vp=F((p+1)**p,factorial(p)); delta=F(p,p+1)**p
    if h>=p*r:return F(0)
    if h<=-r:return F(2)*vp*r**(p+1)/F(p+1)
    if h>=0:
        return 2*delta*vp*power_integral_shift(h/p,r,-h/p,p)
    q=-h
    return 2*vp*q**(p+1)/F(p+1)+2*delta*vp*power_integral_shift(q,r,q/p,p)
def formula(p,r,h):
    vp=F((p+1)**p,factorial(p)); V=2*vp/F(p+1);delta=F(p,p+1)**p
    return delta*V*(r-h/p)**(p+1)-V/F(p)*max(-h,F(0))**(p+1)

for p in range(2,9):
    vp=F((p+1)**p,factorial(p));V=2*vp/F(p+1);delta=F(p,p+1)**p
    check(delta<F(1,2))
    check(1-delta*F(p+1,p)**(p+1)==-F(1,p))
    for r in (F(1,3),F(1),F(7,5)):
        for j in range(-12,12*p+1):
            h=r*F(j,12)
            check(cap_integrated(p,r,h)==formula(p,r,h))
        for j in range(0,12*(p+2)+1):
            h=r*F(j,12)
            paired=cap_integrated(p,r,h)+cap_integrated(p,r,-h)
            check(paired>=2*delta*V*r**(p+1))
            if j:check(paired>2*delta*V*r**(p+1))
        # Endpoint statuses and the canonical derivative.
        check(formula(p,r,-r)==V*r**(p+1))
        check(formula(p,r,p*r)==0)
        check(delta*V*F(p+1,p)*r**p==2*delta*vp/F(p)*r**p)
    # Exact affine cancellation for arbitrary paired integer evaluations.
    vals=(F(-2),F(-1),F(0),F(1),F(2))
    a=F(1,100*p)
    radii={z:F(1)+F(1,20)*(4-z*z) for z in vals}
    total=sum(formula(p,radii[z]+a*z,p*a*z) for z in vals)
    q0=sum(delta*V*radii[z]**(p+1) for z in vals)
    correction=V*p**p*sum(max(-a*z,F(0))**(p+1) for z in vals)
    check(total==q0-correction)
    check(total<q0)
    check(sum(V*(radii[z]+a*z)**(p+1) for z in vals)>sum(V*radii[z]**(p+1) for z in vals))

for j in range(1,101):
    s=F(j,500)
    check(s<=F(1,5))
    mass=3*((1-s)**3+1+(1+s)**3)
    q=sum(formula(2,1+s*z,2*s*z) for z in (-1,0,1))
    check(mass==9+18*s*s)
    check(q==4-12*s**3)
    low=F(4,3)*(1+2*(1-s)**3)
    end=F(4,3)*(1+s)**3
    check(low>end)
    check(q>=F(488,125))
    check(end<=F(288,125))
    # The isolating tilt 10 empties every other fiber as an actual set.
    for source in (-1,1):
        for z in (-1,0,1):
            if z!=source:
                check(2*(1+s*z)+10*source*(z-source)<0)

check(F(1012,3645)>F(27,128))
check(F(488,1215)<F(4,9))
check(F(4,3)*(1+2*F(4,5)**3)==F(1012,375))
check(F(1)+2*F(4,5)**3-F(6,5)**3==F(37,125))
print(f'PASS {checks} independent exact slice, paired-status, affine-cancellation, and source-budget checks')
