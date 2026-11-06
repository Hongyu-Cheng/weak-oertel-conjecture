from fractions import Fraction as F


def area(poly):
    return abs(sum(a[0]*b[1]-a[1]*b[0]
                   for a,b in zip(poly,poly[1:]+poly[:1])))/2


def cut(poly,normal,threshold=F(0)):
    out=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        va=sum(x*y for x,y in zip(a,normal))-threshold
        vb=sum(x*y for x,y in zip(b,normal))-threshold
        if va>=0:
            out.append(a)
        if va*vb<0:
            t=va/(va-vb)
            out.append(tuple(x+t*(y-x) for x,y in zip(a,b)))
    return out


T=[(F(1),F(0)),(F(-4,9),F(1)),(F(-4,9),F(-1))]
K=cut(T,(F(-1),F(0)),F(-2,3))
normals=[(F(1),F(0)),(F(-1,2),F(26,45)),(F(-1,2),F(-26,45))]
assert area(T)==F(13,9)
assert area(K)==F(160,117)
assert area(T)-area(K)==F(1,13)
assert [area(cut(T,v)) for v in normals]==[F(9,13),F(8,13),F(8,13)]
assert [area(cut(K,v)) for v in normals]==[F(8,13)]*3
assert F(81,169)-F(128,279)==F(967,47151)
assert F(9,20)<F(128,279)
points=[(F(0),F(9,13)),(F(0),F(-9,13)),
        (F(4,9),F(5,13)),(F(-4,9),F(-5,13)),
        (F(4,9),F(-5,13)),(F(-4,9),F(5,13))]
for i,v in enumerate(normals):
    for p in points[2*i:2*i+2]:
        assert sum(x*y for x,y in zip(v,p))==0
        assert p[0]<=F(4,9)<F(2,3)
sigmas=[F(18,13),F(20,13),F(20,13)]
assert sum(F(8,13)/s for s in sigmas)==F(56,45)
assert F(195,98)<2 and F(1753,882)<2
T2=[(F(1),F(0)),(F(-9,20),F(1)),(F(-9,20),F(-1))]
K2=cut(T2,(F(-1),F(0)),F(-37,50))
normals2=[(F(1),F(0)),(F(-1,2),F(261,440)),(F(-1,2),F(-261,440))]
assert area(T2)==F(29,20)
assert area(K2)==F(20349,14500)
assert area(T2)-area(K2)==F(169,3625)
assert [area(cut(T2,v))/area(T2) for v in normals2]==[F(400,841),F(360,841),F(360,841)]
assert [area(cut(K2,v)) for v in normals2]==[F(2331,3625),F(18,29),F(18,29)]
assert [area(cut(K2,v))/area(K2) for v in normals2]==[F(1036,2261),F(1000,2261),F(1000,2261)]
assert F(400,841)-F(128,279)==F(3952,234639)
assert F(128,279)-F(1036,2261)==F(364,630819)
assert F(1000,2261)>F(20,49)
assert F(2000,2261)+F(1036,2261)/4==F(2259,2261)<1
assert F(3036,2261)<F(125,93)
assert F(9,20)<F(37,50)
print('Exact rational bridge-triangle cap-ceiling and full-profile certificates: PASS')
