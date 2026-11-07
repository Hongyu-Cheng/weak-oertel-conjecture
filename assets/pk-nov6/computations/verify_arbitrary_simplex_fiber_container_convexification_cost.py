#!/usr/bin/env python3
"""Exact rational regression checks; the arbitrary-container proof is in the note."""
from fractions import Fraction as F
from itertools import product
import random


def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    p=sorted(set(points))
    if len(p)<=1: return p
    lo=[]; hi=[]
    for q in p:
        while len(lo)>=2 and cross(lo[-2],lo[-1],q)<=0: lo.pop()
        lo.append(q)
    for q in reversed(p):
        while len(hi)>=2 and cross(hi[-2],hi[-1],q)<=0: hi.pop()
        hi.append(q)
    return lo[:-1]+hi[:-1]


def area(p):
    return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1])))/2


def contains(poly,p):
    return all(cross(a,b,p)>=0 for a,b in zip(poly,poly[1:]+poly[:1]))


def dot(a,b): return a[0]*b[0]+a[1]*b[1]


def intersect(n,h,m,k):
    det=n[0]*m[1]-n[1]*m[0]
    assert det
    return ((h*m[1]-n[1]*k)/det,(n[0]*k-h*m[0])/det)


checks=0; small_cases=0
random.seed(732941)
for power in range(4,13):
    e=F(1,2**power); a=1+e*e
    A=hull([(e,0),(1,0),(0,1),(0,e)])
    B=[(F(0),F(0)),(e*e,F(0)),(F(0),e*e)]
    P=hull([(a,a),(a,e-a),(e-a,a)])
    assert area(A)==(1-e*e)/2
    assert area(P)==(2*a-e)**2/2
    assert all(contains(P,(u[0]+v[0],u[1]+v[1])) for u in A for v in B)
    assert F(4,9)*(F(1,2)-area(A))==2*e*e/9
    checks+=4
    specs=[(0,0,0,0,0,0)]
    specs += [tuple(random.randrange(-4,5) for _ in range(3)) +
              tuple(random.randrange(0,5) for _ in range(3)) for _ in range(240)]
    for index,(aa,bb,cc,j,k,l) in enumerate(specs):
        tilt=e if index%2 else e*e
        normals=[(-F(1),tilt*aa/8),(tilt*bb/8,-F(1)),(1+tilt*cc/8,1-tilt*cc/8)]
        heights=[max(dot(n,v) for v in A)+e*e*p/16
                 for n,p in zip(normals,(j,k,l))]
        R=hull([intersect(normals[i],heights[i],normals[(i+1)%3],heights[(i+1)%3])
                for i in range(3)])
        assert len(R)==3 and all(contains(R,v) for v in A)
        delta=area(R)-area(A)
        assert delta>=0
        L=hull(P+R)
        assert delta+(area(L)-area(P))/4>=e/16
        checks+=3
        if delta>=e/16: continue
        small_cases+=1
        eta=2*delta/(1-e)
        assert eta<e/4
        assert all(x>=-eta and y>=-eta and x+y<=1+2*delta for x,y in R)
        q0=min(R,key=lambda v:sum(v))
        q1=next(q for q in R if q[0]>=1)
        q2=next(q for q in R if q[1]>=1)
        assert len({q0,q1,q2})==3
        assert cross(q0,q1,q2)>0
        assert abs(q1[1])<=eta and abs(q2[0])<=eta
        bound=eta*(e+eta)/(1-e)
        assert q0[0]<=bound and q0[1]<=bound
        assert sum(q0)<=e/2
        Fedge=[(a,e-a),(e-a,a)]
        outside=area(hull(Fedge+[q0]))
        assert outside==(2*a-e)*(e-sum(q0))/2
        assert area(L)-area(P)>=outside
        assert (area(L)-area(P))/4>=F(31,256)*e
        checks+=10
    # The huge container with exact contact is covered by the first case.
    assert area(P)-area(A)>=e/16
    checks+=1
print(f'PASS {checks} exact rational checks; {small_cases} small-area arbitrary-orientation triangles')

# The exposed-layer extension has no fiber of mass W/2^n.
layer_checks=0
for power in range(4,24):
    e=F(1,2**power)
    masses=[(1-e*e)/2,(2+2*e*e-e)**2/8,e**4/2,F(1,2),F(1,2),F(1,2)]
    W=sum(masses)
    assert W==F(5,2)-e/2+e*e*((e-F(1,4))**2+F(9,16))
    assert W>F(79,32)
    assert max(masses)==F(1,2)
    assert all(m<F(64,79)*W/4<W/4 for m in masses)
    layer_checks+=4
    for n in range(2,13):
        Wn=2**(n-2)*W
        assert all(m<F(64,79)*Wn/(2**n)<Wn/(2**n) for m in masses)
        assert (2**(n-2)*e/16)/(2**(n-2)*2*e*e/9)==F(9,32)/e
        layer_checks+=2
print(f'PASS {layer_checks} exact no-heavy-fiber layer and padding checks')
