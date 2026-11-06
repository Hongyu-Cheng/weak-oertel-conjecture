from fractions import Fraction as F
from random import Random
import json
rng=Random(510273)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,s):return (a[0]*s,a[1]*s)
def hull(v):
 v=sorted(set(v));lo=[];up=[]
 for x in v:
  while len(lo)>1 and cross(sub(lo[-1],lo[-2]),sub(x,lo[-1]))<=0:lo.pop()
  lo.append(x)
 for x in reversed(v):
  while len(up)>1 and cross(sub(up[-1],up[-2]),sub(x,up[-1]))<=0:up.pop()
  up.append(x)
 return lo[:-1]+up[:-1]
def area(v):return sum(cross(a,b) for a,b in zip(v,v[1:]+v[:1]))/2

def clip(v,n):
 out=[]
 for a,b in zip(v,v[1:]+v[:1]):
  fa=sum(x*y for x,y in zip(a,n));fb=sum(x*y for x,y in zip(b,n))
  if fa>=0:out.append(a)
  if fa*fb<0:out.append(mul(sub(mul(a,fb),mul(b,fa)),1/(fb-fa)))
 return out
H=[(F(1),F(0)),(F(1),F(-1)),(F(0),F(-1)),(F(-1),F(0)),(F(-1),F(1)),(F(0),F(1))]
Ts=[[(2,-1),(1,-1),(1,0)],[(-1,2),(-1,1),(0,1)],[(-1,-1),(-1,0),(0,-1)]]
for trial in range(200000):
 pts=list(H)
 for T in Ts:
  for _ in range(2):
   ww=[F(rng.randint(0,50)) for __ in range(3)];sw=sum(ww)
   if not sw:continue
   pts.append(tuple(sum(ww[k]*T[k][j] for k in range(3))/sw for j in range(2)))
 v=hull(pts);ar=area(v);g=tuple(sum((a[j]+b[j])*cross(a,b) for a,b in zip(v,v[1:]+v[:1]))/(6*ar) for j in range(2))
 caps=[]
 for n in [(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]:
  fp=area(clip(v,n))/ar;sp=2*sum(n[j]*g[j] for j in range(2))/ar
  caps.extend([(n,fp,sp),(mul(n,-1),1-fp,-sp)])
 lower=max([(F(0),None)]+[((F(4,9)-p)/(-s),point) for point,p,s in caps if s<0],key=lambda t:t[0]);upper=min([((p-F(4,9))/s,point) for point,p,s in caps if s>0],default=(F(10**20),None),key=lambda t:t[0])
 if lower[0]>upper[0]:
  print('EXACT COUNTER',trial,'vertices',v,'area',ar,'centroid',g,'lower',lower,'upper',upper,'caps',caps,flush=True)
  open('./hexagon-corner-scalar-correction-counter.txt','w').write(repr((v,ar,g,lower,upper,caps)));break
 if trial%10000==0:print(trial,'no hexagon-corner obstruction',flush=True)
else:print('200000 exact hexagon-corner samples no obstruction',flush=True)
