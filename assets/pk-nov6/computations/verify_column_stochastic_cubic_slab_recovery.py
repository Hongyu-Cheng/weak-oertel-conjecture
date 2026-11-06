from fractions import Fraction as Q
from itertools import product
import sympy as sp
checks=0

def ck(v):
 global checks
 assert v
 checks+=1

def rowF(row):
 x,y,z=sorted(row)
 return z*(x+y)-x*y

def cubic(F):
 g=1-sum(F)
 ck(g>=0)
 ck(g*g>=4*F[0]*F[1]*F[2])

# The three exact boundary differences and the two-by-two determinant.
r,s,t=sp.symbols('r s t')
Z=(s+t-s*t)*(r+t-r*t)
qs=[r*(s+t)-s*t,s*(r+t)-r*t,t*(r+s)-r*s]
rs=[t*(1-r)*(t*(1-s)+2*s),t*(1-s)*(t*(1-r)+2*r),t*t*(1-r)*(1-s)+2*r*s*(1-t)]
for q,R in zip(qs,rs): ck(sp.expand(Z-q-R)==0)
a,c,L,z=sp.symbols('a c L z')
ck(sp.expand((1-z-L*a)*(1-z-L*c)-L*L*a*c*z-(1-z)*((1-a*L)*(1-c*L)-z))==0)

# The actual positive second variation quadratics.
l1,l2,l3=sp.symbols('l1 l2 l3', positive=True)
b=[1,1,-(l1+l2)/l3]
ck(sp.simplify(sum(x*y for x,y in zip(b,[l1,l2,l3])))==0)
for j in [0,1]:
 others=[b[i] for i in range(3) if i!=j]
 ck(sp.simplify(b[j]*sum(others)-sp.prod(others)-1)==0)
b=[0,l3,-l2]
ck(sp.simplify(sum(x*y for x,y in zip(b,[l1,l2,l3])))==0)
ck(-b[1]*b[2]==l2*l3)

# Exhaustive rational stochastic matrices, including tied maxima and zeros.
for den in [1,2,3,4,5]:
 cols=[(Q(i,den),Q(j,den),Q(den-i-j,den)) for i in range(den+1) for j in range(den+1-i)]
 for cc in product(cols,repeat=3):
  X=list(zip(*cc));F=[rowF(row) for row in X]
  cubic(F)

# Exact actual triangle cap areas, vertex/edge incidences, and coarea sections.
def dot(u,v): return sum(x*y for x,y in zip(u,v))
def sub(u,v): return tuple(x-y for x,y in zip(u,v))
def clip(poly,u,y):
 out=[]
 for P,R in zip(poly,poly[1:]+poly[:1]):
  p=dot(u,sub(P,y));r=dot(u,sub(R,y))
  if p>=0: out.append(P)
  if (p<0<r) or (r<0<p):
   t=p/(p-r);out.append(tuple(P[j]+t*(R[j]-P[j]) for j in range(2)))
 return out

def area(poly):
 return abs(sum(P[0]*R[1]-P[1]*R[0] for P,R in zip(poly,poly[1:]+poly[:1])))/2 if len(poly)>=3 else Q(0)

def sec(poly,u,y):
 pts=[]
 for P,R in zip(poly,poly[1:]+poly[:1]):
  p=dot(u,sub(P,y));r=dot(u,sub(R,y))
  if p==0:pts.append(P)
  if (p<0<r) or (r<0<p):
   t=p/(p-r);pts.append(tuple(P[j]+t*(R[j]-P[j]) for j in range(2)))
 pts=list(set(pts));ck(len(pts)==2)
 return abs((pts[1][0]-pts[0][0])/u[1]) if u[1] else abs((pts[1][1]-pts[0][1])/u[0])

def edgefrac(a,b):
 if a>=0 and b>=0:return Q(1)
 if a<=0 and b<=0:return Q(0)
 return max(a,b)/abs(a-b)

T=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(0),Q(1))]
source=[(Q(i,d),Q(j,d)) for d in [3,4,5] for i in range(1,d) for j in range(1,d-i)]
multivertex=vertexcuts=0
for y in source:
 for a,b in product(range(-3,4),[-3,-2,-1,1,2,3]):
  U=[(Q(1),Q(0)),(Q(a),Q(b)),(Q(-1-a),Q(-b))]
  cap=[area(clip(T,u,y)) for u in U]
  sigma=[sec(T,u,y) for u in U]
  M=sum(q/s for q,s in zip(cap,sigma))
  X=[]; expected=[]
  for u,q,s in zip(U,cap,sigma):
   heights=[dot(u,sub(P,y)) for P in T]
   multivertex+=sum(h>0 for h in heights)==2
   vertexcuts+=any(h==0 for h in heights)
   E=[edgefrac(heights[(j+1)%3],heights[(j+2)%3]) for j in range(3)]
   for e,h in zip(E,heights):ck(e==2*q-h*s)
   row=[e/(2*s*M) for e in E]
   X.append(row)
   ai=q/(s*M);Fi=rowF(row)
   ck(Fi==ai*ai/(2*q))
   expected.append(Fi)
  for j in range(3):ck(sum(row[j] for row in X)==1)
  cubic(expected)
ck(multivertex>0);ck(vertexcuts>0)
print(f'PASS: {checks} exact checks; {multivertex} two-vertex cuts and {vertexcuts} vertex-boundary cuts in the actual triangle tests.')
