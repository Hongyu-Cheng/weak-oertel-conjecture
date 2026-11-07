#!/usr/bin/env python3
"""Exact actual-simplex obstruction to the stationary-weighted cap bridge."""
from fractions import Fraction as Q
from math import prod
import json
from exact_linear_algebra import solve

n=6
d=5
epsilon=Q(1,10000)
a=(1-3*epsilon)/2
J=(0,1)
R=(2,3,4,5)
P=[]
for j in range(n):
    large={1,2} if j==0 else ({0,2} if j==1 else {0,1})
    P.append([Q(0) if l==j else(a if l in large else epsilon) for l in range(n)])
assert all(sum(row)==1 for row in P)
assert all(P[j][l]>0 for j in range(n) for l in range(n) if j!=l)
stationary=[x[0] for x in solve(
    [[Q(i==j)-P[j][i] for j in range(n)] for i in range(n-1)]+[[Q(1)]*n],
    [[Q(0)]]*(n-1)+[[Q(1)]])]
assert all(q>0 for q in stationary) and sum(stationary)==1
assert all(sum(stationary[j]*P[j][l] for j in range(n))==stationary[l] for l in range(n))
root_mass=sum(stationary[r] for r in R)
assert root_mass==(1+3*epsilon)/(3-3*epsilon)==Q(10003,29997)
caps=[1/prod(1+p for p in row) for row in P]
p=1/((1+a)**2*(1+epsilon)**3)
assert all(cap==p for cap in caps)
weighted_cap=sum(w*cap for w,cap in zip(stationary,caps))
assert weighted_cap==p
gamma=Q(5,6)**5
assert root_mass<gamma
t=a/(1+a)
vertices=[]
for r in R:
    v=[Q(0)]*n
    v[r]=1
    vertices.append(v)
for j in J:
    v=[Q(0)]*n
    v[j]=t
    v[2]=1-t
    vertices.append(v)
assert all(v[j]<=sum(P[j][l]*v[l] for l in range(n)) for v in vertices for j in J)
assert all(any(v[r]>sum(P[r][l]*v[l] for l in range(n)) for v in vertices) for r in R)
rho=t*t
threshold=(weighted_cap-root_mass)/(2**d*(gamma-root_mass))
gap=rho-threshold
assert rho==Q(99940009,899820009)
assert threshold==Q(99849982000600210009,1970430673996059729663)
assert gap==Q(32126566933877094620869342,531963080350738233396309099)>0
contraction=Q(999,1000)
centroid=[sum(v[l] for v in vertices)/n for l in range(n)]
shrunk=[[contraction*v[l]+(1-contraction)*centroid[l] for l in range(n)] for v in vertices]
assert all(v[j]<sum(P[j][l]*v[l] for l in range(n)) for v in shrunk for j in J)
assert contraction**d*rho>threshold
print(json.dumps({
 'verdict':'PASS_ACTUAL_STATIONARY_WEIGHTED_BRIDGE_COUNTEREXAMPLE',
 'P':[[str(x) for x in row] for row in P],
 'stationary_distribution':list(map(str,stationary)),
 'stationary_hit_mass':str(root_mass),
 'vertices':[[str(x) for x in row] for row in vertices],
 'common_own_cap':str(p),
 'gamma':str(gamma),
 'actual_simplex_ratio':str(rho),
 'proposed_capacity_upper_bound':str(threshold),
 'strict_positive_gap':str(gap),
 'strict_miss_contraction_ratio':'999/1000',
 'scope':'Refutes the bridge assuming stationary hit mass<Gamma, not a version additionally imposing the unrelated uniform hit fraction<Gamma, and not Oertel.'
},indent=2))
