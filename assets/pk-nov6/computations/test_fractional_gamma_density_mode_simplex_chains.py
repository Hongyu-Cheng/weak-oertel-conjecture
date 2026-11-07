from fractions import Fraction as F
import random
random.seed(82172)
def derivative(ps,bs):
 v=[F(0)]*(len(ps)-1)+[1/ps[-1]]
 for b in bs:
  for j in reversed(range(len(ps))):v[j]=(ps[j]*v[j]+(b*v[j+1] if j+1<len(ps) else 0))/(ps[j]+b)
 return (v[1]-v[0])/ps[0]
for z in range(200000):
 k=random.randint(1,6);p=random.randint(1,39);m=random.randint(k+1,k+9);ps=[F(1)]*k+[F(p,40)];rem=40*k+p+random.randint(0,40);bs=[]
 if rem>40*m:continue
 for h in range(m-1):
  lo=max(0,rem-40*(m-h-1));hi=min(40,rem);b=random.randint(lo,hi);bs.append(b);rem-=b
 bs.append(rem);bs=[F(b,40) for b in bs]
 v=derivative(ps,bs)
 if v>0:
  print('COUNTER',ps,bs,'derivative',v,flush=True);break
else:print('NO COUNTER')
