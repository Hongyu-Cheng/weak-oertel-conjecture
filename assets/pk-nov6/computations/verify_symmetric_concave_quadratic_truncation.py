#!/usr/bin/env python3
"""Exact regression checks for the proved finite moment identity and truncation theorem."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
import random

checks=0

def moment(r):
    global checks
    N=len(r)-1; R=r[0]
    S1=R+2*sum(r[1:]); S2=R*R+2*sum(x*x for x in r[1:])
    lhs=3*S2-2*R*S1
    star=[R*(1-F(2*k,2*N+1)) for k in range(N+1)]
    u=[x-y for x,y in zip(r,star)]
    curvature=[2*r[j]-r[j-1]-r[j+1] for j in range(1,N)]
    assert all(t>=0 for t in curvature)
    rhs=R*R/F(2*N+1)+6*sum(x*x for x in u[1:])
    rhs+=4*R/F(2*N+1)*sum(j*(N-j)*(N-j+1)*curvature[j-1] for j in range(1,N))
    assert lhs==rhs
    assert lhs>=R*R/F(2*N+1)
    checks+=3
    return S2


def check(r):
    global checks
    N=len(r)-1; R=r[0]
    assert R>0 and r[-1]>=0 and all(a>=b for a,b in zip(r,r[1:]))
    S0=moment(r)
    levels={F(0),R,R/100,R/3,R/2,2*R/3,99*R/100}
    levels.update(r if N<=8 else (r[N//3],r[2*N//3],r[-1]))
    for c in levels:
        h=R-c
        values=[max(F(0),v-c) for v in r]
        Q=values[0]**2+2*sum(v*v for v in values[1:])
        lower=(h/R)**3*S0+c*h*h/(R*(2*N+1))
        assert Q>=lower
        if 0<c<R: assert Q>(h/R)**3*S0
        if c<R:
            active=[v-c for v in r if v>c]
            moment(active)
        checks+=2

# Finite exact grid, including plateaus and zero endpoints.
for N in range(0,9):
    for drops in combinations_with_replacement(range(7),N):
        if sum(drops)>6: continue
        r=[F(1)]
        for drop in drops: r.append(r[-1]-F(drop,6))
        check(r)

# Unbounded-length mechanism tested at larger, distinct rational scales.
random.seed(978103)
for case in range(420):
    N=random.randrange(1,65)
    drops=sorted(random.randrange(0,15) for _ in range(N))
    denominator=sum(drops)+(0 if case%3==0 and sum(drops)>0 else random.randrange(1,20))
    R=F(random.randrange(1,11),random.randrange(1,11))
    r=[R]
    for drop in drops: r.append(r[-1]-R*F(drop,denominator))
    check(r)

# Sharpness of the separate moment lemma, for every tested length.
for N in range(101):
    R=F(7,3)
    r=[R*(1-F(2*k,2*N+1)) for k in range(N+1)]
    S2=moment(r)
    S1=R+2*sum(r[1:])
    assert 3*S2-2*R*S1==R*R/F(2*N+1)
    checks+=1

# The algebraic cap-sector coefficient has its minimum at a=2/3.
for a in [F(2,3),F(3,4),F(1),F(4,3),F(2),F(10),F(100)]:
    f=(3*a-1)**3/(27*a*a*(2*a-1))
    deriv=(3*a-1)**2*(3*a-2)/(27*a**3*(2*a-1)**2)
    assert f>=F(1,4) and deriv>=0
    checks+=2
print(f'PASS {checks} exact rational identity, truncation, endpoint, plateau, and cap-coefficient checks')
