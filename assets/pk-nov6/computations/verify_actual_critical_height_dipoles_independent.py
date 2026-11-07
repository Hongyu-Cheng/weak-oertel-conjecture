from fractions import Fraction as F
P=[(0,0),(1,0),(0,1),(-1,-1)]
e=F(1,4); V=F(9,2);beta=F(13,36);delta=-F(1,36)
U=[(1,0),(0,1),(-1,-1)]
verts=[(2,-1),(-1,2),(-1,-1)]

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def ell(j,z):return [(2*z[0]-z[1]),(2*z[1]-z[0]),(-z[0]-z[1])][j]
assert [(a,b) for a in range(-1,2) for b in range(-1,2) if 2*a-b>=-1 and 2*b-a>=-1 and -a-b>=-1]==[(-1,-1),(0,0),(0,1),(1,0)]
for i in range(3):
 for j,p in enumerate(P[1:]):
  margins=[10*ell(i,p)+dot(U[i],x) for x in verts]
  assert min(margins)>0 if i==j else max(margins)<0
assert 3*delta+F(1,12)==0
assert beta*4*V==(1+F(4,9))*V==F(13,2)
# Unnormalized body facet normals, with L/|v|=3.
faces=[((-1,0),lambda t:(F(-1),-1+3*t)),((0,-1),lambda t:(-1+3*t,F(-1))),((1,1),lambda t:(2-3*t,-1+3*t))]

def integ(fn,a,b): # exact for degree <=2
 return (b-a)*(fn(a)+4*fn((a+b)/2)+fn(b))/6

def row_integral(p,f,phi,weight='sigma',height='fixed'):
 v,xy=f;b=(e*p[0],F(0)); mult=3*(1+dot(v,b)) if height=='fixed' else F(3)
 if p==(0,0):
  intervals=[(F(0),F(1,3),delta),(F(1,3),F(2,3),F(11,36)),(F(2,3),F(1),delta)]
 else:intervals=[(F(0),F(1),delta)]
 if weight=='W':intervals=[(a,b,c+beta) for a,b,c in intervals]
 if weight=='one':intervals=[(F(0),F(1),F(1))]
 return mult*sum(w*integ(lambda t:phi(p,tuple(xx+bb for xx,bb in zip(xy(t),b))),a,c) for a,c,w in intervals)

def whole(phi,weight='sigma',height='fixed'):
 return sum(row_integral(p,f,phi,weight,height) for p in P for f in faces)

f3=faces[2]
assert sum(row_integral(p,f3,lambda z,x:F(1)) for p in P)==0
for k in range(2):
 assert sum(row_integral(p,f3,lambda z,x:z[k]) for p in P)==-e*F([2,1][k],12)
for phi in [lambda z,x:F(1),lambda z,x:z[0],lambda z,x:z[1],lambda z,x:x[0],lambda z,x:x[1]]:
 assert whole(phi)==whole(phi,height='moving')==0
plus=lambda z,x:(z[0]+x[0])**2
minus=lambda z,x:(z[0]-x[0])**2
assert whole(plus)-whole(plus,height='moving')==-V*e*(1+e)/9==-F(5,32)
assert whole(minus)-whole(minus,height='moving')==V*e*(1-e)/9==F(3,32)
assert whole(lambda z,x:F(1),weight='one')==2*4*V
assert whole(lambda z,x:F(1),weight='W')==2*(1+F(4,9))*V
print('PASS: lattice completeness, strict finite cap statuses, critical masses, local height dipole, global affine cancellation, opposite convex-quadratic signs, and scalar divergence budgets.')
