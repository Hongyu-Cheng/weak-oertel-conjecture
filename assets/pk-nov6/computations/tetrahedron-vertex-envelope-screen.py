from fractions import Fraction as F
import random
ns={};exec(open('./tetrahedron-section-centroid-screen.py').read().split("if __name__")[0],ns)
cap=ns['cap']
random.seed(27293);count=0;best=F(1)
for it in range(10000):
 a,b=random.sample(range(1,31),2);c,d=random.sample(range(1,31),2)
 t=list(map(F,[a,b,-c,-d]));v,s,l,q=cap(t)
 if max(l)>=F(1,3):continue
 den=1-3*sum(x*x for x in l);prod=F(1)
 for x in l:prod*=x
 e=den*v+s*sum(l[i]**2*t[i] for i in range(4))-27*prod
 ec=den-54*prod-e
 count+=1;best=min(best,e,ec)
 if min(e,ec)<0:
  print('EXACT ENVELOPE COUNTER','t',t,'lambda',l,'cap',v,'S',s,'slack',e,'complement_slack',ec,flush=True);break
else:print('No envelope violation in',count,'exact rational tests; smallest slack',best,flush=True)
