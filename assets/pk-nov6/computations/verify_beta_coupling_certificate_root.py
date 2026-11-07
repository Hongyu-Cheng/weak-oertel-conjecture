"""Independent verification using only the explicit rational certificate."""
from fractions import Fraction as F
from pathlib import Path
import json

d=json.loads(Path('./beta_coupling_exact_certificate_root.json').read_text())
n=d['n']; assert n==200 and d['Mn']==273 and d['Md']==100
ts=d['triples']; ms=list(map(F,d['mass']))
assert len(ts)==len(ms)==399 and all(m>0 for m in ms)
assert sum(ms)==1
p=[F(0) for _ in range(n)]; q=p.copy()
for (i,j,k),m in zip(ts,ms):
    assert all(isinstance(v,int) and 0<=v<n for v in (i,j,k))
    assert 2*(i+1)+(j+1)+(k+1)<=546
    p[i]+=m;q[j]+=m;q[k]+=m
assert p==[F(2*i+1,n*n) for i in range(n)]
assert q==[F(2*(2*i+1),n*n) for i in range(n)]
assert F(173,100)**2<3
print('PASS: 399 positive rational masses, all 400 exact marginal identities, total mass, and every support bound.')
