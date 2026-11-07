"""Exact rational geometry and polynomial checks for the coordinated path."""
from fractions import Fraction as F
from itertools import product

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def area(P):
    return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[i][1]*P[(i+1)%len(P)][0] for i in range(len(P)))/2)
def clip(P,u):
    out=[]
    for a,b in zip(P,P[1:]+P[:1]):
        va=sum(x*y for x,y in zip(u,a));vb=sum(x*y for x,y in zip(u,b))
        if va>=0:out.append(a)
        if (va<0<vb) or (vb<0<va):
            lam=va/(va-vb)
            out.append(tuple(a[j]+lam*(b[j]-a[j]) for j in range(2)))
    return out
def hull(P):
    P=sorted(set(P))
    if len(P)<=1:return P
    lo=[];hi=[]
    for p in P:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in P[::-1]:
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
def fibers(t,L=F(1)):
    a=F(1,3)
    A=[(-a+t,-a-t),(2*a,-a+t),(-a-t,2*a)]
    B=[(-a-t,-a+t),(2*a,-a-t),(-a+t,2*a)]
    D=[(-a-t,a/2+t/2),(-a,-a),(a/2+t/2,-a-t),
       (2*a,-a),(a/2+t/2,a/2+t/2),(-a,2*a)]
    return [[(L*x,L*y) for x,y in P] for P in (A,D,B)]
def M(t):return F(3,2)*(1+t+2*t*t)
def D(t):return (6+7*t+12*t*t-9*t**3)/(9*(1-t*t))
normals=[(-1,-1),(1,0),(0,1)]
checks=0
for t in [F(k,1000) for k in range(1,334)]:
    A,C,B=fibers(t)
    avgs=[((a[0]+b[0])/2,(a[1]+b[1])/2) for a,b in product(A,B)]
    assert set(hull(avgs))==set(C)
    assert all(cross(C[i],C[(i+1)%6],C[(i+2)%6])>0 for i in range(6))
    expected_values={F(0),t,(1+3*t*t)/4,(1+t)*(1+3*t)/4,(1+t)/2,(1-t)*(1+3*t)/4}
    actual_values={cross(C[i],C[(i+1)%6],p) for i in range(6) for p in avgs}
    assert actual_values==expected_values
    w=(1+3*t*t)/2;W=(1+3*t)/2
    assert area(A)==area(B)==w and area(C)==W
    assert sum(area(P) for P in (A,C,B))==M(t)
    caps=[]
    for u in normals:
        pieces=[area(clip(P,u)) for P in (A,C,B)]
        assert pieces[0]==pieces[2]==w*4/(9*(1-t*t))
        assert pieces[1]==(1+3*t)*(2+3*t)/(9*(1+t))
        caps.append(sum(pieces))
    assert caps==[D(t)]*3
    checks+=1

# Polynomial identity proving the all-parameter derivative formula.
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)
def sub(a,b):
    return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def der(a):return [i*a[i] for i in range(1,len(a))]
N=[F(12),F(14),F(24),F(-18)]
den=mul([F(1),F(0),F(-1)],[F(1),F(1),F(2)])
P=[F(1),F(12),F(-4),F(44),F(45),F(48),F(-18)]
assert sub(mul(der(N),den),mul(N,der(den)))==[2*x for x in P]
# The printed positive decomposition is an exact coefficient identity.
positive=[F(1),F(12),F(-4),F(44),F(45),F(48),F(-18)]
assert positive==P
checks+=1

t0=F(1,10);t=F(9,100);L=F(1007,1000)
M0=M(t0);D0=D(t0)
assert M0==F(42,25) and D0==F(6811,8910)
assert M0/M(t)<L*L<D0/D(t)
A,C,B=fibers(t,L)
avgs=[((a[0]+b[0])/2,(a[1]+b[1])/2) for a,b in product(A,B)]
assert set(hull(avgs))==set(C)
mass=sum(area(P) for P in (A,C,B))
caps=[sum(area(clip(P,u)) for P in (A,C,B)) for u in normals]
assert mass==F(16826115057,10**10)
assert mass-M0==F(26115057,10**10)>0
assert caps==[F(2271685752437,2975700000000)]*3
assert all(D0-c==F(892421526211,883782900000000)>0 for c in caps)
# Every retained cap has an actual strict witness in the middle.
K=[(-F(1,3),-F(1,3)),(F(2,3),-F(1,3)),(-F(1,3),F(2,3))]
for i,u in enumerate(normals):
    p=tuple(L*x for x in K[i])
    assert p in C
    assert sum(u[j]*p[j] for j in range(2))>0
    assert all(sum(v[j]*p[j] for j in range(2))<0 for k,v in enumerate(normals) if k!=i)
checks+=1
# Arbitrarily small rational unrotations, using the midpoint squared scale.
for n in range(2,20):
    t=t0-F(1,10**n)
    q=(M0/M(t)+D0/D(t))/2
    assert q*M(t)>M0 and q*D(t)<D0
    checks+=1
print("PASS:",checks,"exact hull/area/cap/path checks and the polynomial derivative identity.")
print("Rational witness mass gain:",mass-M0)
print("Rational witness common cap drop:",D0-caps[0])
