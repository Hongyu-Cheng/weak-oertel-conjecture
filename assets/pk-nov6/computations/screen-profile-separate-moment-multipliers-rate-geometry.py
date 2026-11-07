"""Discovery only: independent section-moment multipliers on the two sides."""
import importlib.util, numpy as np, random, json
spec=importlib.util.spec_from_file_location('basic','./screen-profile-prestationary-multipliers-rate-geometry.py');basic=importlib.util.module_from_spec(spec);spec.loader.exec_module(basic)
slopes=[0.]+[10**(-3+i/12) for i in range(85)]
rng=random.Random(45368123)
for m in [2,3,4,6]:
 for trial in range(12000):
  A=rng.randint(1,10);B=rng.randint(1,10)
  h=basic.hull([(float(z),float(rng.randint(1,24))) for z in range(-A,B+1)])
  ds=np.array([basic.data(h,s,m) for s in slopes]);p,C,M=ds.T;g=((m+1)/(m+2))**(m+1)
  pos=np.flatnonzero(M>1e-8);neg=np.flatnonzero(M<-1e-8)
  lower=(p[0]-1+g)/C[0];upper=(p[0]-g)/C[0];lc=uc=[0,0]
  if len(pos) and len(neg):
   i=pos[:,None];j=neg[None,:]
   den=-M[j]*C[i]+M[i]*C[j]
   lo=(-M[j]*(p[i]-1+g)+M[i]*(p[j]-1+g))/den
   up=(-M[j]*(p[i]-g)+M[i]*(p[j]-g))/den
   a=np.unravel_index(np.argmax(lo),lo.shape);b=np.unravel_index(np.argmin(up),up.shape)
   if lo[a]>lower:lower=lo[a];lc=[int(pos[a[0]]),int(neg[a[1]])]
   if up[b]<upper:upper=up[b];uc=[int(pos[b[0]]),int(neg[b[1]])]
  if lower>upper+1e-7:
   result={'m':m,'trial':trial,'profile':h,'lower':lower,'upper':upper,'lowpair':[(slopes[k],list(ds[k])) for k in lc],'uppair':[(slopes[k],list(ds[k])) for k in uc]}
   print('CANDIDATE ONLY',result,flush=True)
   with open('./profile-separate-moment-candidate-rate-geometry.json','w') as f:json.dump(result,f,indent=2)
   raise SystemExit
 print('completed m',m,flush=True)
