"""Exact finite polynomial certificates and actual rational geometry checks."""
from fractions import Fraction as F
import random
import sympy as sp

checks=0
def check(value):
    global checks
    assert value
    checks+=1
z,u=sp.symbols('z u');C=2+z*z;x=2-z*z
check(F(279,32)-F(7379,2500)**2==F(85093,12500000))
check(F(17,25)-F(100,1279)>F(3,5))
Pminus=z**4-2*z**3+4*z*z-8*z+4
Pplus=-z**4+4*z**3-4*z*z+4*z-4
check(Pminus.subs(z,sp.Rational(39,50))==-sp.Rational(2408459,6250000))
check(Pplus.subs(z,sp.Rational(61,50))==-sp.Rational(159641,6250000))
T=[sp.Rational(10,7),sp.Rational(5,3)]
mins=[]
for aa,bb,L in [(sp.Rational(39,50),sp.Integer(1),4*z-z*z-2),
                (sp.Integer(1),sp.Rational(61,50),z*z-2*z+2)]:
    polys=[C+2*z*(z*t*t-C*t) for t in T]
    polys += [C+x*(t1*t1-C*t1)+L*(z*t2*t2-C*t2) for t1 in T for t2 in T]
    this=[]
    for P in polys:
        poly=sp.Poly(sp.expand(-P.subs(z,aa+(bb-aa)*u)),u);n=poly.degree()
        B=[sp.factor(sum(poly.nth(k)*sp.binomial(j,k)/sp.binomial(n,k) for k in range(j+1))) for j in range(n+1)]
        check(all(b>sp.Rational(1,2) for b in B))
        check(sp.expand(sum(B[j]*sp.binomial(n,j)*u**j*(1-u)**(n-j) for j in range(n+1))-poly.as_expr())==0)
        this.append(min(B))
    mins.append(this)
expected=[
    [sp.Rational(441821,612500),sp.Rational(4959,6250),sp.Rational(6347669,7656250),sp.Rational(3197731,3750000),sp.Rational(368112407,551250000),sp.Rational(972313,1406250)],
    [sp.Rational(73,49),sp.Rational(13,9),sp.Rational(386711,612500),sp.Rational(308439211,551250000),sp.Rational(374439739,551250000),sp.Rational(136669,225000)],
]
check(mins==expected)

def det(p,q):return p[0]*q[1]-p[1]*q[0]
def sub(p,q):return(p[0]-q[0],p[1]-q[1])
def dot(p,q):return p[0]*q[0]+p[1]*q[1]
def area(P):return abs(sum(det(p,q) for p,q in zip(P,P[1:]+P[:1])))/2
def hull(P):
    P=sorted(set(P));L=[];U=[]
    for p in P:
        while len(L)>1 and det(sub(L[-1],L[-2]),sub(p,L[-1]))<=0:L.pop()
        L.append(p)
    for p in reversed(P):
        while len(U)>1 and det(sub(U[-1],U[-2]),sub(p,U[-1]))<=0:U.pop()
        U.append(p)
    return L[:-1]+U[:-1]
def clip(P,n):
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        vp,vq=dot(p,n),dot(q,n)
        if vp>=0:out.append(p)
        if vp*vq<0:
            a=vp/(vp-vq);out.append((p[0]+a*(q[0]-p[0]),p[1]+a*(q[1]-p[1])))
    return out
e=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
normals=[(1,0),(0,1),(-1,-1)]
def sectors(P):
    return [clip(clip(P,(-a[1],a[0])),(b[1],-b[0])) for a,b in zip(e,e[1:]+e[:1])]
def raypoint(P,r):
    vals=[]
    for a,b in zip(P,P[1:]+P[:1]):
        q=sub(b,a);den=det(r,q)
        if den:
            t=det(a,q)/den;s=det(a,r)/den
            if t>0 and 0<=s<=1:vals.append(t)
    assert vals and len(set(vals))==1
    return(vals[0]*r[0],vals[0]*r[1])
def intersect(n,c,m,d):
    D=det(n,m)
    if not D:return None
    return((c*m[1]-n[1]*d)/D,(n[0]*d-c*m[0])/D)

random.seed(840511);bodies=0
for _ in range(15000):
    K=hull([(F(random.randrange(-20,21)),F(random.randrange(-20,21))) for __ in range(random.randrange(4,13))])
    if len(K)<3 or any(det(sub(q,p),(-p[0],-p[1]))<=0 for p,q in zip(K,K[1:]+K[:1])):continue
    k=area(K);caps=[area(clip(K,n)) for n in normals]
    if max(caps)>=k/2:continue
    P=[raypoint(K,r) for r in e]
    A,B,t,a,b,r=P[0][0],P[1][1],P[2][1],-P[3][0],-P[4][1],P[5][0]
    lines=[((1/A,1/B),F(1)),((-F(1),a/t-1),a),((b/r-1,-F(1)),b)]
    vertices=[intersect(*lines[i],*lines[(i+1)%3]) for i in range(3)]
    check(all(v is not None for v in vertices))
    check(all(dot(v,n)<=c for v in vertices for n,c in lines))
    Tpoly=hull(vertices);check(len(Tpoly)==3)
    check([raypoint(Tpoly,r) for r in e]==P)
    SK=sectors(K);ST=sectors(Tpoly)
    for i in range(6):
        if i%2==0:
            check(area(ST[i])==det(P[i],P[(i+1)%6])/2)
            check(area(SK[i])>=area(ST[i]))
        else:
            check(all(dot(v,n)<=c for v in SK[i] for n,c in lines))
            check(area(SK[i])<=area(ST[i]))
    check(all(sum(dot(v,n)>0 for n in normals)==1 for v in Tpoly))
    bodies+=1
check(bodies>=50)
print(f'PASS: {checks} exact checks, including {bodies} actual half-cap sector-comparison triangles')
