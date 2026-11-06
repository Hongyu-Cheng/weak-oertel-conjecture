"""Independent exact verifier; uses Fraction only, not the generating symbolic code."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json

DATA=Path(__file__).with_name('triangle-six-fiber-depth-bernstein-certificate.json')
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
 P=scale(DEN,-22)
 for k in [-2,-1,0,1,2,3]:
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
  P=add(P,scale(term,9))
 return P

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

cells=[];triangle_count=0;coefficient_count=0
for record in doc['cells']:
 poly=[point(p) for p in record['polygon']]
 assert area2(poly)>0
 assert all(-1<=t<=Q(1,2) and 0<=l<=2 for t,l in poly)
 # A convex polygon is required, not inferred from its area alone.
 assert all(inside(v,poly) for v in poly)
 P=numerator(poly)
 claimed={(int(i),int(j)):Q(v) for i,j,v in record['polynomial']}
 assert P==claimed
 triangles=[]
 for leaf in record['triangles']:
  tri=[point(p) for p in leaf['vertices']]
  assert len(tri)==3 and area2(tri)!=0
  assert all(inside(v,poly) for v in tri)
  coefficients=bernstein(P,tri)
  assert coefficients==list(map(Q,leaf['bernstein']))
  assert min(coefficients)>=0
  triangles.append(orient(tri));triangle_count+=1;coefficient_count+=len(coefficients)
 assert sum(area2(tri) for tri in triangles)==area2(poly)
 for i in range(len(triangles)):
  for j in range(i):assert area2(intersect(triangles[i],triangles[j]))==0
 cells.append(poly)
assert len(cells)==22 and triangle_count==38 and coefficient_count==380
assert sum(area2(poly) for poly in cells)==6  # twice the rectangle's area
for i in range(len(cells)):
 for j in range(i):assert area2(intersect(cells[i],cells[j]))==0
print('PASS: 22 cells exactly partition [-1,1/2]x[0,2]; 38 triangles exactly cover them;')
print('      380 independently recomputed rational Bernstein coefficients are nonnegative.')
