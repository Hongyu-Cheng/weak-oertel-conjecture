from fractions import Fraction as F
import random
random.seed(937142)
def pcap(ps,bs):
 if len(set(ps))<len(ps): return None
 out=F(0)
 for i,p in enumerate(ps):
  v=F(1)
  for j,q in enumerate(ps):
   if i!=j: v*=p/(p-q)
  for b in bs:v*=p/(p+b)
  out+=v
 return out
for z in range(100000):
 k=random.randint(3,8); m=random.randint(2,8)
 ps=random.sample(range(1,41),k)
 total=sum(ps)
 if total<40 or total>40*(m+1):continue
 rem=total-40; bs=[40]
 for h in range(m-1):
  lo=max(0,rem-40*(m-h-1));hi=min(40,rem)
  b=random.randint(lo,hi);bs.append(b);rem-=b
 bs.append(rem)
 if any(b<0 or b>40 for b in bs):continue
 ps=list(map(lambda x:F(x,40),ps));bs=list(map(lambda x:F(x,40),bs))
 i,j=sorted(random.sample(range(k),2),key=lambda i:ps[i])
 if ps[i]+ps[j]>1:continue
 new=[p for t,p in enumerate(ps) if t not in (i,j)]+[ps[i]+ps[j]]
 a=pcap(ps,bs);b=pcap(new,bs)
 if a is None or b is None:continue
 if b>a:
  print('COUNTER',ps,bs,'pair',i,j,'before',a,'after',b,'gap',b-a,flush=True);break
else: print('NO COUNTER')
