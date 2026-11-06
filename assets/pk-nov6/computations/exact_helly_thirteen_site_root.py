"""Exact convex-trace Helly number for the archived 13-site base."""
from fractions import Fraction as F
from itertools import combinations

P=[(0,0,1),(0,0,2),(0,0,3),(0,1,1),(0,1,2),(0,1,3),(0,2,1),
   (1,0,0),(1,0,1),(1,1,0),(1,1,1),(1,2,0),(2,0,0)]
N=len(P)
columns=[(1,)+p for p in P]
direct={}
for k in range(1,5):
    for ids in combinations(range(N),k):
        rows=[[F(columns[j][i]) for j in ids]
              +[F(col[i]) for col in columns] for i in range(4)]
        independent=True
        for c in range(k):
            pivot=next((r for r in range(c,4) if rows[r][c]),None)
            if pivot is None:
                independent=False
                break
            rows[c],rows[pivot]=rows[pivot],rows[c]
            scale=rows[c][c]
            rows[c]=[v/scale for v in rows[c]]
            for r in range(4):
                if r!=c and rows[r][c]:
                    scale=rows[r][c]
                    rows[r]=[v-scale*w for v,w in zip(rows[r],rows[c])]
        if not independent:
            continue
        contained=0
        for j in range(N):
            if all(rows[r][k+j]==0 for r in range(k,4)) and \
               all(rows[r][k+j]>=0 for r in range(k)):
                contained|=1<<j
        mask=sum(1<<j for j in ids)
        direct[mask]=contained

# Caratheodory in R^3: every closure point appears in a simplex of <=4 sites.
closure=[0]*(1<<N)
for mask in range(1,1<<N):
    result=mask|direct.get(mask,0)
    remaining=mask
    while remaining:
        bit=remaining&-remaining
        result|=closure[mask^bit]
        remaining^=bit
    closure[mask]=result

best=0
witnesses=[]
for mask in range(1,1<<N):
    count=bin(mask).count('1')
    if count<best:
        continue
    common=(1<<N)-1
    remaining=mask
    while remaining:
        bit=remaining&-remaining
        common&=closure[mask^bit]
        remaining^=bit
    if common==0:
        if count>best:
            best=count
            witnesses=[]
        witnesses.append(mask)
print("Exact finite convex-trace Helly number:",best)
print("Number of maximum witness sets:",len(witnesses))
for mask in witnesses[:5]:
    print("Witness:",[P[j] for j in range(N) if mask>>j&1])
print("Occupied parity classes:",len({tuple(x%2 for x in p) for p in P}))
