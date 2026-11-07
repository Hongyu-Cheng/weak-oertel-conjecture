"""Numerical falsification only; candidates require independent exact certification."""
import importlib.util,json,random,sys
import numpy as np
from scipy.optimize import minimize
spec=importlib.util.spec_from_file_location('basic','./screen-profile-prestationary-multipliers-rate-geometry.py');basic=importlib.util.module_from_spec(spec);spec.loader.exec_module(basic)
rng=random.Random(10831947);m=int(sys.argv[1]);starts=int(sys.argv[2]);target=((m+1)/(m+2))**(m+1)
sgrid=np.r_[0.,np.geomspace(.0003,300,65)]
def profile(x):
 l,hL,hR,position=x[:4];y=position-l
 return [(-l-y,hL),(-y,1.),(1-l-y,hR)]
def dec(x):
 h=profile(x);ss=np.expm1(x[4:8]);rr=np.array([basic.data(h,float(s),m) for s in ss]);w=x[8:10]
 return h,ss,w,rr,w[0]*rr[0]+(1-w[0])*rr[1],w[1]*rr[2]+(1-w[1])*rr[3]
def obj(x):
 *_,a,b=dec(x);return (b[1]*a[0]+a[1]*(1-b[0]))/(a[1]+b[1])
def moments(x):
 *_,a,b=dec(x);return np.array([a[2]/a[1],b[2]/b[1]])
def init(h):
 rr=np.array([basic.data(h,s,m) for s in sgrid]);p,c,k=rr.T;ip=np.where(k>1e-8)[0];im=np.where(k<-1e-8)[0]
 if not len(ip) or not len(im):return
 i,j=np.meshgrid(ip,im,indexing='ij');i,j=i.ravel(),j.ravel();w=-k[j]/(k[i]-k[j]);pp=np.r_[p[0],w*p[i]+(1-w)*p[j]];cc=np.r_[c[0],w*c[i]+(1-w)*c[j]];pairs=[(0,0,.5)]+list(zip(i,j,w));lo,hi=0.,.5
 for _ in range(30):
  g=(lo+hi)/2
  if max((pp-1+g)/cc)<=min((pp-g)/cc):lo=g
  else:hi=g
 return pairs[int(np.argmin((pp-lo)/cc))],pairs[int(np.argmax((pp-1+lo)/cc))]
best=1.;done=0
while done<starts:
 x=np.array([rng.uniform(.03,.97),rng.random(),rng.random(),rng.uniform(.03,.97)])
 initial=init(profile(x))
 if initial is None:continue
 a,b=initial;xx=np.r_[x,np.log1p([sgrid[a[0]],sgrid[a[1]],sgrid[b[0]],sgrid[b[1]]]),a[2],b[2]]
 res=minimize(obj,xx,method='SLSQP',bounds=[(.0001,.9999),(0,1),(0,1),(.0001,.9999)]+[(0,8)]*4+[(0,1)]*2,constraints=[{'type':'eq','fun':moments}],options={'maxiter':450,'ftol':3e-12})
 done+=1
 if max(abs(moments(res.x)))<1e-8 and res.fun<best:
  best=float(res.fun);h,s,w,rr,aa,bb=dec(res.x);out={'m':m,'trial':done,'value':best,'target':target,'profile':h,'slopes':s.tolist(),'weights':w.tolist(),'records':rr.tolist(),'moments':moments(res.x).tolist(),'success':bool(res.success)};print('DISCOVERY ONLY',json.dumps(out),flush=True)
  if best<target-1e-6:
   with open('./single-kink-two-mixture-candidate-rate-geometry.json','w') as f:json.dump(out,f,indent=2)
   break
 if done%10==0:print('completed',done,'best',best,flush=True)
