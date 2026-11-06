"""Bounded numerical screen around a width-two sixteen-vertex empty polytope."""
import itertools,numpy as np,time,random,json,argparse
from scipy.spatial import ConvexHull,QhullError
ap=argparse.ArgumentParser();ap.add_argument('--seconds',type=float,default=120);args=ap.parse_args();start=time.monotonic();rng=random.Random(981)
B=np.array(list(itertools.product(range(0,6),repeat=4)),dtype=int)
seed=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[2,2,3,5],[1,3,5,5],[0,0,0,2],[1,2,4,5],[1,1,2,3],[0,1,1,1],[0,1,3,2],[1,2,3,4],[0,1,2,1],[1,1,2,2],[1,1,1,2],[1,2,3,3]])
bits=np.array(list(itertools.product(range(2),repeat=4))[1:]);groups=[np.where(((seed*n).sum(axis=1)%2)==c)[0] for n in bits for c in range(2)]
options=[[p for p in B if np.all((p-seed[i])%2==0)] for i in range(16)]
def check(P):
 try:H=ConvexHull(P)
 except QhullError:return False
 if len(H.vertices)!=16:return False
 vals=(B[:,None,:]*H.equations[None,:,:4]).sum(axis=2)+H.equations[None,:,4]
 return np.sum(np.max(vals,axis=1)<=1e-7)==16
def flats(P):return [g for g in groups if np.linalg.matrix_rank(P[g[1:]]-P[g[0]],tol=1e-7)<4]
assert check(seed);assert len(flats(seed))==1
pool=[seed];attempts=0;accepted=0;last=start
while time.monotonic()-start<args.seconds:
 attempts+=1;P=rng.choice(pool).copy()
 for _ in range(rng.choice([1,1,1,2,2,3])):
  i=rng.randrange(16);P[i]=rng.choice(options[i])
 if not check(P):continue
 accepted+=1;F=flats(P)
 if not F:
  print('CANDIDATE',json.dumps(P.tolist()),attempts,accepted,flush=True);break
 if len(F)==1:
  pool.append(P)
  if len(pool)>100:pool.pop(rng.randrange(len(pool)))
 if time.monotonic()-last>15:print('progress',attempts,accepted,'pool',len(pool),flush=True);last=time.monotonic()
print('DONE',attempts,accepted,flush=True)
