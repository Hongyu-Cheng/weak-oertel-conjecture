"""Exact certificate: ambient simplex, centroid midpoint, and own-middle caps.

Standard-library only. Numerical screens are not used.
"""
from fractions import Fraction as F
from math import comb, factorial
from itertools import permutations

checks = 0

def dd(knots, s, power):
    hs = sorted(map(F, knots))
    row = [max(t-s, F(0))**power for t in hs]
    for k in range(1, len(hs)):
        out = []
        for j in range(len(hs)-k):
            if hs[j] == hs[j+k]:
                assert hs[j] != s or k < power
                out.append(F(comb(power,k))*max(hs[j]-s,F(0))**(power-k)
                           if k <= power and hs[j] > s else F(0))
            else:
                out.append((row[j+1]-row[j])/(hs[j+k]-hs[j]))
        row = out
    return row[0]

def density(knots, s):
    s=F(s); m=len(knots)-1
    lo, hi=min(knots),max(knots)
    if s<lo or s>hi: return F(0)
    if s==lo or s==hi:
        if knots.count(s) != m: return F(0)
        other=next(t for t in knots if t!=s)
        return F(m)/abs(other-s)
    return m*dd(knots,s,m-1)

def moment(knots,s,i):
    return density([*knots,knots[i]],s)/len(knots)

def det(A):
    n=len(A)
    return sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
               *product(A[i][p[i]] for i in range(n))
               for p in permutations(range(n)))

def product(xs):
    ans=F(1)
    for x in xs: ans*=x
    return ans

h=list(map(F,[0,4,0,0,1,3,3]))
vertices=[(0,0,0,0,0,0),(4,0,0,0,0,0)]
vertices += [tuple([int(h[i+2])]+[int(j==i) for j in range(5)])
             for i in range(5)]
matrix=[[F(vertices[j+1][i]-vertices[0][i]) for j in range(6)]
        for i in range(6)]
V=abs(det(matrix))/factorial(6)
assert V==F(1,180)

def bary(z,x):
    starred=(z-x[2]-3*x[3]-3*x[4])/4
    return [1-sum(x)-starred,starred,*x]

for i, vertex in enumerate(vertices):
    bs=bary(F(vertex[0]),list(map(F,vertex[1:])))
    assert bs==[F(j==i) for j in range(7)]
    checks+=1

def f_formula(s):
    p=lambda t:max(t-s,F(0))
    return p(4)**5/32-F(5,9)*p(3)**4+p(3)**5/18-p(1)**5/2

for s in [F(k,24) for k in range(97)]:
    f=density(h,s)
    assert f==f_formula(s)>=0
    js=[moment(h,s,i) for i in range(7)]
    assert sum(js)==f
    assert sum(h[i]*js[i] for i in range(7))==s*f
    checks+=1

weights=[density(h,F(j)) for j in range(5)]
assert weights==[0,F(139,288),F(1,2),F(1,32),0]
M=sum(weights)
assert M==F(73,72)
assert [w/M for w in weights[1:4]]==[F(139,292),F(144,292),F(9,292)]
assert all(0<w<M/2 for w in weights[1:4])

centers={j:[moment(h,F(j),i)/weights[j] for i in range(7)]
         for j in (1,2,3)}
assert centers[1][2:]==[F(5801,30024),F(5801,30024),F(1,6),
                        F(227,2502),F(227,2502)]
assert centers[3][2:]==[F(1,24),F(1,24),F(1,18),F(1,6),F(1,6)]
assert centers[2]==[F(25,243),F(5,27),F(25,243),F(25,243),
                    F(7,54),F(61,324),F(61,324)]
for j,c in centers.items():
    assert sum(c)==1 and min(c)>0 and sum(t*x for t,x in zip(h,c))==j
    assert bary(F(j),c[2:])==c
    checks+=1
mid=[(a+b)/2 for a,b in zip(centers[1],centers[3])]
assert mid[2:]==[F(1763,15012),F(1763,15012),F(1,9),
                F(161,1251),F(161,1251)]
assert min(mid)>0 and sum(h[i]*mid[i] for i in range(7))==2
assert centers[1][1]==F(241,3336) and centers[3][1]==F(35,72)
assert mid[1]==F(1397,5004)>F(1,4)

def cap_contributions(i,c):
    return [(1-c)**5*density(h,(F(j)-c*h[i])/(1-c)) for j in range(5)]

cs=cap_contributions(1,F(1,4))
assert cs[0]==cs[1]==cs[4]==0
assert sum(cs)==F(559,3072)
assert sum(cs)/M==F(1677,9344)
target=F(5,6)**5/2
assert target*M-sum(cs)==F(48739,2239488)>0
assert sum(cap_contributions(1,mid[1]))/M==F(
    4150356952177626013,28629870146058409344)<target
checks+=2

expected={
    0:F(1208406711707,2290817351457),
    1:F(96895537,349156737),
    2:F(1208406711707,2290817351457),
    3:F(1208406711707,2290817351457),
    4:F(59476257373,134076187008),
    5:F(31539470594257,115841825574912),
    6:F(31539470594257,115841825574912)}
for i in range(7):
    c=centers[2][i]
    upper=sum(cap_contributions(i,c))/M
    assert upper==expected[i]
    assert target<upper<1-target
    # Continuous normal of lambda_i is nonzero: complementary caps
    # have no full-dimensional boundary mass on the positive fibers.
    assert any(bary(0,[F(j==k) for j in range(5)])[i]
               !=bary(0,[F(0)]*5)[i] for k in range(5))
    checks+=1

print(f"PASS: {checks} exact checks; midpoint refuted, all 14 own-middle canonical orientations above target.")
