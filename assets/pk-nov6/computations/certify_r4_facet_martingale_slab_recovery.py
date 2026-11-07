"""Recover and verify an exact rational martingale from a support suggestion."""
from pathlib import Path
from fractions import Fraction as F
import json
import sympy as s
raw=json.loads(Path(__file__).with_name('r4_facet_martingale_lp_slab_recovery.json').read_text())
H=raw['high'];L=raw['low'];edges=[(i,j) for i,j,_ in raw['positive']]
A=s.zeros(4*len(H)+len(L),len(edges));b=s.zeros(A.rows,1)
for i,p in enumerate(H):
 b[4*i]=22
 for k in range(3):b[4*i+k+1]=22*p[k]
for j in range(len(L)):b[4*len(H)+j]=9
for e,(i,j) in enumerate(edges):
 A[4*i,e]=1
 for k in range(3):A[4*i+k+1,e]=L[j][k]
 A[4*len(H)+j,e]=1
sol,params=A.gauss_jordan_solve(b)
assert not params.rows
assert A*sol==b
assert all(v>0 for v in sol)
certificate=[]
for (i,j),v in zip(edges,sol):certificate.append([i,j,int(v.p),int(v.q)])
out={'high':H,'low':L,'source_mass':22,'target_mass':9,'edges':certificate}
Path(__file__).with_name('r4_facet_martingale_exact_slab_recovery.json').write_text(json.dumps(out,indent=2))
print('EXACT PASS:',len(edges),'positive rational masses; max denominator digits',max(len(str(v.q)) for v in sol))
