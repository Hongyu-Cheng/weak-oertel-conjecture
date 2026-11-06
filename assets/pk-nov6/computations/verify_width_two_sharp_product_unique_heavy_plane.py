"""Exact certificate; standard library only. No numerical geometry is used."""
from itertools import combinations,product
from math import gcd
from functools import reduce
from fractions import Fraction

P=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(2,2,3,5),(1,3,5,5),(0,0,0,2),(1,2,4,5),(1,1,2,3),(0,1,1,1),(0,1,3,2),(1,2,3,4),(0,1,2,1),(1,1,2,2),(1,1,1,2),(1,2,3,3))
def det(A):
 n=len(A)
 if n==0:return 1
 return sum((-1)**j*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(n))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def difference(a,b):return tuple(x-y for x,y in zip(a,b))
assert len(set(P))==16
assert len({tuple(x%2 for x in p) for p in P})==16
# Full dimension.
assert det([list(difference(P[i],P[0])) for i in (1,2,3,4)])!=0
# Enumerate every possible facet using four affine-independent vertices.
facets=set()
for I in combinations(range(16),4):
 A=[list(difference(P[i],P[I[0]])) for i in I[1:]]
 n=tuple((-1)**j*det([row[:j]+row[j+1:] for row in A]) for j in range(4))
 if not any(n):continue
 b=dot(n,P[I[0]])
 vals=[dot(n,p)-b for p in P]
 if min(vals)<0<max(vals):continue
 if max(vals)>0:n=tuple(-x for x in n);b=-b
 g=reduce(gcd,map(abs,(*n,b)))
 facets.add(tuple(x//g for x in (*n,b)))
facets=sorted(facets)
assert all(dot(f[:4],p)<=f[4] for f in facets for p in P)
# The generated supporting polytope has no additional vertices: its facets
# are all true facets of conv(P), and all true facets were enumerated above.
# Bounding box follows directly from convex hull; enumerate every possible
# integer point and test exact facet inequalities.
inside={z for z in product(range(3),range(4),range(6),range(6)) if all(dot(f[:4],z)<=f[4] for f in facets)}
assert inside==set(P),(inside-set(P),set(P)-inside)
# Vertex exposure is certified by the sum of all active outward normals.
expose=[]
for i,p in enumerate(P):
 n=tuple(sum(f[j] for f in facets if dot(f[:4],p)==f[4]) for j in range(4))
 gaps=[dot(n,difference(p,q)) for q in P if q!=p]
 assert min(gaps)>0,(i,n,gaps)
 expose.append((n,min(gaps)))
# A hyperplane containing eight points has primitive integer normal,
# so its eight vertices are exactly one affine F2-hyperplane class.
flat=[];rank_cert=[]
for n in product(range(2),repeat=4):
 if not any(n):continue
 for c in range(2):
  I=[i for i,p in enumerate(P) if dot(n,p)%2==c]
  assert len(I)==8
  witness=None
  for J in combinations(I[1:],4):
   D=det([list(difference(P[i],P[I[0]])) for i in J])
   if D:witness=(I[0],*J,D);break
  if witness is None:flat.append((n,c,I))
  else:rank_cert.append((n,c,witness))
assert len(flat)==1 and flat[0][:2]==((1,0,0,0),1)
assert all(P[i][0]==1 for i in flat[0][2])
assert det([list(difference(P[i],P[0]))[1:] for i in (5,7,8)])==1
assert min(p[0] for p in P)==0 and max(p[0] for p in P)==2
# Every proper supporting hyperplane has at most seven points.
assert max(sum(dot(f[:4],p)==f[4] for p in P) for f in facets)==7
# Exact width is two: x1 has width2. The seed e_i,(2,2,3,5)
# has no width1: if the integer values at e_i lie in {a,a+1},
# a belongs to {-1,0} and subset sums of 2,2,3,5 must be 11,12 or0,1.
# Only sums0,12 are possible, both yielding zero normal.
weights=(2,2,3,5)
assert {sum(w*b for w,b in zip(weights,bits)) for bits in product(range(2),repeat=4)}.isdisjoint({1,11})
print('PASS: 16 exposed lattice vertices; width exactly 2; unique half-cardinality hyperplane x1=1; every supporting hyperplane has <=7 vertices.')
print('FACETS',len(facets),facets)
print('EXPOSING_NORMALS',expose)
print('RANK_CERTIFICATES',rank_cert)

# Uniform-in-epsilon weighted calibration uses an affine inequality.
for e in (Fraction(0),Fraction(1,30)):
 A=1-2*e;B=1+2*e
 assert 8*A+8*B==16
 assert 8*A/16==Fraction(1,2)-e
 assert 7*B/16<=Fraction(1,2)-e
 assert B/A<=Fraction(8,7)
print('PASS: weighted all-hyperplane calibration for 0<=epsilon<=1/30 by endpoint verification of the affine budget inequality.')
