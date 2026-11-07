#!/usr/bin/env python3
"""Exact finite source-fan certificate; no mixed-integer body inference here."""
from fractions import Fraction as Q
import json


def determinant(A):
    rows=[list(row) for row in A]
    n=len(rows)
    result=Q(1)
    for k in range(n):
        p=next(i for i in range(k,n) if rows[i][k])
        if p!=k:
            rows[k],rows[p]=rows[p],rows[k]
            result=-result
        pivot=rows[k][k]
        result*=pivot
        for i in range(k+1,n):
            multiplier=rows[i][k]/pivot
            for j in range(k+1,n):
                rows[i][j]-=multiplier*rows[k][j]
    return result


N=24
d=23
v=Q(1,4)
weight=Q(1,4)
alpha=Q(199,200)
gamma=Q(23,24)**23
records=[]
hit_counts=[0]*N
for a in range(3):
    R=[j for j in range(N) if j%3==a]
    J=[j for j in range(N) if j not in R]
    vertices=[]
    for r in R:
        for length in (1,2,3):
            lam=[Q(0)]*N
            for offset in range(length):
                lam[(r-offset)%N]=Q(1,length)
            vertices.append(lam)
    assert len(vertices)==N
    det=abs(determinant([[vertices[l][j] for l in range(N)] for j in range(N)]))
    assert det==Q(1,6**8)
    assert all(lam[j]<=lam[(j+1)%N] for lam in vertices for j in J)
    assert all(max(lam[r]-lam[(r+1)%N] for lam in vertices)==1 for r in R)
    centroid=[sum(lam[j] for lam in vertices)/N for j in range(N)]
    assert min(centroid)==Q(1,72)
    assert all(centroid[r]==Q(11,144) for r in R)
    shrunk=[[alpha*lam[j]+(1-alpha)*centroid[j] for j in range(N)] for lam in vertices]
    assert min(min(lam) for lam in shrunk)==Q(1,14400)
    strict_margin=min(lam[(j+1)%N]-lam[j] for lam in shrunk for j in J)
    assert strict_margin==Q(1,9600)
    assert all(max(lam[r]-lam[(r+1)%N] for lam in shrunk)==Q(637,640) for r in R)
    source_volume=v*det*alpha**d
    assert source_volume>Q(1,2**d)
    assert alpha**d>=1-d*(1-alpha)==Q(177,200)>Q(6561,8192)
    for r in R:hit_counts[r]+=1
    records.append({'rotation':a,'root_indices_zero_based':R,
                    'unshrunk_volume_ratio':str(det),
                    'centroid':list(map(str,centroid)),
                    'strict_source_absolute_volume_V_units':str(source_volume),
                    'minimum_barycentric_coordinate':str(Q(1,14400)),
                    'strict_miss_margin':str(strict_margin),
                    'root_hit_support_maximum':str(Q(637,640))})
assert hit_counts==[1]*N
score=v/2+weight
assert score==Q(3,8)<gamma
assert gamma*Q(999,1000)>score
assert 8*23**23>3*24**23
report={'verdict':'PASS_EXACT_FINITE_SOURCE_FAN_CERTIFICATE',
        'dimension':d,'N':N,'B_volume_V_units':str(v),
        'source_weights_V_units':[str(weight)]*3,
        'contraction':str(alpha),'all_24_scores_V_units':str(score),
        'gamma':str(gamma),'strict_gamma_gap':str(gamma-score),
        'gamma_times_999_over_1000_gap':str(gamma*Q(999,1000)-score),
        'source_volume_threshold_V_units':str(Q(1,2**d)),
        'source_records':records,
        'scope':'An exact finite simplex-source hitting-fan construction. Any implication for an actual mixed-integer body requires independent verification of the completion/reduction.'}
print(json.dumps(report,indent=2))
