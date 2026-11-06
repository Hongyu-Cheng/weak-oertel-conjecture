"""Certify a numerical support with exact rational linear algebra."""
from fractions import Fraction as F
from pathlib import Path
import json
import numpy as np

data=np.load('./beta_weighted_coupling_column_root.npz')
n=int(data['n']); mn=int(data['Mn']); md=int(data['Md'])
triples=[tuple(map(int,t)) for t in data['triples']]
nv=len(triples)
rows=[{} for _ in range(2*n)]
rhs=[F(2*i+1,n*n) for i in range(n)]+[F(2*(2*i+1),n*n) for i in range(n)]
for c,(i,j,k) in enumerate(triples):
    assert 2*(i+1)+(j+1)+(k+1)<=mn*n//md
    for r in (i,n+j,n+k): rows[r][c]=rows[r].get(c,F(0))+1
active=set(range(2*n)); remain=set(range(nv)); equations=[]
while remain:
    candidates=[r for r in active if rows[r]]
    assert candidates
    r=min(candidates,key=lambda r:len(rows[r]))
    c=min(rows[r],key=lambda c:sum(c in rows[rr] for rr in active))
    v=rows[r][c]
    row={j:a/v for j,a in rows[r].items()}; b=rhs[r]/v
    equations.append((c,row,b))
    active.remove(r); remain.remove(c)
    for rr in active:
        a=rows[rr].pop(c,None)
        if a is None: continue
        for j,x in row.items():
            if j==c:continue
            z=rows[rr].get(j,F(0))-a*x
            if z: rows[rr][j]=z
            else:rows[rr].pop(j,None)
        rhs[rr]-=a*b
    if len(equations)%50==0:print('exact pivots',len(equations),flush=True)
for r in active:assert not rows[r] and not rhs[r]
mass=[F(0) for _ in triples]
for c,row,b in reversed(equations):
    mass[c]=b-sum(a*mass[j] for j,a in row.items() if j!=c)
assert all(t>0 for t in mass)
qa=[F(0) for _ in range(n)]; qb=qa.copy()
for t,(i,j,k) in zip(mass,triples):qa[i]+=t;qb[j]+=t;qb[k]+=t
assert qa==[F(2*i+1,n*n) for i in range(n)]
assert qb==[F(2*(2*i+1),n*n) for i in range(n)]
assert sum(mass)==1
out={'n':n,'Mn':mn,'Md':md,'triples':triples,'mass':[str(t) for t in mass]}
Path('./beta_coupling_exact_certificate_root.json').write_text(json.dumps(out))
print('PASS',n,nv,'positive exact masses; maximum weighted coordinate',F(max(2*(i+1)+j+k+2 for i,j,k in triples),n),flush=True)
