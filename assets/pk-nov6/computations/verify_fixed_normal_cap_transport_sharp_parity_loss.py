#!/usr/bin/env python3
"""Stdlib exact checks of collision bounds and the sharp actual cone family."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from random import Random

checks=0


def check(x):
    global checks
    assert x
    checks+=1


def coupling(a,b):
    aa=sorted((z,v) for z,v in a.items() if v>0)
    bb=sorted((z,v) for z,v in b.items() if v>0)
    A=sum(v for z,v in aa)
    B=sum(v for z,v in bb)
    i=j=0
    ra,rb=aa[0][1]/A,bb[0][1]/B
    out=[]
    while i<len(aa) and j<len(bb):
        p=min(ra,rb)
        check(p>0)
        out.append((aa[i],bb[j],p))
        ra-=p
        rb-=p
        if ra==0:
            i+=1
            if i<len(aa):ra=aa[i][1]/A
        if rb==0:
            j+=1
            if j<len(bb):rb=bb[j][1]/B
    check(sum(p for _,_,p in out)==1)
    return out


def cap_volume(lower,upper,threshold):
    return max(F(0),min(upper-lower,upper-threshold))


rng=Random(736425)
for n in (1,2,3):
    for trial in range(80):
        P=list(product(range(3),repeat=n))
        # Actual intervals: affine center and positive affine width on a box.
        centers=[F(rng.randrange(-4,5),3) for _ in range(n)]
        growth=[F(rng.randrange(-3,4),5) for _ in range(n)]
        base_width=1+2*sum(abs(v) for v in growth)
        tilt=[F(rng.randrange(-5,6),4) for _ in range(n)]
        intervals={}
        for z in P:
            width=base_width+sum(v*k for v,k in zip(growth,z))
            center=sum(v*k for v,k in zip(centers,z))
            check(width>0)
            intervals[z]=(center-width/2,center+width/2)
        s=F(rng.randrange(-20,21),5)
        t=s+F(rng.randrange(1,21),5)
        h=(s+t)/2
        tails=[]
        for q in (s,t,h):
            tails.append({z:cap_volume(lo,hi,q-sum(v*k for v,k in zip(tilt,z)))
                          for z,(lo,hi) in intervals.items()})
        av,bv,hv=tails
        vrows,crows=[],[]
        omega=F(0)
        for r in product(range(2),repeat=n):
            aa={z:v for z,v in av.items() if tuple(k%2 for k in z)==r and v>0}
            bb={z:v for z,v in bv.items() if tuple(k%2 for k in z)==r and v>0}
            if not bb:continue
            A,B=sum(aa.values()),sum(bb.values())
            phi=(A+B)/2  # d=1 here, so all expressions are rational.
            omega+=phi
            vrow,crow={},{}
            for (z,a),(w,b),p in coupling(aa,bb):
                k=tuple((zi+wi)//2 for zi,wi in zip(z,w))
                check(all((zi+wi)%2==0 for zi,wi in zip(z,w)))
                check(k not in vrow)
                vrow[k]=p*phi
                crow[k]=(a+b)/2
                check(crow[k]>=vrow[k])
                check(hv[k]>=crow[k])
            check(sum(vrow.values())==phi)
            vrows.append(vrow)
            crows.append(crow)
        if not vrows:continue
        Q=sum(max(row.get(z,F(0)) for row in vrows) for z in P)
        strong=sum(max([bv[z]]+[row.get(z,F(0)) for row in crows]) for z in P)
        check(sum(hv.values())>=strong>=Q)
        collision=sum(sum(row.get(z,F(0)) for row in vrows)
                      -max(row.get(z,F(0)) for row in vrows) for z in P)
        check(Q==omega-collision)
        check(omega/len(vrows)<=Q<=omega)
        check(Q>=max(sum(row.values()) for row in vrows))


def U(n,d,N):
    return sum(F(comb(k+n-1,n-1)*(N-k)**d,factorial(d))
               for k in range(N+1))


def parity_U(n,d,N,weight):
    if N<weight:return F(0)
    return sum(F(comb(k+n-1,n-1)*(N-weight-2*k)**d,factorial(d))
               for k in range((N-weight)//2+1))


for n in range(1,5):
    for d in range(1,6):
        D=n+d
        for N in (1,n+1,2*n+3,23,70):
            mass=U(n,d,N)
            check(F(N**D,factorial(D))<=mass<=F((N+n)**D,factorial(D)))
            check(sum(comb(n,r)*parity_U(n,d,N,r) for r in range(n+1))==mass)
        for r in range(n+1):
            check(parity_U(n,d,n+1,r)>0)
        for L in (1,3,10,50):
            N=2*L+n+1
            M=U(n,d,N)
            mid=U(n,d,L+n+1)
            exact_upper=2**d*mid/M
            bound=2**d*F(L+2*n+1,2*L+n+1)**D
            check(exact_upper<=bound)
            check(bound==F(1,2**n)*(1+F(3*n+1,2*L+n+1))**D)
            # For d=1 Phi is linear, so the actual aggregation ratio is exact.
            if d==1:
                omega=(M+U(n,d,n+1))/2
                check(F(1,2**n)<=mid/omega<=bound)
        eps=F(1,10)
        L=10*D*(3*n+1)
        x=F(3*n+1,2*L+n+1)
        check(D*x<=eps/2)
        check((1+x)**D<=1/(1-D*x)<=1+2*D*x<=1+eps)

for A in (F(2),F(7,2),F(10),F(1000)):
    s,t=-2*A-1,F(3,2)
    h=(s+t)/2
    # f=z+x1; the other d-1 factors have volume one.
    intervals=[(-2*A-2,-A-2),(F(1),F(2))]
    values=[sum(cap_volume(lo,hi,q) for lo,hi in intervals) for q in (s,t,h)]
    check(values==[A,F(1,2),F(1)])
    check(0<cap_volume(*intervals[0],s)<A)
    check(0<cap_volume(*intervals[1],t)<1)

print(f"PASS {checks} exact checks")
