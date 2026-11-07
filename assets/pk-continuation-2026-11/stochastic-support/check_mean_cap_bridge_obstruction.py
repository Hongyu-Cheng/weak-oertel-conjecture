#!/usr/bin/env python3
"""Exact actual-simplex counterexample to the proposed mean-cap capacity bridge."""
from fractions import Fraction as Q
from itertools import product
from math import prod
import json

n=6
d=5
J=range(4)
R=(4,5)
epsilon=Q(1,10000)
P=[]
for j in range(n):
    if j in J:
        row=[Q(0) if l==j else (1-4*epsilon if l==4 else epsilon)
             for l in range(n)]
    else:
        row=[Q(0) if l==j else Q(1,5) for l in range(n)]
    P.append(row)
assert all(sum(row)==1 for row in P)
assert all(P[j][j]==0 for j in range(n))
assert all(P[j][l]>0 for j,l in product(range(n),repeat=2) if j!=l)
t=(1-4*epsilon)/(2-4*epsilon)
vertices=[]
for r in R:
    v=[Q(0)]*n
    v[r]=1
    vertices.append(v)
for j in J:
    v=[Q(0)]*n
    v[j]=t
    v[4]=1-t
    vertices.append(v)
assert all(v[j]<=sum(P[j][l]*v[l] for l in range(n)) for v in vertices for j in J)
assert all(any(v[r]>sum(P[r][l]*v[l] for l in range(n)) for v in vertices) for r in R)
# Expansion in the four constrained rows leaves four diagonal t's and
# a two-by-two identity in surviving-root coordinates, up to permutation.
rho=t**4
gamma=Q(5,6)**5
caps=[1/prod(1+x for x in row) for row in P]
mean_cap=sum(caps)/n
hit_fraction=Q(2,6)
assert gamma>hit_fraction
threshold=(mean_cap-hit_fraction)/(2**d*(gamma-hit_fraction))
gap=rho-threshold
assert gap>0
assert rho==Q(39000037490001,624500149980001)
assert threshold==Q(156203494652860562789651,2558911628811531009068832)
assert gap==Q(449798683564218185227421478115819,319672073610396031852077442623411168)
# Even a homothetic contraction about the source centroid misses all J
# strictly and retains volume above the proposed upper bound.
contraction=Q(999,1000)
centroid=[sum(v[l] for v in vertices)/n for l in range(n)]
shrunk=[[contraction*v[l]+(1-contraction)*centroid[l] for l in range(n)] for v in vertices]
assert all(v[j]<sum(P[j][l]*v[l] for l in range(n)) for v in shrunk for j in J)
assert contraction**d*rho>threshold
print(json.dumps({
 'verdict':'PASS_ACTUAL_MEAN_CAP_BRIDGE_COUNTEREXAMPLE',
 'P':[[str(x) for x in row] for row in P],
 'vertices':[[str(x) for x in row] for row in vertices],
 'own_caps':list(map(str,caps)),
 'gamma':str(gamma),
 'actual_simplex_ratio':str(rho),
 'proposed_capacity_upper_bound':str(threshold),
 'strict_positive_gap':str(gap),
 'strict_miss_contraction_ratio':'999/1000',
 'strict_miss_source_volume_ratio':str(contraction**d*rho),
 'scope':'Counterexample only to the proposed mean-of-own-caps capacity bridge; no Oertel or sharp fan counterexample is asserted.'
},indent=2))
