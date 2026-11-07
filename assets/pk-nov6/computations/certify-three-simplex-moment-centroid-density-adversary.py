"""Exact rational certificate after floating-point discovery of primal/dual choices.
Every enclosure inequality below is independently verified with Fraction.
Floats only select proposed rational witnesses; they prove nothing.
"""
from fractions import Fraction as F
import math,json
import numpy as np
from scipy.optimize import brentq
exec(open('./test-three-simplex-moment-centroid-density-adversary.py').read().split('rng=np.random.default_rng')[0])

def emom(poly):
    if len(poly)<3:return F(0),(F(0),F(0))
    area=F(0);mom=[F(0),F(0)]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        cross=p[0]*q[1]-p[1]*q[0];area+=cross
        for j in range(2):mom[j]+=(p[j]+q[j])*cross
    return area/2,(mom[0]/6,mom[1]/6)

def eclip(poly,u,t):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=sum(u[j]*p[j] for j in range(2))-t;fq=sum(u[j]*q[j] for j in range(2))-t
        if fp>=0:out.append(p)
        if fp*fq<0:out.append(tuple(p[j]+(q[j]-p[j])*fp/(fp-fq) for j in range(2)))
    return out

def down(x,den=10**10):return F(math.floor(x*den)-2,den)
def nearest(x,den=10**10):return F(round(x*den),den)
def fs(x):return f'{x.numerator}/{x.denominator}'

EK=[(F(-1,3),F(-1,3)),(F(2,3),F(-1,3)),(F(-1,3),F(2,3))]
a=F(1,8);c=F(257,256);s=(F(-223,1536),)*2
EP=[[(s[0]+a*x,s[1]+a*y) for x,y in EK],EK,[(s[0]+c*x,s[1]+c*y) for x,y in EK]]
polys=[np.array([[float(x),float(y)] for x,y in p]) for p in EP]
ws=[emom(p)[0] for p in EP];M=sum(ws);q=M/2
lo=max(F(0),(q-ws[1])/2);hi=min(ws[0],ws[2],q/2)
N=8
us=sorted(set((x,y) for x in range(-N,N+1) for y in range(-N,N+1) if max(abs(x),abs(y))==N),key=lambda u:math.atan2(u[1],u[0]))
primal=[];duals=[];records=[]
for u in us:
    fu=np.array(u,float)
    def der(m):return cutoff(polys[0],fu,m)+cutoff(polys[2],fu,m)-2*cutoff(polys[1],fu,float(q)-2*m)
    if der(float(lo))<=0:ell=lo;mode='lo'
    elif der(float(hi))>=0:ell=hi;mode='hi'
    else:ell=nearest(brentq(der,float(lo),float(hi),xtol=1e-14));mode='interior'
    assert lo<=ell<=hi
    masses=[ell,q-2*ell,ell]
    thresholds=[];mp=[F(0),F(0)]
    for p,fp,mass in zip(EP,polys,masses):
        if mass==0:thresholds.append(F(0));continue
        h=down(cutoff(fp,fu,float(mass)))
        cp=eclip(p,u,h);ar,mom=emom(cp)
        assert ar>=mass and ar>0
        thresholds.append(h)
        for j in range(2):mp[j]+=mom[j]*mass/ar
    pp=tuple(x/q for x in mp);primal.append(pp)
    hs=[cutoff(p,fu,float(m)) for p,m in zip(polys,masses)]
    if mode=='lo':b=nearest((hs[0]+hs[2])/2);v=nearest((hs[2]-hs[0])/2)
    elif mode=='hi':b=nearest(hs[1]);v=nearest(hs[2]-hs[1])
    else:b=nearest(hs[1]);v=nearest((hs[2]-hs[0])/2)
    hinge=F(0)
    for z,p in zip([-1,0,1],EP):
        h=b+v*z;ar,mom=emom(eclip(p,u,h));hinge+=sum(u[j]*mom[j] for j in range(2))-h*ar
    bound=b+hinge/q
    assert sum(u[j]*pp[j] for j in range(2))<=bound
    duals.append((u,bound));records.append({'u':u,'ell':fs(ell),'thresholds':[fs(h) for h in thresholds],'b':fs(b),'v':fs(v),'point':[fs(x) for x in pp],'bound':fs(bound)})
# Convex hull of feasible points, with exact orientation.
def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(pts):
    pts=sorted(set(pts));lower=[];upper=[]
    for p in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    for p in pts[::-1]:
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]
P=hull(primal)
# Every moment body is contained in original K, since the base mean is zero.
Q=EK[:]
for u,h in duals:Q=eclip(Q,(-u[0],-u[1]),-h)
print('built',len(P),len(Q),flush=True)
# Avoid enormous denominator growth: directed rational intervals for shoelace
# summands, with a fixed denominator. All coordinates above remain exact.
D=10**24

def floorD(x):return F(x.numerator*D//x.denominator,D)
def ceilD(x):return -floorD(-x)
def enclosed_mom(poly):
    al=F(0);au=F(0);ml=[F(0),F(0)];mu=[F(0),F(0)]
    for p,r in zip(poly,poly[1:]+poly[:1]):
        cr=p[0]*r[1]-p[1]*r[0];al+=floorD(cr/2);au+=ceilD(cr/2)
        for j in range(2):
            term=(p[j]+r[j])*cr/6;ml[j]+=floorD(term);mu[j]+=ceilD(term)
    return al,au,ml,mu
pl,pu,pml,pmu=enclosed_mom(P);ql,qu,qml,qmu=enclosed_mom(Q)
assert pl>0 and ql>0
# Safe centroid upper bound: integral_B x <= integral_P x + max_Q x*(|Q|-|P|).
# With negative numerator, divide by largest possible area to get upper bound.
res=[]
for j in range(2):
    R=max(p[j] for p in Q);assert R>=0
    numerator=pmu[j]+R*(qu-pl);assert numerator<0
    upper=numerator/qu
    assert upper<F(-1,250)
    res.append(upper)
print('area P interval',float(pl),float(pu),'Q',float(ql),float(qu),flush=True)
print('centroid upper bounds',[float(x) for x in res],flush=True)
print('EXACT VERIFIED: both centroid coordinates < -1/250',flush=True)
with open('./three-simplex-moment-rational-certificate.json','w') as f:json.dump({'M':fs(M),'t':fs(q),'records':records,'P':[[fs(x) for x in p] for p in P],'Q':[[fs(x) for x in p] for p in Q],'area_P_lower':fs(pl),'area_Q_upper':fs(qu),'moment_P_upper':[fs(x) for x in pmu],'centroid_upper':[fs(x) for x in res]},f)
