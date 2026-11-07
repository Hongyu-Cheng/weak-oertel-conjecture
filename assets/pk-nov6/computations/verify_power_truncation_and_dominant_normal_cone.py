"""Exact checks for the new truncation application and its shared-tilt sector."""
from fractions import Fraction as F
import random

rng=random.Random(9121)
checks=0

def qp(r,p,c):return sum(max(F(0),x-c)**p for x in r)
def kap(r,j,t):
    I=[i for i,x in enumerate(r) if x>t]
    return (F(1,2*(j-min(I))+1)+F(1,2*(max(I)-j)+1))/2
def integral(r,j,c):
    R=max(r)
    cuts=sorted({F(0),c}|{x for x in r if 0<x<c})
    return sum(kap(r,j,(a+b)/2)*(1/(R-b)-1/(R-a)) for a,b in zip(cuts,cuts[1:]))

# Nonsymmetric concave roofs; exact active-block integral, including knots.
for case in range(220):
    left=rng.randrange(0,13);right=rng.randrange(0,13)
    R=F(rng.randrange(1,10),rng.randrange(1,10))
    def side(n):
        drops=sorted(rng.randrange(0,9) for _ in range(n))
        total=sum(drops)
        denom=total+(rng.randrange(1,8) if case%3 else 0)
        if not denom:denom=1
        out=[R]
        for d in drops:out.append(out[-1]-R*F(d,denom))
        return out
    a,b=side(left),side(right)
    r=list(reversed(a[1:]))+[R]+b[1:];j=left
    assert all(2*r[i]>=r[i-1]+r[i+1] for i in range(1,len(r)-1))
    levels={F(0),R/7,R/3,R/2,6*R/7,R}|set(r)
    for p in (2,3,4,7):
        for c in levels:
            h=R-c
            basic=(h/R)**(p+1)*qp(r,p,0)+kap(r,j,0)*c*h**p/R
            assert qp(r,p,c)>=basic
            if c<R:
                stronger=(h/R)**(p+1)*qp(r,p,0)+h**(p+1)*integral(r,j,c)
                assert qp(r,p,c)>=stronger>=basic
                active=[x-c for x in r if x>c]
                mom=(p+1)*sum(x**p for x in active)-p*h*sum(x**(p-1) for x in active)
                assert mom>=kap(r,j,c)*h**p
                checks+=2
            if 0<c<R:assert qp(r,p,c)>(h/R)**(p+1)*qp(r,p,0)
            checks+=1

# Exact d=1 countercertificates, at and away from a truncation knot.
r=[F(1,3),F(1),F(1,3)]
assert (1-F(1,3))**2*qp(r,1,0)-qp(r,1,F(1,3))==F(2,27)
assert (1-F(1,4))**2*qp(r,1,0)-qp(r,1,F(1,4))==F(1,48)
checks+=2

# Conditional pair inequalities over arbitrary shifts, in all tested dimensions.
for d in range(2,21):
    t=F(1,d+1);G=(1-t)**d
    a=1-F(1,50*d)
    for variant in range(3):
        raw=[F(rng.randrange(1,8)) for _ in range(d-1)]
        u=[a]+[(1-a)*x/sum(raw) for x in raw]
        b=max(u[1:])
        assert a>b and b<t
        assert ((a-t)/(a-b))**d<=F(1,2)
        assert (1-t/a)**(d+1)>=G/2
        C=a**(d-1)
        for x in u[1:]:C/=a-x
        assert C>=1
        for z in [F(0),b/3,b/2,b]:
            def tail(v):
                if v<=z:return F(1)
                if v>=a:return F(0)
                return ((a-v)/(a-z))**d
            for radius in [F(1,5),F(1,2),F(3,4),F(1)]:
                v=t/radius
                for s in [F(k,20) for k in range(31)]+[max(F(0),v-z),v,v+a]:
                    assert tail(v-s)+tail(v+s)>=2*tail(v)
                    checks+=1
        checks+=4
print(f"PASS {checks} exact checks")
