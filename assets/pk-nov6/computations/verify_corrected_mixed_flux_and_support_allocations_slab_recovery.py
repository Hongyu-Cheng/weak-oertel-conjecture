"""Exact critical-cap sign certificate and all-status interval flux checks."""
from fractions import Fraction as F

checks=0
def check(b):
    global checks
    assert b
    checks+=1

def interval_cap(lo,hi,p,a,v,b,sigma):
    t=(b-a*p)/v
    if v == 1:
        caplo=max(lo,t); caphi=hi
        if t<lo: alpha=(F(1),F(1)); section=F(0)
        elif t==lo: alpha=(1-sigma,F(1)); section=sigma
        elif t<hi: alpha=(F(0),F(1)); section=F(1)
        elif t==hi: alpha=(F(0),sigma); section=sigma
        else: alpha=(F(0),F(0)); section=F(0)
    else:
        caplo=lo; caphi=min(hi,t)
        if t>hi: alpha=(F(1),F(1)); section=F(0)
        elif t==hi: alpha=(F(1),1-sigma); section=sigma
        elif t>lo: alpha=(F(1),F(0)); section=F(1)
        elif t==lo: alpha=(sigma,F(0)); section=sigma
        else: alpha=(F(0),F(0)); section=F(0)
    if caphi<caplo: length=moment=F(0)
    else: length=caphi-caplo; moment=(caphi**2-caplo**2)/2
    flux1=-alpha[0]*lo+alpha[1]*hi-v*section*t
    flux2=-alpha[0]*lo**2+alpha[1]*hi**2-v*section*t**2
    check(length==flux1)
    check(2*moment==flux2)
    check(p*length==p*flux1)
    return length,moment,alpha,section,t

# An actual concave-radius, affine-center five-fiber family.
for p in map(F,range(-2,3)):
    center=p/3; radius=3-abs(p)
    lo,hi=center-radius,center+radius
    for a in map(F,[-1,0,1]):
        for v in (F(-1),F(1)):
            # Exact support, proper, empty and full statuses.
            thresholds=[lo-1,lo,(2*lo+hi)/3,(lo+hi)/2,hi,hi+1]
            for t in thresholds:
                b=a*p+v*t
                for sigma in (F(0),F(1,3),F(1)):
                    interval_cap(lo,hi,p,a,v,b,sigma)

# The full critical family: every cut proper, nu=eta, Q_transport=0.
P=list(map(F,[-1,0,1]))
for a1 in [F(j,16) for j in range(-7,8)]:
    for a2 in [F(j,16) for j in range(-7,8)]:
        mp=[]; mx=[]; Vpp=[]; Vxx=[]
        for a,v in ((a1,F(1)),(a2,F(-1))):
            data=[interval_cap(F(-1,2),F(1,2),p,a,v,F(0),F(0))
                  for p in P]
            check(sum(row[0] for row in data)==F(3,2))
            check(sum(row[3] for row in data)==3)
            check(sum(row[4] for row in data)==0)
            mp.append(sum(p*row[0] for p,row in zip(P,data)))
            mx.append(sum(row[1] for row in data))
            Vpp.append(sum(p*p*row[3] for p,row in zip(P,data)))
            Vxx.append(sum(row[3]*row[4]**2 for row in data))
        check(-sum(mp)==-Vpp[0]*a1-Vpp[1]*a2)
        check(-2*sum(mx)==Vxx[0]-Vxx[1])
        if a1+a2:
            check(-sum(mp)!=Vpp[0]*a1+Vpp[1]*a2)

check(-F(1,2)==-2*F(1,4))
check(-2*(F(5,16)-F(3,8))==F(1,8))

# Conditional covariance of a genuinely curved sheared disk family.
for t in ((F(1),F(2)),(F(-3,2),F(1,4))):
    for u in ((F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5))):
        w=(F(1),)+t
        normal=(-sum(ti*ui for ti,ui in zip(t,u)),)+u
        Q=[[F(2,3)*wi*wj for wj in w] for wi in w]
        for row in Q:
            check(sum(x*y for x,y in zip(row,normal))==0)

print(f"PASS: {checks} exact checks")
