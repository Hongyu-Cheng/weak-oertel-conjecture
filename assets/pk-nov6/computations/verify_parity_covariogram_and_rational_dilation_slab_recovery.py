from fractions import Fraction as F
from math import gcd
from itertools import product
checks=0
def ck(p,msg):
 global checks
 assert p,msg
 checks+=1
def axis(c):return 2*c+c*c if c<=F(1,2) else 1+2*c-3*c*c
ck(axis(F(1,2))==F(5,4),'exact reflection maximum')
ck((F(1,2)+F(1,8))/F(3,2)==F(5,12),'exact original halfspace depth')
ck(F(5,12)<F(4,9),'continuous selector fails Gamma')
for i in range(101):
 c=F(i,100)
 ck(axis(c)<=F(5,4),'axis maximum')
 if c!=F(1,2):ck(axis(c)<F(5,4),'strict vertical uniqueness')
for n in range(7):
 ck(F(5,12*2**n)<F(4,9*2**n),'binary product target gap')
 for p in product((0,1),repeat=n):
  for z in product((0,1),repeat=n):
   ell=sum((2*pp-1)*(zz-pp) for pp,zz in zip(p,z))
   ck(ell==0 if p==z else ell<=-1,'finite ambient cap isolates base')
   w=tuple(2*pp-zz for pp,zz in zip(p,z))
   ck((all(ww in (0,1) for ww in w))==(p==z),'binary reflection only self')
for R in range(1,8):
 P=list(range(-R,R+1))
 for r in range(1,6):
  for s in range(1,6):
   if gcd(r,s)!=1:continue
   m=r+s
   pairs=[(z,w) for z in P for w in P if (r*z+s*w)%m==0]
   residue=sum(sum(z%m==c for z in P)**2 for c in range(m))
   ck(len(pairs)==residue,'rational residue-class product count')
   for z,w in pairs:
    p=(r*z+s*w)//m
    ck((z-p)%s==0 and (p-w)%r==0 and (z-p)//s==(p-w)//r,'exact paired-base indexing')
    if z!=w:ck(m<=2*R,'nonself denominator bounded by diameter')
for j in range(1,20):
 t=F(j,20)
 pairs=[(z,w) for z in (-1,0,1) for w in (-1,0,1) if t*z+(1-t)*w==0]
 ck(len(pairs)==(3 if t==F(1,2) else 1),'actual three-fiber rational spike')
 for d in range(1,6):
  value=len(pairs)*min(t,1-t)**d
  ck(value==(3*F(1,2)**d if t==F(1,2) else min(t,1-t)**d),'exact scaled spike value')
print(f'{checks} exact rational checks passed.')
