exec(open('./polygon-scalar-centroid-correction-exact-screen.py').read().split('for trial in range(20000):')[0])
from fractions import Fraction as F
for trial in range(100000):
 h=1+F(rng.randint(1,50),51);a=2*(h*h-h+1)/(3*(h-1));l=h+F(rng.randint(1,50),51)*(a-h)
 yy=F(rng.randint(-50,50),51)*(a-l)
 v=hull([(-h,a-h),(-h,-a+h),(F(1),a+1),(F(1),-a-1),(-l,yy)])
 ar=area(v);g=tuple(sum((aa[j]+bb[j])*cross(aa,bb) for aa,bb in zip(v,v[1:]+v[:1]))/(6*ar) for j in range(2));ps=set()
 for aa,bb in zip(v,v[1:]+v[:1]):
  uu=sub(bb,aa)
  for cp,dp in zip(v,v[1:]+v[:1]):
   cc=mul(cp,-1);dd=mul(dp,-1);ww=sub(dd,cc);den=cross(uu,ww)
   if not den:continue
   t=cross(sub(cc,aa),ww)/den;ss=cross(sub(cc,aa),uu)/den
   if 0<=t<=1 and 0<=ss<=1:ps.add(add(aa,mul(uu,t)))
 caps=[]
 for pp in ps:
  n=(-pp[1],pp[0]);fp=area(clip(v,n))/ar;sp=2*sum(n[j]*g[j] for j in range(2))/ar;caps.append(('vertical',pp,fp,sp))
 # D=B intersect[-h,h] has centroid0 by construction and upper endpoint1<h.
 Darea=(a+1)**2-(a-h)**2;R=Darea/ar;po=1-R/2;so=-R*g[0]/(2*h)
 caps.extend([('oblique',h,po,so),('oblique complement',h,1-po,-so)])
 low=max([(F(0),None)]+[((F(27,64)-p)/(-s),(name,point)) for name,point,p,s in caps if s<0],key=lambda v:v[0]);up=min([((p-F(27,64))/s,(name,point)) for name,point,p,s in caps if s>0],default=(F(10**30),None),key=lambda v:v[0])
 if low[0]>up[0]:
  rec=(h,a,l,v,ar,g,low,up,caps);print('EXACT PENTAGON PRISM FAILURE',trial,rec,flush=True);open('./pentagon-prism-scalar-correction-counter.txt','w').write(repr(rec));break
 if trial%5000==0:print(trial,'no exact pentagon-prism scalar obstruction',flush=True)
else:print('100000 exact pentagon-prism samples no scalar obstruction',flush=True)
