from fractions import Fraction as F
from itertools import combinations
import sympy as s

checks = 0
def ck(x):
    global checks
    assert x
    checks += 1

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lo, hi = [], []
    for p in points:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:
            lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi)>1 and cross(hi[-2],hi[-1],p)<=0:
            hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

def area(poly):
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(poly,poly[1:]+poly[:1])))/2 if poly else F(0)

def clip(poly,v,t):
    # The retained closed trace is v.x <= t. Its area equals the strict trace.
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=t-v[0]*p[0]-v[1]*p[1]
        fq=t-v[0]*q[0]-v[1]*q[1]
        if fp>=0:
            out.append(p)
        if (fp<0<fq) or (fq<0<fp):
            lam=fp/(fp-fq)
            out.append(tuple(p[j]+lam*(q[j]-p[j]) for j in (0,1)))
    return hull(out)

normals=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]
T=hull([(F(1),F(1)),(F(1),F(-2)),(F(-2),F(1))])
for scale in [F(1),F(3,2),F(2),F(3)]:
    for shift in [(F(0),F(0)),(F(1,3),F(-1,5)),(F(-1,2),F(-1,2))]:
        A=hull([(-scale*p[0]+shift[0],-scale*p[1]+shift[1]) for p in T])
        for br in [F(1,3),F(2,3),F(1)]:
            B=[(br*p[0],br*p[1]) for p in T]
            b=area(B)
            K=hull([((p[0]+q[0])/2,(p[1]+q[1])/2) for p in A for q in B])
            images={}
            for i in range(3):
                R=A
                for j in range(3):
                    if j!=i:
                        R=clip(R,normals[j],F(-1))
                ri=area(R)
                if ri==0:
                    continue
                Z=hull([((p[0]+q[0])/2,(p[1]+q[1])/2) for p in R for q in B])
                images[i]=Z
                for p in Z:
                    for j in range(3):
                        if j!=i:
                            ck(normals[j][0]*p[0]+normals[j][1]*p[1]<=0)
                slack=4*area(Z)-ri-b
                ck(slack>=0 and slack*slack>=4*ri*b)
            for i,j in combinations(images,2):
                other=next(k for k in range(3) if k not in (i,j))
                missed=clip(K,normals[other],F(0))
                ck(area(missed)>=area(images[i])+area(images[j]))
                overlap=images[i]
                for k in range(3):
                    if k!=j:
                        overlap=clip(overlap,normals[k],F(0))
                ck(area(overlap)==0)

r=s.symbols('r', positive=True)
c=s.Rational(367,192)
A=c-s.Rational(4,3)*r
f=(50-47*r)/(32*A)+18*s.sqrt(r/(32*A))
derivative=-s.Rational(1483,64)+9*c*s.sqrt(32)*s.sqrt(A/r)
ap=s.symbols('ap',positive=True)
fp=(50-47*r)/(32*ap)+18*s.sqrt(r/(32*ap))
total_derivative=s.diff(fp,r)-s.Rational(4,3)*s.diff(fp,ap)
cp=ap+s.Rational(4,3)*r
expected=s.Rational(200,3)-47*cp+9*cp*s.sqrt(32)*s.sqrt(ap/r)
ck(s.simplify(32*ap*ap*total_derivative-expected)==0)
ck(s.Rational(200,3)-47*c==-s.Rational(1483,64))
ck(s.simplify(f.subs(r,s.Rational(1,4))-
              (s.Rational(153,202)+18/s.sqrt(202)))==0)
ck(18**2*202==65448 and 251**2==63001 and 65448>63001)
# The scalar comparison (33) from the two geometric profile bounds.
z,y,root=s.symbols('z y root')
upper=s.Rational(5,9)+(s.Rational(1,18)*(10*r-7)-y)*z
lower=s.Rational(1,2)+(2*r+y-1)*z/4+root/2
ck(s.expand(36*(upper-lower)-(2-(5-2*r+45*y)*z-18*root))==0)
print(f'PASS: {checks} exact checks')
