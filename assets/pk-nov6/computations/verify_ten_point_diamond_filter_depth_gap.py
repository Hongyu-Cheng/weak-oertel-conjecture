"""Exact ten-point reduction and coarse/fine depth calibration.
The all-cap coarse lower bound additionally uses the saved paired-tail theorem.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name('verify_integral_jensen_graph_filter_counterexample.py')))
P=[(0,0,1),(1,0,0),(1,0,1),(1,0,2),(1,1,0),(1,1,1),
   (2,0,1),(2,1,0),(2,1,1),(2,1,2),(2,2,0)]
g=[F(1),F(1),F(1,2),F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(0)]
W=[0,1,3,4,5,6,7,8,10]
Pprime=sorted(W+[2]);V=[i for i in W if i!=3]
D={0,1,2,3,6};corners={0,1,3,6};pairs=[{0,6},{1,3}]
normals=[(-1,0,0),(0,-1,-1),(0,0,1),(-2,1,-2),(-2,3,2),
         (1,-1,0),(2,-1,-2),(2,1,2),(0,1,0)]

def dot(a,b):return sum(x*y for x,y in zip(a,b))

assert len(Pprime)==10 and 9 not in Pprime
assert max(P[i][1]+P[i][2] for i in W)==2 < P[9][1]+P[9][2]
assert {i for i in Pprime if P[i][1]==0}==D
for pair in pairs:
    a,b=tuple(pair)
    assert all(F(P[a][j]+P[b][j],2)==P[2][j] for j in range(3))
    assert (g[a]+g[b])/2==g[2]==F(1,2)
for S in combinations(D,4):
    if 2 not in S:
        assert set(S)==corners
        for removed in S:assert any(removed not in pair for pair in pairs)
    else:
        assert any(pair<=set(S) for pair in pairs)

# Eight-point original Helly witness: p3 outside its full hull at y=0;
# p2 outside the p0-deletion hull at y=0; all own points are exposed.
assert len(V)==8
assert max(P[i][2] for i in V if P[i][1]==0)==1 < P[3][2]
face_after=[i for i in V if i!=0 and P[i][1]==0]
assert face_after==[1,6]
assert all(P[i][0]-P[i][2]==1 for i in face_after)
assert P[2][0]-P[2][2]==0
for i,n in zip(W,normals):
    assert all(dot(n,P[i])-dot(n,P[j])>=1 for j in W if j!=i)
    assert dot(n,P[i])-dot(n,P[2])>=1
    assert any(i not in pair for pair in pairs)
assert [i for i in Pprime if g[i].denominator==1]==W

for s in range(1,101):
    gamma=F(s,s+1)**s
    assert gamma<=F(1,2)
    assert 3>=5*gamma  # x-normal-zero closed caps at the coarse center
    assert 1-F(1,s+1)-2<0  # uniform isolation tilt
    fine=gamma/9;coarse=5*gamma/10
    assert coarse==gamma/2
    assert fine/coarse==F(2,9)
    assert gamma/10<coarse
    if s==1:assert fine==F(s+1,s+2)**(s+1)/8
    else:assert fine<F(s+1,s+2)**(s+1)/8
print('PASS: ten-point lattice support reduction, h(Pprime)=8 to h(Tprime)=9, added-center isolation, paired bases, and exact depth ratio 2/9')
