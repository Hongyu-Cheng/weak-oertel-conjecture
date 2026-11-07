"""Independent exact polygon/slice checks, not a replacement for global proof."""
from fractions import Fraction as F

ncheck=0
def check(p):
    global ncheck
    assert p
    ncheck+=1

T=[(F(2),F(-1)),(F(-1),F(2)),(F(-1),F(-1))]
def area(poly):
    if len(poly)<3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2
V=area(T)
check(V==F(9,2))

def clip(poly,u,b):
    out=[]
    dot=lambda p:u[0]*p[0]+u[1]*p[1]-b
    for p,q in zip(poly,poly[1:]+poly[:1]):
        dp,dq=dot(p),dot(q)
        if dp>=0:
            out.append(p)
        if (dp<0<dq) or (dq<0<dp):
            s=-dp/(dq-dp)
            out.append((p[0]+s*(q[0]-p[0]),p[1]+s*(q[1]-p[1])))
    return out

def covector(R):
    return ((R+2)/3,(2*R-2)/3)
def Ftail(R,q):
    return area(clip(T,covector(R),q))/V

for k in range(1,73):
    R=1+F(k-1,24)
    for j in range(97):
        q=F(j,16)
        check(Ftail(R,q)+Ftail(R,-q)>=F(8,9))
    if 1<R<4:
        D=(R+2)*(4-R)
        for q in [F(0),F(1,8),F(1,4)]:
            if q>=R-2:
                check(Ftail(R,q)==(2-q)**2/D)

def frustum_cap(R,beta,eps,t0):
    u=covector(R)
    vals=[u[0]*p[0]+u[1]*p[1] for p in T]
    knots={F(-1),F(1)}
    for v in vals:
        denominator=eps*v+beta
        if denominator:
            t=(beta*t0-v)/denominator
            if -1<t<1:
                knots.add(t)
    knots=sorted(knots)
    def section(t):
        r=1+eps*t
        triangle=[(r*x,r*y) for x,y in T]
        return area(clip(triangle,u,-beta*(t-t0)))
    mass=F(0)
    for lo,hi in zip(knots,knots[1:]):
        # On every vertex-incidence cell, actual polygon vertices are affine
        # in t and area is quadratic, so this Simpson rule is exact.
        mass+=(hi-lo)*(section(lo)+4*section((lo+hi)/2)+section(hi))/6
    return mass/(2*V*(1+eps*eps/3))

delta=F(1,12*1287**2)
for R in [1+F(j,8) for j in range(25)]:
    for beta in [F(0),F(1,8),F(1,4),F(1,2),F(1),F(2),F(4),F(72),F(73),F(1000)]:
        product=frustum_cap(R,beta,F(0),F(0))
        check(product>=F(4,9))
        if R-1>=F(1,4) or beta>=F(1,4):
            check(product>=F(4,9)+delta)
        for eps in [F(1,10**9),F(1,10**12)]:
            for signed_beta in {beta,-beta}:
                actual=frustum_cap(R,signed_beta,eps,eps/3)
                check(actual>=F(4,9))
                check(abs(actual-product)<=8*eps)
                check((actual==F(4,9))==(R==1 and beta==0))
                if R-1<=F(1,4) and beta<=F(1,4):
                    check(actual==(4+beta*beta/3)/(9-(R-1)**2))

for eps in [F(1,10**9),F(1,10**12)]:
    for h in [F(-1,10**12),F(0),F(1,10**12)]:
        t0=eps/3+h
        beta=2*h/(F(1,3)+t0*t0)
        expected=F(4,9)-4*h*h/(9*(1+eps*eps/3)*(F(1,3)+t0*t0))
        check(frustum_cap(F(1),beta,eps,t0)==expected)

for d in range(1,6):
    check(F(d,d+1)**d>F(2,5))
print(f'PASS: {ncheck} exact checks')
