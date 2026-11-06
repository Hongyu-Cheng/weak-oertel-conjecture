from fractions import Fraction as Q
P=[(Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(-1))]
U=[(Q(2),Q(-1)),(Q(-1),Q(2)),(Q(-1),Q(-1))]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def clip(poly,u,b=Q(0)):
 out=[]
 for a,c in zip(poly,poly[1:]+poly[:1]):
  da,dc=dot(u,a)-b,dot(u,c)-b
  if da>=0: out.append(a)
  if (da<0<dc) or (dc<0<da):
   t=da/(da-dc);out.append(add(scale(1-t,a),scale(t,c)))
 return out
def area(poly):
 return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1])))/2
A=area(P); gamma=Q(4,9); beta=Q(13,36); lam=Q(12,13)
assert A==Q(3,2)
assert [z for x in range(-2,3) for y in range(-2,3) if all(dot(u,z:=(x,y))>=-1 for u in U)]==[(-1,-1),(0,0),(0,1),(1,0)]
assert sum(lam for _ in U)==1/beta>1/gamma
for j,u in enumerate(U):
 assert area(clip(P,u))==gamma*A
 assert [dot(u,p) for p in P]==[2 if i==j else -1 for i in range(3)]
 assert min(10*dot(u,P[j])+dot(u,x) for x in P)>0
 assert all(max(10*dot(u,p)+dot(u,x) for x in P)<0 for i,p in enumerate(P) if i!=j)
for ell in range(3):
 a,b=[p for i,p in enumerate(P) if i!=ell]
 center=scale(Q(1,2),add(a,b))
 central_mass=Q(0);central_moment=(Q(0),Q(0))
 for u in U:
  da,db=dot(u,a),dot(u,b)
  if max(da,db)<0: continue
  if min(da,db)>=0: lo,hi=Q(0),Q(1)
  else:
   cross=-da/(db-da)
   lo,hi=(cross,Q(1)) if db>da else (Q(0),cross)
  mass=hi-lo
  midpoint=add(a,scale((lo+hi)/2,add(b,scale(-1,a))))
  central_mass+=mass
  central_moment=add(central_moment,scale(mass,midpoint))
 assert central_mass==Q(4,3)
 assert central_moment==scale(Q(4,3),center)
 assert lam*(3+central_mass)==4
 assert scale(lam,add(scale(3,center),central_moment))==scale(4,center)
R=((0,-1),(1,-1))
def matvec(R,x):return tuple(dot(row,x) for row in R)
for i,p in enumerate(P):
 assert matvec(R,p)==P[(i+1)%3]
 assert add(add(p,matvec(R,p)),matvec(R,matvec(R,p)))==(0,0)
t=Q(1,10); radii=[1-t,Q(1),1+t]
newbeta=max(gamma*max(radii)**2,gamma+min(radii)**2)/(1+sum(r*r for r in radii))
assert newbeta==Q(1129,3618)<beta
print('PASS: lattice set, cap areas, exact isolation, cyclic coupling algebra, all shared-facet mass/first moments, and improving deformation.')
print('beta=',beta,'group multiplier sum=',3*lam,'excess over gamma^-1=',3*lam-1/gamma,'beta(1/10)=',newbeta)
