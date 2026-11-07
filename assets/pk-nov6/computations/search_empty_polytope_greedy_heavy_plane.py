"""Numerical bounded greedy empty-polytopes screen; never a proof."""
import argparse,itertools,random,time,json
import numpy as np
from scipy.spatial import ConvexHull,QhullError
ap=argparse.ArgumentParser();ap.add_argument('--seconds',type=float,default=120);args=ap.parse_args()
rng=random.Random(3392);start=time.monotonic();stats=[0,0,0];best=0
B=np.array(list(itertools.product(range(-1,3),repeat=4)),dtype=int)
cube=list(map(tuple,itertools.product(range(2),repeat=4)))
def check(P):
  try:H=ConvexHull(np.array(P))
  except QhullError:return False
  if len(H.vertices)!=len(P):return False
  val=(B[:,None,:]*H.equations[None,:,:4]).sum(axis=2)+H.equations[None,:,4]
  return int(np.sum(np.max(val,axis=1)<=1e-7))==len(P)
def maxplane(P):
  P=np.array(P);co=np.array(list(itertools.combinations(range(len(P)),4)));A=P[co[:,1:]]-P[co[:,:1]]
  n=np.array([(-1)**j*np.linalg.det(np.delete(A,j,axis=2)) for j in range(4)]).T;sel=np.max(abs(n),axis=1)>1e-6;n=np.rint(n[sel]).astype(int);ii=co[sel,0]
  val=(P[None,:,:]*n[:,None,:]).sum(axis=2)-(P[ii]*n).sum(axis=1)[:,None]
  return int(np.max(np.sum(val==0,axis=1)))
last=start
pool=[]
while time.monotonic()-start<args.seconds:
  stats[0]+=1
  if pool and rng.random()<.7:
    P=rng.choice(pool).copy();rng.shuffle(P);P=P[:rng.randrange(5,len(P))]
  else:
    P=rng.sample(list(map(tuple,B)),5)
  if not check(P):continue
  inds=list(range(len(B)));rng.shuffle(inds)
  par={tuple(x%2 for x in p) for p in P}
  for k in inds:
    p=tuple(B[k]);pa=tuple(x%2 for x in p)
    if pa in par:continue
    if check(P+[p]):P.append(p);par.add(pa)
    if len(P)==16:break
  stats[1]+=1
  if len(P)>=12:
    pool.append(P)
    if len(pool)>100:pool.pop(rng.randrange(len(pool)))
  if len(P)>best:
    best=len(P);print('BESTSIZE',best,'plane',maxplane(P),json.dumps([[int(x) for x in p] for p in P]),flush=True)
  if len(P)==16:
    stats[2]+=1;ma=maxplane(P)
    if ma<8:print('CANDIDATE',json.dumps([[int(x) for x in p] for p in P]),flush=True);break
  if time.monotonic()-last>15:print('progress',stats,'best',best,'pool',len(pool),flush=True);last=time.monotonic()
print('DONE',stats,'best',best,flush=True)
