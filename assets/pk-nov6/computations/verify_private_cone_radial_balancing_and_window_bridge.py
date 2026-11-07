#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations

checks=0


def check(x):
    global checks
    assert x
    checks+=1


def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(poly,poly[1:]+poly[:1])))/2


def clip(poly,a,b=F(0)):
    def f(p):return sum(x*y for x,y in zip(a,p))-b
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp,fq=f(p),f(q)
        if fp>=0:out.append(p)
        if fp*fq<0:
            t=fp/(fp-fq)
            out.append(tuple((1-t)*x+t*y for x,y in zip(p,q)))
    return out


normals=[(F(0),F(-2)),(F(1),F(1)),(F(-1),F(1))]
S=[[-F(1,2),-F(3,2)],[F(1,2),-F(1,2)]]


def transform(p):return tuple(sum(a*x for a,x in zip(row,p)) for row in S)


check(S[0][0]*S[1][1]-S[0][1]*S[1][0]==1)
for p in ((F(1),F(0)),(F(0),F(1)),(F(3),F(-7))):
    check(transform(transform(transform(p)))==p)
    old=[sum(a*x for a,x in zip(u,p)) for u in normals]
    new=[sum(a*x for a,x in zip(u,transform(p))) for u in normals]
    check(new==[old[2],old[0],old[1]])

for L in (F(2),F(3),F(7,2),F(4),F(7),F(10),F(100),F(1000)):
    eps=1/L**2
    K=[(-L,-eps),(L,-eps),(L,F(1)),(-L,F(1))]
    W=2*L*(1+eps)
    D=1+2*L*eps-eps**2
    check(area(K)==W)
    private=[]
    for i in range(3):
        piece=K
        for j,u in enumerate(normals):
            piece=clip(piece,u if j==i else tuple(-v for v in u))
        private.append(area(piece))
    check(private==[eps**2,L-F(1,2),L-F(1,2)])
    check(W-sum(private)==D)
    pairs=[]
    for i,j in combinations(range(3),2):
        pairs.append(area(clip(clip(K,normals[i]),normals[j])))
    check(sum(pairs)==D)
    triple=K
    for u in normals:triple=clip(triple,u)
    check(area(triple)==0)
    fibers=[K,[transform(p) for p in K],[transform(transform(p)) for p in K]]
    for fiber in fibers:
        check(area(fiber)==W)
        for u in normals:
            check(0<area(clip(fiber,u))<W)
    budgets=[sum(area(clip(fiber,u)) for fiber in fibers) for u in normals]
    check(budgets==[W+D]*3)
    check(D<W/2)
    check(all(B/(3*W)<F(1,2) for B in budgets))
    check(W/2-D==L-1-1/L+1/L**4)
    Pplus=[(L/2,F(1,2)),(L,F(1,2)),(L,F(1)),(L/2,F(1))]
    check(area(Pplus)==L/4)
    check((L+1)/(L/2+F(1,2))==2)
    for s in (F(1,2),F(2,3),F(1)):
        for ss in (F(1,2),F(3,4),F(1)):
            tt=L*F(3,4)
            tt2=ss-s-tt
            if -L<=tt2<=-L/2:
                check(tt+s==-tt2+ss)
                midpoint=((tt+tt2)/2,(s+ss)/2)
                check(abs(midpoint[0])<=F(1,4))
                check(F(1,2)<=midpoint[1]<=1)
                check(sum(x*y for x,y in zip(normals[1],midpoint))>0)
                check(sum(x*y for x,y in zip(normals[2],midpoint))>0)

# Exact margin inequalities: h_i(x)=a, h_j(x)=-c a and conversely,
# with c <= 1-eta. Remaining negative margins fill the zero sum.
for d in range(2,9):
    for eta in (F(1,4),F(1,3),F(1,2),F(3,4)):
        for q in (F(1),1/(1-eta),(1+1/(1-eta))/2):
            H=F(3,7)
            bound=(1-(1-eta)*q)*H/2
            check(bound>=0)
            for a in (H,q*H):
                for b in (H,q*H):
                    for c in (F(0), (1-eta)/2,1-eta):
                        for e in (F(0), (1-eta)/2,1-eta):
                            x=[a,-c*a]+[-(1-c)*a/(d-1)]*(d-1)
                            y=[-e*b,b]+[-(1-e)*b/(d-1)]*(d-1)
                            check(sum(x)==sum(y)==0)
                            mid=[(u+v)/2 for u,v in zip(x,y)]
                            check(mid[0]>=bound and mid[1]>=bound)
                            check(all(v<=0 for v in mid[2:]))
            for local_height in (H,2*H,7*H):
                contraction=H/local_height
                check(0<contraction<=1)
                check(contraction*local_height==H)
                check(contraction*q*local_height==q*H)
                check(contraction**d==H**d/local_height**d)

check(F(4,27)>F(1,9))
print(f"PASS {checks} exact checks")
