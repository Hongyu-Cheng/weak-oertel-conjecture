from fractions import Fraction as F
from random import Random

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def clip(poly, a, b, h):
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        sp, sq = a*p[0]+b*p[1]-h, a*q[0]+b*q[1]-h
        if sp >= 0:
            out.append(p)
        if (sp < 0 < sq) or (sq < 0 < sp):
            f = sp/(sp-sq)
            out.append(tuple(p[j]+f*(q[j]-p[j]) for j in range(2)))
    return out

def area(poly):
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(poly,poly[1:]+poly[:1])))/2 if poly else F(0)

def hull(points):
    points = sorted(set(points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    def half(ps):
        out=[]
        for p in ps:
            while len(out)>1 and cross(out[-2],out[-1],p)<=0:
                out.pop()
            out.append(p)
        return out
    return half(points)[:-1]+half(points[::-1])[:-1]

def section(poly, s):
    vals=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        if p[0]==q[0]:
            if s==p[0]: vals.extend((p[1],q[1]))
        elif min(p[0],q[0])<=s<=max(p[0],q[0]):
            vals.append(p[1]+(s-p[0])*(q[1]-p[1])/(q[0]-p[0]))
    return min(vals),max(vals)

def roof(poly,h):
    knots=sorted(set(p[0] for p in poly))
    return sum((b-a)*(2*h+section(poly,a)[1]+section(poly,b)[1])/2
               for a,b in zip(knots,knots[1:]))

T=[(F(1),F(1)),(F(-2),F(1)),(F(1),F(-2))]
polys=[T]
for ax,ay in [(1,0),(0,1),(1,1),(1,-1),(2,1),(-1,2)]:
    for cut in [F(-3,2),F(-1),F(-1,3),F(0),F(1,3),F(2,3)]:
        p=clip(T,F(ax),F(ay),cut)
        if area(p)>0: polys.append(p)
for c in [F(-2),F(-1),F(-3,4),F(-1,2),F(0),F(1,3),F(2)]:
    # The inequality is s=x-c*t=(1+c)*x+c*y.
    for low,high in [(F(-1),F(1)),(F(-1,2),F(1,4)),(F(0),F(1,2))]:
        p=clip(clip(T,1+c,c,low),-1-c,-c,-high)
        if area(p)>0: polys.append(p)

for p in polys:
    b=area(p)
    for c in [F(-3),F(-4,3),F(-1),F(-3,4),F(-1,2),F(0),F(1,3),F(2)]:
        st=[((1+c)*x+c*y,-x-y) for x,y in p]
        check(area(st)==b)
        for h in [F(5,2),F(3),F(13,3),F(10)]:
            H=h+1
            R=roof(st,h)
            check(3*R>=H*b)
            z=R/H
            check(z>=3 or 2*b<=6*z-z*z)
            # Actual Minkowski sum with an endpoint segment; q is cap area /4.
            lo=F(-5,4)
            swept=hull([(s,t+v) for s,t in st for v in [lo,h]])
            check(area(clip(swept,F(0),F(1),F(0)))==R)

# Exact strip equalities for all interior shear slopes.
for c in [F(-1),F(-3,4),F(-1,2),F(-1,4),F(0)]:
    for v in [F(0),F(1,4),F(1),F(2),F(11,4)]:
        s0=1+2*c
        left=s0-(1+c)*(3-v)
        right=s0-c*(3-v)
        p=clip(clip(T,1+c,c,left),-1-c,-c,-right)
        check(area(p)==(9-v*v)/2)
        st=[((1+c)*x+c*y,-x-y) for x,y in p]
        for h in [F(5,2),F(4)]:
            check(roof(st,h)==(h+1)*(3-v))

# Exact distribution formula and dominance for outward segment slopes.
for c in [F(1,8),F(1,3),F(1),F(7,2)]:
    m=1+c
    for H in [F(7,2),F(4),F(16,3),F(9)]:
        for scale in [F(1),F(9,8),F(2),F(7)]:
            lam=H*m*scale/3
            Fc=F(9,2)-m*H*H/(2*lam*lam)-c*m*(H-3)**2/(2*(lam-m)**2)
            F0=F(9,2)-H*H/(2*lam*lam)
            check(0<=Fc<=F0<=F(9,2))

roof_checks=checks

# Actual polygon audit of the additive far-tail reserve. This supplements,
# and does not replace, the section-boundary proof in the companion note.
rng=Random(1713)
for _ in range(900):
    A=hull([(F(rng.randrange(-12,13),4),F(rng.randrange(-12,25),4))
            for _ in range(7)])
    lo=min(A,key=lambda p:p[1])
    hi=max(A,key=lambda p:p[1])
    l,h=lo[1],hi[1]
    if not(l < -1 and h > 2):
        continue
    c=(hi[0]-lo[0])/(h-l)
    for pb in rng.sample(polys,min(5,len(polys))):
        B=[(x,-x-y) for x,y in pb]
        total=hull([(x+u,t+v) for x,t in A for u,v in B])
        captured=area(clip(total,F(0),F(1),F(0)))
        R=roof([(x-c*t,t) for x,t in B],h)
        far_tail=area(clip(A,F(0),F(1),F(2)))
        check(captured>=R+far_tail)

print('PASS:',checks,'exact checks;',roof_checks,'roof-capacity,',
      checks-roof_checks,'additive-reserve polygon checks')
