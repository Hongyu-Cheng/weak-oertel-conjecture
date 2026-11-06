from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
old=json.loads(Path(__file__).with_name('r4_facet_martingale_exact_slab_recovery.json').read_text()); H=old['high']
for corner in [(-4,-4),(4,0)]:
 L=[q for q in old['low'] if tuple(q[:2])!=corner]
 n=len(H)*len(L); A=lil_matrix((4*len(H),n)); B=lil_matrix((len(L),n)); rhs=np.zeros(A.shape[0])
 for i,p in enumerate(H):
  rhs[4*i]=2
  for k in range(3):rhs[4*i+k+1]=2*p[k]
  for j,q in enumerate(L):
   e=i*len(L)+j; A[4*i,e]=1; B[j,e]=1
   for k in range(3):A[4*i+k+1,e]=q[k]
 res=linprog(np.zeros(n),A_eq=A.tocsr(),b_eq=rhs,A_ub=B.tocsr(),b_ub=np.full(len(L),1.),bounds=(0,None),method='highs')
 print(corner,res.message,flush=True)
 if res.success:
  out={'high':H,'low':L,'removed':corner,'source_mass':2,'target_capacity':1,'edges':[(i//len(L),i%len(L),float(v)) for i,v in enumerate(res.x) if v>1e-8],'tight':[j for j,q in enumerate(B@res.x) if abs(q-1)<1e-7]}
  Path(__file__).with_name('r4_one_outer_deleted_transport_%s_lp_slab_recovery.json'%('opposite' if corner==(-4,-4) else 'incident')).write_text(json.dumps(out,indent=2))
  print('support',len(out['edges']),'tight',len(out['tight']))
