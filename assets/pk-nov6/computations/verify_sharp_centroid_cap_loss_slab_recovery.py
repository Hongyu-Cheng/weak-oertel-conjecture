"""Supplementary exact convex-polygon and all-d cone checks."""
from fractions import Fraction as F
checks=0
def ck(x):
 global checks
 assert x
 checks+=1

def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(pts):
 pts=sorted(set(pts));lo=[];hi=[]
 for p in pts:
  while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
  lo.append(p)
 for p in reversed(pts):
  while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
  hi.append(p)
 return lo[:-1]+hi[:-1]
def mass_centroid(P):
 cr=[P[i][0]*P[(i+1)%len(P)][1]-P[i][1]*P[(i+1)%len(P)][0] for i in range(len(P))]
 a=sum(cr)/2
 return a,tuple(sum((P[i][j]+P[(i+1)%len(P)][j])*cr[i] for i in range(len(P)))/(6*a) for j in range(2))
def dot(u,p):return sum(x*y for x,y in zip(u,p))
def cut(P,u,b):
 out=[];section=set()
 for p,q in zip(P,P[1:]+P[:1]):
  x=dot(u,p)-b;y=dot(u,q)-b
  if x>=0:out.append(p)
  if x==0:section.add(p)
  if x*y<0:
   z=tuple(p[j]+x/(x-y)*(q[j]-p[j]) for j in range(2))
   out.append(z);section.add(z)
 ck(len(section)==2)
 v,w=sorted(section)
 sigma=abs((v[1]-w[1])/u[0]) if u[0] else abs((v[0]-w[0])/u[1])
 return out,sigma
raws=[[(0,0),(3,0),(0,2)],[(0,0),(3,0),(3,2),(0,2)],
      [(-2,-1),(1,-2),(4,1),(2,4),(-1,3)],
      [(-3,0),(-1,-2),(3,-1),(4,2),(0,5)]]
for raw in raws:
 P=hull([tuple(map(F,p)) for p in raw]);a,g=mass_centroid(P)
 for u in ((F(1),F(0)),(F(0),F(-2)),(F(1),F(2)),(F(-3),F(1)),(F(2),F(-5))):
  lo=min(dot(u,p) for p in P);hi=max(dot(u,p) for p in P)
  for j in range(1,12):
   b=lo+F(j,12)*(hi-lo);cap,sigma=cut(P,u,b);U,_=mass_centroid(cap)
   L=2*U+(b-dot(u,g))*sigma
   ck(0<U<a and sigma>0 and L>0)
   ck(9*L*L>=16*a*U)
# Exact cone first-moment identities, including d=1 and arbitrary fractions
# whose dth reciprocal root s is rational.
for d in range(1,13):
 for a in (F(1),F(7,3)):
  for D in (F(1,2),F(5,3)):
   for s in (F(7,6),F(3,2),F(7,2)):
    U=a/s**d;sigma=d*U/D
    pos=U*D/F(d+1)
    neg=a*D*(s-1)-U*D*(s**(d+1)-1)/F(d+1)
    mu=D*(1-F(d,d+1)*s)
    ck(pos-neg==a*mu)
    L=d*U-sigma*mu
    ck(L==F(d*d,d+1)*U*s)
    if d==1:ck(L==a/2)
print(f'PASS {checks} exact actual polygon, signed-moment, and all-dimensional cone checks')
