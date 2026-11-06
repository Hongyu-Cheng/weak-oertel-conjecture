"""Exact actual-polygon checks; no criticality or Lorentz failure inferred."""
from fractions import Fraction as F

def cross(p,q): return p[0]*q[1]-p[1]*q[0]
def sub(p,q): return (p[0]-q[0],p[1]-q[1])
def val(p,n): return p[0]*n[0]+p[1]*n[1]
def area(P): return abs(sum(cross(p,q) for p,q in zip(P,P[1:]+P[:1])))/2
def clip(P,n):
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        vp,vq=val(p,n),val(q,n)
        if vp>=0: out.append(p)
        if (vp<0<vq) or (vq<0<vp):
            t=vp/(vp-vq)
            out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return out
P=[(F(0),F(1)),(-F(63,100),F(63,50)),(-F(1),F(1)),
   (F(0),-F(11,10)),(F(61,110),-F(61,55)),(F(11,10),-F(11,10))]
checks=0
def check(q):
    global checks
    assert q
    checks+=1
for j in range(6):
    check(cross(sub(P[(j+1)%6],P[j]),sub(P[(j+2)%6],P[(j+1)%6]))>0)
    check(cross(sub(P[(j+1)%6],P[j]),sub((F(0),F(0)),P[j]))>0)
check(area(P)==F(117,50))
q=[area(clip(P,n)) for n in [(1,0),(0,1),(-1,-1)]]
check(q==[F(29,25),F(2423,2100),F(29,25)])
for a in q: check(2*a<area(P))
qs=sorted(q)
check(qs[0]+qs[1]+qs[2]/4-area(P)==F(277,1050))
e=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
W=[]
for j in range(6):
    # cross(e_j,x)>=0 and cross(x,e_(j+1))>=0.
    u,v=e[j],e[(j+1)%6]
    W.append(area(clip(clip(P,(-u[1],u[0])),(v[1],-v[0]))))
check(W==[F(11,42),F(63,100),F(11,42),F(121,420),F(61,100),F(121,420)])
check(sum(W)==area(P))
check(F(63,100)>F(1,2))
check(F(61,100)>F(121,200))
check(F(63,100)<11)
for point in [(F(11,21),F(0)),(-F(11,21),F(0))]:
    found=False
    for p,r in zip(P,P[1:]+P[:1]):
        if cross(sub(point,p),sub(r,p))==0:
            if min(p[0],r[0])<=point[0]<=max(p[0],r[0]) and min(p[1],r[1])<=point[1]<=max(p[1],r[1]):
                found=True
    check(found)
print(f'PASS: {checks} exact actual-polygon checks')
