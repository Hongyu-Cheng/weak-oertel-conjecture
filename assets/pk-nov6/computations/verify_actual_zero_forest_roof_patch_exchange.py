"""Exact finite calibration and algebra for the roof-patch/mass-exchange note.
The general face and two-case proofs are in the note; no finite screen is used as a lemma.
"""
from fractions import Fraction as F
from itertools import product
P=[(-1,-2),(-1,-1),(-1,0),(0,0),(0,1),(0,2),(1,2),(2,3)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def radius(p):return min(1+F(p[1],4),F(17,25)-F(8,25)*p[0])
facets=[((-2,1),2),((-1,0),1),((-1,2),4),((5,-3),1)]
assert [p for p in product(range(-1,3),range(-2,4)) if all(dot(n,p)<=b for n,b in facets)]==P
r=[radius(p) for p in P]
assert r==list(map(lambda v:F(v,100),[50,75,100,68,68,68,36,4]))
assert all(v>0 for v in r) and min(r)==F(1,25)
roots={(1,0):2,(1,1):1,(0,0):3,(0,1):4}
for c,root in roots.items():
 cls=[i for i,p in enumerate(P) if tuple(t%2 for t in p)==c]
 assert all(r[root]>=r[i] for i in cls)
 ties=[i for i in cls if r[i]==r[root]]
 assert min(ties,key=lambda i:(dot(P[i],P[i]),P[i]))==root
edges=[(0,1,2),(5,4,3),(6,4,2),(7,6,4)]
G=[tuple(map(F,p))+(ri/2,) for p,ri in zip(P,r)]
for child,parent,partner in edges:
 assert tuple(P[child][j]+P[partner][j] for j in range(2))==tuple(2*v for v in P[parent])
 assert r[child]+r[partner]==2*r[parent]
 assert tuple(G[child][j]+G[partner][j] for j in range(3))==tuple(2*v for v in G[parent])
# The two graph lines, including BOTH points on the ray opposite point 2.
assert tuple(G[6][j]-G[4][j] for j in range(3))==tuple(G[4][j]-G[2][j] for j in range(3))
assert tuple(G[7][j]-G[4][j] for j in range(3))==tuple(2*(G[4][j]-G[2][j]) for j in range(3))
assert tuple(G[3][j]+G[5][j] for j in range(3))==tuple(2*G[4][j] for j in range(3))
# The two selected exposed upper patches, with exact boundary included.
E={0,1,2};QF={2,3,4,5,6,7}
# Plane E can be tilted in x1 so that only the line is exposed.
def majE(p):return 1+F(p[1],4)+(p[0]+1)
def majF(p):return F(17,25)-F(8,25)*p[0]
assert {i for i,p in enumerate(P) if majE(p)==r[i]}==E
assert {i for i,p in enumerate(P) if majF(p)==r[i]}==QF
assert all(majE(p)>=v and majF(p)>=v for p,v in zip(P,r))
assert E & QF=={2} and E|QF==set(range(8))
# Root 1 is relatively interior in E; root4 is relatively interior in F.
assert tuple(P[0][j]+P[2][j] for j in range(2))==tuple(2*P[1][j] for j in range(2))
# Four spanning vertices 2,3,5,7 have a strictly positive representation of point4.
lam=[F(1,2),F(1,8),F(1,8),F(1,4)]
assert sum(lam)==1 and tuple(sum(t*P[i][j] for t,i in zip(lam,[2,3,5,7])) for j in range(2))==P[4]
# Exact independent-patch budget failure.
w=[100*v for v in r];T=sum(w);WE=sum(w[i] for i in E);WF=sum(w[i] for i in QF)
assert (WE,WF,w[2],T)==(225,344,100,469)
assert max(WE/2,WF/3)==F(344,3)<T/4
assert T/4-WF/3==F(31,12)
# Root inequalities and the stronger grouped-ray budget.
assert w[0]<=w[2] and w[5]<=w[3]
assert max(w[6],w[7])<=w[4]<=w[2]
A,Gm,L,B,C=w[3],w[2],w[0]+w[1],w[4]+w[5],w[6]+w[7]
assert (A,Gm,L,B,C)==(68,100,125,136,40)
assert C<=2*w[4]<=w[4]+w[2]<=B+Gm
D=max(A,Gm,L,B+min(Gm,C))
assert D==176 and T<=4*D
# Both formal decompositions use each of A,G,L,B,C exactly once.
# The coordinate order is (A,G,L,B,C).
parts1=[(1,0,0,0,0),(0,1,0,0,0),(0,0,1,0,0),(0,0,0,1,1)]
parts2=[(1,0,0,0,0),(0,0,1,0,0),(0,1,0,1,0),(0,0,0,0,1)]
assert tuple(map(sum,zip(*parts1)))==(1,1,1,1,1)
assert tuple(map(sum,zip(*parts2)))==(1,1,1,1,1)
print('PASS: actual radii, forestresearch-agent orders, ray identities, patch gap31/12, and four-budget exchange')
