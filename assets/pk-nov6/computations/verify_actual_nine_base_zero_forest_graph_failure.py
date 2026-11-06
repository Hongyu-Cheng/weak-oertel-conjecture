"""Standalone exact verifier for the actual nine-base graph obstruction."""
from fractions import Fraction as F
from itertools import product
from math import comb
P=[(1,1),(2,0),(2,1),(3,-2),(3,-1),(3,0),(3,1),(3,2),(4,3)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
facets=[((-3,-2),-5),((5,-1),17),((-2,3),1)]
assert [p for p in product(range(1,5),range(-2,4)) if all(dot(n,p)<=b for n,b in facets)]==P
V=[P[i] for i in (0,3,8)]
assert all(sum(dot(n,p)==b for n,b in facets)==2 for p in V)
assert all(all(dot(n,P[i])<b for n,b in facets) for i in (1,2,4,5,6,7))
t=[min(14,17-p[0]-2*p[1]) for p in P]
assert t==[14,14,13,14,14,14,12,10,7]
assert [t[i] for i in (0,3,8)]==[14,14,7] and min(t)==7
roots={(1,1):0,(0,0):1,(0,1):2,(1,0):5}
for c,v in roots.items():
 cls=[i for i,p in enumerate(P) if tuple(x%2 for x in p)==c]
 assert all(t[v]>=t[i] for i in cls)
 ties=[i for i in cls if t[i]==t[v]]
 assert min(ties,key=lambda i:(dot(P[i],P[i]),P[i]))==v
edges=[(3,4,5),(4,1,0),(6,2,0),(7,6,5),(8,7,2)]
parent={i:i for i in roots.values()}
for p,f,v in edges:
 assert tuple(P[p][j]+P[v][j] for j in range(2))==tuple(2*x for x in P[f])
 assert t[p]+t[v]==2*t[f]
 assert v==roots[tuple(x%2 for x in P[p])]
 parent[p]=f
for i in range(9):
 seen=set();p=i
 while p not in roots.values():
  assert p not in seen;seen.add(p);p=parent[p]
G=[p+(v,) for p,v in zip(P,t)]
rows=[((-1,0,0),-1,{0}),((-1,0,1),12,{0,1}),((-2,1,0),-3,{0,2}),
 ((0,-1,0),2,{3}),((0,-1,0),1,{3,4}),((1,1,1),17,{5}),
 ((3,3,2),36,{5,6}),((0,0,-1),-10,{7,8}),((0,0,-1),-7,{8})]
w=[21+x for x in t];assert w==[35,35,34,35,35,35,33,31,28] and sum(w)==301
masses=[]
for i,(u,b,cap) in enumerate(rows):
 assert dot(u,G[i])==b and {j for j,q in enumerate(G) if dot(u,q)>=b}==cap
 masses.append(sum(w[j] for j in cap))
assert masses==[35,70,69,35,70,35,68,59,28]
assert tuple(G[0][j]+G[4][j] for j in range(3))==tuple(2*G[1][j] for j in range(3))
assert w[0]==w[1]==w[4]==35
assert max(masses)==70 and F(70,301)==F(10,43)<F(1,4)
assert F(1,4)-F(10,43)==F(3,172)
# The displayed graph-to-ambient affine substitution.
for d in (1,2,5):
 for R in (0,21,63*d-7):
  for i,(u,b,cap) in enumerate(rows):
   actual=set()
   for j,p in enumerate(P):
    x=F(R+t[j],d+1)
    if u[0]*p[0]+u[1]*p[1]+(d+1)*u[2]*x>=b+R*u[2]:actual.add(j)
   assert actual==cap
# Finite exact calibrations of the explicitly proved all-d binomial inequality.
for d in range(1,21):
 R=63*d-7
 assert (1+F(1,9*d))**d<=sum(F(1,9)**k for k in range(d+1))<F(9,8)
 T=sum((R+x)**d for x in t)
 assert 8*(R+14)**d<T
 assert all(comb(d,k)<=d**k for k in range(d+1))
# Actual interval compensation at root1: three identical fibers, symmetric base pair.
assert tuple(P[0][j]+P[4][j] for j in range(2))==tuple(2*P[1][j] for j in range(2))
assert 3*F(35,2)==F(105,2)
assert F(105,2*301)==F(15,86)>F(1,8)
captured=[max(F(0),min(F(wi),F(wi)-F(p[0]+33,2))) for p,wi in zip(P,w)]
assert captured==list(map(F,[18,F(35,2),F(33,2),17,17,17,15,13,F(19,2)]))
assert sum(captured)==F(281,2)
print('PASS: actual support/body, canonical forest, all closed graph caps, exact10/43, and continuous compensation')
