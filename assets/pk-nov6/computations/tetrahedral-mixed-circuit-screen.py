from fractions import Fraction as F
from itertools import combinations
import random
ns={};exec(open('./tetrahedron-section-centroid-screen.py').read().split("if __name__")[0],ns)
random.seed(719300);best=1.;record=None
for it in range(4000):
 a,b=random.sample(range(1,31),2);c,d=random.sample(range(1,31),2)
 t=list(map(F,[a,b,-c,-d]));l,caps=ns['data'](t)
 for k in range(2,5):
  for inds in combinations(range(len(caps)),k):
   if not any(i<2 for i in inds):continue
   rows=[[float(caps[j][2][i]) for j in inds] for i in range(3)]+[[1.]*k]
   w=ns['solve'](rows,[0.,0.,0.,1.],1e-8)
   if w is None or min(w)<=1e-7:continue
   val=sum(w[i]*float(caps[j][1]) for i,j in enumerate(inds))
   if val<best:
    best=val;record=(t,l,[caps[j][0] for j in inds],w)
   if val<float(F(27,64))-1e-8:
    exactrows=[[caps[j][2][i] for j in inds] for i in range(3)]+[[F(1)]*k]
    ww=ns['solve'](exactrows,[F(0),F(0),F(0),F(1)])
    if ww is not None and min(ww)>0:
     vv=sum(ww[i]*caps[j][1] for i,j in enumerate(inds))
     if vv<F(27,64):print('EXACT COUNTER',t,l,[caps[j] for j in inds],ww,vv,flush=True);raise SystemExit
 if it%500==0:print('screen',it,'mixed best',best,'record',record,flush=True)
print('finished',best,record,flush=True)
