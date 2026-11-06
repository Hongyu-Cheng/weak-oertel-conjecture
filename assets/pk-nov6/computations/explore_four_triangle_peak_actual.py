"""Exploratory shared-normal/shared-tilt screen; not a proof over the normal."""
from fractions import Fraction as F
from explore_four_triangle_peak_profile import minimum as lower_min

def cap(r,q,x):
 b=1-x
 if q<=0:return r*r
 if q>=b*r:return 0*r
 if x==0:return (r-q)**2
 if x==F(1,2):return r*r-4*q*q
 if q<=x*r:return r*r-q*q/(x*b)
 return (b*r-q)**2/(b*(b-x))

def minimum(rs,j,x):
 A=rs[j]/3;b=1-x
 breaks=sorted({(A-q)/(k-j) for k,r in enumerate(rs) if k!=j for q in (0*r,x*r,b*r)})
 def value(beta):return sum(cap(r,A-beta*(k-j),x) for k,r in enumerate(rs))
 cand=[(value(v),v) for v in breaks]
 for lo,hi in zip(breaks,breaks[1:]):
  mid=(lo+hi)/2;qa=qb=0*A
  for k,r in enumerate(rs):
   t=k-j;q=A-mid*t
   if q<=0 or q>=b*r:continue
   if x==0:
    qa+=t*t;qb+=2*t*(r-A)
   elif x==F(1,2) or q<x*r:
    den=x*b
    qa-=t*t/den;qb+=2*A*t/den
   else:
    den=b*(b-x)
    qa+=t*t/den;qb+=2*t*(b*r-A)/den
  if qa>0:
   v=-qb/(2*qa)
   if lo<v<hi:cand.append((value(v),v))
 return min(cand)

if __name__=='__main__':
 worst=None;n=0;below=0;lowerfail=0
 for ib in range(11,21):
  b=F(ib,20)
  for ia in range(1,2*ib-20+1):
   a=F(ia,20)
   for ic in range(1,21):
    c=F(ic,20);rs=[a,b,F(1),c];S=sum(r*r for r in rs)
    if S<=2:continue
    target=2*S/9;n+=1
    if max(lower_min(rs,j)[0] for j in (1,2))>=target:continue
    lowerfail+=1
    pts=[min((minimum(rs,j,F(ix,40))+(F(ix,40),) for ix in range(21))) for j in (1,2)]
    gap=max(p[0] for p in pts)-target
    row=(gap,rs,pts,target)
    if worst is None or gap<worst[0]:worst=row
    if gap<0:below+=1;print('ACTUAL COUNTER',row,flush=True)
 print('cases',n,'lowerfail',lowerfail,'actualfail',below,'worst',worst)
