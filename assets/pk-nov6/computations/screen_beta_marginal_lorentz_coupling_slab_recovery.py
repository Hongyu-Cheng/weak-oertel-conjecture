# Falsification of a marginal-only inequality; never an actual-body claim.
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
for n,M in [(40,2.731),(80,2.731),(120,2.731)]:
 v=np.sqrt(np.arange(1,n+1)/n)
 triples=np.array([(i,j,k) for i in range(n) for j in range(n) for k in range(n) if 2*v[i]+v[j]+v[k]<=M],dtype=np.int32)
 nv=len(triples);row=np.r_[triples[:,0],n+triples[:,1],2*n+triples[:,2]];col=np.tile(np.arange(nv),3)
 A=coo_matrix((np.ones(3*nv),(row,col)),shape=(3*n,nv)).tocsr()
 res=linprog(np.zeros(nv),A_eq=A,b_eq=np.full(3*n,1/n),bounds=(0,None),method='highs')
 print(n,M,nv,res.success,res.message,flush=True)
 if res.success:
  ix=np.where(res.x>1e-9)[0];print([(triples[i].tolist(),float(res.x[i])) for i in ix],flush=True);break
