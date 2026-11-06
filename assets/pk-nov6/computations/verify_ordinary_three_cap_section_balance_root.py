from fractions import Fraction as F

P=[(F(-15),F(-22)),(F(16),F(-4)),(F(-2),F(25))]
normals=[(1,0),(0,1),(-1,-1)]
fractions=[F(128,279),F(625,1363),F(1369,2940)]
sections=[F(9784,279),F(30575,1363),F(45251,2940)]
ratios=[F(927,1519),F(12151,18424),F(20531,24720)]

def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(poly):return abs(sum(cross(a,b) for a,b in zip(poly,poly[1:]+poly[:1])))/2
def clip(poly,u):
    out=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        va=sum(x*y for x,y in zip(a,u));vb=sum(x*y for x,y in zip(b,u))
        if va>=0:out.append(a)
        if va*vb<0:
            t=va/(va-vb)
            out.append(tuple(a[j]+t*(b[j]-a[j]) for j in range(2)))
    return out

assert area(P)==F(1223,2)
for a,b in zip(P,P[1:]+P[:1]):
    assert cross(tuple(b[j]-a[j] for j in range(2)),tuple(-a[j] for j in range(2)))>0
checks=4
for i,u in enumerate(normals):
    cap=clip(P,u)
    pts=[pt for pt in cap if sum(x*y for x,y in zip(pt,u))==0]
    axis=1 if i==0 else 0
    lo,hi=sorted(pt[axis] for pt in pts)
    assert area(cap)/area(P)==fractions[i]
    assert hi-lo==sections[i]
    assert min(-lo,hi)/max(-lo,hi)==ratios[i]
    assert fractions[i]<F(47,100)
    assert 3*ratios[i]**2>1
    checks+=5
assert sections[0]>2*sections[2]
weights=[1/s for s in sections]
assert weights[0]/sum(weights)<F(2,9)
checks+=2
print('PASS:',checks,'exact rational assertions')
