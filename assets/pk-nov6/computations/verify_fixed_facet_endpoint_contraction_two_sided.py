from fractions import Fraction as F
from itertools import product
import sympy as s
checks=0
def ck(v):
    global checks
    assert v
    checks+=1

# A=2T, K=3T, B=T/2 is an actual compatible equal-support-cap MENU.
# Its menu is not asserted to be the globally critical menu.
t,u,v,px,py,qx,qy=s.symbols('t u v px py qx qy', real=True)
yvel=s.Matrix([s.Rational(5,16)*(u*px+v*qx),s.Rational(5,16)*(u*py+v*qy)])
for normal in [s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([-1,-1])]:
    p=normal.dot(s.Matrix([px,py]));q=normal.dot(s.Matrix([qx,qy]));dy=normal.dot(yvel)
    ah=4*(1-u*t)+1-v*t+u*t*p+v*t*q-2*t*dy
    kh=6-t*dy
    menu=(ah*ah+kh*kh)/2
    ck(s.simplify(menu.subs(t,0)-s.Rational(61,2))==0)
    ck(s.simplify(s.diff(menu,t).subs(t,0)+20*u+5*v)==0)
    # Frozen source threshold and A-only contraction loss.
    ownA=(5-4*t+t*p)**2/2
    ck(s.simplify(-s.diff(ownA,t).subs(t,0)-(20-5*p))==0)

# Exact actual polygon check of removed-shell coverage and individual derivative.
def clip(poly,normal,b):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=sum(normal[j]*p[j] for j in (0,1))-b
        fq=sum(normal[j]*q[j] for j in (0,1))-b
        if fp>=0:out.append(p)
        if (fp<0<fq) or (fq<0<fp):
            a=fp/(fp-fq)
            out.append(tuple(p[j]+a*(q[j]-p[j]) for j in (0,1)))
    return out

def area(poly):
    if not poly:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2

A=[(F(-2),F(-2)),(F(4),F(-2)),(F(-2),F(4))]
normals=[(1,0),(0,1),(-1,-1)]
for pp,tt in product([(F(0),F(0)),(F(1),F(0)),(F(-2),F(-2)),(F(-1),F(2))],[F(1,100),F(1,20),F(1,10)]):
    At=[tuple(pp[j]+(1-tt)*(x[j]-pp[j]) for j in (0,1)) for x in A]
    losses=[]
    for nn in normals:
        dot=sum(nn[j]*pp[j] for j in (0,1))
        old=area(clip(A,nn,F(-1)))
        new=area(clip(At,nn,F(-1)))
        ck(old==F(25,2))
        ck(new==(5-4*tt+tt*dot)**2/2)
        losses.append(old-new)
    ck(sum(losses)>=area(A)-area(At))

# Missing-corner pointwise load, every Boolean pattern, many positive weights.
for weights in product([F(1),F(2),F(7,2)],repeat=3):
    for empty in product([False,True],repeat=3):
        candidates=[weights[i] for i in range(3) if not empty[i]]
        candidates += [weights[i]+weights[j] for i in range(3) for j in range(i)]
        tau=min(candidates)
        for bits in product([0,1],repeat=3):
            n=sum(bits)
            if not n:continue
            if n==1 and any(bits[i] and empty[i] for i in range(3)):continue
            ck(sum(weights[i]*bits[i] for i in range(3))>=tau)
    lo=min(weights);hi=max(weights)
    if hi/lo<=F(7,4):ck(lo/sum(weights)>=F(2,9))

# Exact algebra for the tied-B threshold, retaining both active sources.
a,k,b,Q,L,J=s.symbols('a k b Q L J', positive=True)
r=Q/(a+k+b)
expr=(L-2*r*a)+(a/(a+k))*(J-2*r*b)
ck(s.simplify(expr-((a+k)*L+a*J-2*a*Q)/(a+k))==0)
print(f'PASS: {checks} exact checks')
