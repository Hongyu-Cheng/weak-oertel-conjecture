import numpy as np,json
from scipy.optimize import minimize,LinearConstraint,Bounds,linprog
rng=np.random.default_rng(999431)
def depth(l,u,j,y):
 z=np.arange(len(l));w=u-l;M=sum(w)
 aa=[(v-y)/(i-j) for i in z if i!=j for v in (l[i],u[i])]
 vals=[np.clip(y+a*(z-j)-l,0,w).sum() for a in aa]
 vals += [sum(w[z<j])+y-l[j],sum(w[z>j])+y-l[j]]
 return min(min(vals),M-max(vals))/M

def path(w,u,l,j,ts):
 N=len(w);z=np.arange(N)-j;A=np.array([np.ones(N),z]);box=Bounds(np.zeros(N),w)
 ans=[]
 for t in ts:
  ini=np.zeros(N);ini[j]=min(t,w[j])
  # LP supplies a feasible start even beyond the anchor's own mass.
  ip=linprog(np.zeros(N),A_eq=A,b_eq=[t,0],bounds=list(zip(np.zeros(N),w)),method='highs')
  if not ip.success:return None
  vals=[]
  for v in (u,-l):
   op=minimize(lambda m:.5*m@m-v@m,ip.x,jac=lambda m:m-v,
     constraints=[LinearConstraint(A,[t,0],[t,0])],bounds=box,
     method='SLSQP',options={'ftol':1e-11,'maxiter':100})
   if not op.success or max(abs(A@op.x-[t,0]))>1e-7:return None
   vals.append(v@op.x-.5*op.x@op.x)
  y=(vals[0]-vals[1])/(2*t)
  de=depth(l,u,j,y)
  ans.append((float(t),float(y),float(de)))
  if de>=.25000001:return ans
 return ans
best=1
for it in range(5000):
 N=int(rng.integers(4,9));z=np.arange(N);curv=rng.integers(0,31,N-2)
 w=np.linspace(int(rng.integers(1,31)),int(rng.integers(1,31)),N)
 for q,c in enumerate(curv,1):w += c*(np.minimum(z,q)-z*q/(N-1))
 theta=rng.integers(0,2,N-2)
 if it%3==0:theta=np.ones(N-2)
 if it%3==1:theta=np.zeros(N-2)
 u=-sum((int(c*th)*np.maximum(z-q,0) for q,c,th in zip(range(1,N-1),curv,theta)),np.zeros(N));l=u-w
 W=sum(w);w,u,l=w/W,u/W,l/W
 j=int(np.searchsorted(np.cumsum(w),.5))
 if j in (0,N-1) or w[j]>=.5:continue
 A=np.array([z-j]);lp=linprog(-np.ones(N),A_eq=A,b_eq=[0],bounds=list(zip(np.zeros(N),w)),method='highs')
 Tmax=-lp.fun
 # Prioritize extremes, then a dense interior grid; early stop on success.
 ts=Tmax*np.r_[.0001,.5,.99,np.linspace(.025,.975,39),1.0]
 ans=path(w,u,l,j,ts)
 if ans is None:continue
 score=max(a[2] for a in ans)
 if score<best:
  best=score;out=dict(it=it,N=N,w=(w*W).tolist(),u=(u*W).tolist(),l=(l*W).tolist(),j=j,Tmax=Tmax*W,maxdepth=score,path=ans)
  print(json.dumps(out),flush=True);json.dump(out,open('./all_mass_moment_centroid_path_best.json','w'),indent=2)
 if len(ans)==len(ts) and score<.25-1e-7:break
