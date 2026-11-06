from random import Random
from fractions import Fraction as F
from interval_centroid_search import hull, fibers, depth
r=Random(17273)
def fdepth(D,k):
 l,u=D[k]; m=(l+u)/2; total=sum(u-l for l,u in D.values())
 cand=[sum(u-l for j,(l,u) in D.items() if j<k)+(u-l)/2,sum(u-l for j,(l,u) in D.items() if j>k)+(u-l)/2]
 slopes=[(e-m)/(j-k) for j,B in D.items() if j!=k for e in B]
 for a in slopes:
  above=sum(max(0,min(u-l,u-m-a*(j-k))) for j,(l,u) in D.items())
  cand.extend([above,total-above])
 return min(cand)/total
best=1
for it in range(200000):
 W=r.randrange(2,9)
 P=hull([(r.randrange(W+1),r.randrange(-1000,1001)) for z in range(r.randrange(3,9))])
 if len(P)<3:continue
 D=fibers(P);Dfloat={k:tuple(map(float,B)) for k,B in D.items()}
 if sum(u-l for l,u in Dfloat.values())<=0:continue
 vals=[(fdepth(Dfloat,k),k) for k in Dfloat]
 v,k=max(vals)
 if v<best-1e-9:
  best=v;print('BEST',it,v,'k',k,'P',P,flush=True)
 if v<.25-1e-8:
  exact=[(depth(D,k),k) for k in D]
  print('CANDIDATE',P,exact,flush=True)
  if max(x[0][0] for x in exact)<F(1,4):break
