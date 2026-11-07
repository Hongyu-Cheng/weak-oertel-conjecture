"""Exact algebra and actual-polygon checks; no global row claim."""
from fractions import Fraction as F
import sympy as sp
A,B,a,b,t,al,be=sp.symbols('A B a b t al be',positive=True)
ell=a/t
D2=1-al+al*ell;D3=be+(1-be)*ell
N2=2*B*a+B**2*(1-ell)-a*t*(1-al)
N3=2*a*b-b**2*(1-ell)-a*a*(1-be)
raw=(be*N2-b*b*D2+al*N3-B*B*D3)/a
squares=(B-be*t)**2/t+(b-al*a)**2/a+(1-al-be)*(be*t+al*a)
assert sp.factor(raw+squares)==0
m=t*(1-al)/B;n=B*(1-ell)/a
assert sp.factor(B*t*(2+n-m)/(2*(1+m*n))-N2/(2*D2))==0
s=(1-ell)*b/a;w=(1-be)*a/b
assert sp.factor(a*b*(2-s-w)/(2*(1-s*w))-N3/(2*D3))==0
checks=3

def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def sub(p,q):return(p[0]-q[0],p[1]-q[1])
def dot(p,n):return p[0]*n[0]+p[1]*n[1]
def area(P):return abs(sum(cross(p,q) for p,q in zip(P,P[1:]+P[:1])))/2

def clip(P,n):
 out=[]
 for p,q in zip(P,P[1:]+P[:1]):
  vp,vq=dot(p,n),dot(q,n)
  if vp>=0:out.append(p)
  if (vp<0<vq) or (vq<0<vp):
   z=vp/(vp-vq);out.append((p[0]+z*(q[0]-p[0]),p[1]+z*(q[1]-p[1])))
 return out

def check(v):
 global checks
 assert v
 checks+=1

T=[(-F(1),F(2)),(F(2),-F(1)),(-F(1),-F(1))]
K=[(-F(1),F(2)),(F(5,4),-F(1,4)),(F(5,3),-F(3,4)),(F(5,4),-F(1)),(-F(1),-F(1))]
Q=[(-F(1),F(2)),(F(3,2),-F(1,2)),(F(3,2),-F(1)),(-F(1),-F(1))]
for P in [T,K,Q]:
 for j in range(len(P)):
  check(cross(sub(P[(j+1)%len(P)],P[j]),sub(P[(j+2)%len(P)],P[(j+1)%len(P)]))<0)
  check(cross(sub(P[(j+1)%len(P)],P[j]),sub((F(0),F(0)),P[j]))<0)
check(area(T)==F(9,2))
check(area(K)==area(Q)==F(35,8))
check(area(T)-area(K)==F(1,8))
v=[(1,0),(0,1),(-1,-1)]
check([area(clip(K,n)) for n in v]==[F(15,8),F(2),F(2)])
check([area(clip(K,n)) for n in v]==[area(clip(Q,n)) for n in v])
e=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def sectors(P):
 out=[]
 for j in range(6):
  u,v=e[j],e[(j+1)%6]
  out.append(area(clip(clip(P,(-u[1],u[0])),(v[1],-v[0]))))
 return out
check(sectors(K)==sectors(Q)==[F(1,2),F(1),F(1,2),F(1),F(1,2),F(7,8)])
check(F(16,35)<F(128,279))
check(F(15,8)+2+F(2,4)==area(K))
print(f'PASS: {checks} exact symbolic and actual-polygon checks')
