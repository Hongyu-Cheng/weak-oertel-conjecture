from itertools import combinations,product
from random import Random
rng=Random(2419)
def cr(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(pts):
 p=sorted(set(pts));lo=[];hi=[]
 for x in p:
  while len(lo)>1 and cr(lo[-2],lo[-1],x)<=0:lo.pop()
  lo.append(x)
 for x in reversed(p):
  while len(hi)>1 and cr(hi[-2],hi[-1],x)<=0:hi.pop()
  hi.append(x)
 return lo[:-1]+hi[:-1]
def inside(p,H):return all(cr(H[i],H[(i+1)%len(H)],p)>=0 for i in range(len(H)))
for trial in range(150000):
 H=hull([(rng.randrange(-5,6),rng.randrange(-5,6)) for _ in range(rng.randrange(3,8))])
 if len(H)<3:continue
 P={p for p in product(range(-5,6),repeat=2) if inside(p,H)}
 N={p:sum((2*p[0]-z[0],2*p[1]-z[1]) in P for z in P) for p in P}
 good=[p for p in sorted(P) if 4*N[p]>=len(P)]
 for p,q in combinations(good,2):
  if any((p[i]+q[i])%2 for i in range(2)):continue
  m=tuple((p[i]+q[i])//2 for i in range(2))
  if 4*N[m]<len(P):
   print('H',H,'count',len(P),'pqm',p,q,m,'counts',N[p],N[q],N[m],flush=True);print('P',sorted(P),flush=True);raise SystemExit
print('none')
