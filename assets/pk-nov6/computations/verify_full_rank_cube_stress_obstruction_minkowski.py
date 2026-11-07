#!/usr/bin/env python3
"""Exact rank, cube-face integral, stress, and deformation checks."""
from fractions import Fraction as F

checks=0
def check(condition):
    global checks
    assert condition
    checks+=1

def circuit(d):
    m=(d+1)//2
    N=d+1
    b=[1]*m+[-1]*m
    columns=[b[:]]
    for i in range(m-1):
        c=b[:]
        c[i]-=2
        c[m]+=2
        columns.append(c)
    for j in range(m,2*m-1):
        c=b[:]
        c[m-1]-=2
        c[j]+=2
        columns.append(c)
    return [tuple(c[row] for c in columns) for row in range(N)]

def rank(matrix):
    A=[list(map(F,row)) for row in matrix]
    r=0
    for col in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][col]),None)
        if pivot is None:
            continue
        A[r],A[pivot]=A[pivot],A[r]
        c=A[r][col]
        A[r]=[x/c for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][col]:
                c=A[i][col]
                A[i]=[x-c*y for x,y in zip(A[i],A[r])]
        r+=1
    return r

def clip(poly,a,b,c):
    """Keep a*y+b*z+c>=0, with exact rational vertices."""
    result=[]
    for P,Q in zip(poly,poly[1:]+poly[:1]):
        f=a*P[0]+b*P[1]+c
        g=a*Q[0]+b*Q[1]+c
        if f>=0:
            result.append(P)
        if (f<0<g) or (g<0<f):
            s=f/(f-g)
            result.append((P[0]+s*(Q[0]-P[0]),P[1]+s*(Q[1]-P[1])))
    return result

def moments(poly):
    area=F(0)
    y=F(0)
    z=F(0)
    for P,Q in zip(poly,poly[1:]+poly[:1]):
        cross=P[0]*Q[1]-Q[0]*P[1]
        area+=cross/2
        y+=(P[0]+Q[0])*cross/6
        z+=(P[1]+Q[1])*cross/6
    return area,y,z

for d in range(3,32,2):
    U=circuit(d)
    N=d+1
    check(len(U)==N)
    check(all(len(u)==d for u in U))
    check(all(x in (-1,1) for u in U for x in u))
    check(all(sum(u[k] for u in U)==0 for k in range(d)))
    check(rank(U)==d)
    for skip in range(N):
        check(rank([u for j,u in enumerate(U) if j!=skip])==d)
    beta=F(3,2*(d+2))
    lam=F(2*(d+2),3*N)
    check(N*lam==1/beta)
    check(lam*(N+F(N,2))==d+2)
    check(N*lam>1/F(d,d+1)**d)
    s=F(1,4*d)
    mass=1+(1-s)**d+(1+s)**d+(N-2)
    central=F(1,2)+(1-s)**d
    outer=F(1,2)*(1+s)**d
    check(mass>=d+2)
    check(max(central,outer)/mass<beta)

U=circuit(3)
square=[(F(-1),F(-1)),(F(1),F(-1)),(F(1),F(1)),(F(-1),F(1))]
for k in range(3):
    other=[j for j in range(3) if j!=k]
    for eps in (-1,1):
        total=[F(0),F(0),F(0)]
        for u in U:
            polygon=clip(square,F(u[other[0]]),F(u[other[1]]),F(eps*u[k]))
            m=moments(polygon)
            total=[x+y for x,y in zip(total,m)]
        check(total==[F(8),F(0),F(0)])
        check(F(5,6)*(4*4+total[0])==5*4)

check(F(10,3)-F(64,27)==F(26,27))
print(f"PASS: {checks} exact algebraic checks")
