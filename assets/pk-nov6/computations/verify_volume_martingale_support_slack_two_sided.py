"""Exact actual-polygon and transport checks for the support-slack note."""
from fractions import Fraction as F
from itertools import combinations, product

count=0
def ck(v):
    global count
    assert v
    count+=1

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def hull(points):
    points=sorted(set(points))
    lo=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:
            lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(points):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0:
            up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]

def area(poly):
    return sum(a[0]*b[1]-a[1]*b[0]
               for a,b in zip(poly,poly[1:]+poly[:1]))/2

def moment_x2(poly):
    return sum((a[0]**2+a[0]*b[0]+b[0]**2)
               *(a[0]*b[1]-a[1]*b[0])
               for a,b in zip(poly,poly[1:]+poly[:1]))/12

def support(poly,u):
    return max(x*u[0]+y*u[1] for x,y in poly)

K=hull([(F(x),F(y)) for x,y in product((-1,1),repeat=2)])
D=hull([(F(a)*sgn,F(b)*sgn2)
        for a,b in ((1,F(1,2)),(F(1,2),1))
        for sgn,sgn2 in product((-1,1),repeat=2)])
B=hull([(F(4,11)*p[0]+F(7,11)*q[0],
         F(4,11)*p[1]+F(7,11)*q[1]) for p in K for q in D])
ck(area(K)==4)
ck(area(D)==F(7,2))
ck(area(B)==F(919,242))
ck(area(K)-area(B)==F(49,242))
ck(moment_x2(K)==F(4,3))
ck(moment_x2(D)==F(47,48))
ck((moment_x2(K)+2*moment_x2(D))/11==F(79,264))
ck(F(79,264)<1)
ck(F(4,11)<1)
ck(F(11,2)+F(6,10)<F(15,2))

# Exact support equality on the source surface-area support, but a
# strictly positive diagonal gap and shorter actual source face traces.
axes=((1,0),(-1,0),(0,1),(0,-1))
for u in axes:
    ck(support(K,u)==support(D,u)==support(B,u)==1)
    face=[p for p in B if p[0]*u[0]+p[1]*u[1]==1]
    ck(len(face)==2)
    ck(abs(face[0][0]-face[1][0])+abs(face[0][1]-face[1][1])==F(15,11))
for u in product((-1,1),repeat=2):
    ck(support(B,u)==F(37,22))
    ck(support(K,u)-support(B,u)==F(7,22))
ck(sum(2*(support(K,u)-support(B,u)) for u in axes)==0)
for u in product(range(-8,9),repeat=2):
    if u==(0,0):
        continue
    ck(support(B,u)==F(4,11)*support(K,u)+F(7,11)*support(D,u))
    ck(support(B,u)<=support(K,u))

# All five proper nonempty closed minors, retaining inherited parity.
P=(-1,0,1)
V={-1:F(7,2),0:F(4),1:F(7,2)}
minor_count=0
for size in (1,2):
    for subset in combinations(P,size):
        if tuple(z for z in P if min(subset)<=z<=max(subset))!=subset:
            continue
        kp=len({z%2 for z in subset})
        ck(sum(V[z] for z in subset)<F(11*kp,2))
        minor_count+=1
ck(minor_count==5)
w={z:V[z]/11 for z in P}
ck(sum(w.values())==1)
ck(sum(z*w[z] for z in P)==0)
ck(w[-1]==w[1]==F(7,22))
ck(w[0]==F(4,11))

# Original-volume/projective rescaling identities on exact one-source
# affine contact rows with varying nonconstant ell.  These are algebraic
# checks; compatibility is proved geometrically in the source.
for left,right in product(range(1,9),repeat=2):
    ell={-1:F(left),0:F(left+right,2),1:F(right)}
    lam={-1:F(1,4),0:F(1,2),1:F(1,4)}
    pi={z:lam[z]/ell[0] for z in P}
    hat={z:pi[z]*ell[z] for z in P}
    ck(sum(hat.values())==1)
    ck(sum(hat[z]*F(z)/ell[z] for z in P)==0)
    ck(sum(hat[z]/ell[z] for z in P)==1/ell[0])
    for z in P:
        ck(hat[z]/ell[z]==lam[z]/ell[0])

print(f"PASS: {count} exact checks")
