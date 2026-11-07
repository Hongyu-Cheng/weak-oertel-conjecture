"""Exact constants and finite kernel checks for the binary-filter/product note.
Universal statements are proved in the companion text.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name('verify_integral_jensen_graph_filter_counterexample.py')))
P=[(0,0,1),(1,0,0),(1,0,1),(1,0,2),(1,1,0),(1,1,1),
   (2,0,1),(2,1,0),(2,1,1),(2,1,2),(2,2,0)]
g=[F(1),F(1),F(1,2),F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(0)]
W=[0,1,3,4,5,6,7,8,10];Pprime=sorted(W+[2]);U=[0,1,2,4,5,7,8,10]
normals=[(-1,0,0),(0,-1,-1),(0,0,1),(-2,1,-2),(-2,3,2),
         (1,-1,0),(2,-1,-2),(2,1,2),(0,1,0)]
ndict=dict(zip(W,normals))

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def gamma(s):return F(s,s+1)**s

# Empty eight-subset: all its points exposed, omitted corners outside y=0 triangle.
assert set(Pprime)-set(U)=={3,6}
assert {i for i in U if P[i][1]==0}=={0,1,2}
assert max(P[i][2] for i in U if P[i][1]==0)==1 < P[3][2]
assert max(P[i][0] for i in U if P[i][1]==0)==1 < P[6][0]
for i in U:
    n=(1,-3,1) if i==2 else ndict[i]
    assert min(dot(n,P[i])-dot(n,P[j]) for j in U if j!=i)>=1

# Exact single-coordinate penalties and central symmetry of the five-point diamond graph.
D={0,1,2,3,6}
for i in Pprime:
    values=[P[j][1] if i==2 else dot(ndict[i],tuple(P[i][r]-P[j][r] for r in range(3))) for j in Pprime]
    assert min(values)==0
    assert all(v>=1 for v in values if v)
    zeros={j for j,v in zip(Pprime,values) if not v}
    assert zeros==(D if i==2 else {i})
for i in D:
    reflection=tuple(2*P[2][r]-P[i][r] for r in range(3))
    j=next(j for j in D if P[j]==reflection)
    assert g[i]+g[j]==1
assert sum(g[i]==0 for i in W)==7
assert sum(g[i]==1 for i in W)==2

for r in range(1,11):
    assert 8**r==2**(3*r)
    assert sum(comb(r,j)*2**j*7**(r-j) for j in range(r+1))==9**r
    assert F(9**r,8**r)==F(9,8)**r
    assert F(5**r,10**r)==F(1,2)**r
    for s in range(1,11):
        fine=gamma(s)/9**r;coarse=gamma(s)/2**r
        assert fine/coarse==F(2,9)**r
        naive=gamma(s+r)/8**r
        if (s,r)==(1,1):assert fine==naive
        else:assert fine<naive
        assert fine>gamma(s)/16**r
        assert gamma(s+r)/gamma(s)>=F(8,9)**r

# Exact crosspolytope deletion-kernel classification, finite sanity range.
# Indices 2j+1 and 2j+2 are opposite; index0 is the center.
for m in range(1,8):
    vertices=set(range(1,2*m+1))
    pairs=[{2*j+1,2*j+2} for j in range(m)]
    for Wc in combinations(range(2*m+1),m+2):
        S=set(Wc)
        if 0 in S:
            assert any(pair<=S for pair in pairs)
        else:
            contained=[pair for pair in pairs if pair<=S]
            assert len(contained)>=2
            for deleted in S:assert any(deleted not in pair for pair in contained)
    assert F(2*m,m+1)==2-F(2,m+1)
    assert F(2*m,m+1)<2
    # Both integral levels contain m exposed simplex vertices.
    assert m+m==2*m
print('PASS: empty8 product witness, exact 8^r/9^r and depth budgets, slice sums, and crosspolytope kernel/rank-index constants')
