from fractions import Fraction as F
import random
random.seed(11931)
def pcap(ps,bs):
 v=[F(1)]*len(ps)
 for b in bs:
  for j in reversed(range(len(ps))):v[j]=(ps[j]*v[j]+(b*v[j+1] if j+1<len(ps) else 0))/(ps[j]+b)
 return v[0]
for z in range(200000):
 k=random.randint(1,6);p=random.randint(1,39);m=random.randint(max(2,k),k+8);ps=[F(1)]*k+[F(p,40)];rem=40*(k-1)+p;bs=[40]
 for h in range(m-1):
  lo=max(0,rem-40*(m-h-1));hi=min(40,rem);b=random.randint(lo,hi);bs.append(b);rem-=b
 bs.append(rem);bs=[F(b,40) for b in bs]
 i,j=sorted(random.sample(range(1,m+1),2),key=lambda i:bs[i]);delta=(bs[j]-bs[i])/2
 new=bs.copy();new[i]+=delta;new[j]-=delta
 a=pcap(ps,bs);b=pcap(ps,new)
 if b>a:
  print('COUNTER',ps,bs,'pair',i,j,'before',a,'after',b,'gap',b-a,flush=True);break
else:print('NO COUNTER')
