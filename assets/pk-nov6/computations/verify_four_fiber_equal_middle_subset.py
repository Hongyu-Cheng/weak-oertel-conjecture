"""Exact checks for the four-source equal-middle theorem and its tail limitation."""
from fractions import Fraction as F
from itertools import product


def area(poly):
    if len(poly)<3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(poly,poly[1:]+poly[:1])))/2


def clip(poly,u,t):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        a=u[0]*p[0]+u[1]*p[1]-t
        b=u[0]*q[0]+u[1]*q[1]-t
        if a>=0:
            out.append(p)
        if (a<0<b) or (b<0<a):
            s=a/(a-b)
            out.append((p[0]+s*(q[0]-p[0]),p[1]+s*(q[1]-p[1])))
    return out


for d in range(1,21):
    g=F(d,d+1)**d
    for a,c in product((F(1,10),F(1,3),F(1,2),F(1)),repeat=2):
        bound=g+max(a,c)/2
        target=g*(2+a+c)/2
        assert bound>=target
        assert bound-target >= (1-2*g)*(a+c)/4

K=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
g=(F(1,3),F(1,3));V=area(K);gamma=F(4,9)
normals=[(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(2,-1),(-1,2)]
subsets=[K]
for u,t in product(normals,(F(-1,4),F(0),F(1,4),F(1,2))):
    P=clip(K,u,t)
    if area(P)>0:
        subsets.append(P)
checks=0
for A,C in product(subsets,repeat=2):
    a,c=area(A),area(C)
    j=1 if a>=c else 2
    bound=gamma*V+max(a,c)/2
    for u,tilt in product(normals,(F(-3),F(-1),F(-1,3),F(0),F(1,3),F(1),F(3))):
        base=u[0]*g[0]+u[1]*g[1]
        captured=sum(area(clip(P,u,base-tilt*(z-j)))
                     for z,P in enumerate([A,K,K,C]))
        assert captured>=bound
        checks+=1
    for sign in (-1,1):
        captured=sum(area(P)for z,P in enumerate([A,K,K,C])if sign*(z-j)>=0)
        assert captured>=bound

r=[F(1),F(1)]+[1-F(k,100)for k in range(1,9)]
assert all(x>0 for x in r)
assert all(r[i]-r[i-1]>=r[i+1]-r[i]for i in range(1,9))
w=[x*x for x in r];M=sum(w)
assert M==F(23251,2500)
assert gamma*M/2-2==F(751,11250)>0
assert sum(w[:4])==F(39405,10000)<M/2
assert sum(w[5:])==F(44190,10000)<M/2
assert sum(w[2:])>M/2  # neither prescribed peak base is a median
assert sum(w[1:])>M/2
print(f"PASS: all selector arithmetic, {checks} exact triangular caps plus vertical caps, and complete plateau-tail counterexample")
