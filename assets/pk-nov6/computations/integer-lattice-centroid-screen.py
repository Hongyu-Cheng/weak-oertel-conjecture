"""Exact-count screening of integral centroids of planar lattice polygons."""
import numpy as np
from scipy.spatial import ConvexHull
import json
rng=np.random.default_rng(864233)
grid=np.array([(x,y) for x in range(-9,10) for y in range(-9,10)],dtype=np.int64)
best=1.;accepted=0
for case in range(30000):
 v=np.unique(rng.integers(-9,10,size=(rng.integers(3,10),2)),axis=0)
 if len(v)<3:continue
 try:v=v[ConvexHull(v).vertices]
 except Exception:continue
 e=np.roll(v,-1,axis=0)-v
 cross=e[:,0,None]*(grid[None,:,1]-v[:,None,1])-e[:,1,None]*(grid[None,:,0]-v[:,None,0])
 P=grid[np.all(cross>=0,axis=0)];N=len(P)
 if N<3 or np.any(P.sum(axis=0)%N):continue
 accepted+=1;g=P.sum(axis=0)//N;Q=P-g
 qq=Q[np.any(Q!=0,axis=1)]
 normals=np.concatenate([np.stack([-qq[:,1]*100000+sgn*qq[:,0],qq[:,0]*100000+sgn*qq[:,1]],axis=1) for sgn in[-1,1]])
 counts=np.sum(Q@normals.T>=0,axis=0);j=int(np.argmin(counts));ratio=counts[j]/N
 if ratio<best:
  best=ratio; data=dict(case=case,N=N,centroid=g.tolist(),vertices=v.tolist(),normal=normals[j].tolist(),cap=int(counts[j]),ratio=float(ratio),accepted=accepted)
  print(json.dumps(data),flush=True)
  with open('./integer-lattice-centroid-screen-best.json','w') as f:json.dump(data,f,indent=2)
 if 4*counts[j]<N:break
print('finished',accepted,best,flush=True)
