"""Exact check on the archived rank-increasing 13-point canonical lift."""
from itertools import combinations, product
from math import gcd, lcm
import sympy as s

P=[(0,0,1),(0,0,2),(0,0,3),(0,1,1),(0,1,2),(0,1,3),(0,2,1),
   (1,0,0),(1,0,1),(1,1,0),(1,1,1),(1,2,0),(2,0,0)]
g=[0,0,0,3,3,3,6,0,0,0,1,0,0]
L=[p+(v,) for p,v in zip(P,g)]
assert s.Matrix([(1,)+p for p in P]).rank()==4
assert s.Matrix([(1,)+p for p in L]).rank()==5

# Enumerate supporting facet hyperplanes from every affine independent
# four-point set. All normal coefficients are integer, and all containment
# decisions below are exact.
facets=set()
for ids in combinations(range(len(L)),4):
    mat=s.Matrix([(1,)+L[i] for i in ids])
    if mat.rank()!=4:
        continue
    v=mat.nullspace()[0]
    den=lcm(*(int(x.q) for x in v))
    coeff=[int(x*den) for x in v]
    common=gcd(*coeff)
    coeff=tuple(x//common for x in coeff)
    vals=[sum(a*b for a,b in zip(coeff,(1,)+p)) for p in L]
    if min(vals)>=0:
        coeff=tuple(-x for x in coeff)
    elif max(vals)>0:
        continue
    facets.add(coeff)
assert facets

found=[]
for p in product(range(3),range(3),range(4),range(7)):
    if all(sum(a*b for a,b in zip(f,(1,)+p))<=0 for f in facets):
        found.append(p)
assert set(found)==set(L)
assert len({tuple(a%2 for a in p) for p in P})==8
assert len({tuple(a%2 for a in p) for p in L})==8
for m in range(2,8):
    for i,j in combinations(range(len(P)),2):
        old=all((a-b)%m==0 for a,b in zip(P[i],P[j]))
        new=all((a-b)%m==0 for a,b in zip(L[i],L[j]))
        assert old==new
print(f"PASS: {len(facets)} exact facets; all 13 lifted integer points and no extras")
print("PASS: rank rises from 3 to 4 while occupied parity count stays exactly 8")
print("PASS: all pairwise congruences checked for moduli 2 through 7")
