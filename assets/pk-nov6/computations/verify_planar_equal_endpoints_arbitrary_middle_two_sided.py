from fractions import Fraction as F
from itertools import product
import sympy as s
checks=0
def ck(v):
    global checks
    assert v
    checks+=1
r=s.symbols('r',positive=True)
W=2*r/(9*(2*r-1));Qw=4*r/9+W
ck(s.simplify(s.diff(Qw,r)-(s.Rational(4,9)-2/(9*(2*r-1)**2)))==0)
ck(Qw.subs(r,s.Rational(33,20))==s.Rational(308,345))
ck(33*23**2-132**2==33)
ck(720>625)
ck(s.Rational(308,1383)-s.Rational(2,9)==s.Rational(2,4149))
ck(s.Rational(308,345)/(s.Rational(4,9))==s.Rational(231,115))
ck(s.Rational(308,345)/(2+s.Rational(231,115))==s.Rational(308,1383))
beta=s.symbols('beta',positive=True)
ck(s.simplify(s.Rational(308,345)/(1+beta+s.Rational(231,115))-308/(3*(346+115*beta)))==0)
ck((308/(3*(346+115*beta))).subs(beta,s.Rational(116,115))==s.Rational(2,9))


def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
    points=sorted(set(points));lo=[];hi=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
def area(poly):
    if len(poly)<3:return F(0)
    return sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1]))/2

def centroid(poly):
    terms=[p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])]
    aa=sum(terms)/2
    return tuple(sum((p[j]+q[j])*tt for p,q,tt in zip(poly,poly[1:]+poly[:1],terms))/(6*aa) for j in (0,1))
def dot(u,x):return u[0]*x[0]+u[1]*x[1]
def width(poly,u):return max(dot(u,x) for x in poly)-min(dot(u,x) for x in poly)
def clip(poly,u,b):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=dot(u,p)-b;fq=dot(u,q)-b
        if fp>=0:out.append(p)
        if (fp<0<fq) or (fq<0<fp):
            tt=fp/(fp-fq)
            out.append(tuple(p[j]+tt*(q[j]-p[j]) for j in (0,1)))
    return out

def normalized(poly):
    poly=hull([tuple(F(x) for x in p) for p in poly]);aa=area(poly)
    # A genuine rational affine change, tracked exactly, makes area 1/2.
    return [(x/(2*aa),y) for x,y in poly]

polys=[normalized(p) for p in [
    [(0,0),(1,0),(0,1)],
    [(-1,-1),(2,-1),(-1,2)],
    [(0,0),(3,0),(3,1),(0,1)],
    [(-2,0),(0,-1),(3,0),(1,2)],
    [(-1,-1),(2,-1),(3,0),(1,3),(-2,1)],
    [(0,0),(4,0),(3,1),(1,1)],
]]
for A,B in product(polys,repeat=2):
    aa=area(A);ck(aa==area(B)==F(1,2))
    M=hull([tuple((p[j]+q[j])/2 for j in (0,1)) for p in A for q in B])
    mm=area(M);rr=mm/aa;gm=centroid(M)
    ck(rr>=1)
    # A genuine arbitrary superbody, not merely a homothet of M.
    K=hull(M+[(gm[0]+F(1,3),gm[1]+F(2,5)),(gm[0]-F(1,5),gm[1]-F(1,7))])
    kk=area(K);ck(kk>=mm)
    for u in [(1,0),(0,1),(1,1),(2,-1),(3,2)]:
        wa=width(A,u);wb=width(B,u);rat=wa/wb
        ck(rat+1/rat<=4*rr-2)
        wdir=(wa+wb)**2/(9*(wa*wa+wb*wb))
        wvol=2*rr/(9*(2*rr-1))
        ck(wdir>=wvol)
        for tt in [F(-2),F(-1,5),F(0),F(1,7),F(3)]:
            level=dot(u,gm)
            pair=area(clip(A,u,level+tt))+area(clip(B,u,level-tt))
            ck(pair>=aa*wdir)
            # Squared exact test of pair/a >= F(r), with positive left side.
            lhs=pair/aa+20*rr/9
            ck(lhs>=0 and lhs*lhs>=F(80,9)*rr)
            own=area(clip(K,u,level))
            ck(own+pair>=F(308,345)*aa)
    sratio=kk/aa
    lb=max(F(4,9)*sratio,F(308,345))/(sratio+2)
    ck(lb>=F(308,1383))

# Original denominator is retained for all unequal-area ratio checks.
for bb in [F(1),F(116,115),F(6,5),F(2),F(9,2)]:
    for ks in [F(1),F(3,2),F(231,115),F(3),F(10)]:
        val=max(F(4,9)*ks,F(308,345))/(ks+1+bb)
        ck(val>=F(308)/(3*(346+115*bb)))
print(f'PASS: {checks} exact checks')

# Direct unequal-area Section 6: exact moving-split algebra.
be=s.symbols('be',positive=True)
rs=(19*be+14)/20
ww=4*rs/9+2*rs/(9*(2*rs-1))-4*(1+be)/9
ck(s.factor(ww-(46-23*be-19*be**2)/(45*(19*be+4)))==0)
poly=-2781*be**2+3858*be-961
ck(s.expand(900*be*(19*be+14)-(141*be+31)**2-poly)==0)
ck(poly.subs(be,1)==116)
ck(poly.subs(be,s.Rational(21,20))==s.Rational(9539,400))
ck((46-23*be-19*be**2).subs(be,s.Rational(21,20))==s.Rational(361,400))
ck(s.Rational(132,5)+5-29*s.Rational(21,20)==s.Rational(19,20))
for bex in [F(101,100),F(21,20)]:
    for A,B0 in product(polys,repeat=2):
        B=[(bex*x,y) for x,y in B0]
        aa=area(A);bb=area(B);ck(bb/aa==bex)
        M=hull([tuple((p[j]+q[j])/2 for j in (0,1)) for p in A for q in B])
        mm=area(M);rr=mm/aa;gm=centroid(M)
        for u in [(1,0),(0,1),(1,1),(2,-1)]:
            for tt in [F(-1),F(0),F(2,7)]:
                level=dot(u,gm)
                pair=area(clip(A,u,level+tt))+area(clip(B,u,level-tt))
                ck(pair/aa>=2*rr/(9*(2*rr-1)))
                lhs=pair/aa-1+bex+20*rr/9
                ck(lhs>0 and lhs*lhs>=F(80,9)*bex*rr)
                raw=area(clip(M,u,level))+pair
                ck(raw>F(4,9)*(aa+bb))
print(f'PASS WITH UNEQUAL-AREA SECTION 6: {checks} exact checks')
