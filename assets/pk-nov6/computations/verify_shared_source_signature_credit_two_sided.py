#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
checks=0

def ok(x):
 global checks
 assert x
 checks+=1

def clip(poly,a,b,positive):
 if not positive:a,b=-a,-b
 out=[]
 for P,Q in zip(poly,poly[1:]+poly[:1]):
  p=a*P[0]+b*P[1];q=a*Q[0]+b*Q[1]
  if p>=0:out.append(P)
  if (p<0<q) or (q<0<p):
   t=p/(p-q);out.append((P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1])))
 return out

def area(poly):
 if not poly:return F(0)
 return abs(sum(P[0]*Q[1]-Q[0]*P[1] for P,Q in zip(poly,poly[1:]+poly[:1])))/2

# Verify optimal Boolean hitting costs and fixed LP formula on exact finite samples.
for a,b,c in product(range(1,7),repeat=3):
 c1=min(a,b);c2=min(a,c);c12=min(a,b+c);rho=c1+c2-c12
 ok(rho>=0)
 for s,t in product([0,1],repeat=2):
  costs=[a*i+b*j+c*k for i,j,k in product([0,1],repeat=3) if i+j>=s and i+k>=t]
  ok(min(costs)==c1*s+c2*t-rho*s*t)
 for p,q,o in [(F(1,2),F(1,2),F(11,24)),(F(1,3),F(2,3),F(1,6)),(F(3,4),F(1,4),F(1,4))]:
  vertices={(F(0),F(0)),(F(min(a,b)),F(0)),(F(0),F(min(a,c)))}
  if b+c<=a:vertices.add((F(b),F(c)))
  for x in [F(0),F(b),F(a-c),F(a)]:
   y=F(a)-x
   if 0<=x<=b and 0<=y<=c:vertices.add((x,y))
  old=max(x*p+y*q for x,y in vertices)
  joint=c1*p+c2*q-rho*o
  ok(joint-old==rho*(min(p,q)-o))

# Full actual three-bit joint distribution for the SAME rectangle coupling.
square=[(F(-1),F(-1)),(F(1),F(-1)),(F(1),F(1)),(F(-1),F(1))]
n1=[(F(3,2),F(1)),(F(-3,2),F(1)),(F(0),F(-1))]
n2=[(F(1),F(1)),(F(-1),F(1)),(F(0),F(-1))]
states=list(product([0,1],repeat=3));table={}
for s,t in product(states,repeat=2):
 poly=square
 for (a,b),sign in zip(n1+n2,s+t):poly=clip(poly,a,b,sign)
 mass=area(poly)/4
 if mass:table[(s,t)]=mass
ok(sum(table.values())==1)
for i in range(3):
 p=sum(v for (s,t),v in table.items() if s[i]);q=sum(v for (s,t),v in table.items() if t[i]);o=sum(v for (s,t),v in table.items() if s[i] and t[i])
 ok(p==q==F(1,2))
 ok(o==([F(11,24),F(11,24),F(1,2)][i]))
 ok(4*p+4*q-4*o==([F(13,6),F(13,6),F(2)][i]))
# Exact scalar comparisons for zero root credits: (1+sqrt2)^2<6 iff2sqrt2<3.
ok(8<9)
ok(4<6)
# Actual widths concave and volumes exact.
w=[F(1),F(3),F(2),F(1)];slopes=[w[i+1]-w[i] for i in range(3)]
ok(slopes==[2,-1,-1]);ok([4*r for r in w]==[4,12,8,4])
# Parity-forest source and target identities with a shared source.
s=(F(2),F(1));a=(F(0),F(1));b=(F(1),F(2));c=(F(0),F(0));p=(F(1),F(1))
ok(tuple((s[i]+a[i])/2 for i in range(2))==p)
ok(tuple((s[i]+b[i]+c[i])/3 for i in range(2))==p)
ok((F(1,10)+F(1,100))/2==F(11,200))
ok((F(1,10)+F(1,10)+F(1,100))/3==F(7,100))
print(f'PASS: {checks} exact checks. Nonzero three-bit joint cells:')
for (s,t),v in sorted(table.items()):print(''.join(map(str,s)),''.join(map(str,t)),str(v))
