"""Standalone exact proof checks; standard library only."""
from fractions import Fraction as F
from itertools import product

P=((-1,-2),(-1,-1),(-1,0),(0,0),(0,1),(0,2),(1,2),(2,3))
t=(8,11,14,16,12,8,10,8)
G=tuple((*p,q) for p,q in zip(P,t))

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def diff(a,b):return tuple(x-y for x,y in zip(a,b))

base_facets=((-2,1,2),(-1,0,1),(-1,2,4),(5,-3,1))
assert all(dot(f[:2],p)<=f[2] for p in P for f in base_facets)
inside=tuple(p for p in product(range(-1,3),range(-2,4))
             if all(dot(f[:2],p)<=f[2] for f in base_facets))
assert inside==P
assert all(any(dot(f[:2],P[i])==f[2] for f in base_facets)
           for i in (0,2,5,7))
profile=((16,2,3),(16,2,-4),(16,-40,24))
assert tuple(min(a+b*p[0]+c*p[1] for a,b,c in profile) for p in P)==t
assert min(t[i] for i in (0,2,5,7))==8

roots={(1,0):2,(1,1):1,(0,0):3,(0,1):4}
for parity,i in roots.items():
    members=[j for j,p in enumerate(P) if tuple(x%2 for x in p)==parity]
    assert i in members
    assert all(t[i]>t[j] for j in members if j!=i)
forest=[]
for i,p in enumerate(P):
    v=roots[tuple(x%2 for x in p)]
    mid=tuple((x+y)//2 for x,y in zip(p,P[v]))
    w=P.index(mid)
    assert 2*t[w]==t[i]+t[v]
    forest.append(w)
assert forest==[1,1,2,3,4,4,4,6]

W=(0,1,3,4,6)
normals=((-5,-1,0),(-16,4,1),(-11,4,3),(-16,11,1),(-5,6,0))
assert [min(dot(n,diff(G[i],G[j])) for j in W if j!=i)
        for i,n in zip(W,normals)]==[1,7,8,7,1]
exclusions=((-9,4,1,16),(-5,3,-1,-9),(2,-1,0,0))
for f in exclusions:
    assert all(dot(f[:3],G[i])<=f[3] for i in W)
assert [dot(f[:3],G[i])-f[3] for f,i in zip(exclusions,(2,5,7))]==[7,7,1]
# Distinct vertices plus these exclusions give the exact five-set Helly
# witness described in the note, without any numerical hull routine.

lam=(F(1,2),F(1,6),F(1,3));inds=(0,2,7)
assert tuple(sum(a*P[i][j] for a,i in zip(lam,inds)) for j in range(2))==P[3]
assert sum(a*t[i] for a,i in zip(lam,inds))==9<t[3]

# R=1,d=2, in area units |standard simplex|/64.
weights=tuple((8+q)**2 for q in t)
assert weights==(256,361,484,576,400,256,324,256)
assert sum(weights)==2913
assert 4*max(weights)<sum(weights)
for a,b in ((3,5),(2,6)):
    assert tuple(F(x+y,2) for x,y in zip(G[a],G[b]))==G[4]
credit=weights[4]+min(weights[3],weights[5])+min(weights[2],weights[6])
assert credit==980 and 4*credit>sum(weights)
print('PASS: exact compatible profile, eight lattice bases, unique parity roots,')
print('zero forest slack, five-point centroid-graph Helly obstruction, and non-heavy OC certificate.')
