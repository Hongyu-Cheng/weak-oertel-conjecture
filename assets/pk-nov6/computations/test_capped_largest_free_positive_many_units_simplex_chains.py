from fractions import Fraction as F
import random
random.seed(618233)
def pcap(ps,bs):
 v=[F(1)]*len(ps)
 for b in bs:
  for j in reversed(range(len(ps))):v[j]=(ps[j]*v[j]+(b*v[j+1] if j+1<len(ps) else 0))/(ps[j]+b)
 return v[0]
for z in range(200000):
 units=random.randint(1,4);k=random.randint(2,6);m=random.randint(units+1,units+8)
 ps=[40]*units+[random.randint(1,39) for _ in range(k)]
 total=sum(ps);rem=total-40;bs=[40]
 if rem>40*m:continue
 for h in range(m-1):
  lo=max(0,rem-40*(m-h-1));hi=min(40,rem)
  b=random.randint(lo,hi);bs.append(b);rem-=b
 bs.append(rem)
 ps=[F(p,40) for p in ps];bs=[F(b,40) for b in bs]
 free=[i for i,p in enumerate(ps) if p<1];j=max(free,key=lambda i:ps[i]);i=random.choice([i for i in free if i!=j]);transfer=min(ps[i],1-ps[j])
 new=[p for t,p in enumerate(ps) if t not in (i,j)]+[ps[j]+transfer]
 if ps[i]>transfer:new.append(ps[i]-transfer)
 a=pcap(ps,bs);b=pcap(new,bs)
 if b>a:
  print('COUNTER',ps,bs,'pair',i,j,'before',a,'after',b,'gap',b-a,flush=True);break
else:print('NO COUNTER')
