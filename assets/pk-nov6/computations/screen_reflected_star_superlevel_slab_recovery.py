from itertools import combinations
from random import Random
rng=Random(917)
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
for trial in range(30000):
 H=hull([(rng.randrange(-4,5),rng.randrange(-4,5)) for _ in range(rng.randrange(3,9))])
 if len(H)<3:continue
 P={p for p in __import__('itertools').product(range(-4,5),repeat=2) if inside(p,H)}
 N={p:sum((2*p[0]-z[0],2*p[1]-z[1]) in P for z in P) for p in P}
 for p,q in combinations(sorted(P),2):
  if any((p[i]+q[i])%2 for i in range(2)):continue
  m=tuple((p[i]+q[i])//2 for i in range(2))
  if N[m]<min(N[p],N[q]):
   print('H',H,'count',len(P),'pqm',p,q,m,'counts',N[p],N[q],N[m]);print('P',sorted(P));raise SystemExit
print('none')
