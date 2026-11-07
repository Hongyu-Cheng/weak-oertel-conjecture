"""Bounded exploratory LP; its output is not a proof without exact certification."""
from pathlib import Path
from itertools import product
import json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
P=[(x,y) for x in range(-4,5) for y in range(-4,5) if min(-x-y,2*x-y,2*y-x)>=-4]
hi=[];lo=[]
for x,y in P:
 e=(-x-y,2*x-y,2*y-x)
 for s in range(3):
  w=sum(t>0 for t in e)+(e[1]==0 and s>=1)+(e[2]==0 and s<=1)
  assert w in (1,2)
  (hi if w==2 else lo).append((x,y,s))
assert len(hi)==27 and len(lo)==66
n=len(hi)*len(lo);m=4*len(hi)+len(lo)
A=lil_matrix((m,n),dtype=float);b=np.zeros(m)
for i,p in enumerate(hi):
 b[4*i]=22
 for k in range(3):b[4*i+k+1]=22*p[k]
 for j,q in enumerate(lo):
  col=i*len(lo)+j;A[4*i,col]=1
  for k in range(3):A[4*i+k+1,col]=q[k]
  A[4*len(hi)+j,col]=1
b[4*len(hi):]=9
res=linprog(np.zeros(n),A_eq=A.tocsr(),b_eq=b,bounds=(0,None),method='highs')
print(res.message,flush=True)
out={'high':hi,'low':lo,'success':bool(res.success)}
if res.success:
 out['positive']=[(i//len(lo),i%len(lo),float(x)) for i,x in enumerate(res.x) if x>1e-8]
 print('positive',len(out['positive']),'minimum',min(x[2] for x in out['positive']),flush=True)
else:
 # Find an explicit convex separating support if infeasible later; no conclusion here.
 print('No finite-grid martingale found',flush=True)
Path(__file__).with_name('r4_facet_martingale_lp_slab_recovery.json').write_text(json.dumps(out,indent=2))
