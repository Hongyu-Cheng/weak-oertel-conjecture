from itertools import product
import numpy as np,json
L=3;J=4;e=np.eye(J,dtype=np.int64);K=set(map(tuple,e));level={tuple(e[0])}
for l in range(L):
 level={tuple(2*np.array(k)-e[c]) for k in level for c in (1,2,3)};K.update(level)
K=np.array(sorted(K),dtype=np.int64);P=K[:,1:];N=len(K)
U=np.array([q for q in product(range(-12,13),repeat=3) if q!=(0,0,0)],dtype=np.int64)
U=np.vstack([U,np.random.default_rng(713).integers(-100000,100001,size=(100000,3))])
V=P@U.T;cert=[]
for i,k in enumerate(K):
 counts=np.sum(V>=V[i],axis=0);mi=int(np.argmin(counts));cert.append({'k':k.tolist(),'normal':U[mi].tolist(),'count':int(counts[mi])});print(i,k.tolist(),int(counts[mi]),U[mi].tolist(),flush=True)
print('MAX',max(c['count'] for c in cert),'N',N,flush=True)
open('./ternary_root_tree_depth_candidate.json','w').write(json.dumps(cert,indent=2))
