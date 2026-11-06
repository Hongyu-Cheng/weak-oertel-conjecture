"""Exact support, compatibility, and first-variation checks; not a proof substitute."""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial
import random

rng = random.Random(91173)
checks = 0

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return [x-y for x,y in zip(a,b)]
def support(A,u): return max(dot(x,u) for x in A)

def solve(M,b):
    n=len(b)
    R=[[F(x) for x in M[i]]+[F(b[i])] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if R[i][j])
        R[j],R[p]=R[p],R[j]
        c=R[j][j];R[j]=[x/c for x in R[j]]
        for i in range(n):
            if i!=j:
                c=R[i][j]
                R[i]=[x-c*y for x,y in zip(R[i],R[j])]
    return [R[i][-1] for i in range(n)]

def det(M):
    n=len(M);R=[[F(x) for x in row] for row in M];res=F(1)
    for j in range(n):
        p=next((i for i in range(j,n) if R[i][j]),None)
        if p is None:return F(0)
        if p!=j:R[j],R[p]=R[p],R[j];res=-res
        c=R[j][j];res*=c
        for i in range(j+1,n):
            ratio=R[i][j]/c
            for k in range(j,n):R[i][k]-=ratio*R[j][k]
    return res

def envelope(A,U):
    h=[support(A,u) for u in U]
    d=len(U)-1
    return [solve([U[j] for j in range(d+1) if j!=i],
                  [h[j] for j in range(d+1) if j!=i]) for i in range(d+1)]

def volume(P):
    d=len(P)-1
    return abs(det([[P[k+1][j]-P[0][j] for k in range(d)] for j in range(d)]))/factorial(d)

# Matrix differentiation verifies (10) independently of the fixed-edge formula.
for d in range(1,7):
    U=[[F(1)]*d]+[[-F(int(i==j)) for j in range(d)] for i in range(d)]
    for trial in range(12):
        shift=[F(rng.randint(-4,4),3) for _ in range(d)]
        L=[[F(rng.randint(-3,3),5) if i>j else
            F(rng.randint(1,4),2) if i==j else F(0) for j in range(d)] for i in range(d)]
        A=[shift]+[[shift[i]+L[i][j] for i in range(d)] for j in range(d)]
        P=envelope(A,U);h=[support(A,u) for u in U]
        V=volume(P)
        for selected in range(d+1):
            v=[F(rng.randint(-4,4),3) for _ in range(d)]
            contacts=[x for x in A if dot(U[selected],x)==h[selected]]
            k=max(dot(v,x) for x in contacts)
            derivatives=[]
            for omitted,p in enumerate(P):
                rows=[j for j in range(d+1) if j!=omitted]
                rhs=[k-dot(v,p) if j==selected else F(0) for j in rows]
                derivatives.append(solve([U[j] for j in rows],rhs))
            E=[[P[c+1][r]-P[0][r] for c in range(d)] for r in range(d)]
            DE=[[derivatives[c+1][r]-derivatives[0][r] for c in range(d)] for r in range(d)]
            derivative_det=F(0)
            for c in range(d):
                replaced=[[DE[r][j] if j==c else E[r][j] for j in range(d)] for r in range(d)]
                derivative_det+=det(replaced)
            derivative=(1 if det(E)>0 else -1)*derivative_det/factorial(d)
            facet=[P[j] for j in range(d+1) if j!=selected]
            centroid=[sum(x[j] for x in facet)/d for j in range(d)]
            height_numerator=h[selected]-dot(U[selected],P[selected])
            predicted=d*V/height_numerator*(k-dot(v,centroid))
            assert derivative==predicted
            checks+=1
        # Exact support-offset compatibility for a nontrivial Minkowski average.
        B=[[F(2)*x[j]+F(j+1,7) for j in range(d)] for x in A]
        theta=F(2,5)
        K=[[theta*x[j]+(1-theta)*y[j] for j in range(d)] for x,y in product(A,B)]
        for u in U:
            assert support(K,u)==theta*support(A,u)+(1-theta)*support(B,u)
            checks+=1

# Exact stationary, nonoptimal two-body example from Section 6.
A=[[F(3,5),F(2,5)],[F(0),F(3,5)],[F(2,5),F(0)]]
B=[[F(2,5),F(3,5)],[F(0),F(2,5)],[F(3,5),F(0)]]
U=[[F(1),F(1)],[-F(1),F(0)],[F(0),-F(1)]]
PA,PB=envelope(A,U),envelope(B,U)
assert volume(PA)+volume(PB)==1
for j in range(3):
    ca=[x for x in A if dot(U[j],x)==support(A,U[j])]
    cb=[x for x in B if dot(U[j],x)==support(B,U[j])]
    assert len(ca)==len(cb)==1
    facet=[PA[k] for k in range(3) if k!=j]
    c=[sum(x[r] for x in facet)/2 for r in range(2)]
    assert ca[0]!=c and cb[0]!=c
    assert [ca[0][r]+cb[0][r] for r in range(2)]==[2*x for x in c]
    for v in product(range(-4,5),repeat=2):
        assert dot(v,ca[0])+dot(v,cb[0])-2*dot(v,c)==0
        checks+=1
W=[[F(1),F(3)],[-F(3),-F(2)],[F(2),-F(1)]]
assert [support(A,u) for u in W]==[F(9,5),-F(6,5),F(4,5)]
assert [support(B,u) for u in W]==[F(11,5),-F(4,5),F(6,5)]
for u in W:
    assert support(B,u)==dot(u,[-F(2,7)]*2)+F(13,7)*support(A,u)
    checks+=1
assert volume(A)==F(7,50)
assert volume(envelope(A,W))+volume(envelope(B,W))==F(109,175)<1
checks+=5
print(f"PASS {checks} exact checks")
