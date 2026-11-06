from itertools import combinations,product
from random import Random
import numpy as np
rng=Random(835112)
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
def atom(P,w,p):
 v=np.array([(z[0]-p[0],z[1]-p[1]) for z in P],dtype=np.int64)
 vv=v[np.any(v!=0,axis=1)]
 n=np.array([(s*1000*dy+t*dx,-s*1000*dx+t*dy) for dx,dy in vv for s,t in product([-1,1],repeat=2)],dtype=np.int64)
 return int(np.min((n@v.T>=0)@np.array([w[z] for z in P],dtype=np.int64)))
for trial in range(50000):
 H=hull([(rng.randrange(-3,4),rng.randrange(-3,4)) for _ in range(rng.randrange(3,8))])
 if len(H)<3:continue
 P=sorted(p for p in product(range(-3,4),repeat=2) if inside(p,H));S=set(P)
 planes=[]
 for j in range(rng.randrange(2,7)):
  a,b=rng.randrange(-3,4),rng.randrange(-3,4)
  c=rng.randrange(1,6)-min(a*x+b*y for x,y in P)
  planes.append((c,a,b))
 r={p:min(c+a*p[0]+b*p[1] for c,a,b in planes) for p in P}
 w={p:r[p]**2 for p in P}
 Rp={p:sum(min(w[z],w[(2*p[0]-z[0],2*p[1]-z[1])]) for z in P if z<p and (2*p[0]-z[0],2*p[1]-z[1]) in S) for p in P}
 D={p:atom(P,w,p) for p in P}
 F={p:D[p]+Rp[p] for p in P}
 for p,q in combinations(P,2):
  if any((p[i]+q[i])%2 for i in range(2)):continue
  m=tuple((p[i]+q[i])//2 for i in range(2))
  if F[m]<min(F[p],F[q]):
   print('H',H,'N',len(P),'planes',planes,'pqm',p,q,m,'F',F[p],F[q],F[m],'D',D[p],D[q],D[m],'R',Rp[p],Rp[q],Rp[m],flush=True);print('P',P,flush=True);raise SystemExit
print('none')
