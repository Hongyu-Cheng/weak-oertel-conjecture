from itertools import combinations, product
from fractions import Fraction
import random
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull
ns={};exec(open('./fractional-tverberg-search-3d.py').read().split('random.seed')[0],ns)
edges=ns['edges']

def dual(es,w):
 mat=np.zeros((len(es),len(w)))
 for i,e in enumerate(es):mat[i,list(e)]=-1
 r=linprog(w,A_ub=mat,b_ub=-np.ones(len(es)),bounds=(0,1),method='highs')
 return r.fun,r.x

def inside(h,p):return np.all(h.equations[:,:3]@p+h.equations[:,3]<1e-8)
random.seed(817334)
for it in range(6000):
 abc=random.choice([(2,3,6),(2,4,4),(3,3,3)])
 grid=[p for p in product(*(range(a+1) for a in abc)) if sum(Fraction(p[i],abc[i]) for i in range(3))<=1]
 raw=random.sample(grid,random.randrange(10,min(24,len(grid))))
 try:h=ConvexHull(np.array(raw))
 except Exception:continue
 vs=[raw[i] for i in h.vertices]
 if len(vs)<=8:continue
 pts=[p for p in grid if inside(h,np.array(p))]
 eslist=[edges(vs,p) for p in pts]
 w=np.ones(len(vs))/len(vs)
 best=1
 for rnd in range(8):
  vals=[dual(es,w) for es in eslist]
  mx=max(v[0] for v in vals)
  best=min(best,mx)
  if mx<.125-1e-7:
   ww=[Fraction(float(v)).limit_denominator(100000) for v in w]
   ds=[]
   for p,es in zip(pts,eslist):
    val,t=dual(es,[float(v) for v in ww]);tt=[Fraction(float(v)).limit_denominator(10000) for v in t]
    assert all(sum(tt[i] for i in e)>=1 for e in es)
    ds.append((p,sum(a*b for a,b in zip(ww,tt)),tt))
   if max(d[1] for d in ds)<sum(ww)/8:
    print('EXACT COUNTER',vs,'weights',ww,'pts',pts,'duals',ds,flush=True);raise SystemExit
  # Select a dual certificate at each target and improve weights within that dual cell.
  mat=np.array([list(t)+[-1] for v,t in vals])
  rr=linprog([0]*len(vs)+[1],A_ub=mat,b_ub=np.zeros(len(vals)),A_eq=[np.append(np.ones(len(vs)),0)],b_eq=[1],bounds=[(0,1)]*len(vs)+[(0,1)],method='highs')
  if rnd<3:w=rr.x[:-1]
  else:
   # Random restarts allow changes of dual cells; screening is not a proof.
   w=np.array([random.random()**2 for _ in vs]);w/=sum(w)
 if it%50==0:print('screen',it,'template',abc,'vertices',len(vs),'candidates',len(pts),'best',best,flush=True)
print('completed',flush=True)
