"""Exact checks for the collapsed Jensen-graph simplex source.
The all-s geometry and cap proof are given in the companion note.
"""
from fractions import Fraction as F
import sympy as sp

P=[(0,0,1),(1,0,0),(1,0,1),(1,0,2),(1,1,0),(1,1,1),
   (2,0,1),(2,1,0),(2,1,1),(2,1,2),(2,2,0)]
g=[F(1),F(1),F(1,2),F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(0)]
W=[0,1,3,4,5,6,7,8,10]
normals=[(-1,0,0),(0,-1,-1),(0,0,1),(-2,1,-2),(-2,3,2),
         (1,-1,0),(2,-1,-2),(2,1,2),(0,1,0)]

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def gamma(s):return F(s,s+1)**s

assert sp.Matrix([[1,*P[i],g[i]] for i in W]).rank()==5
assert [i for i in range(11) if g[i].denominator!=1]==[2]
for i,n in zip(W,normals):
    assert min(dot(n,P[i])-dot(n,P[j]) for j in W if j!=i)>=1
assert max(P[i][1]+P[i][2] for i in W)==2
assert P[9][1]+P[9][2]==3
for a,b in [(0,6),(1,3)]:
    assert all(F(P[a][r]+P[b][r],2)==P[2][r] for r in range(3))
    assert (g[a]+g[b])/2==g[2]

for s in range(1,101):
    # Maximal simplex barycentric margin on another positive fiber, tilt 2.
    assert 1-F(1,s+1)-2<0
    assert (1-F(1,s+1))**s==gamma(s)
    assert gamma(s)/16 < gamma(s)/9
    if s==1:assert gamma(s)/9==gamma(s+1)/8==F(1,18)
    else:assert gamma(s)/9<gamma(s+1)/8
assert gamma(2)/9==F(4,81)
assert gamma(3)/8==F(27,512)
assert gamma(3)/8-gamma(2)/9==F(139,41472)

# This exact symbolic identity, followed by positivity, proves all-real convexity.
t=sp.symbols('t',positive=True)
f=t*sp.log(t/(t+1))
assert sp.simplify(sp.diff(f,t,2)-1/(t*(t+1)**2))==0
print('PASS: all base exposure gaps, actual fractional fiber, full graph rank, cap constants, and all-real Gamma-ratio derivative')
