import numpy as np,json
from scipy.optimize import minimize,linprog,LinearConstraint,Bounds
rng=np.random.default_rng(98362271)
def endpoint(w,v,z,j,t,initial):
 A=np.stack([np.ones(len(w)),z-j])
 ans=minimize(lambda q:.5*(q@q)-v@q,initial,jac=lambda q:q-v,constraints=[LinearConstraint(A,[t,0],[t,0])],bounds=Bounds(np.zeros(len(w)),w),method='SLSQP',options={'ftol':1e-10,'maxiter':150})
 if not ans.success or max(abs(A@ans.x-[t,0]))>1e-6:return None
 return (v@ans.x-.5*(ans.x@ans.x))/t,ans.x

def capdepth(w,l,u,z,j,y):
 slopes=np.array([(v-y)/(i-j) for i,li,ui in zip(z,l,u) if i!=j for v in [li,ui]])
 vals=np.clip(y+slopes[:,None]*(z-j)[None,:]-l,0,w).sum(axis=1).tolist()
 vals += [sum(w[z<j])+y-l[j],sum(w[z>j])+y-l[j]]
 M=sum(w)
 return min(min(vals),M-max(vals))/M
best=1
for it in range(100000):
 N=int(rng.integers(3,13));z=np.arange(N);w=np.linspace(rng.uniform(.001,1),rng.uniform(.001,1),N)
 for q in rng.choice(np.arange(1,N-1),size=int(rng.integers(1,N-1)),replace=False):w+=rng.exponential(2)*np.minimum(z/q,(N-1-z)/(N-1-q))
 curv=-np.diff(w,2);theta=rng.uniform(0,1,N-2)
 if it%3==0:theta=rng.integers(0,2,N-2)
 u=-sum((cv*th*np.maximum(z-q,0) for q,cv,th in zip(range(1,N-1),curv,theta)),np.zeros(N));l=u-w;M=w.sum();mu=w@z/M;k=int(np.floor(mu));th=mu-k;t=th*M
 if min(th,1-th)<.001:continue
 A=np.stack([np.ones(N),z-k-1]);lp=linprog(np.zeros(N),A_eq=A,b_eq=[t,0],bounds=list(zip(np.zeros(N),w)),method='highs')
 if not lp.success:raise Exception('feasibility')
 hi=endpoint(w,u,z,k+1,t,lp.x);neglo=endpoint(w,-l,z,k+1,t,lp.x)
 if hi is None or neglo is None:continue
 h,hm=hi;nl,lm=neglo;moment=((u*u-l*l)/2).sum();cs=[]
 for y,label,m in [(h,'upper',hm),(-nl,'lower',lm)]:
  yc=(moment-t*y)/(M-t)
  cs.extend([dict(j=k+1,y=y,depth=capdepth(w,l,u,z,k+1,y),label=label,m=m.tolist()),dict(j=k,y=yc,depth=capdepth(w,l,u,z,k,yc),label=label+' complement')])
 value=max(x['depth'] for x in cs)
 if value<best:
  best=value;out=dict(it=it,w=w.tolist(),l=l.tolist(),u=u.tolist(),M=M,mu=mu,t=t,candidates=cs)
  print(json.dumps(out),flush=True);json.dump(out,open('./adjacent_integer_partition_four_centroid_best.json','w'),indent=2)
 if best<.25-1e-6:break
