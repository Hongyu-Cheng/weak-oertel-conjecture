"""Finite integer screen; printed cap normals provide exact certificates."""
from itertools import product,combinations
import numpy as np,json
J=4;roots=np.eye(4,dtype=np.int64)
K={tuple(p) for p in roots}
for c0,c1 in product(range(J),repeat=2):K.add(tuple(4*roots[0]-roots[c0]-2*roots[c1]))
K=np.array(sorted(K),dtype=np.int64);P=K[:,1:];N=len(P)
print('POINTS',N,K.tolist(),flush=True)
cert=[]
for ii,y in enumerate(P):
 D=P-y;D=D[np.any(D,axis=1)];best=N;bn=None
 for va,vb in combinations(D,2):
  n0=np.cross(va,vb)
  if not np.any(n0):continue
  for sign in (-1,1):
   n=sign*n0;on=D[D@n==0]
   for w in on:
    tangent=np.cross(n,w)
    for st,sw in product((-1,1),repeat=2):
     v=st*tangent*100+sw*w
     u=n*100000+v
     count=int(np.sum((P-y)@u>=0))
     if count<best:best=count;bn=u.copy()
 if bn is None:raise Exception(ii)
 cert.append((best,bn.tolist()))
 print('CAP',ii,best,bn.tolist(),flush=True)
print('MAX',max(x[0] for x in cert),'N',N,'CERT',json.dumps(cert),flush=True)
