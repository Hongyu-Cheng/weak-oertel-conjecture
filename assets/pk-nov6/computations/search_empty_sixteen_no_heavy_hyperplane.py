"""Bounded numerical screening only; any output requires an exact certificate."""
import argparse,itertools,json,time,random
import numpy as np
from scipy.spatial import ConvexHull,QhullError
ap=argparse.ArgumentParser();ap.add_argument('--seconds',type=float,default=100);ap.add_argument('--seed',type=int,default=919);args=ap.parse_args()
rng=random.Random(args.seed);start=time.monotonic();stats=dict(generated=0,empty=0,widthscreen=0);best=16
cube=np.array(list(itertools.product(range(2),repeat=4)),dtype=int)
box=np.array(list(itertools.product(range(-1,3),repeat=4)),dtype=int)
comb=np.array(list(itertools.combinations(range(16),4)))
def maximum_plane(P):
  A=P[comb[:,1:]]-P[comb[:,:1]]
  norms=np.array([(-1)**j*np.linalg.det(np.delete(A,j,axis=2)) for j in range(4)]).T
  good=np.max(abs(norms),axis=1)>1e-6;norms=np.rint(norms[good]).astype(int);inds=comb[good,0]
  vals=(P[None,:,:]*norms[:,None,:]).sum(axis=2)-(P[inds]*norms).sum(axis=1)[:,None]
  return int(np.max(np.sum(vals==0,axis=1)))
def accept(P):
  global best
  stats['generated']+=1
  try:H=ConvexHull(P)
  except QhullError:return False
  if len(H.vertices)!=16:return False
  lo=P.min(axis=0);hi=P.max(axis=0)
  if np.prod(hi-lo+1)>1800:return False
  B=box if np.all(lo>=-1) and np.all(hi<=2) else np.array(list(itertools.product(*(range(int(a),int(b)+1) for a,b in zip(lo,hi)))))
  inside=np.max(np.sum(B[:,None,:]*H.equations[None,:,:4],axis=2)+H.equations[None,:,4],axis=1)<=1e-7
  if np.sum(inside)!=16:return False
  stats['empty']+=1
  # Only expensive all-normal screen after coordinate hyperplanes pass.
  score=max(max(np.unique(P[:,j],return_counts=True)[1]) for j in range(4))
  if score<8:
    stats['widthscreen']+=1;score=maximum_plane(P)
  if score<best:
    best=score;print('BEST',score,json.dumps(P.tolist()),json.dumps(stats),flush=True)
  if score<8:
    print('CANDIDATE',json.dumps(P.tolist()),flush=True);raise SystemExit
  return True
pool=[cube.copy()];last=start
while time.monotonic()-start<args.seconds:
  kind=stats['generated']%5
  if kind in (0,1):
    P=cube.copy()
    # Choose representatives in [-1,2]^4; favor a random affine cube initially.
    if kind==0:
      for i in range(16):
        for j in range(4):
          if rng.random()<.3:P[i,j]+=2*(1 if P[i,j]==0 else -1)
    else:
      for i in range(16):
        for j in range(4):
          if rng.random()<.5:P[i,j]+=2*(1 if P[i,j]==0 else -1)
  else:
    P=rng.choice(pool).copy()
    count=rng.choice([1,1,2,3,5,8])
    for i in rng.sample(range(16),count):
      j=rng.randrange(4);P[i,j]+=rng.choice([-2,2])
    if np.max(abs(P))>4:stats['generated']+=1;continue
  if accept(P):
    pool.append(P)
    if len(pool)>600:pool.pop(rng.randrange(len(pool)-1))
  if time.monotonic()-last>15:
    print('progress',stats,'pool',len(pool),'best',best,flush=True);last=time.monotonic()
print('DONE',stats,'pool',len(pool),'best',best,flush=True)
