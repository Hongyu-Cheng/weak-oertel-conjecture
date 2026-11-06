import numpy as np,json
from scipy.optimize import minimize,LinearConstraint,Bounds
rng=np.random.default_rng(92439855)
def capdepth(w,l,u,z,j,y):
 slopes=np.array([(v-y)/(i-j) for i,li,ui in zip(z,l,u) if i!=j for v in [li,ui]])
 vals=np.clip(y+slopes[:,None]*(z-j)[None,:]-l,0,w).sum(axis=1).tolist()
 vals += [sum(w[z<j])+y-l[j],sum(w[z>j])+y-l[j]]
 M=sum(w)
 return min(min(vals),M-max(vals))/M

def candidate(w,l,u,z,j):
 N=len(w);A=np.zeros((3,2*N));A[0,:N]=1;A[0,N:]=-1;A[1,:N]=z-j;A[2,N:]=z-j
 v=np.concatenate([u,-l]);b=np.concatenate([w,w]);ini=np.zeros(2*N);ini[j]=ini[N+j]=w[j]/2
 ans=minimize(lambda x:.5*x@x-v@x,ini,jac=lambda x:x-v,constraints=[LinearConstraint(A,np.zeros(3),np.zeros(3))],bounds=Bounds(np.zeros(2*N),b),method='SLSQP',options={'ftol':1e-9,'maxiter':150})
 if not ans.success or max(abs(A@ans.x))>1e-6:return None
 a=ans.x[:N];bb=ans.x[N:];t=sum(a);hp=u@a-.5*a@a;nhp=-l@bb-.5*bb@bb
 y=(hp-nhp)/(2*t);score=hp+nhp
 return dict(j=int(j),y=float(y),t=float(t),score=float(score),depth=float(capdepth(w,l,u,z,j,y)),plus=a.tolist(),minus=bb.tolist())
best=1
for it in range(20000):
 N=int(rng.integers(3,10));z=np.arange(N);w=np.linspace(rng.uniform(.001,1),rng.uniform(.001,1),N)
 for q in rng.choice(np.arange(1,N-1),size=int(rng.integers(1,N-1)),replace=False):w+=rng.exponential(2)*np.minimum(z/q,(N-1-z)/(N-1-q))
 curv=-np.diff(w,2);theta=rng.uniform(0,1,N-2)
 if it%3==0:theta=rng.integers(0,2,N-2)
 u=-sum((cv*th*np.maximum(z-q,0) for q,cv,th in zip(range(1,N-1),curv,theta)),np.zeros(N));l=u-w
 cs=[candidate(w,l,u,z,j) for j in range(N)]
 if any(c is None for c in cs):continue
 m=max(cs,key=lambda c:c['score']);dep=m['depth']
 if dep<best:
  best=dep;out=dict(it=it,w=w.tolist(),u=u.tolist(),l=l.tolist(),candidates=cs,chosen=m)
  print(json.dumps(out),flush=True);json.dump(out,open('./raw-moment-john-width-selector-best.json','w'),indent=2)
 if dep<.25-1e-6:break
