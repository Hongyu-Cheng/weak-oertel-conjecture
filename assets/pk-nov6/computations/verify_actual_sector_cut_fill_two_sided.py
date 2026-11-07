"""Exact actual-polygon certificate for the local sector cut-and-fill."""
from fractions import Fraction as F

checks = 0


def check(value):
    global checks
    assert value
    checks += 1


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def area(poly):
    return abs(sum(a[0]*b[1]-a[1]*b[0]
                   for a,b in zip(poly,poly[1:]+poly[:1])))/2


def clip(poly, normal):
    out=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        da,db=dot(a,normal),dot(b,normal)
        if da>=0:
            out.append(a)
        if da*db<0:
            t=da/(da-db)
            out.append(tuple(a[j]+t*(b[j]-a[j]) for j in range(2)))
    return out


def section(poly, normal):
    pts=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        da,db=dot(a,normal),dot(b,normal)
        if da==0:
            pts.append(a)
        if da*db<0:
            t=da/(da-db)
            pts.append(tuple(a[j]+t*(b[j]-a[j]) for j in range(2)))
    coordinate=1 if normal==(1,0) else 0
    return max(p[coordinate] for p in pts)-min(p[coordinate] for p in pts)


normals=((1,0),(0,1),(-1,-1))
P0=(F(-26,25),F(-49,50))
P1=(F(49,25),F(-49,50))
R=(F(1,2),F(1,2))
S=(F(-26,25),F(101,50))
old=[P0,P1,R,S]
P=(F(147,148),F(0))
epsilon=F(25,732008)
tau=F(1,20)
Pe=(P[0]+epsilon,F(0))
R1=tuple((1-tau)*R[i]+tau*Pe[i] for i in range(2))
R2=tuple((1-tau)*R[i]+tau*S[i] for i in range(2))
filled=[P0,P1,Pe,R,S]
new=[P0,P1,Pe,R1,R2,S]

for poly in (old,filled,new):
    for i in range(len(poly)):
        check(cross(poly[i-1],poly[i],poly[(i+1)%len(poly)])>0)
        check(cross(poly[i],poly[(i+1)%len(poly)],(0,0))>0)

check(cross(P1,R,P)==0)
check(area(old)==F(453,100))
check(area(filled)-area(old)==F(1,39568))
check(area([R,R1,R2])==F(1,39568))
check(area(new)==area(old))
check(cross(Pe,R,S)/2==F(3,296)-F(19,25)*epsilon)
for point in (R,R1,R2):
    check(point[0]>0 and point[1]>0)

old_q=[area(clip(old,v)) for v in normals]
new_q=[area(clip(new,v)) for v in normals]
old_s=[section(old,v) for v in normals]
new_s=[section(new,v) for v in normals]
check(old_q==[F(374177,192500),F(763573,370000),F(10201,5000)])
check(old_s==[F(3799,1925),F(7523,3700),F(101,50)])
check([a-b for a,b in zip(old_q,new_q)]==[F(0),F(49,2928032),F(0)])
check([b-a for a,b in zip(old_s,new_s)]==[F(0),epsilon,F(0)])

for qs,ss in ((old_q,old_s),(new_q,new_s)):
    check(max(qs)/area(old)<F(128,279))
    x,y,z=sorted(qs)
    check(x+y+z/4<area(old))
    check(ss[1]>ss[2]>ss[0])

x,y,z=sorted(old_q)
check(area(old)-(x+y+z/4)==F(3429703,113960000))
old_w=[1/s for s in old_s]
new_w=[1/s for s in new_s]
check(new_w[1]/sum(new_w)<old_w[1]/sum(old_w))
check(new_w[1]/sum(new_w)>F(2,9))  # It is not a weight-bound counterexample.

# Entire exact rational family of smaller edge-fraction shaves.
for denominator in range(20,121):
    tt=F(1,denominator)
    ee=tt*tt*F(3,296)/(F(37,50)+tt*tt*F(19,25))
    pp=(P[0]+ee,F(0))
    rr1=tuple((1-tt)*R[i]+tt*pp[i] for i in range(2))
    rr2=tuple((1-tt)*R[i]+tt*S[i] for i in range(2))
    poly=[P0,P1,pp,rr1,rr2,S]
    check(area(poly)==area(old))
    qq=[area(clip(poly,v)) for v in normals]
    ss=[section(poly,v) for v in normals]
    check([a-b for a,b in zip(old_q,qq)]==[F(0),F(49,100)*ee,F(0)])
    check([b-a for a,b in zip(old_s,ss)]==[F(0),ee,F(0)])
    check(max(qq)/area(poly)<F(128,279))
    x,y,z=sorted(qq)
    check(x+y+z/4<area(poly))
    ww=[1/s for s in ss]
    check(ww[1]/sum(ww)<old_w[1]/sum(old_w))

print(f"PASS: {checks:,} exact actual sector cut-and-fill checks")
