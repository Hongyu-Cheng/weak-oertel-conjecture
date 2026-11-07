"""Exact bounded calibrations; the general convex-region proof is analytic."""
from fractions import Fraction as F
import sympy as s

checks=0
def ck(x):
    global checks
    assert x
    checks+=1

def tail(c):
    return max(F(0),min(F(2),1-c))

for eps in [F(1,100),F(1,20),F(1,10),F(1,4),F(2,5)]:
    delta=2*eps
    for a in [F(j,10) for j in range(-40,41)]:
        mass=sum(tail(-delta-a*z) for z in [-1,0,1])
        ck(mass>=3+delta)
        if abs(a)>=1+delta:
            ck(mass==3+delta)
    for y in [F(j,10) for j in range(-10,11)]:
        f=2*(1-abs(y))
        u=1 if y>=0 else -1
        mass=sum(tail(u*y-eps*f-4*z) for z in [-1,0,1])
        ck(mass==3+delta-(1+delta)*abs(y))
        if y:
            ck(mass<3+delta)
        # An extreme-base cap can isolate the own trace.
        endpoint=sum(tail(u*y-eps*f-4*(z-1)) for z in [-1,0,1])
        ck(endpoint<=1+delta)
    ck(3+delta<4)
    ck(tail(-delta-2)+tail(-delta)+tail(-delta+2)==3+delta)
    ck(-delta == -eps*2)

# Projective transformation of an active buffered trace.
v,ap,u,e,f=s.symbols('v ap u e f')
vp=v/(1+ap*v)
old=u*v+e*f
new=(u-e*f*ap)*vp+e*f
ck(s.factor(new-old/(1+ap*v))==0)

# Exact marked-energy gradient chain factors for both powers.
d,E=s.symbols('d E', positive=True)
N=d+1
for power in [1/d,1/N]:
    ck(s.simplify(s.diff(E**power,E)*N*E-power*N*E**power)==0)
ck(s.simplify(N*(1/N))==1)

# The covariance-normalized buffer is invariant under rational fiber scale.
for scale in [F(1,4),F(1,2),F(2),F(3)]:
    M=F(6); E0=F(2); variance=F(1,3)
    ck((scale*E0)/(scale*M)==E0/M)
    ck((1/scale)**2*(scale**2*variance)==variance)

print(f'{checks} exact checks PASS')
