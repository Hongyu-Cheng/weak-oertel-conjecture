"""Independent exact verifier; uses Fraction only, not the generating symbolic code."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json

DATA=Path(__file__).with_name('triangle-eight-fiber-depth-exact-certificate.json')
doc=json.loads(DATA.read_text());assert doc['degree']==3

def add(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,Q(0))+v
 return {k:v for k,v in c.items() if v}
def scale(a,s):return {k:v*s for k,v in a.items() if v*s}
def mul(a,b):
 c={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():c[i+k,j+l]=c.get((i+k,j+l),Q(0))+v*w
 return {k:v for k,v in c.items() if v}
def power(a,n):
 c={(0,0):Q(1)}
 for _ in range(n):c=mul(c,a)
 return c
ONE={(0,0):Q(1)};T={(1,0):Q(1)};X={(0,1):Q(1)}
A=add(T,ONE);B=add(scale(T,-1),scale(ONE,2));C=add(scale(T,-2),ONE)
DEN=mul(mul(A,B),C)
def point(p):return tuple(Q(*z) for z in p)
def cross(a,b,p):return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
def area2(poly):return sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1]))
def orient(poly):return poly if area2(poly)>=0 else list(reversed(poly))
def clean(poly):
 out=[]
 for p in poly:
  if not out or p!=out[-1]:out.append(p)
 if len(out)>1 and out[0]==out[-1]:out.pop()
 return out

def clip(poly,a,b):
 out=[]
 for p,q in zip(poly,poly[1:]+poly[:1]):
  vp=cross(a,b,p);vq=cross(a,b,q)
  if vp>=0:out.append(p)
  if vp*vq<0:
   r=vp/(vp-vq);out.append((p[0]+r*(q[0]-p[0]),p[1]+r*(q[1]-p[1])))
 return clean(out)
def intersect(p,q):
 out=p
 for a,b in zip(q,q[1:]+q[:1]):
  out=clip(out,a,b)
  if not out:return []
 return out

def inside(x,poly):return all(cross(a,b,x)>=0 for a,b in zip(poly,poly[1:]+poly[:1]))
def numerator(poly):
 t=sum(p[0] for p in poly)/len(poly);l=sum(p[1] for p in poly)/len(poly)
 P=scale(DEN,-112)
 for k in [-3,-2,-1,0,1,2,3,4]:
  z=k*l
  if z<=-1:
   assert all(k*y<=-1 for x,y in poly)
   term=DEN
  elif z>=1-t:
   assert all(k*y>=1-x for x,y in poly)
   term={}
  elif z<t:
   assert all(-1<=k*y<=x for x,y in poly)
   term=add(DEN,scale(mul(power(add(scale(X,k),ONE),2),C),-1))
  else:
   assert all(x<=k*y<=1-x for x,y in poly)
   linear=add(add(ONE,scale(T,-1)),scale(X,-k))
   term=mul(power(linear,2),A)
  P=add(P,scale(term,33))
 return P

def evaluate(P,x):return sum(v*x[0]**i*x[1]**j for (i,j),v in P.items())

def bernstein(P,tri):
 a,b,c=tri
 t={(0,0):a[0],(1,0):b[0]-a[0],(0,1):c[0]-a[0]}
 x={(0,0):a[1],(1,0):b[1]-a[1],(0,1):c[1]-a[1]}
 transformed={}
 for (i,j),v in P.items():transformed=add(transformed,scale(mul(power(t,i),power(x,j)),v))
 out=[]
 for i in range(4):
  for j in range(4-i):
   coefficient=Q(0)
   for (a,b),v in transformed.items():
    assert a+b<=3
    if a<=i and b<=j:
     coefficient+=v*Q(comb(i,a)*comb(j,b),comb(3,a+b)*comb(a+b,a))
   out.append(coefficient)
 return out

cells=[];triangle_count=0;coefficient_count=0;sos_count=0
for record in doc['cells']:
 poly=[point(p) for p in record['polygon']]
 assert area2(poly)>0
 assert all(-1<=t<=Q(1,2) and 0<=l<=2 for t,l in poly)
 # A convex polygon is required, not inferred from its area alone.
 assert all(inside(v,poly) for v in poly)
 P=numerator(poly)
 claimed={(int(i),int(j)):Q(v) for i,j,v in record['polynomial']}
 assert P==claimed
 if record["method"]=="sum_of_squares":
  linear=add(add(scale(X,11),T),scale(ONE,-1))
  SOS=mul(A,add(scale(power(linear,2),12),scale(power(A,2),28)))
  assert P==SOS and all(t+1>=0 for t,l in poly)
  assert not record["triangles"]
  sos_count+=1;cells.append(poly);continue
 assert record["method"]=="bernstein"
 triangles=[]
 for leaf in record['triangles']:
  tri=[point(p) for p in leaf['vertices']]
  assert len(tri)==3 and area2(tri)!=0
  assert all(inside(v,poly) for v in tri)
  coefficients=bernstein(P,tri)
  assert coefficients==list(map(Q,leaf['bernstein']))
  assert min(coefficients)>=0 and any(v>0 for v in coefficients)
  for v in tri:
   if -1<v[0]<Q(1,2):assert evaluate(P,v)>0
  for a,b in zip(tri,tri[1:]+tri[:1]):
   mid=((a[0]+b[0])/2,(a[1]+b[1])/2)
   if -1<mid[0]<Q(1,2):assert evaluate(P,mid)>0
  triangles.append(orient(tri));triangle_count+=1;coefficient_count+=len(coefficients)
 assert sum(area2(tri) for tri in triangles)==area2(poly)
 for i in range(len(triangles)):
  for j in range(i):assert area2(intersect(triangles[i],triangles[j]))==0
 cells.append(poly)
assert len(cells)==35 and triangle_count==42 and coefficient_count==420 and sos_count==1
assert sum(area2(poly) for poly in cells)==6  # twice the rectangle's area
for i in range(len(cells)):
 for j in range(i):assert area2(intersect(cells[i],cells[j]))==0
print('PASS: 35 cells exactly partition [-1,1/2]x[0,2]; one exact sum-of-squares cell;')
print('      42 triangles cover the other cells; 420 rational Bernstein coefficients are nonnegative.')

# Endpoint projection directions: exact one-variable piecewise quadratic minima.
qstar=Q(112,33)
canon_bounds=[Q(0),Q(1,3),Q(1,2),Q(2,3),Q(1),Q(2)]
mins=[]
for lo,hi in zip(canon_bounds,canon_bounds[1:]):
 mid=(lo+hi)/2;aa=bb=cc=Q(0)
 for k in range(-3,5):
  z=k*mid
  if z<=-1:cc+=1
  elif z>=2:pass
  else:aa+=Q(k*k,9);bb-=Q(4*k,9);cc+=Q(4,9)
 at=max(lo,min(hi,-bb/(2*aa)))
 value=aa*at*at+bb*at+cc;assert value>=qstar
 mins.append((value,at))
assert mins==[(Q(112,33),Q(2,11)),(Q(157,45),Q(2,5)),(Q(94,27),Q(2,3)),(Q(94,27),Q(2,3)),(Q(31,9),Q(2))]
reverse_bounds=[Q(0),Q(1,8),Q(1,6),Q(1,4),Q(1,3),Q(1,2),Q(1)]
def reverse_tail(x):
 if x<=-1:return Q(1)
 if x>=Q(1,2):return Q(0)
 return 1-Q(4,9)*(x+1)**2
rev=[sum(reverse_tail(k*l) for k in range(-3,5)) for l in reverse_bounds]
assert rev==[Q(40,9),Q(133,36),Q(287,81),Q(125,36),Q(95,27),Q(31,9),Q(32,9)]
assert min(rev)>qstar
print('PASS: strict positivity for -1<t<1/2; endpoint equality only at t=-1,L=2/11.')
