"""Exact common-normal paired counter and all-normal ordinary-depth calibration."""
from fractions import Fraction as F


def area(poly):
    if not poly:
        return F(0)
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]
                   -poly[i][1]*poly[(i+1)%len(poly)][0]
                   for i in range(len(poly))))/2


def cap(poly,u,threshold):
    out=[]
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        vp=sum(a*b for a,b in zip(u,p))-threshold
        vq=sum(a*b for a,b in zip(u,q))-threshold
        if vp>=0:
            out.append(p)
        if (vp<0<vq) or (vq<0<vp):
            alpha=vp/(vp-vq)
            out.append(tuple(p[k]+alpha*(q[k]-p[k]) for k in range(2)))
    return area(out)


def triangle(r):
    return [(F(0),F(0)),(r,F(0)),(F(0),r)]


V=F(1,2)
def ordinary(r,y):
    scaled=sorted([r-sum(y),*y])
    assert scaled[0]>=0
    return 4*V*scaled[0]*scaled[1]


r,s=F(1),F(4,3)
y=(F(4,9),F(4,9))
A,B=triangle(r),triangle(s)
fa,fb=ordinary(r,y),ordinary(s,y)
assert (fa,fb)==(F(16,81)*V,F(64,81)*V)
assert cap(A,(F(4),F(3)),F(28,9))==fa
assert cap(B,(F(1),F(0)),F(4,9))==fb
assert cap(A,(F(1),F(1)),F(4,9))==F(65,81)*V
assert cap(B,(F(1),F(1)),F(4,3))==0
assert fa+fb-F(65,81)*V==F(5,27)*V
properA=cap(A,(F(1),F(1)),F(5,9))
properB=cap(B,(F(1),F(1)),F(11,9))
assert properA==F(56,81)*V and properB==F(23,81)*V
assert properA+properB==F(79,81)*V<fa+fb
assert F(5,9)+F(11,9)==2*sum(y)
assert 0<F(5,9)<r and 0<F(11,9)<s

# Arithmetic screen only; the proof of the ordinary lower bound for ALL real
# normals is the two-cap-type argument in Section 2 of the note.
normalchecks=0
for ux in range(-8,9):
    for uy in range(-8,9):
        if ux==uy==0:
            continue
        u=(F(ux),F(uy)); threshold=sum(x*z for x,z in zip(u,y))
        assert cap(A,u,threshold)>=fa
        assert cap(B,u,threshold)>=fb
        normalchecks+=2

families=0
for r in [F(1),F(3,2),F(2)]:
    for j in range(1,10):
        s=r*(1+F(j,20))
        for theta in [F(0),F(1,5),F(2,5),F(3,5),F(4,5)]:
            L=2*s/3+theta*(r-2*s/3)
            assert 0<r<s<3*r/2 and 2*s/3<=L<r
            y=(L/2,L/2)
            fa,fb=ordinary(r,y),ordinary(s,y)
            assert fa==2*V*L*(r-L) and fb==2*V*L*(s-L)
            alpha=2*L-s
            cost=cap(triangle(r),(F(1),F(1)),alpha)
            assert cost==V*(r*r-alpha*alpha)
            Delta=(s-r)*(r+s-2*L)
            assert fa+fb-cost==Delta*V>0
            eps=Delta/(8*s)
            assert 0<alpha+eps<r and 0<s-eps<s
            proper=cap(triangle(r),(F(1),F(1)),alpha+eps)
            proper+=cap(triangle(s),(F(1),F(1)),s-eps)
            assert proper-cost==V*(4*(s-L)*eps-2*eps*eps)
            assert proper<=fa+fb-Delta*V/2
            if theta==0:
                assert cost/(fa+fb)==(3*r+s)/(4*s)
            families+=1
print('PASS: exact rational counter, matching ordinary minimizing caps, and both proper paired cuts;')
print(families,'strict family/proper-perturbation certificates and',normalchecks,'rational ordinary-cap checks')
