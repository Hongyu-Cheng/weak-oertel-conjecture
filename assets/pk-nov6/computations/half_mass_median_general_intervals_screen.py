import numpy as np,json
from scipy.optimize import minimize,linprog,LinearConstraint,Bounds
rng=np.random.default_rng(893675)
def endpoint(w,v,z,j,t,initial):
 A=np.stack([np.ones(len(w)),z-j])
 ans=minimize(lambda q:.5*(q@q)-v@q,initial,jac=lambda q:q-v,constraints=[LinearConstraint(A,[t,0],[t,0])],bounds=Bounds(np.zeros(len(w)),w),method='SLSQP',options={'ftol':1e-11,'maxiter':150})
 if not ans.success or max(abs(A@ans.x-[t,0]))>1e-7:return None
 return (v@ans.x-.5*(ans.x@ans.x))/t,ans.x

def capdepth(w,l,u,z,j,y):
 slopes=[(v-y)/(i-j) for i,li,ui in zip(z,l,u) if i!=j for v in [li,ui]]
 vals=[sum(np.clip(y+s*(z-j)-l,0,w)) for s in slopes]
 vals += [sum(w[z<j])+y-l[j],sum(w[z>j])+y-l[j]]
 M=sum(w)
 return min(min(vals),M-max(vals))/M,slopes,vals
best=1
for it in range(20000):
 N=int(rng.integers(4,11));z=np.arange(N);w=np.linspace(rng.uniform(.001,1),rng.uniform(.001,1),N)
 for q in rng.choice(np.arange(1,N-1),size=int(rng.integers(1,N-1)),replace=False):w+=rng.exponential(2)*np.minimum(z/q,(N-1-z)/(N-1-q))
 curv=-np.diff(w,2);theta=rng.uniform(0,1,N-2)
 if it%3==0:theta=rng.integers(0,2,N-2)
 u=-sum((cv*th*np.maximum(z-q,0) for q,cv,th in zip(range(1,N-1),curv,theta)),np.zeros(N));l=u-w;M=w.sum();t=M/2
 elig=[j for j in range(N) if sum(w[:j+1])>=t-1e-10 and sum(w[j:])>=t-1e-10]
 candidates=[]
 for j in elig:
  T=linprog(-np.ones(N),A_eq=(z-j).reshape(1,-1),b_eq=[0],bounds=list(zip(np.zeros(N),w)),method='highs')
  if not T.success or -T.fun<t-1e-8:continue
  initial=T.x*(t/(-T.fun))
  hi=endpoint(w,u,z,j,t,initial);neglo=endpoint(w,-l,z,j,t,initial)
  if hi is None or neglo is None:continue
  h,hm=hi;nl,lm=neglo;y=(h-nl)/2;length=h+nl
  dep,slopes,vals=capdepth(w,l,u,z,j,y)
  candidates.append(dict(j=int(j),y=y,length=length,depth=dep,upperm=hm.tolist(),lowerm=lm.tolist()))
 if not candidates:continue
 length=max(x['length'] for x in candidates);selected=[x for x in candidates if abs(x['length']-length)<1e-8];ans=min(selected,key=lambda x:x['depth'])
 if ans['depth']<best:
  best=ans['depth'];out=dict(it=it,w=w.tolist(),l=l.tolist(),u=u.tolist(),M=M,candidates=candidates)
  print(json.dumps(out),flush=True);json.dump(out,open('./half_mass_median_general_intervals_best.json','w'),indent=2)
 if best<.25-1e-6:break
