"""Exact verification of geometric transfer identities and boundary factors."""
from fractions import Fraction as F
from math import prod
import random
random.seed(994715)
checks=0;cases=0

def ck(v):
 global checks
 assert v
 checks+=1
for m in range(1,10):
 for _ in range(80):
  q=F(random.randint(1,12),random.randint(1,9));p=q+F(random.randint(1,15),random.randint(1,9))
  r=[F(random.randint(1,25),random.randint(1,13)) for j in range(m)]
  s=[p/(p+x) for x in r];t=[q/(q+x) for x in r]
  X=prod(s);Y=prod(t);rho=Y/X;h=1-q/p
  a=[x/(q+x) for x in r];L=h*rho/(1-rho);S=sum(a)
  cap=(p*X-q*Y)/(p-q);density=(X-Y)/(p-q)
  muq=1/h-rho*S/(1-rho)
  mup=-q/(p-q)+sum(1-z for z in s)/(1-rho)
  mun=[(u-rho*v)/(1-rho) for u,v in zip(s,t)]
  ck(rho==prod(1-h*z for z in a))
  ck(muq==(1-L*S)/h)
  ck(mun==[u*(1+L*z) for u,z in zip(s,a)])
  ck(mup+muq+sum(mun)==m+1)
  ck(p*mup+q*muq==sum(x*z for x,z in zip(r,mun)))
  ck(cap==X*(1-(1-h)*rho)/h)
  ck(all(z>0 for z in [mup,muq,*mun]))
  if muq<=1:
   ck(L*S>=1-h)
   ck(cap>muq*prod(mun))
   ck(mup<muq)
   ck(cap>mup*prod(mun))
   # Adding z zero-height vertices only appends factors 1 to d*b.
   for z in [1,3]:
    actuald=m+1+z;b=[mup/actuald,muq/actuald,*[v/actuald for v in mun],*[F(1,actuald)]*z]
    ck(sum(b)==1)
    ck(cap>actuald**actuald*prod(b[1:]))
   cases+=1
for m in range(1,12):
 for _ in range(30):
  r=[F(random.randint(1,14),random.randint(1,12)) for j in range(m)]
  a=[1/(1+x) for x in r];t=[1-x for x in a];Z=sum(t);L=prod(a)
  cap=L*(1+Z);mup=(Z*Z+sum(x*x for x in t))/(2*Z)
  mun=[x*(Z+y)/Z for x,y in zip(a,t)]
  ck(2*mup+sum(mun)==m+1)
  ck(2*mup==sum(x*z for x,z in zip(r,mun)))
  if mup<=1:
   ck(cap>mup*prod(mun));cases+=1
ck(cases>200)
print(f'PASS: {checks} exact checks, including {cases} central specified-cap cases')
