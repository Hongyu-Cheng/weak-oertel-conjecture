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
for trial in range(20000):
 raw=hull([(F(rng.randint(-10,10)),F(rng.randint(-10,10))) for _ in range(rng.randint(5,14))])
 if len(raw)<3:continue
 weights=[F(rng.randint(1,20)) for _ in raw];tot=sum(weights);y=tuple(sum(w*p[j] for p,w in zip(raw,weights))/tot for j in range(2));v=[sub(p,y) for p in raw]
 ar=area(v);g=tuple(sum((a[j]+b[j])*cross(a,b) for a,b in zip(v,v[1:]+v[:1]))/(6*ar) for j in range(2))
 ps=set()
 for a,b in zip(v,v[1:]+v[:1]):
  u=sub(b,a)
  for cp,dp in zip(v,v[1:]+v[:1]):
   c=mul(cp,-1);d=mul(dp,-1);w=sub(d,c);den=cross(u,w)
   if den==0:continue
   t=cross(sub(c,a),w)/den;ss=cross(sub(c,a),u)/den
   if 0<=t<=1 and 0<=ss<=1:ps.add(add(a,mul(u,t)))
 caps=[]
 for pp in ps:
  n=(-pp[1],pp[0]);fp=area(clip(v,n))/ar;sp=2*sum(n[j]*g[j] for j in range(2))/ar
  caps.append((pp,fp,sp))
 lower=max([(F(0),None)]+[((F(4,9)-p)/(-s),point) for point,p,s in caps if s<0],key=lambda t:t[0]);upper=min([((p-F(4,9))/s,point) for point,p,s in caps if s>0],default=(F(10**20),None),key=lambda t:t[0])
 if lower[0]>upper[0]:
  print('EXACT COUNTER trial',trial,'raw',raw,'weights',weights,'center',y,'area',ar,'g',g,'lower',lower,'upper',upper,flush=True)
  for pp,p,s in caps:
   if pp in [lower[1],upper[1]]:print('cap',pp,p,s,flush=True)
  rec={'raw':raw,'weights':weights,'center':y,'area':ar,'centroid_relative':g,'lower':lower,'upper':upper,'caps':[x for x in caps if x[0] in [lower[1],upper[1]]]}
  open('./polygon-scalar-centroid-correction-exact-candidate.txt','w').write(repr(rec));break
 if trial%1000==0:print(trial,'no obstruction so far',flush=True)
else:print('20000 exact polygon samples no obstruction',flush=True)
