from fractions import Fraction as F

def profile(r,q):
 if q<=0:return r*r
 if q<=r/3:return (r-q)**2
 if q<=r/2:return 4*q*(r-2*q)
 return F(0)

def minimum(rs,j):
 A=rs[j]/3
 breaks=sorted({(A-q)/(k-j) for k,r in enumerate(rs) if k!=j for q in (F(0),r/3,r/2)})
 def value(beta):return sum(profile(r,A-beta*(k-j)) for k,r in enumerate(rs))
 cand=[(value(b),b) for b in breaks]
 for lo,hi in zip(breaks,breaks[1:]):
  mid=(lo+hi)/2
  qa=qb=qc=F(0)
  for k,r in enumerate(rs):
   t=k-j;q=A-mid*t
   if q<=0:qc+=r*r
   elif q<r/3:
    qa+=t*t;qb+=2*t*(r-A);qc+=(r-A)**2
   elif q<r/2:
    qa-=8*t*t;qb+=t*(16*A-4*r);qc+=4*A*(r-2*A)
  if qa>0:
   v=-qb/(2*qa)
   if lo<v<hi:cand.append((value(v),v))
 return min(cand)

if __name__=='__main__':
 failures=[];worst=None;n=0
 for ib in range(11,21):
  b=F(ib,20)
  for ia in range(1,2*ib-20+1):
   a=F(ia,20)
   for ic in range(1,21):
    c=F(ic,20);rs=[a,b,F(1),c];S=sum(r*r for r in rs)
    if S<=2:continue
    p1=minimum(rs,1);p2=minimum(rs,2);target=2*S/9
    gap=max(p1[0],p2[0])-target;n+=1
    row=(gap,rs,p1,p2,target)
    if worst is None or gap<worst[0]:worst=row
    if gap<0:failures.append(row)
 print('cases',n,'failures',len(failures),'worst',worst)
 print('first failures',failures[:3])
