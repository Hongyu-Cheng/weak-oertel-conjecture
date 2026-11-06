"""Bounded falsification only; any candidate requires a separate exact proof."""
from itertools import product
from fractions import Fraction
import numpy as np,time,json
from scipy.optimize import linprog
from scipy.spatial import ConvexHull,QhullError
rng=np.random.default_rng(20260916)
start=time.time();trials=0;graphs=0
U=np.vstack([np.array([v for v in product(range(-5,6),repeat=3) if any(v)],float),rng.normal(size=(3000,3))])
def setup(P):
 N=len(P);P=np.array(P,dtype=int);ids={tuple(p):i for i,p in enumerate(P)};roots={}
 for i,p in enumerate(P):
  c=tuple(p%2)
  if c not in roots or (p@p,tuple(p))<(P[roots[c]]@P[roots[c]],tuple(P[roots[c]])):roots[c]=i
 eq=[];ub=[];edges=[]
 for i,p in enumerate(P):
  v=roots[tuple(p%2)];w=ids[tuple((p+P[v])//2)];edges.append((i,w,v))
  row=np.zeros(3*N);row[i]+=1;row[v]+=1;row[w]-=2;eq.append(row)
  row=np.zeros(3*N);row[i]+=1;row[v]-=1;ub.append(row)
 for i,p in enumerate(P):
  for j,q in enumerate(P):
   row=np.zeros(3*N);row[j]+=1;row[i]-=1;row[N+2*i:N+2*i+2]-=q-p;ub.append(row)
 return P,roots,np.array(eq),np.array(ub),edges
seen=set()
while time.time()-start<150:
 seeds=np.unique(rng.integers(-3,5,size=(rng.integers(4,9),2)),axis=0)
 try:h=ConvexHull(seeds)
 except QhullError:continue
 P=[p for p in product(range(-3,5),repeat=2) if np.max(h.equations[:,:2]@p+h.equations[:,2])<1e-8]
 if not 7<=len(P)<=24 or tuple(P) in seen:continue
 seen.add(tuple(P));P,roots,eq,ub,edges=setup(P);N=len(P)
 for st in range(8):
  res=linprog(np.r_[rng.normal(size=N),np.zeros(2*N)],A_ub=ub,b_ub=np.zeros(len(ub)),A_eq=eq,b_eq=np.zeros(len(eq)),bounds=[(1,2)]*N+[(None,None)]*(2*N),method='highs')
  if not res.success:continue
  f=res.x[:N];trials+=1
  if np.linalg.matrix_rank(np.column_stack([np.ones(N),P,f]),tol=1e-6)<4:continue
  graphs+=1
  # Remove affine height components for stable generic-normal sampling.
  X=np.column_stack([np.ones(N),P]);v=f-X@np.linalg.lstsq(X,f,rcond=None)[0];v/=np.max(abs(v))
  G=np.column_stack([P,v]);V=np.einsum("ij,kj->ik",G,U);assert np.all(np.isfinite(V))
  for R,d in [(0,1),(0,2),(0,4),(0,8),(3,1),(3,2),(30,1),(100000,1)]:
   weights=((R+f)/(R+np.max(f)))**d;T=sum(weights);cert=[]
   for i in range(N):
    mass=np.sum(weights[:,None]*(V>=V[i]-1e-9),axis=0);assert np.all(np.isfinite(mass));ix=int(np.argmin(mass));cert.append((float(mass[ix]),U[ix].tolist()))
    if mass[ix]>=T/4-1e-8:break
   else:
    out={'P':P.tolist(),'r':[str(Fraction(float(t)).limit_denominator(100000)) for t in f],'roots':[[list(c),int(i)]for c,i in roots.items()],'edges':[[int(t)for t in e]for e in edges],'R':R,'d':d,'cert':cert}
    open('./actual_zero_forest_weighted_depth_candidate.json','w').write(json.dumps(out,indent=2,default=lambda x:int(x)))
    print('FOUND',out,flush=True);raise SystemExit
print('no candidate',len(seen),'polygons',trials,'LPs',graphs,'nonaffinegraphs',flush=True)
