"""Exact rational certificate against the maximal symmetric-overlap selector.

No floating-point arithmetic, numerical optimization, or external dependencies.
"""
from fractions import Fraction as F
from itertools import combinations

K=[tuple(map(F,p)) for p in [(-4,-3),(4,4),(2,3),(-3,0)]]
c=(F(-182,233),F(123,233))
expected_pairs=[('U0','L3'),('U1','L3'),('U1','U2'),('L0','U2'),
                ('L0','U3'),('L1','U3'),('L1','L2'),('U0','L2')]

def area(P):
    return sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(P,P[1:]+P[:1]))/2
def cross(p,q,r):
    return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
def ev(a): return a[0]+a[1]*c[0]+a[2]*c[1]
def mul(a,b):
    return [a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[2]*b[0],
            a[1]*b[1],a[1]*b[2]+a[2]*b[1],a[2]*b[2]]

assert area(K)==9
assert all(cross(K[i-1],K[i],K[(i+1)%4])>0 for i in range(4))
cons={}
for i,(p,q) in enumerate(zip(K,K[1:]+K[:1])):
    n=(-(q[1]-p[1]),q[0]-p[0]);b=n[0]*p[0]+n[1]*p[1]
    # Each tuple is (normal, affine RHS in (s,t), inequality sign).
    cons['L'+str(i)]=(n,(b,F(0),F(0)),1)
    cons['U'+str(i)]=(n,(-b,2*n[0],2*n[1]),-1)
    assert n[0]*c[0]+n[1]*c[1]>b

def intersection(a,b):
    n,r,_=cons[a];m,s,_=cons[b]
    det=n[0]*m[1]-n[1]*m[0]
    if not det:return None
    x=tuple((m[1]*u-n[1]*v)/det for u,v in zip(r,s))
    y=tuple((n[0]*v-m[0]*u)/det for u,v in zip(r,s))
    return x,y

valid={}
for a,b in combinations(cons,2):
    xy=intersection(a,b)
    if xy is None:continue
    x,y=xy;v=ev(x),ev(y)
    slacks={name:sign*(n[0]*v[0]+n[1]*v[1]-ev(rhs))
            for name,(n,rhs,sign) in cons.items()}
    if min(slacks.values())>=0:
        assert {name for name,s in slacks.items() if s==0}=={a,b}
        valid[frozenset((a,b))]=(x,y,slacks)
assert set(valid)=={frozenset(p) for p in expected_pairs}
assert min(s for _,_,sl in valid.values() for s in sl.values() if s>0)==F(12,233)

vertices=[valid[frozenset(p)][:2] for p in expected_pairs]
numeric_vertices=[(ev(x),ev(y)) for x,y in vertices]
assert all(cross(numeric_vertices[i-1],numeric_vertices[i],numeric_vertices[(i+1)%8])>0 for i in range(8))

# Strict inactive constraints establish this active polygon on an open neighborhood.
# Its shoelace area is therefore the following exact local quadratic.
poly=[F(0)]*6
for (px,py),(qx,qy) in zip(vertices,vertices[1:]+vertices[:1]):
    for j,(a,b) in enumerate(zip(mul(px,qy),mul(py,qx))):poly[j]+=(a-b)/2
expected=[F(v,935) for v in [-12816,-26292,31544,-9516,21644,-13864]]
assert poly==expected
k,lx,ly,a,b,d=poly
assert lx+2*a*c[0]+b*c[1]==0
assert ly+b*c[0]+2*d*c[1]==0
assert a<0 and 4*a*d-b*b==F(3728,55)>0
R=k+lx*c[0]+ly*c[1]+a*c[0]**2+b*c[0]*c[1]+d*c[1]**2
assert R==F(1440,233)==area(numeric_vertices)

# The through-c halfspace 3x-y>=-669/233 cuts this exact quadrilateral.
t=3*c[0]-c[1];assert t==F(-669,233)
cap=[(F(-260,233),F(-111,233)),(F(4),F(4)),(F(2),F(3)),(F(-104,233),F(357,233))]
assert 3*cap[0][0]-cap[0][1]==t
assert 3*cap[-1][0]-cap[-1][1]==t
assert cross(K[0],K[1],cap[0])==0
assert cross(K[2],K[3],cap[-1])==0
A=area(cap);assert A==F(210855,54289)
assert A/9==F(70285,162867)<F(4,9)
assert A/18==F(70285,325734)<F(2,9)
assert F(2,9)-A/18==F(6301,977202)

# In [0,1]xK, the +/-100 integer coefficients isolate the required fiber.
assert max(3*x-y-100 for x,y in K)<t
assert max(3*x-y for x,y in K)<100+t

print('All exact checks passed.')
print('Unique overlap center:',c,'maximum overlap:',R)
print('Continuous cap ratio:',A/9)
print('Mixed cap ratio:',A/18,'strict gap:',F(2,9)-A/18)
