from fractions import Fraction as F
import random
random.seed(140917)
checks=0

def tail(a,r,s):
    if s<=0:return r*r
    if s>=a*r:return F(0)
    if a==1:return (r-s)**2
    if a==F(1,2):return r*r-4*s*s
    if s<=(1-a)*r:return r*r-s*s/(a*(1-a))
    return (a*r-s)**2/(a*(2*a-1))
def pair(a,r,t,s):return tail(a,r,t-s)+tail(a,r,t+s)
def floor(a,r,t):
    R=3*t
    if a>=F(2,3):return 2*tail(a,r,t)
    if a==F(1,2):return 8*t*max(r-2*t,0)
    if r<=t/a:return F(0)
    if r<=t/(1-a):return 2*(a*r-t)**2/(a*(2*a-1))
    return r*r-(2*t-a*r)**2/(a*(2-3*a))
def exact_pair_min(a,r,t):
    cuts={F(0)}
    for height in [F(0),(1-a)*r,a*r]:
        cuts.add(abs(t-height))
    cuts.add(t+r+1)
    cuts=sorted(cuts);cand=cuts[:]
    for lo,hi in zip(cuts,cuts[1:]):
        x=(lo+hi)/2; h=(hi-lo)/4
        f0=pair(a,r,t,x); fm=pair(a,r,t,x-h); fp=pair(a,r,t,x+h)
        A=(fp+fm-2*f0)/(2*h*h);B=(fp-fm)/(2*h)
        if A>0:
            s=x-B/(2*A)
            if lo<s<hi:cand.append(s)
    return min(pair(a,r,t,s) for s in cand)
for a in [F(1,2),F(6,11),F(3,5),F(7,11),F(2,3),F(7,10),F(3,4),F(6,7),F(1)]:
    for r in [F(k,36) for k in range(1,37)]:
        t=F(1,3)
        assert floor(a,r,t)==exact_pair_min(a,r,t),(a,r)
        if a<=F(2,3):
            assert floor(a,r,t)>=F(8,3)*max(r-F(2,3),0)
            assert F(1,2)+F(8,3)*max(r-F(2,3),0)-F(2,9)*(1+2*r*r)>=F(13,162)
        checks+=1
        if F(1,2)<a<F(2,3):
            lo=abs(t-(1-a)*r);hi=min(t,a*r-t)
            if lo<=hi:
                K=(2-3*a)/(a*(2*a-1)*(1-a))
                ss=a*((1-a)*r-t)/(2-3*a)
                J=r*r-(2*t-a*r)**2/(a*(2-3*a))
                for num in range(7):
                    s=lo+(hi-lo)*F(num,6)
                    assert pair(a,r,t,s)==J+K*(s-ss)**2
                    checks+=1
for trial in range(450):
    m=random.randrange(0,21)
    drops=sorted(F(random.randrange(0,11),10) for _ in range(m))
    b=F(random.randrange(1,21),10)
    R=b+sum(drops);rs=[R]
    for x in drops:rs.append(rs[-1]-x)
    mass=R*R+2*sum(r*r for r in rs[1:])
    hinge=max(R-F(2,3)*R,0)+2*sum(max(r-F(2,3)*R,0) for r in rs[1:])
    assert hinge>=mass/(6*R)-F(13,162)*R
    f=lambda r:6*R*max(r-F(2,3)*R,0)-r*r
    assert f(R)+2*sum(f(r) for r in rs[1:])>=f(b)-(R-b)**2/3
    equal_floor=F(5,9)*R*R+sum(F(8,3)*R*max(r-F(2,3)*R,0) for r in rs[1:])
    assert equal_floor>=F(2,9)*mass+R*R/F(243)
    checks+=3
    for a in [F(1,2),F(2,3),F(3,4),F(1)]:
        for beta in [F(0),R/F(29),R/F(3),R]:
            cap=tail(a,R,R/3)+sum(pair(a,r,R/3,h*beta) for h,r in enumerate(rs[1:],1))
            if a==F(1,2):assert cap>=F(2,9)*mass+R*R/F(243)
            else:
                zero=tail(a,R,R/3)+sum(2*tail(a,r,R/3) for r in rs[1:])
                assert cap>=zero
                formula=a/(2*a-1)*(max(R-R/(3*a),0)**2+2*sum(max(r-R/(3*a),0)**2 for r in rs[1:]))
                assert zero==formula
            checks+=1
# The tempting uncorrected hinge fails exactly.
rs=[F(1,3),F(2,3),F(1),F(2,3),F(1,3)]
assert sum(max(r-F(2,3),0) for r in rs)==F(1,3)
assert sum(r*r for r in rs)/6==F(19,54)
checks+=2
print('PASS',checks,'exact pair, chamber, concave-sequence, sector and lattice-phase checks')
