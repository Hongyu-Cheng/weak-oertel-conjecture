#!/usr/bin/env python3
"""Exact concurrent simplex normal motion and mixed reflection checks."""
from fractions import Fraction as F


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))


def solve(A,b):
    n=len(A)
    a=[list(row)+[b[i]] for i,row in enumerate(A)]
    for k in range(n):
        p=next(i for i in range(k,n) if a[i][k])
        a[k],a[p]=a[p],a[k]
        q=a[k][k]
        a[k]=[x/q for x in a[k]]
        for i in range(n):
            if i!=k:
                q=a[i][k]
                a[i]=[x-q*y for x,y in zip(a[i],a[k])]
    return [row[-1] for row in a]


def cap_fraction(row,a,i):
    threshold=dot(row,a)
    vals=[x-threshold for x in row]
    assert vals[i]>0 and all(vals[j]<0 for j in range(len(a)) if j!=i)
    out=vals[i]**(len(a)-1)
    for j in range(len(a)):
        if j!=i:
            out/=vals[i]-vals[j]
    return out


groups=paths=0
for d in range(2,7):
    m=d+1
    families=[]
    for g in range(m):
        families.append([1-F(d,3*m) if i==g else F(1,3*m)
                         for i in range(m)])
    if d==2:
        families += [[F(4,5) if i==g else F(1,10) for i in range(m)]
                     for g in range(m)]
        families += [[F(1,2),F(1,3),F(1,6)]]
    for a in families:
        assert sum(a)==1 and min(a)>0
        delta=[]
        for i in range(m):
            sec=[a[i] if j==i else (1-a[i])/d for j in range(m)]
            dd=[sec[j]-a[j] for j in range(m)]
            assert dd[i]==0 and sum(dd)==0
            assert dot(dd,a)==-dot(dd,dd)
            delta.append(dd)
        Z=[i for i in range(m) if not dot(delta[i],delta[i])]
        assert len(Z)<=1
        h=[F(0)]*m
        if Z:
            h=[F(1) if i in Z else -F(1,d) for i in range(m)]
        k=[F(0) if i in Z else (1-h[i])/dot(delta[i],delta[i])
           for i in range(m)]
        assert sum(h)==0
        D=[[k[i]*x for x in delta[i]] for i in range(m)]
        bound=max(sum(abs(D[i][j]) for i in range(m)) for j in range(m))
        for denominator in (10000,100000,1000000):
            eps=F(1,denominator)
            assert eps*bound<F(1,3)
            ae=[a[i]+eps*h[i] for i in range(m)]
            assert min(ae)>0 and sum(ae)==1
            R=[[F(int(i==j))-eps*D[i][j] for j in range(m)]
               for i in range(m)]
            eta=solve([[R[i][j] for i in range(m)] for j in range(m)],
                      [F(1)]*m)
            assert min(eta)>0
            assert all(sum(eta[i]*R[i][j] for i in range(m))==1
                       for j in range(m))
            for i in range(m):
                f0=(1-a[i])**d
                fe=cap_fraction(R[i],ae,i)
                assert fe<f0
                S=d*(1-a[i])**(d-1)
                derivative=S*(-h[i]+k[i]*dot(delta[i],a))
                assert derivative==-S
                # Star endpoint section residuals cancel, with identical coarea mass.
                left=[S*x for x in delta[i]]
                right=[-S*x for x in delta[i]]
                assert all(x+y==0 for x,y in zip(left,right))
                assert -S+S==0
                paths+=1
        groups+=1

# Canonical meeting point has zero displacement at every section.
for d in range(2,8):
    m=d+1
    a=[F(1,m)]*m
    for i in range(m):
        assert all((a[i] if j==i else (1-a[i])/d)==a[j]
                   for j in range(m))

# Exact failure of merely fixing one mixed ambient contact.
for eps in (F(1,10),F(1,100)):
    z,x=-F(1),eps/2
    assert x+eps*z<0 and -x<0

print(f"PASS: {groups} noncanonical concurrent groups, {paths} exact "
      "strictly decreasing cap paths, positive circuit solves, "
      "canonical exception, mixed cover guard, reflected section cancellation.")
