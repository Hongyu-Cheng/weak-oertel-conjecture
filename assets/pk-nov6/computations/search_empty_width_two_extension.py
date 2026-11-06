"""Exploratory width-two seed extension; exact certification required for conclusions."""
import itertools,numpy as np,time,random,json,argparse
from scipy.spatial import ConvexHull,QhullError
ap=argparse.ArgumentParser();ap.add_argument('--seconds',type=float,default=120);args=ap.parse_args()
start=time.monotonic();rng=random.Random(677);B=np.array(list(itertools.product(range(0,6),repeat=4)),dtype=int)
seed=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(2,2,3,5)]

def check(P):
 try:H=ConvexHull(np.array(P))
 except QhullError:return False
 if len(H.vertices)!=len(P):return False
 vals=(B[:,None,:]*H.equations[None,:,:4]).sum(axis=2)+H.equations[None,:,4]
 return np.sum(np.max(vals,axis=1)<=1e-7)==len(P)
assert check(seed)
# Retain width-two seed in every extension; any extra point must preserve emptiness.
options=[]
for p in B:
 p=tuple(p)
 if p in seed:continue
 if check(seed+[p]):options.append(p)
print('OPTIONS',len(options),flush=True)
bits=np.array(list(itertools.product(range(2),repeat=4))[1:])
def flatblocks(P):
 P=np.array(P);out=[]
 for n in bits:
  val=(P*n).sum(axis=1)%2
  for c in range(2):
   A=P[val==c]
   if np.linalg.matrix_rank(A[1:]-A[0],tol=1e-7)<4:out.append((list(map(int,n)),c))
 return out
count=0;best=5;bestplane=31;pool=[]
while time.monotonic()-start<args.seconds:
 count+=1
 if pool and rng.random()<.8:
  P=rng.choice(pool).copy()
  for _ in range(rng.randint(1,5)):
   old=rng.randrange(5,len(P));p=options[rng.randrange(len(options))]
   if tuple(x%2 for x in p)!=tuple(x%2 for x in P[old]):continue
   P[old]=p
  if not check(P):continue
  P=P[:5]+rng.sample(P[5:],rng.randrange(3,len(P)-4))
 else:P=seed.copy()
 order=options.copy();rng.shuffle(order)
 for p in order:
  if check(P+[p]):P.append(p)
 if len(P)>best:
  best=len(P);print('BEST',best,json.dumps([[int(x) for x in p] for p in P]),flush=True)
 if len(P)==16:
  ma=len(flatblocks(P))
  if ma<bestplane:
   bestplane=ma;pool=[];print('FLATBLOCKS',ma,json.dumps([[int(x) for x in p] for p in P]),flush=True)
  if ma<=bestplane+1:
   pool.append(P.copy())
   if len(pool)>150:pool.pop(rng.randrange(len(pool)))
  if ma==0:print('CANDIDATE',json.dumps([[int(x) for x in p] for p in P]),flush=True);break
print('DONE',count,best,flush=True)
