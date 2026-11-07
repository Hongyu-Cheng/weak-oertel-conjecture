from fractions import Fraction as F
from itertools import product
import random

def ratio(t):
 e=sum(t[i]*t[j] for i in range(len(t)) for j in range(i))
 if not e:return F(1,2)
 p=F(1)
 for x in t:p*=1-x
 return p/(2*e)
random.seed(31771)
checks=0
for m in range(2,25):
 gamma=F(m-1,m)**(m-1)
 assert ratio([F(1,m)]*m)==gamma
 assert ratio([F(1)]+[F(0)]*(m-1))==F(1,2)
 for _ in range(80):
  ns=[random.randrange(0,20) for i in range(m)]
  if not sum(ns):ns[0]=1
  t=[F(n,sum(ns)) for n in ns]
  r=ratio(t);assert gamma<=r<=F(1,2)
  i,j=random.sample(range(m),2)
  new=t[:];new[i]=new[j]=(t[i]+t[j])/2
  assert ratio(new)<=r
  d=m-1;l=[(1-x)/d for x in t]
  if all(l):
   den=1-d*sum(x*x for x in l)
   prodl=F(1)
   for x in l:prodl*=x
   assert F(d**d)*prodl/den==r
   theta=[x*(1-d*x)/den for x in l]
   assert sum(theta)==1
   fs=[F(d**d)*prodl/x for x in l]
   assert sum(w*f for w,f in zip(theta,fs))==r
  checks+=1
print('Exact Fraction checks passed:',checks)
