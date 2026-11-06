"""Exact rational certificate for the cap-cover BM nongluing polygons."""
from fractions import Fraction as F

A=[(-1,2),(-2,-1),(2,-3),(2,-1)]
B=[(F(-13,8),F(17,8)),(F(-5,2),F(-1,2)),(F(3,2),F(-5,2)),(F(3,2),-1)]
A=[tuple(map(F,p)) for p in A]
B=[tuple(map(F,p)) for p in B]
K=[tuple((x+y)/2 for x,y in zip(p,q)) for p,q in zip(A,B)]
normals=[(1,0),(0,1),(-1,-1)]
facet_normals=[(-3,1),(-1,-2),(1,0),(1,1)]
supports=[[5,4,2,1],[7,F(7,2),F(3,2),F(1,2)],[6,F(15,4),F(7,4),F(3,4)]]
ratios=[F(3,4),F(17,16),F(1)]
translations=[(F(0),F(-1,4)),(F(-9,16),F(0)),(F(-1,2),F(1,2))]

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def area(poly):
    return sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1]))/2
def clip(poly,u):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp,fq=dot(p,u),dot(q,u)
        if fp>=0: out.append(p)
        if fp*fq<0:
            out.append(tuple((fq*x-fp*y)/(fq-fp) for x,y in zip(p,q)))
    return out

checks=0
for poly,rhs in zip([A,B,K],supports):
    assert all(h>0 for h in rhs)  # origin strictly satisfies every facet.
    for p in poly:
        assert all(dot(n,p)<=h for n,h in zip(facet_normals,rhs))
        assert sum(dot(n,p)==h for n,h in zip(facet_normals,rhs))==2
        checks+=2
    assert area(poly)>0
    checks+=2
for p in A:
    for q in B:
        avg=tuple((x+y)/2 for x,y in zip(p,q))
        assert all(dot(n,avg)<=h for n,h in zip(facet_normals,supports[2]))
        checks+=1
assert [area(poly) for poly in [A,B,K]]==[F(10),F(271,32),F(1183,128)]
checks+=1
expected=[[F(5),F(45,16),F(245,64)],[F(8,3),F(289,96),F(363,128)],[F(55,8)]*3]
for u,ratio,v,vals in zip(normals,ratios,translations,expected):
    ac,bc,kc=[clip(poly,u) for poly in [A,B,K]]
    assert set(bc)=={tuple(ratio*x+y for x,y in zip(p,v)) for p in ac}
    assert set(kc)=={tuple((1+ratio)*x/2+y/2 for x,y in zip(p,v)) for p in ac}
    assert [area(poly) for poly in [ac,bc,kc]]==vals
    assert all(0<area(c)<area(p) for c,p in zip([ac,bc,kc],[A,B,K]))
    assert area(bc)==ratio**2*area(ac)
    assert area(kc)==((1+ratio)/2)**2*area(ac)
    assert area(ac)/area(A)!=area(bc)/area(B)
    assert dot(u,v)==0
    checks+=8
a,b,k=map(area,[A,B,K])
assert 4*k-a-b==F(37,2)
assert (4*k-a-b)**2-4*a*b==F(7,2)
assert a+b+k==F(3547,128)
assert max(a,b,k)<(a+b+k)/2
assert B[2][0]-B[1][0]==A[2][0]-A[1][0]
assert B[3][1]-B[2][1]==F(3,4)*(A[3][1]-A[2][1])
checks+=6
def roof(p,constant): return constant-11*p[0]-p[1]
for ratio,v in zip(ratios,translations):
    for p in [(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]:
        bp=tuple(ratio*x+y for x,y in zip(p,v))
        kp=tuple((1+ratio)*x/2+y/2 for x,y in zip(p,v))
        assert roof(bp,F(14))==ratio*roof(p,F(19))
        assert roof(kp,F(33,2))==(1+ratio)*roof(p,F(19))/2
        checks+=2
ap=A[:3]+[(F(9,5),F(-4,5))]
bp=B[:3]+[(F(27,20),F(-17,20))]
assert roof(ap[3],F(19))==0 and roof(bp[3],F(14))==0
assert tuple(bp[3][j]-bp[2][j] for j in range(2))==tuple(F(3,4)*(ap[3][j]-ap[2][j]) for j in range(2))
checks+=2
print(f"PASS: {checks} exact geometry, cap, BM, and embedding checks")
