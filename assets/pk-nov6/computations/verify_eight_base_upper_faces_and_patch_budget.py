"""Exact upper-face, finite Helly, and revised-profile certificates."""
from fractions import Fraction as Q
from itertools import combinations, product

P=((-1,-2),(-1,-1),(-1,0),(0,0),(0,1),(0,2),(1,2),(2,3))
t=(8,11,14,16,12,8,10,8)
G=tuple((*p,z) for p,z in zip(P,t))
new=(50,75,100,68,68,68,36,4)

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross3(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

facets=set(); upper=set()
for i,j,k in combinations(range(8),3):
    n=cross3(sub(G[j],G[i]),sub(G[k],G[i]))
    if not any(n): continue
    for n0 in (n,tuple(-x for x in n)):
        b=dot(n0,G[i])
        if all(dot(n0,x)<=b for x in G):
            face=frozenset(h for h,x in enumerate(G) if dot(n0,x)==b)
            facets.add(face)
            if n0[2]>0: upper.add(face)
assert upper=={frozenset((0,1,2,3)),frozenset((2,3,4,5,6,7)),frozenset((0,3,7))}
for root,expected in ((1,{0,1,2}),(2,{2}),(3,{3}),(4,{2,3,4,5,6,7})):
    minimal=set.intersection(*(set(f) for f in facets if root in f))
    assert minimal==expected
    assert any(root in f for f in upper)

def hull(inds):
    pts=sorted((P[i],i) for i in inds)
    if len(pts)<=1:return [p[1] for p in pts]
    lo=[];hi=[]
    for p in pts:
        while len(lo)>1 and cross(lo[-2][0],lo[-1][0],p[0])<=0:lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi)>1 and cross(hi[-2][0],hi[-1][0],p[0])<=0:hi.pop()
        hi.append(p)
    return [p[1] for p in lo[:-1]+hi[:-1]]

def contains(point,inds):
    h=hull(inds)
    if len(h)==1:return point==P[h[0]]
    if len(h)==2:
        a,b=(P[i] for i in h)
        return cross(a,b,point)==0 and all(min(a[k],b[k])<=point[k]<=max(a[k],b[k]) for k in (0,1))
    return all(cross(P[h[j]],P[h[(j+1)%len(h)]],point)>=0 for j in range(len(h)))

for face in upper:
    found={q for q in product(range(-1,3),range(-2,4)) if contains(q,face)}
    assert found=={P[i] for i in face}
F=(2,3,4,5,6,7); E=(0,1,2)
quads=[]
for size in range(4,7):
    for W in combinations(F,size):
        if len(hull(W))<size:continue
        quads.append(W)
        kernel=[i for i in F if all(contains(P[i],tuple(j for j in W if j!=v)) for v in W)]
        assert kernel==[4]
assert quads==[(2,3,5,6),(2,3,5,7)]
assert {i for i in F if contains(P[i],(2,3,4))}=={2,3,4}
assert not any(all(contains(P[i],tuple(j for j in (2,3,4) if j!=v)) for v in (2,3,4)) for i in F)

assert all(Q(new[i],100)==min(1+Q(y,4),Q(17,25)-Q(8*x,25)) for i,(x,y) in enumerate(P))
assert min(new[i] for i in (0,2,5,7))==4
assert all(7*new[i]==76-274*x+100*y+25*t[i] for i,(x,y) in enumerate(P))
roots={(1,0):2,(1,1):1,(0,0):3,(0,1):4}
for parity,root in roots.items():
    inds=[i for i,p in enumerate(P) if tuple(x%2 for x in p)==parity]
    assert new[root]==max(new[i] for i in inds)
    ties=[i for i in inds if new[i]==new[root]]
    assert dot(P[root],P[root])==min(dot(P[i],P[i]) for i in ties)
    assert sum(dot(P[root],P[root])==dot(P[i],P[i]) for i in ties)==1
for i,w,v in ((0,1,2),(5,4,3),(6,4,2),(7,6,4)):
    assert tuple(P[i][j]+P[v][j] for j in (0,1))==tuple(2*x for x in P[w])
    assert new[i]+new[v]==2*new[w]
assert sum(new)==469 and sum(new[i] for i in E)==225 and sum(new[i] for i in F)==344
assert max(Q(225,2),Q(100),Q(68),Q(344,3))==Q(344,3)
assert Q(469,4)-Q(344,3)==Q(31,12)
assert new[4]+min(new[3],new[5])+min(new[2],new[6])==172
assert 4*172>469 and Q(86,469)>Q(1,8)
oldweights=tuple((8+x)**2 for x in t)
assert (sum(oldweights[i] for i in E),sum(oldweights[i] for i in F),oldweights[2],sum(oldweights))==(1101,2296,484,2913)
print("PASS: all upper facets, minimal root faces, projected lattice sets, h(F)=3,")
print("revised positive convex profile, canonical forest, and exact independent-patch budget gap")
