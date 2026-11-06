from fractions import Fraction as F
from itertools import product
checks=0
def ck(x):
 global checks
 assert x
 checks+=1
P=[(x,y) for x in range(-4,5) for y in range(-4,5) if min(-x-y,2*x-y,2*y-x)>=-4]
def ell(z):x,y=z;return(-x-y,2*x-y,2*y-x)
B={z:sum(t*t for t in ell(z)) for z in P}
ck(len(P)==31);ck(max(B.values())==96)
for j in range(3):
 plus=[z for z in P if ell(z)[j]>0];zero=[z for z in P if ell(z)[j]==0]
 ck(len(plus)==12);ck(len(zero)==3)
 ck(sum(B[z] for z in plus)==360);ck(sum(B[z]**2 for z in plus)==18144)
 for k in range(3):ck(sum(ell(z)[k]**2 for z in zero)==(0 if j==k else 18))
for e in [F(1,1000),F(1,192),F(1,100),F(1,97)]:
 ck(0<e<F(1,96))
 for z in P:ck(1-e*B[z]>0)
 for j,k in product(range(3),repeat=2):
  mass=F(0)
  for z in P:
   es=ell(z);a=[e*t*t for t in es];r=1-sum(a);threshold=F(1,3)-es[j]
   if es[j]>0:
    ck(a[k]>threshold);mass+=r*r
   elif es[j]<0:ck(a[k]+r<threshold)
   else:
    ck(a[k]<threshold<a[k]+r)
    mass+=(a[k]+r-threshold)**2
  expected=F(40,3)-(768 if j==k else 744)*e+(18792 if j==k else 18306)*e*e
  ck(mass==expected)
 for j in range(3):
  sectionmass=F(0);moment=[F(0)]*5
  for z in P:
   es=ell(z)
   if es[j]:continue
   a=[e*t*t for t in es];ks=[k for k in range(3) if k!=j]
   width=F(2,3)-sum(a[k] for k in ks)
   centroid=[F(1,3)]*3
   centroid[ks[0]]=(F(2,3)+a[ks[0]]-a[ks[1]])/2
   centroid[ks[1]]=1-F(1,3)-centroid[ks[0]]
   for k,val in enumerate((*z,*centroid)):moment[k]+=width*val
   sectionmass+=width
  ck(sectionmass==2-36*e)
  ck(moment[:2]==[0,0]);ck(all(v==sectionmass/3 for v in moment[2:]))
 for z in P:
  s,t,_=ell(z);h=s+2
  upper=1-e*s*s-e*(s+t)**2
  L=upper-2*e*t-6*(e*s*s+4*e*s+4*e)-(1-7*e)
  ck(L==e*(6*h-7*h*h-(s+t+1)**2))
  if z==(1,1):
   ck(L==0);ck(1-6*e>e/2);ck(ell(z)==(-2,1,1))
  else:ck(L<=-e)
 ck(24*e-486*e*e>0)
print('PASS:',checks,'exact finite-base, cap-status, cap-mass, section-moment and exposing-hinge checks')
