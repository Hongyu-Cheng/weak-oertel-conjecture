"""Independent physical caps, explicit source gaps, and deficient-rank checks."""
from fractions import Fraction as F
from itertools import product
import sympy as s

checks=0
def eq(a,b):
    global checks
    assert s.simplify(a-b)==0,(a,b)
    checks+=1
def yes(p):
    global checks
    assert p
    checks+=1
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def clip(poly,u,c):
    out=[]
    for i,P in enumerate(poly):
        Q=poly[(i+1)%len(poly)]
        f=dot(u,P)+c;g=dot(u,Q)+c
        if f>=0:out.append(P)
        if (f>0 and g<0) or (f<0 and g>0):
            t=f/(f-g);out.append(tuple(x+t*(y-x) for x,y in zip(P,Q)))
    return out
def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly))))/2
T=[(F(-1),F(-1)),(F(2),F(-1)),(F(-1),F(2))]
U=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]
V=F(9,2)
def source_gaps(P,radii):
    RR=sum(r*r for r in radii);SS=sum(radii);rmin=min(radii)
    for z0 in P:
        if not any(z0):continue
        ds=[dot(z0,tuple(a-b for a,b in zip(z,z0))) for z in P]
        JJ=max(abs(d) for d in ds);HH=sum(d*d for d in ds);norm=dot(z0,z0)
        tt=min(rmin/(2*JJ),SS*norm/HH)
        yes(tt>0);yes(max(abs(tt*d) for d in ds)<=rmin/2)
        target=2*RR-2*tt*SS*norm+tt*tt*HH/2
        yes(target<=2*RR-F(3,2)*tt*SS*norm)
        yes(target<2*RR)
        for u in U:
            actual=sum(area(clip([(r*x,r*y) for x,y in T],u,tt*d)) for r,d in zip(radii,ds))
            eq(actual,target)
    return RR

for n in [1,2,3]:
    P=list(product([-1,0,1],repeat=n))
    radii=[1-F(sum(j*j for j in z),10*n) for z in P]
    R0=source_gaps(P,radii)
    G=s.Matrix(n,n,lambda i,j:sum(z[i]*z[j] for z in P))
    alpha=s.Matrix([s.Rational(i+1,500) for i in range(n)])
    new=[r+F((s.Matrix(z).T*alpha)[0]) for r,z in zip(radii,P)]
    bb=s.Matrix([sum(r*z[i] for r,z in zip(new,P)) for i in range(n)])
    eq((bb-G*alpha).norm()**2,0)
    WW=(bb.T*G.pinv()*bb)[0];RR=sum(r*r for r in new)
    eq(RR-WW,R0)
    tilts=list(-2*G.pinv()*bb)
    for u in U:
        actual=sum(area(clip([(r*x,r*y) for x,y in T],u,F(dot(tilts,z)))) for r,z in zip(new,P))
        eq(actual,2*R0)
    eq(V*RR-V*R0,V*WW)

# Genuine full-dimensional thin projection with noncoordinate rank-one base:
# |z1-z2|<=1/4, |z3|<=1/4, |(z1+z2)/2|<=2 has exactly these integers.
P=[(j,j,0) for j in range(-2,3)]
rs=[1-F(z[0]**2,20) for z in P]
R0=source_gaps(P,rs)
G=s.Matrix(3,3,lambda i,j:sum(z[i]*z[j] for z in P))
yes(G.rank()==1)
Gp=G.pinv();eq((G*Gp*G-G).norm()**2,0)
new=[r+F(z[0],100) for r,z in zip(rs,P)]
bb=s.Matrix([sum(r*z[i] for r,z in zip(new,P)) for i in range(3)])
RR=sum(r*r for r in new);WW=(bb.T*Gp*bb)[0]
eq(RR-WW,R0);eq((G*Gp*bb-bb).norm()**2,0)
tilt=list(-2*Gp*bb)
for u in U:
    actual=sum(area(clip([(r*x,r*y) for x,y in T],u,F(dot(tilt,z)))) for r,z in zip(new,P))
    eq(actual,2*R0)
    invisible=[F(7),F(-7),F(19)]
    same=sum(area(clip([(r*x,r*y) for x,y in T],u,F(dot([a+b for a,b in zip(tilt,invisible)],z)))) for r,z in zip(new,P))
    eq(same,actual)

# Complete rank zero in a thin full-dimensional projection.
G=s.zeros(2);bb=s.zeros(2,1)
eq((bb.T*G.pinv()*bb)[0],0)
for r in [F(1,3),F(1),F(7,4)]:
    for u in U:eq(area(clip([(r*x,r*y) for x,y in T],u,F(0))),2*r*r)
print(f'PASS {checks} exact checks')
