exec(open('./all_mass_moment_centroid_path_screen.py').read().split('best=1')[0])
from scipy.optimize import minimize_scalar
rng=np.random.default_rng(9928347)
best=1
for it in range(3000):
 a=int(rng.integers(1,41));b=int(rng.integers(10,251));e1=int(rng.integers(0,min(15,b)));e2=int(rng.integers(0,min(15,b-e1)))
 ds=np.array([b,b-e1,b-e1-e2]);w=np.r_[a,a+np.cumsum(ds)]
 c=2*a+ds[0]-ds[2]+float(rng.uniform(.001,8))
 w=np.r_[w,c];z=np.arange(5);curv=-np.diff(w,2)
 if min(curv)<0:continue
 theta=rng.integers(0,2,3)
 if it%3==0:theta=np.zeros(3)
 u=-sum((cv*th*np.maximum(z-q,0) for q,cv,th in zip(range(1,4),curv,theta)),np.zeros(5));l=u-w
 W=sum(w);w,u,l=w/W,u/W,l/W;j=3
 if np.cumsum(w)[2]>=.5 or w[4]>=.5:continue
 lp=linprog(-np.ones(5),A_eq=[z-j],b_eq=[0],bounds=list(zip(np.zeros(5),w)),method='highs');Tmax=-lp.fun
 # Try only a handful to identify whether the observed continuous path
 # already crosses the deep interval, using quasiconcavity in y.
 ts=Tmax*np.r_[.0001,.1,.25,.4,.55,.7,.85,.95,1.]
 ans=path(w,u,l,j,ts)
 if ans is None:continue
 ys=[x[1] for x in ans]
 opt=minimize_scalar(lambda y:-depth(l,u,j,y),bounds=(min(ys),max(ys)),method='bounded',options={'xatol':1e-11})
 score=max(max(x[2] for x in ans),-opt.fun)
 if score<best:
  best=score;out=dict(it=it,w=(w*W).tolist(),u=(u*W).tolist(),j=j,Tmax=Tmax*W,score=score,path=ans)
  print(json.dumps(out),flush=True);json.dump(out,open('./all_mass_targeted_interval_path_best.json','w'),indent=2)
 if score<.25-1e-7 and len(ans)==len(ts):break
