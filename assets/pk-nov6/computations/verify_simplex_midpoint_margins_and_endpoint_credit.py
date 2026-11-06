"""Exact finite checks for the determinant and cap-accounting constants."""
from fractions import Fraction as F
from math import ceil, prod
import random

def determinant(P):
    A=[list(row) for row in P];N=len(A);out=F(1)
    for i in range(N):
        pivot=next((j for j in range(i,N) if A[j][i]),None)
        if pivot is None:return F(0)
        if pivot!=i:A[pivot],A[i]=A[i],A[pivot];out=-out
        q=A[i][i];out*=q
        for k in range(i,N):A[i][k]/=q
        for j in range(i+1,N):
            q=A[j][i]
            for k in range(i,N):A[j][k]-=q*A[i][k]
    return out

def check(P):
    N=len(P);det=abs(determinant(P))
    assert all(sum(P[i][j] for i in range(N))==1 for j in range(N))
    assert all(x>=0 for row in P for x in row)
    if det<F(1,2**(N-1)):return
    maxima=sorted((max(row) for row in P),reverse=True)
    rowsums=[sum(row) for row in P]
    norms2=[sum(x*x for x in row) for row in P]
    assert det*det<=prod(norms2)<=prod(max(P[i])*rowsums[i] for i in range(N))
    assert prod(rowsums)<=1
    assert det*det<=prod(maxima)
    j=(N+1)//2
    if N==2:
        assert maxima[0]>=F(3,4)
    else:
        R=N-j+1
        assert R==N//2+1 and 2*R>N
        # Exact form p_j >= N^(-N/(2R)); no numerical root.
        assert maxima[j-1]**(2*R)>=F(1,N**N)
        assert maxima[j-1]**R>=F(1,4**(N-1))
        assert maxima[j-1]>F(1,N)
    centered_square=F(N)**N/F(2)**(2*N-2)*prod(maxima[1:])**2
    assert det*det<=centered_square

random.seed(739021)
for N in range(2,11):
    # Homothetic half-simplex, determinant exactly2^(-(N-1)).
    v=[F(i+1,N*(N+1)//2) for i in range(N)]
    P=[[F(i==j,2)+v[i]/2 for j in range(N)] for i in range(N)]
    assert abs(determinant(P))==F(1,2**(N-1));check(P)
    # Vertex-shift half-simplex.
    P=[[F(i==j,2)+F(i==0,2) for j in range(N)] for i in range(N)]
    check(P)
    # Positive near-permutation matrices provide additional exact checks.
    for _ in range(20):
        columns=[]
        for j in range(N):
            a=[random.randint(0,10) for i in range(N)];a[j]+=1
            q=[F(x,sum(a)) for x in a]
            columns.append([F(9,10)*F(i==j)+q[i]/10 for i in range(N)])
        check([[columns[j][i] for j in range(N)] for i in range(N)])

# All-d comparison j/N >=1/2>gamma_d for d>=2.
for d in range(2,101):
    N=d+1;j=(N+1)//2
    assert F(j,N)>=F(1,2)>F(d,N)**d

# Distinguish the midpoint-fraction surrogate from actual endpoint costs.
N=16;d=15
midpoint_sum=1+d*F(N-2,N)**d
assert F(N,2)*F(d,N)**d-midpoint_sum==F(2088523134105583,144115188075855872)>0

print('PASS: determinant margin constants and endpoint-credit arithmetic')
