from fractions import Fraction as F
checks=0
def ck(x):
 global checks
 assert x
 checks+=1

def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(points):
 pts=sorted(set(points)); lo=[];hi=[]
 for p in pts:
  while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
  lo.append(p)
 for p in reversed(pts):
  while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
  hi.append(p)
 return lo[:-1]+hi[:-1]
def area(P):return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[i][1]*P[(i+1)%len(P)][0] for i in range(len(P))))/2 if P else F(0)
def clip(P,u,t):
 out=[]
 for p,q in zip(P,P[1:]+P[:1]):
  a=sum(x*y for x,y in zip(u,p))-t;b=sum(x*y for x,y in zip(u,q))-t
  if a>=0:out.append(p)
  if (a<0<b) or (b<0<a):
   lam=a/(a-b);out.append(tuple(p[i]+lam*(q[i]-p[i]) for i in range(2)))
 return out
def add(A,B):return hull([tuple(a[i]+b[i] for i in range(2)) for a in A for b in B])
def union_miss(P):return area(P)-area(clip(clip(P,(F(1),F(0)),0),(F(0),F(1)),0))
B=hull([(F(1),F(1)),(F(1),F(-2)),(F(-2),F(1))])
for height in (F(2),F(5,2),F(3),F(4)):
 p=(height+2,F(-2));q=(F(-2),height+2)
 A=hull([p,q,(F(0),F(0))]);P=[p,q]
 b=area(B);a=area(A);PB=add(P,B);AB=add(A,B)
 w=(q[0]-p[0],q[1]-p[1]);eta=-max(p[1]+v[1] for v in B)
 delta=min(F(1,2),eta/(2*w[1]))
 dets=[w[0]*v[1]-w[1]*v[0] for v in B];J=max(dets)-min(dets)
 E=a-area(clip(clip(A,(F(1),0),-1),(0,F(1)),-1))
 Ux=area(clip(A,(F(1),0),-1));Uy=area(clip(A,(0,F(1)),-1))
 ck(E==2*a-Ux-Uy)
 ck(area(clip(clip(A,(-F(1),0),1),(0,-F(1)),1))==0)
 ck(delta>0 and J>0)
 ck(union_miss(PB)>=2*b+delta*J)
 ck(union_miss(AB)>=union_miss(PB)+E)
 ck(union_miss(AB)>2*b+E)
 ck(area(PB)==b+J)
 if height==2:
  print({'a':str(a),'b':str(b),'source_union':str(E),'baseline_union':str(union_miss(PB)),
    'sum_union':str(union_miss(AB)),'delta_J':str(delta*J)})
print(f'PASS {checks} exact actual convex-polygon checks')
