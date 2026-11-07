import random
from fractions import Fraction as F
random.seed(933)
P=[(0,0),(1,0),(0,1)]
def cap(n,p):
 b=n[0]*p[0]+n[1]*p[1];out=[]
 for x,y in zip(P,P[1:]+P[:1]):
  s=n[0]*x[0]+n[1]*x[1]-b;t=n[0]*y[0]+n[1]*y[1]-b
  if s>=0:out.append(x)
  if s*t<0:
   u=s/(s-t);out.append((x[0]+u*(y[0]-x[0]),x[1]+u*(y[1]-x[1])))
 return abs(sum(x[0]*y[1]-x[1]*y[0] for x,y in zip(out,out[1:]+out[:1])))
for it in range(950000):
 a=random.randint(1,18);b=random.randint(1,19-a);p=(a/20,b/20)
 u=(random.randint(-8,8),random.randint(-8,8));v=(random.randint(-8,8),random.randint(-8,8));w=(-u[0]-v[0],-u[1]-v[1]);ns=[u,v,w]
 if u[0]*v[1]==u[1]*v[0]:continue
 qs=[cap(n,p) for n in ns]
 count=[sum(n[0]*(x[0]-p[0])+n[1]*(x[1]-p[1])>1e-10 for x in P) for n in ns]
 if max(qs)<128/279-1e-9 and sum(qs)-.75*max(qs)<1 and max(count)>=2:
  pp=(F(a,20),F(b,20));QQ=[cap(n,pp) for n in ns]
  print('FOUND',ns,pp,QQ,count,'F',sum(QQ)-F(3,4)*max(QQ),flush=True);break
else:print('NONE',flush=True)
