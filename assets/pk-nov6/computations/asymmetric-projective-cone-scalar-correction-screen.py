exec(open('./polygon-scalar-centroid-correction-exact-screen.py').read().split('for trial in range(20000):')[0])
from fractions import Fraction as F
for trial in range(50000):
 raw=hull([(F(rng.randint(-7,7)),F(rng.randint(-7,7))) for j in range(rng.randint(5,12))])
 if len(raw)<3:continue
 ar0=area(raw);c0=tuple(sum((a[j]+b[j])*cross(a,b) for a,b in zip(raw,raw[1:]+raw[:1]))/(6*ar0) for j in range(2));D=[sub(p,c0) for p in raw]
 kk=(F(rng.randint(-5,5)),F(rng.randint(-5,5)));sup=max(abs(sum(a*b for a,b in zip(kk,p))) for p in D)
 if not sup:continue
 positive=max(sum(a*b for a,b in zip(kk,p)) for p in D);negative=-min(sum(a*b for a,b in zip(kk,p)) for p in D)
 kk=mul(kk,F(rng.randint(50,99),100)*min(1/positive,1/(2*negative)))
 v=[mul(p,1/(1-sum(a*b for a,b in zip(kk,p)))) for p in D]
 ar=area(v);g=tuple(sum((a[j]+b[j])*cross(a,b) for a,b in zip(v,v[1:]+v[:1]))/(6*ar) for j in range(2));ps=set()
 for aa,bb in zip(v,v[1:]+v[:1]):
  uu=sub(bb,aa)
  for cp,dp in zip(v,v[1:]+v[:1]):
   cc=mul(cp,-1);dd=mul(dp,-1);ww=sub(dd,cc);den=cross(uu,ww)
   if not den:continue
   t=cross(sub(cc,aa),ww)/den;ss=cross(sub(cc,aa),uu)/den
   if 0<=t<=1 and 0<=ss<=1:ps.add(add(aa,mul(uu,t)))
 caps=[]
 for pp in ps:
  n=(-pp[1],pp[0]);fp=area(clip(v,n))/ar;sp=F(9,8)*2*sum(n[j]*g[j] for j in range(2))/ar;caps.append(('vertical',pp,fp,sp))
 po=F(8,27)*ar0/ar;so=-ar0/(9*ar)*(1+9*sum(a*b for a,b in zip(kk,g)))
 caps.extend([('apex',kk,po,so),('apex complement',kk,1-po,-so)])
 low=max([(F(0),None)]+[((F(27,64)-p)/(-s),(name,point)) for name,point,p,s in caps if s<0],key=lambda v:v[0]);up=min([((p-F(27,64))/s,(name,point)) for name,point,p,s in caps if s>0],default=(F(10**30),None),key=lambda v:v[0])
 if low[0]>up[0]:
  rec=(D,kk,v,ar0,ar,g,low,up,caps);print('EXACT CONE FAILURE',trial,rec,flush=True);open('./asymmetric-projective-cone-scalar-correction-counter.txt','w').write(repr(rec));break
 if trial%1000==0:print(trial,'no exact projective-polygon-cone scalar obstruction',flush=True)
else:print('50000 exact asymmetric-range projective-polygon-cone samples no scalar obstruction',flush=True)
