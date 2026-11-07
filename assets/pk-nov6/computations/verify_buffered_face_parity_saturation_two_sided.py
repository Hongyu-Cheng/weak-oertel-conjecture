#!/usr/bin/env python3
"""Exact small-base checks; proofs are in the companion Markdown source."""
from itertools import combinations
from fractions import Fraction as F

checks=0

def check(v):
    global checks
    assert v
    checks+=1

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def hull(P):
    P=sorted(set(P))
    if len(P)<=1:return tuple(P)
    lo=[]
    for p in P:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(P):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return tuple(lo[:-1]+hi[:-1])

def onseg(p,a,b):
    return cross(a,b,p)==0 and all(min(a[j],b[j])<=p[j]<=max(a[j],b[j]) for j in (0,1))

def inside(p,H):
    if len(H)==1:return p==H[0]
    if len(H)==2:return onseg(p,*H)
    return all(cross(a,b,p)>=0 for a,b in zip(H,H[1:]+H[:1]))

def maximal_faces(P):
    H=hull(P)
    if len(H)==1:return [frozenset(P)]
    if len(H)==2:
        return [frozenset(P)] if len(P)>2 else [frozenset([p]) for p in P]
    edges=[frozenset(p for p in P if onseg(p,a,b)) for a,b in zip(H,H[1:]+H[:1])]
    boundary=set().union(*edges)
    if set(P)-boundary:return [frozenset(P)]
    large=[e for e in edges if len(e)>2]
    covered=set().union(*large) if large else set()
    return large+[frozenset([p]) for p in H if p not in covered]

def colors(P):return {(p[0]%2,p[1]%2) for p in P}

def components(Fs):
    remain=list(Fs); out=[]
    while remain:
        C=set(remain.pop())
        while True:
            take=[f for f in remain if C.intersection(f)]
            if not take:break
            for f in take:C.update(f);remain.remove(f)
        out.append(frozenset(C))
    return out

grid=tuple((x,y) for x in range(-1,2) for y in range(-1,2))
seen=set()
for mask in range(1,1<<len(grid)):
    H=hull([p for i,p in enumerate(grid) if mask>>i&1])
    P=frozenset(p for p in grid if inside(p,H))
    if P in seen:continue
    seen.add(P)
    Fs=maximal_faces(P); Cs=components(Fs); k=len(colors(P)); m=len(Fs)
    check(m<=k)
    check((m==k)==(len(P)==k and set(hull(P))==set(P)))
    check(set().union(*Cs)==set(P))
    check(sum(len(C) for C in Cs)==len(P))
    check(sum(len(colors(C)) for C in Cs)==k)
    check(m<=k-sum(len(C)>1 for C in Cs))
    for C in Cs:
        CH=hull(C)
        check({p for p in grid if inside(p,CH)}==set(C))
        check(set(maximal_faces(C))==set(f for f in Fs if f.issubset(C)))
    for a,b in combinations(P,2):
        if colors([a])==colors([b]):
            mid=((a[0]+b[0])//2,(a[1]+b[1])//2)
            check(any({a,b,mid}.issubset(C) for C in Cs))
    # Every actual anchored relation has support inside one component:
    # in dimension two a minimal such support has size at most three.
    for z in P:
        for r in (1,2,3):
            for A in combinations(P,r):
                if inside(z,hull(A)):
                    # For a redundant support there need not be positive
                    # weights on every listed member. Restrict to relint.
                    HA=hull(A)
                    positive=(len(HA)==1 or (len(HA)==2 and z not in HA)
                              or (len(HA)==3 and all(cross(a,b,z)>0 for a,b in zip(HA,HA[1:]+HA[:1]))))
                    if positive:check(any(set(A).union([z]).issubset(C) for C in Cs))

# Exact interval counterexample arithmetic, with original total mass.
M=F(211,50); Q=F(11,10); MI=F(21,10)+F(46,25)
check(Q>=F(1,2)*MI/2)
check(Q/M==F(55,211))
check(MI/M==F(197,211))
check(F(1,2)*MI/2==F(197,200))
print(f'{checks} exact checks PASS; {len(seen)} complete bases on the 3x3 grid')
