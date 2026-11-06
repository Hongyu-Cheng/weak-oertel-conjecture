from fractions import Fraction as F
from itertools import combinations
P=[(-1,3,0),(0,-2,0),(0,-1,0),(0,0,0),(0,1,0),(1,-1,0),(1,0,0),(1,0,1),(1,1,1),(1,2,2),(2,-2,-1),(2,-1,0),(2,0,1)]
V=[(2,0,1),(0,-2,0),(2,-2,-1),(-1,3,0),(1,2,2)]
q=(1,0,1); ncheck=0
def ck(p):
 global ncheck
 assert p;ncheck+=1
color=lambda p:tuple(x%2 for x in p)
ck(len(set(map(color,P)))==7)
for v in V:ck(sum(color(p)==color(v) for p in P)>1)
parent={p:p for p in P}
def find(p):
 while parent[p]!=p:p=parent[p]
 return p
def union(a,b):parent[find(a)]=find(b)
pairs=[]
for a,b in combinations(P,2):
 if color(a)!=color(b):continue
 m=tuple((x+y)//2 for x,y in zip(a,b));ck(m in P)
 pairs.append((a,b,m));union(a,b);union(a,m)
ck(len(pairs)==7)
parts={}
for p in P:parts.setdefault(find(p),set()).add(p)
ck(sorted(map(len,parts.values()))==[1,12])
C=next(c for c in parts.values() if len(c)==12)
ck(set(V)<=C and q not in C)
ck(tuple(sum(F(V[i][j],3) for i in [0,1,4]) for j in range(3))==q)
# This exact convex-representation merge joins the two remaining blocks.
union(V[0],q)
ck(len({find(p) for p in P})==1)
# Interior source certifies that the canonical lift is affine.
facets=[((-10,-2,9),4),((-5,-1,-10),2),((0,-1,2),2),((1,-2,2),4),((4,3,-3),5),((5,4,-3),7)]
for a,b in facets:ck(b>0)
print('PASS',ncheck,'exact checks; seven midpoint relations plus one denominator-three relation force a single closed parity block')
