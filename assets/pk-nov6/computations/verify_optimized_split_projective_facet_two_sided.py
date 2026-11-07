"""Exact calibrations for optimized split-projective facet transport.

The analytic transport proof is in the adjacent Markdown source.
These checks verify the scalar inequality on rational-power inputs,
all bit identities, and two actual interval-face calibrations.
"""
from fractions import Fraction as Q
from itertools import product

checks = 0
def check(condition):
    global checks
    assert condition
    checks += 1

def f(s, delta, d):
    if s >= delta:
        return s**(-d)
    return delta**(-d)-d*delta**(-d-1)*(s-delta)

def q(s, delta, d):
    return max(s, delta)**(-d-1)

def R(s, delta, d):
    return f(s, delta, d)/q(s, delta, d)

# Inputs chosen as kth powers make every fractional power exact.
roots = [Q(j, 3) for j in range(1, 10)]
for d in range(2, 9):
    k = d-1
    for delta_root, x_root, y_root in product(roots[::2], roots, roots):
        delta, x, y = delta_root**k, x_root**k, y_root**k
        if x < delta or y < delta:
            continue
        mean = (x+y)/2
        jac = ((x_root**(d+1)+y_root**(d+1))/2)**k
        check(f(mean, delta, d)*jac >= (R(x,delta,d)+R(y,delta,d))/2)
        ell=(R(x,delta,d)+R(y,delta,d))/2
        diff=(R(x,delta,d)-R(y,delta,d))/2
        check(f(mean,delta,d)*jac>=ell+Q(d+1,3*d-1)*diff**2/ell)
    for delta_root, y_root in product(roots[::2], roots):
        if y_root < delta_root:
            continue
        delta, y = delta_root**k, y_root**k
        for j in range(13):
            # Whole feasible mixed interval x in [2delta-y,delta].
            x = delta - Q(j,12)*(y-delta)
            mean = (x+y)/2
            jac = ((delta_root**(d+1)+y_root**(d+1))/2)**k
            check(f(mean,delta,d)*jac >= (R(x,delta,d)+R(y,delta,d))/2)
            check(R(x,delta,d)==(d+1)*delta-d*x)
            ell=(R(x,delta,d)+R(y,delta,d))/2
            diff=(R(x,delta,d)-R(y,delta,d))/2
            check(f(mean,delta,d)*jac>=ell+Q(d+1,3*d-1)*diff**2/ell)

# Exact simultaneous-bit formula, including missed source surplus.
for ra, rb in product(range(1,15), repeat=2):
    ell, diff = Q(ra+rb,2), Q(ra-rb,2)
    for ia, ib, ik in product((0,1), repeat=3):
        if ia+ib < ik:
            continue
        cap = ra*ia+rb*ib
        check(cap == ell*ik+ell*(ia+ib-ik)+diff*(ia-ib))
        check(cap >= min(ra,rb)*ik)

def interval_tail(length, threshold, sign):
    if sign == 1:
        return max(Q(0),length-max(Q(0),threshold)) if threshold<=length else Q(0)
    return min(length,max(Q(0),threshold))

# The weights are constant because the projective vector is normal to
# the parallel faces; split offsets prescribe the stated denominators.
for alen, blen, la, lb, delta in [
        (Q(8),Q(1),Q(2),Q(1),Q(1)),
        (Q(1),Q(27),Q(-1,2),Q(3,2),Q(1,2))]:
    d=2
    j = alen*q(la,delta,d)
    check(j==blen*q(lb,delta,d))
    slen=(alen+blen)/2
    ls=(la+lb)/2
    ra,rb=R(la,delta,d),R(lb,delta,d)
    ell=(ra+rb)/2
    source=slen*f(ls,delta,d)
    acost,bcoat=alen*f(la,delta,d),blen*f(lb,delta,d)
    check(acost+bcoat==2*j*ell)
    check(acost+bcoat<=2*source)
    check(source>=(acost+bcoat)/2+Q(d+1,3*d-1)*(acost-bcoat)**2/(2*(acost+bcoat)))
    for ha,hb,sign in product([Q(i,2) for i in range(-4,21)],
                              [Q(i,2) for i in range(-4,21)],(1,-1)):
        hs=(ha+hb)/2
        ca=interval_tail(alen,ha,sign)*f(la,delta,d)
        cb=interval_tail(blen,hb,sign)*f(lb,delta,d)
        frac=interval_tail(slen,hs,sign)/slen
        zeta_h=j*ell*frac
        defect=j*abs(ra-rb)*frac/2
        check(ca+cb>=zeta_h-defect)
        source_h=source*frac
        check(ca+cb>=source_h-(source_h-zeta_h)-defect)

# Sharp equal-face example and unavailable a=0 shift calibration.
check(Q(2)==2*Q(1))
check(Q(1)+Q(9)>2*Q(4))
for d in range(2,12):
    for u in [Q(j,7) for j in range(7,78)]:
        alpha=u**(d+1)
        beta=Q(1)
        check(alpha*q(u,Q(1),d)==beta*q(2-u,Q(1),d))
        cost=alpha*f(u,Q(1),d)+beta*f(2-u,Q(1),d)
        check(cost==beta*((d+1)*u-(d-1)))
        kappa=Q(d-1)*(u-1)/((d+1)*u-(d-1))
        check(kappa<Q(d-1,d+1))
        check(1-kappa==2*u/((d+1)*u-(d-1)))
gamma=Q(4,9)
t=Q(21,40)
check(Q(1,2)<t<1-gamma)
check(gamma*(1+2*t)/2-gamma==Q(1,90))
check(Q(1,2)+Q(1,18)==1-gamma)
check(t<1-gamma)
print(f"PASS: {checks:,} exact checks")
