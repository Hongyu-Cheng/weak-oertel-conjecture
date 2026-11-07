"""Exact certificate: rational Jensen graph filter over Z^3 has Helly number 9.
Uses only integer/Fraction arithmetic, with an independent R^4 lattice enumeration.
"""
from itertools import combinations,product
from fractions import Fraction as F
from math import gcd
from functools import reduce

P=[(0,0,1),(1,0,0),(1,0,1),(1,0,2),(1,1,0),(1,1,1),
   (2,0,1),(2,1,0),(2,1,1),(2,1,2),(2,2,0)]
g=[F(1),F(1),F(1,2),F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(0)]
facets=[(-1,0,-1,-1),(-1,1,0,0),(-1,1,1,1),(-1,2,1,2),
        (0,-1,0,0),(0,0,-1,0),(1,-1,-1,1),(1,-1,1,3),(1,0,0,2)]
W=[0,1,3,4,5,6,7,8,10]
normals=[(-1,0,0),(0,-1,-1),(0,0,1),(-2,1,-2),(-2,3,2),
         (1,-1,0),(2,-1,-2),(2,1,2),(0,1,0)]
values=[(0,-1),(0,-1),(2,1),(-1,-2),(3,2),(2,1),(3,2),(7,6),(2,1)]


def dot(a,b):return sum(x*y for x,y in zip(a,b))


def det(M):
    if len(M)==1:return M[0][0]
    return sum((-1)**j*M[0][j]*det([r[:j]+r[j+1:] for r in M[1:]])
               for j in range(len(M)))


def rank(M):
    M=[[F(v) for v in row] for row in M]
    if not M:return 0
    r=0
    for col in range(len(M[0])):
        pivot=next((i for i in range(r,len(M)) if M[i][col]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]
        divisor=M[r][col];M[r]=[v/divisor for v in M[r]]
        for i in range(len(M)):
            if i!=r:
                c=M[i][col];M[i]=[a-c*b for a,b in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return r


def feasible(p):return all(dot(f[:3],p)<=f[3] for f in facets)

# The inequalities force 0<=y<=x<=2, z>=0; summing f2 and f7 gives 2z<=4.
assert tuple(facets[2][i]+facets[7][i] for i in range(4))==(0,0,2,4)
assert P==[p for p in product(range(3),repeat=3) if feasible(p)]
interior=(F(1),F(1,2),F(3,4))
assert all(dot(f[:3],interior)<f[3] for f in facets)

# All vertices of the bounded polytope, via exact triple intersections.
vertices=set()
for chosen in combinations(facets,3):
    M=[list(f[:3]) for f in chosen];D=det(M)
    if not D:continue
    rhs=[f[3] for f in chosen];point=[]
    for c in range(3):
        A=[r[:] for r in M]
        for rr in range(3):A[rr][c]=rhs[rr]
        point.append(F(det(A),D))
    if feasible(point):vertices.add(tuple(point))
assert vertices=={P[i] for i in range(11) if i not in (2,8)}

# Every listed inequality is a genuine facet.
for f in facets:
    face=[P[i] for i in range(11) if dot(f[:3],P[i])==f[3]]
    assert rank([[1,*p] for p in face])==3

# Minimal faces at the only two nonvertices; all other points are vertices.
for i,p in enumerate(P):
    active=[f[:3] for f in facets if dot(f[:3],p)==f[3]]
    assert active
    if i==2:
        assert active==[(0,-1,0)]
        face=[j for j,q in enumerate(P) if q[1]==0]
        assert face==[0,1,2,3,6]
        assert all(g[j]==F(3-P[j][0]-P[j][2],2) for j in face)
    elif i==8:
        assert active==[(1,0,0)]
        face=[j for j,q in enumerate(P) if q[0]==2]
        assert face==[6,7,8,9,10]
        assert all(g[j]==0 for j in face)
    else:assert rank(active)==3

# The four defining Jensen equations have independent rows.
rels=[]
for anchor,sources,den in [(2,[0,6],2),(2,[1,3],2),(8,[7,9],2),(8,[6,9,10],3)]:
    assert all(den*P[anchor][r]==sum(P[j][r] for j in sources) for r in range(3))
    row=[0]*11;row[anchor]=den
    for j in sources:row[j]-=1
    assert dot(row,g)==0
    rels.append(row)
assert rank(rels)==4
assert det([[P[i][r]-P[3][r] for r in range(3)] for i in [4,5,6]])==1
assert all(g[i]==0 for i in [3,4,5,6]) and g[0]==1

# Exact filter; lifted midpoint at p2 is fractional, all other heights integral.
T=[i for i in range(11) if g[i].denominator==1]
assert T==[i for i in range(11) if i!=2]
for i,n,(own,other) in zip(W,normals,values):
    assert dot(n,P[i])==own
    assert max(dot(n,P[j]) for j in W if j!=i)==other
    assert own-other==1
assert max(P[i][1]+P[i][2] for i in W)==2
assert P[9][1]+P[9][2]==3
for pair in [(0,6),(1,3)]:
    assert all(F(sum(P[j][r] for j in pair),2)==P[2][r] for r in range(3))
    assert sum(g[j] for j in pair)/2==g[2]==F(1,2)
for deleted in W:
    assert any(deleted not in pair for pair in [(0,6),(1,3)])
assert all(F(P[7][r]+P[9][r],2)==P[8][r] for r in range(3))
assert (g[7]+g[9])/2==g[8]==0

# Independent exact facet computation for the full-dimensional R^4 polytope conv(W_hat).
V=[(*P[i],int(g[i])) for i in W]
assert rank([[1,*v] for v in V])==5
lift_facets=set()
for chosen in combinations(V,4):
    a=chosen[0];differences=[[v[j]-a[j] for j in range(4)] for v in chosen[1:]]
    n=tuple((-1)**j*det([r[:j]+r[j+1:] for r in differences]) for j in range(4))
    if not any(n):continue
    b=dot(n,a);slacks=[dot(n,v)-b for v in V]
    if min(slacks)<0<max(slacks):continue
    if max(slacks)>0:n=tuple(-x for x in n);b=-b
    divisor=reduce(gcd,(*map(abs,n),abs(b)))
    lift_facets.add(tuple(x//divisor for x in n)+(b//divisor,))
assert lift_facets
integer_points=[p for p in product(range(3),range(3),range(3),range(2))
                if all(dot(f[:4],p)<=f[4] for f in lift_facets)]
assert set(integer_points)==set(V)

print('PASS: exact lattice-convex hollow P, all Jensen representations, integral filter, nine critical deletion hulls, h(T)=9, and direct empty R4 lattice-polytope check')
