"""Finite LP over ALL interval families with given concave, base-balanced widths.
Numerical screen only; exact certificates must be separately verified.
"""
import numpy as np
from scipy.optimize import linprog
from itertools import product
import json

def solve_widths(w,z=None,full=True,tail_filter=None):
 w=np.asarray(w,float); N=len(w)
 if z is None:z=np.arange(N)-(N-1)//2
 z=np.asarray(z); anchor=int(np.flatnonzero(z==0)[0]); M=w.sum(); Q=w@w
 assert abs(w@z)<1e-7*M
 assert min(w)>0 and max(np.diff(w,2),default=0)<1e-7
 rows=[]; rhs=[]
 for i in range(1,N-1):
  r=np.zeros(N);r[i-1:i+2]=[1,-2,1]
  rows.extend([r,-r]);rhs.extend([0,-(w[i-1]-2*w[i]+w[i+1])])
 best=None
 for p in range(anchor+1):
  for q in range(anchor,N):
   for left,right in product([0,1],repeat=2):
    if not full and (left or right):continue
    if tail_filter is not None and not tail_filter(p,q,left,right,N):continue
    types=[left*2]*p+[1]*(q-p+1)+[right*2]*(N-1-q)
    c=np.array([t==1 for t in types],float)
    constant=sum(w[i] for i,t in enumerate(types) if t==2)
    bounds=[(None,0) if t==0 else (0,w[i]) if t==1 else (w[i],None) for i,t in enumerate(types)]
    res=linprog(c,A_ub=np.array(rows) if rows else None,b_ub=np.array(rhs) if rhs else None,A_eq=w.reshape(1,-1),b_eq=[Q/2],bounds=bounds,method='highs')
    if res.success:
     value=(res.fun+constant)/M
     if best is None or value<best['value']-1e-12:
      best=dict(value=value,z=z.tolist(),w=w.tolist(),r=res.x.tolist(),pattern=types,block=[p,q],tail=[left,right],Qover2mM=Q/(2*w.max()*M))
 return best

if __name__=='__main__':
 for w,z in [([1.5,1.5,1,.25],[-1,0,1,2]),([1,1,1],[-1,0,1]),([1,3,1],[-1,0,1]),([1,2,3,2,1],[-2,-1,0,1,2])]:
  print(json.dumps(solve_widths(w,z)))
