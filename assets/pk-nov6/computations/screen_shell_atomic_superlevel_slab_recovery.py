from itertools import combinations,product
from random import Random
rng=Random(7512)
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
def atom(P,p):
 v=[(z[0]-p[0],z[1]-p[1]) for z in P if z!=p]
 return 1+min(sum(a*x+b*y>0 for x,y in v) for dx,dy in v for s,t in product([-1,1],repeat=2) for a,b in [(s*1000*dy+t*dx,-s*1000*dx+t*dy)])
for trial in range(10000):
 H=hull([(rng.randrange(-3,4),rng.randrange(-3,4)) for _ in range(rng.randrange(3,8))])
 if len(H)<3:continue
 P={p for p in product(range(-3,4),repeat=2) if inside(p,H)}
 N={p:sum((2*p[0]-z[0],2*p[1]-z[1]) in P for z in P) for p in P}
 D={p:atom(P,p) for p in P}
 F={p:D[p]+(N[p]-1)//2 for p in P}
 for p,q in combinations(sorted(P),2):
  if any((p[i]+q[i])%2 for i in range(2)):continue
  m=tuple((p[i]+q[i])//2 for i in range(2))
  if F[m]<min(F[p],F[q]):
   print('H',H,'N',len(P),'pqm',p,q,m,'F',F[p],F[q],F[m],'D',D[p],D[q],D[m],'starN',N[p],N[q],N[m],flush=True);print('P',sorted(P),flush=True);raise SystemExit
print('none')
