"""Exact rational certificate: integer-coordinate exponential-tilt candidates fail OC.

This is a counterexample only to a proposed selector, not to Oertel's conjecture.
All calculations use fractions.Fraction; no floating point or numerical optimizer.
"""
from fractions import Fraction as F

K0 = [(-218, -194), (-150, -410), (176, -362), (82, 104)]
K1 = [(-228, 332), (-160, -218), (-125, -326), (-76, -342),
      (87, -318), (40, -85), (-198, 484)]
K2 = [(-100, -242), (-2, -274), (-80, -196)]
Ks = [[tuple(map(F,p)) for p in K] for K in (K0,K1,K2)]

def cross(p,q,r):
    return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])

def area_centroid(poly):
    a=cx=cy=F(0)
    for p,q in zip(poly,poly[1:]+poly[:1]):
        t=p[0]*q[1]-p[1]*q[0]
        a+=t; cx+=(p[0]+q[0])*t; cy+=(p[1]+q[1])*t
    if not a: return F(0),(F(0),F(0))
    return a/2,(cx/(3*a),cy/(3*a))

def clip(poly,b,t):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        sp=sum(x*y for x,y in zip(p,b))-t
        sq=sum(x*y for x,y in zip(q,b))-t
        if sp>=0: out.append(p)
        if sp*sq<0:
            r=sp/(sp-sq)
            out.append(tuple(x+r*(y-x) for x,y in zip(p,q)))
    return out

for K in Ks:
    assert all(cross(K[i-1],K[i],K[(i+1)%len(K)])>0 for i in range(len(K)))
    assert area_centroid(K)[0]>0

# Convexity at the middle integer fiber: K1 contains all midpoint generators.
midpoints=[tuple((x+y)/2 for x,y in zip(p,q)) for p in Ks[0] for q in Ks[2]]
min_cross=[min(cross(p,q,m) for m in midpoints)
           for p,q in zip(Ks[1],Ks[1][1:]+Ks[1][:1])]
assert min_cross==[F(550),F(0),F(0),F(0),F(0),F(0),F(26988)]

As,Cs=zip(*(area_centroid(K) for K in Ks))
assert As==(F(120746),F(252101,2),F(2574))
T=sum(As); assert T==F(498741,2)

# The exp(a*z) tilted integer mean is 1 exactly when r=exp(a)=sqrt(A0/A2).
# The inequalities below prove its continuous first-coordinate mean exceeds -79.
assert As[0]/As[2] < 49
assert Cs[1][0]+79 < 0
N7=As[0]*(Cs[0][0]+Cs[2][0]+158)+7*As[1]*(Cs[1][0]+79)
assert N7>0
mean_x_at_7=(As[0]*(Cs[0][0]+Cs[2][0])+7*As[1]*Cs[1][0])/(2*As[0]+7*As[1])
assert mean_x_at_7+79==F(105118,6743073)

# H1={x+255*z>=176}; it contains the mean at z=1 because x>-79.
assert max(p[0] for p in Ks[0])==176
assert min(p[0] for p in Ks[2])>-334
cap1=area_centroid(clip(Ks[1],(F(1),F(0)),F(-79)))[0]+As[2]
assert cap1==F(10727233,196)
assert cap1/T==F(10727233,48876618)<F(2,9)

# H0={x+3*y-2000*z>=b0} contains centroid(K0), excludes other fibers.
b0=Cs[0][0]+3*Cs[0][1]
assert b0==F(-112127948,181119)
for z in (1,2):
    assert max(p[0]+3*p[1]-2000*z for p in Ks[z])<b0
cap0=area_centroid(clip(Ks[0],(F(1),F(3)),b0))[0]
assert cap0/T==F(353119997339753853217,1592080527583076149611)<F(2,9)

# H2={-x-y+10000*z>=20298} contains centroid(K2), excludes other fibers.
assert -Cs[2][0]-Cs[2][1]+20000==20298
for z in (0,1):
    assert max(-p[0]-p[1]+10000*z for p in Ks[z])<20298
cap2=area_centroid(clip(Ks[2],(F(-1),F(-1)),F(298)))[0]
assert cap2==F(4,9)*As[2]
assert cap2/T<F(2,9)

print('All exact checks passed.')
print('Areas:',As,'total:',T)
print('Halfspace mass ratios:',cap0/T,cap1/T,cap2/T)
