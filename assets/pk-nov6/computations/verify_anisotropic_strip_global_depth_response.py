"""Exact tail-cell, score, and actual seven-fiber cap checks."""
from fractions import Fraction as F
from itertools import product

def positive(x):return max(F(0),x)

def upper(x,A,B):
    """Tail of independent centered uniforms of half-widths A and B."""
    A,B=abs(A),abs(B)
    if A==0:
        return min(F(1),max(F(0),(B-x)/(2*B)))
    if B==0:return upper(x,B,A)
    cdf=(positive(x+A+B)**2-positive(x-A+B)**2
         -positive(x+A-B)**2+positive(x-A-B)**2)/(8*A*B)
    assert 0<=cdf<=1
    return 1-cdf

def paired_min(x,A,B):
    """All shifts: every polynomial cell and every interior critical point."""
    A,B=abs(A),abs(B)
    knots=sorted(set([-A-B,-A+B,A-B,A+B]))
    end=abs(x)+A+B+1
    events=sorted(set([F(0),end]+[abs(k-x) for k in knots]))
    fun=lambda q:upper(x+q,A,B)+upper(x-q,A,B)
    best=min(map(fun,events))
    for q0,q1 in zip(events,events[1:]):
        width=q1-q0
        v0,vm,v1=fun(q0),fun((q0+q1)/2),fun(q1)
        qa=2*(v0+v1-2*vm)/(width*width)
        qb=(v1-v0)/width-qa*width
        if qa>0:
            shift=-qb/(2*qa)
            if 0<shift<width:
                best=min(best,fun(q0+shift))
    return best

clip01=lambda x:min(F(1),max(F(0),x))
tail_checks=0
for L,H in product([F(1,12),F(1,6),F(1,4)],[F(1,2),F(1),F(3,2)]):
    c=-H/2
    for sigma,q in product(
        [F(0),F(1,8),F(1,2),F(1),F(-3),F(10),F(100)],
        [c+F(k,4)*H for k in range(-6,9)]):
        got=paired_min(q-c,abs(sigma)*L,H)
        floor=clip01(1-(q-c)/H)
        assert floor<=got<=1
        if sigma==0:assert got==floor
        if q<=c:assert got==1
        A=abs(sigma)*L
        if A>=H+abs(q-c) and q>=c:
            assert got==1-(q-c)/A
        tail_checks+=1

kappa=F(2,3)
balance_checks=0
for L,H in product([F(1,24),F(1,12),F(1,6),F(1,4)],
                   [F(1,3),F(1),F(2)]):
    a=4*L*H;c=-H/2
    v0=a*c/(F(3,2)*kappa*H+a)
    v1=v2=-v0/2
    level=a+kappa*v0/2
    assert c<v0<0 and v1==L*H/(1+4*L)
    assert level==a*(1-1/(6*(1+4*L)))
    assert level>a/2>0
    assert -kappa*v0+a*clip01(1-(v0-c)/H)==level
    assert a-kappa*v1==a-kappa*v2==level
    # Exact checks in every scalar piece and unequal-coordinate branch.
    for q in [c-H,c,c/2,F(0),c+H,c+2*H,v0]:
        prof=min(-kappa*q+a*clip01(1-(q-c)/H),a+kappa*q/2)
        assert prof<=level
        if q!=v0:assert prof<level
        balance_checks+=1

def clip(P,u,c):
    if not P:return []
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        v=sum(a*x for a,x in zip(u,p))+c
        w=sum(a*x for a,x in zip(u,q))+c
        if v>=0:out.append(p)
        if v*w<0:
            t=v/(v-w)
            out.append(tuple(p[i]+t*(q[i]-p[i]) for i in range(2)))
    return out

def area(P):
    if len(P)<3:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(P,P[1:]+P[:1])))/2

L,H,c=F(1,6),F(1),F(-1,2)
a=F(2,3);g=(F(1,3),F(1,3));v=(F(1,10),F(1,10))
T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
Q=list(product([0,1],repeat=2))
extras=[(-1,0),(-1,1),(1,-1)]
support=Q+extras
assert sorted(support)==[
    (x,y) for x,y in product(range(-2,3),repeat=2)
    if -1<=x<=1 and y<=1 and x+2*y>=-1]

actual_checks=0
for t in [F(k,1000) for k in range(1,21)]:
    E=[(g[0]+s-t*r/2,g[1]-s-t*r/2)
       for s,r in [(-L,c-H),(L,c-H),(L,c+H),(-L,c+H)]]
    assert area(E)==t*a
    assert all(x>0 and y>0 and x+y<1 for x,y in E)
    fibers=[(z,T) for z in Q]+[(z,E) for z in extras]
    y=tuple(g[i]+t*v[i] for i in range(2))
    for i,u in enumerate([(-1,-1),(1,0),(0,1)]):
        shift=F(0) if i==0 else F(2)
        beta=(-4+shift/2,-4-shift/2)
        masses=[area(clip(P,u,
                    sum(beta[j]*z[j]-u[j]*y[j] for j in range(2))))
                for z,P in fibers]
        assert masses[1:4]==[0,0,0]
        assert masses[4]==t*a
        if i==0:
            assert masses[5:]==[F(7,20)*t*a,F(7,20)*t*a]
            assert sum(masses)==F(2,9)+F(19,15)*t+t*t/50
        else:
            assert masses[5:]==[0,t*a]
            assert sum(masses)==F(2,9)+F(19,15)*t+t*t/200
        actual_checks+=1
    # At g the canonical atomic-direction cap has a smaller first coefficient.
    masses=[area(clip(P,(-1,-1),g[0]+g[1]-4*sum(z))) for z,P in fibers]
    assert sum(masses)==F(2,9)+t
    actual_checks+=1

assert (4*F(19,15)-3*F(4,9)*a)/(16*F(1,2))==F(47,90)
print(f"PASS: {tail_checks} exact all-shift tail minima, {balance_checks} "
      f"score checks, {actual_checks} actual seven-fiber cap checks.")
