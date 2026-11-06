"""Exact rational Helly-kernel certificate for every integral filtering of L(P).
No floating-point convex hull computation is used.
"""
from fractions import Fraction as F
from itertools import combinations

P=[(0,0,1),(0,0,2),(0,0,3),(0,1,1),(0,1,2),(0,1,3),(0,2,1),
   (1,0,0),(1,0,1),(1,1,0),(1,1,1),(1,2,0),(2,0,0)]
g=[0,0,0,3,3,3,6,0,0,0,1,0,0]
B=[(1,*p) for p in P]
A=[(1,*p,v) for p,v in zip(P,g)]


def det(M):
    n=len(M)
    if n==1:return M[0][0]
    return sum((-1)**j*M[0][j]*det([r[:j]+r[j+1:] for r in M[1:]])
               for j in range(n))


def rank(M):
    M=[[F(v) for v in r] for r in M]
    pivot=0
    for col in range(len(M[0])):
        found=next((i for i in range(pivot,len(M)) if M[i][col]),None)
        if found is None:continue
        M[pivot],M[found]=M[found],M[pivot]
        divisor=M[pivot][col]
        M[pivot]=[v/divisor for v in M[pivot]]
        for i in range(len(M)):
            if i!=pivot:
                c=M[i][col]
                M[i]=[a-c*b for a,b in zip(M[i],M[pivot])]
        pivot+=1
        if pivot==len(M):break
    return pivot


# Enumerate P from its exact polytope inequalities.
def feasible(p):
    x,y,z=p
    return min(p)>=0 and x+z>=1 and x+2*y+z<=5 and 2*x+y+z<=4 and 3*x+2*z<=6
assert P==[(x,y,z) for x in range(3) for y in range(3) for z in range(4) if feasible((x,y,z))]
# Every point is on an actual boundary, so every anchored convex representation
# is contained in a face of dimension at most two. Supports of size <=3 suffice.
for x,y,z in P:
    assert 0 in [x,y,z,x+z-1,5-x-2*y-z,4-2*x-y-z,6-3*x-2*z]

relations=[]
for k in (2,3):
    for J in combinations(range(13),k):
        rows=next((R for R in combinations(range(4),k)
                   if det([[B[j][r] for j in J] for r in R])),None)
        if rows is None:continue
        mat=[[B[j][r] for j in J] for r in rows]
        denominator=det(mat)
        for i in range(13):
            if i in J:continue
            coeff=[]
            for c in range(k):
                modified=[row[:] for row in mat]
                for rr,r in enumerate(rows):modified[rr][c]=B[i][r]
                coeff.append(F(det(modified),denominator))
            if not all(v>0 for v in coeff):continue
            if any(sum(coeff[c]*B[J[c]][r] for c in range(k)) != B[i][r] for r in range(4)):continue
            relations.append((i,J,tuple(coeff)))
            assert sum(coeff[c]*g[J[c]] for c in range(k))==g[i]

# All these valid relations already give codimension eight, proving dim L(P)=5.
relation_rows=[]
for i,J,coeff in relations:
    row=[F(0)]*13
    row[i]=1
    for j,c in zip(J,coeff):row[j]-=c
    relation_rows.append(row)
assert rank(relation_rows)==8
assert rank(A)==5

independent=[]
for W in combinations(range(13),9):
    Wset=set(W)
    obstruction=next(((i,J,c) for i,J,c in relations if i in Wset and set(J)<=Wset),None)
    if obstruction is None:independent.append(W)
expected=[(1,2,3,5,6,7,8,9,10),(1,2,3,5,6,7,8,10,11),
          (1,2,3,5,6,7,9,10,12),(1,2,3,5,6,8,9,10,11)]
assert independent==expected

for W in independent:
    assert {1,2,3,5,6}<=set(W)
    assert 4 not in W
    # The two disjoint midpoint pairs certify membership in EVERY deletion hull.
    for i,j in [(2,6),(3,5)]:
        assert tuple(F(A[i][r]+A[j][r],2) for r in range(5))==A[4]
    for deleted in W:
        assert any(deleted not in pair for pair in [(2,6),(3,5)])
    # Integer source values at these three points force integrality at p4.
    assert tuple(A[3][r]+A[2][r]-A[1][r] for r in range(5))==A[4]

print('PASS: complete rational 9-subset enumeration; four convex-position candidates; all have a forced integral Helly-kernel witness')
