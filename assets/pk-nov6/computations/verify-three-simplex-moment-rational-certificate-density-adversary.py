"""Pure exact verifier: only Python standard library and rational arithmetic.
Run from workspace root. No floating-point calculation is used.
"""
from fractions import Fraction as F
import json
from pathlib import Path

DATA=Path(__file__).with_name('three-simplex-moment-rational-certificate.json')

def moment(poly):
    area=F(0);mom=[F(0),F(0)]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        cr=p[0]*q[1]-p[1]*q[0];area+=cr
        for j in range(2):mom[j]+=(p[j]+q[j])*cr
    return area/2,(mom[0]/6,mom[1]/6)

def clip(poly,u,h):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=sum(u[j]*p[j] for j in range(2))-h
        fq=sum(u[j]*q[j] for j in range(2))-h
        if fp>=0:out.append(p)
        if fp*fq<0:out.append(tuple(p[j]+(q[j]-p[j])*fp/(fp-fq) for j in range(2)))
    return out

def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
    pts=sorted(set(points));lower=[];upper=[]
    for p in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    for p in pts[::-1]:
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

D=10**24
def floorD(x):return F(x.numerator*D//x.denominator,D)
def ceilD(x):return -floorD(-x)
def enclose_moments(poly):
    al=F(0);au=F(0);ml=[F(0),F(0)];mu=[F(0),F(0)]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        cr=p[0]*q[1]-p[1]*q[0]
        al+=floorD(cr/2);au+=ceilD(cr/2)
        for j in range(2):
            val=(p[j]+q[j])*cr/6;ml[j]+=floorD(val);mu[j]+=ceilD(val)
    return al,au,ml,mu

K=[(F(-1,3),F(-1,3)),(F(2,3),F(-1,3)),(F(-1,3),F(2,3))]
a,c=F(1,8),F(257,256);s=F(-223,1536)
fibers=[[(s+a*x,s+a*y) for x,y in K],K,[(s+c*x,s+c*y) for x,y in K]]
weights=[moment(p)[0] for p in fibers];M=sum(weights);t=M/2
assert M==F(132609,131072) and t==F(132609,262144)
assert weights[0]<t and weights[2]<t
assert weights[0]+weights[1]>t
cert=json.loads(DATA.read_text())
assert F(cert['M'])==M and F(cert['t'])==t
points=[];duals=[]
assert len(cert['records'])==64
for r in cert['records']:
    u=tuple(r['u']);ell=F(r['ell']);hs=list(map(F,r['thresholds']))
    masses=[ell,t-2*ell,ell]
    assert all(F(0)<=m<=w for m,w in zip(masses,weights))
    assert sum(masses)==t and -masses[0]+masses[2]==0
    total_moment=[F(0),F(0)]
    for poly,h,mass in zip(fibers,hs,masses):
        area,mom=moment(clip(poly,u,h))
        assert F(0)<mass<=area
        # Density mass/area on this rational cap is <=1 and has exact mass.
        for j in range(2):total_moment[j]+=mom[j]*mass/area
    p=tuple(x/t for x in total_moment)
    assert p==tuple(map(F,r['point']))
    points.append(p)
    # This dual upper bound holds for EVERY feasible submeasure.
    b,v=F(r['b']),F(r['v']);hinge=F(0)
    for z,poly in zip([-1,0,1],fibers):
        h=b+v*z;area,mom=moment(clip(poly,u,h))
        hinge+=sum(u[j]*mom[j] for j in range(2))-h*area
    bound=b+hinge/t
    assert bound==F(r['bound'])
    assert sum(u[j]*p[j] for j in range(2))<=bound
    duals.append((u,bound))
P=hull(points);Q=K[:]
for u,bound in duals:Q=clip(Q,(-u[0],-u[1]),-bound)
assert P==[tuple(map(F,p)) for p in cert['P']]
assert Q==[tuple(map(F,p)) for p in cert['Q']]
assert len(P)==len(Q)==64
pl,pu,pml,pmu=enclose_moments(P)
ql,qu,qml,qmu=enclose_moments(Q)
assert pl>0 and ql>0
# The following small rational bounds suffice for a hand-readable conclusion.
assert pl>=F(73,100000)
assert qu<=F(74,100000)
for j in range(2):
    assert pmu[j]<=F(-327,100000000)
    assert max(p[j] for p in Q)<=F(11,1000)
    assert max(p[j] for p in Q)>=0
# P subset B subset Q. For each coordinate, the extra first moment is
# at most max_Q x * (area Q-area P). The resulting bound is negative.
num=F(-327,100000000)+F(11,1000)*F(1,100000)
assert num/F(74,100000)==F(-79,18500)<F(-1,250)
# Cap certificate: x1+x2+z<=-1/125 contains every resulting centroid.
cap=F(1,128)+F(1,2)*F(247,375)**2
target=F(2,9)*M
assert cap==F(4045201,18000000)
assert target-cap==F(872713,9216000000)>0
print('PASS: all 64 rational primal and dual witnesses verified.')
print('PASS: centroid coordinate bounds <= -79/18500 < -1/250.')
print('PASS: fixed-mass centroid violates the desired OC constant; it is not an OC counterexample.')
