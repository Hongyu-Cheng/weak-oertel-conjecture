from fractions import Fraction as F
from itertools import combinations
import random
ns={};exec(open('./fractional-tverberg-search.py').read().split("if __name__")[0],ns)
hull=ns['hull'];points_in=ns['points_in']
def val(P,z):
 ds=[(p[0]-z[0],p[1]-z[1]) for p in P if p!=z]
 cand={(F(0),F(0))}
 for a,b in combinations(ds,2):
  D=a[0]*b[1]-a[1]*b[0]
  if not D:continue
  for s in [-1,1]:
   for t in [-1,1]:cand.add((F(s*b[1]-t*a[1],D),F(a[0]*t-b[0]*s,D)))
 best=None
 for a,b in cand:
  value=sum(max(F(0),min(F(2),1+a*(p[0]-z[0])+b*(p[1]-z[1]))) for p in P)
  if best is None or value<best[0]:best=(value,(a,b))
 return (best[0]/(2*len(P)),best[1])
if __name__=='__main__':
 random.seed(66212)
 for it in range(1000):
  h=hull([(random.randrange(-3,4),random.randrange(-3,4)) for _ in range(random.randrange(4,9))])
  if len(h)<3:continue
  P=points_in(h)
  if not 5<=len(P)<=17:continue
  vs={z:val(P,z) for z in P}
  for u,v in combinations(P,2):
   if any((u[k]+v[k])%2 for k in [0,1]):continue
   m=tuple((u[k]+v[k])//2 for k in [0,1])
   if vs[m][0]==min(vs[u][0],vs[v][0]) and vs[u][0]!=vs[v][0]:
    print('STRICT-MEAN COUNTER',h,'P',P,'values',vs,'triple',u,m,v,flush=True);raise SystemExit
   if 2*vs[u][0]*vs[v][0]>vs[m][0]*(vs[u][0]+vs[v][0]):
    print('HARMONIC COUNTER',h,'P',P,'values',vs,'triple',u,m,v,flush=True);raise SystemExit
  if it%20==0:print('screen',it,flush=True)
 print('complete',flush=True)
