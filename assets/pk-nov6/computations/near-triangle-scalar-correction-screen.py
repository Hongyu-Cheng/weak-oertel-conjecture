exec(open('./polygon-scalar-centroid-correction-exact-screen.py').read().split('for trial in range(20000):')[0])
from fractions import Fraction as F
from itertools import product
trial=0
for ee,gg,jj,facet in product(range(1,20),[2,3,5,7],range(1,20),range(3)):
 e=F(ee,120);lam=[F(1,3)-e,F(1,3),F(1,3)+e];y=(lam[1],lam[2]);q=F(jj,20);eps=F(1,10**gg)
 extra=[(q,-eps),(-eps,q),(q+eps,1-q+eps)][facet];raw=hull([(F(0),F(0)),(F(1),F(0)),(F(0),F(1)),extra]);v=[sub(p,y) for p in raw]
 ar=area(v);g=tuple(sum((a[k]+b[k])*cross(a,b) for a,b in zip(v,v[1:]+v[:1]))/(6*ar) for k in range(2));ps=set()
 for a,b in zip(v,v[1:]+v[:1]):
  u=sub(b,a)
  for cp,dp in zip(v,v[1:]+v[:1]):
   c=mul(cp,-1);d=mul(dp,-1);w=sub(d,c);den=cross(u,w)
   if den==0:continue
   t=cross(sub(c,a),w)/den;ss=cross(sub(c,a),u)/den
   if 0<=t<=1 and 0<=ss<=1:ps.add(add(a,mul(u,t)))
 caps=[]
 for pp in ps:
  n=(-pp[1],pp[0]);fp=area(clip(v,n))/ar;sp=2*sum(n[k]*g[k] for k in range(2))/ar;caps.append((pp,fp,sp))
 lo=max([(F(0),None)]+[((F(4,9)-p)/(-s),point) for point,p,s in caps if s<0],key=lambda z:z[0]);up=min([((p-F(4,9))/s,point) for point,p,s in caps if s>0],default=(F(10**20),None),key=lambda z:z[0])
 if lo[0]>up[0]:
  rec=(raw,lam,ar,g,lo,up,[c for c in caps if c[0] in [lo[1],up[1]]]);print('EXACT NEAR TRIANGLE COUNTER',ee,gg,jj,facet,rec,flush=True);open('./near-triangle-scalar-correction-counter.txt','w').write(repr(rec));break
 trial+=1
 if trial%1000==0:print(trial,'no near-triangle obstruction',flush=True)
else:print('all near-triangle cases no scalar obstruction',trial,flush=True)
