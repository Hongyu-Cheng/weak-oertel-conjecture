import numpy as np
import math
for m in [4,6,8,10,12,16]:
 P=[(x,y) for x in range(-m,m+1) for y in range(-m,m+1) if max(x+y,y-2*x,x-2*y)<=m]
 ix={z:i for i,z in enumerate(P)}
 rr=np.array([1-max(x+y,y-2*x,x-2*y)/(m+1) for x,y in P])
 partners=[[((rr[ix[z]]+rr[ix[(2*p[0]-z[0],2*p[1]-z[1])]])/2) for z in P if z<(2*p[0]-z[0],2*p[1]-z[1]) and (2*p[0]-z[0],2*p[1]-z[1]) in ix] for p in P]
 angles=sorted(set(round((math.atan2(y,x)+math.pi/2)%(2*math.pi),13) for x,y in P if x or y))
 norms=[(math.cos((a+(angles[(j+1)%len(angles)]+(2*math.pi if j==len(angles)-1 else 0)))/2),math.sin((a+(angles[(j+1)%len(angles)]+(2*math.pi if j==len(angles)-1 else 0)))/2)) for j,a in enumerate(angles)]
 arr=np.array(P); sg=np.array([arr@np.array(v)>=-1e-10 for v in norms],float)
 refl=[(ix[z],ix[(-z[0],-z[1])]) for z in P if z<(0,0) and (-z[0],-z[1]) in ix]
 for d in [2,3,4,6,8,12]:
  M=sum(rr**d); target=M/4
  old=0;oldwhere=None
  for i,rp in enumerate(rr):
   rho=np.array(partners[i]); qs=np.unique(np.r_[0,rp,rho,(d+1)/d*rho]);qs=qs[qs<=rp+1e-10]
   vals=qs**d+2*np.sum(np.maximum(0,np.minimum(qs[:,None],(d+1)*rho[None,:]-d*qs[:,None]))**d,axis=1)
   b=vals.max()
   if b>old:old=b;oldwhere=(P[i],qs[vals.argmax()])
  best=0;where=None
  for q in np.linspace(.02,1,197):
   w=np.maximum(0,np.minimum(q,(d+1)*rr-d*q))**d
   D=(sg@w).min();R=sum(min(w[i],w[j]) for i,j in refl)
   if D+R>best:best=D+R;where=q
  print(m,d,len(P),'target',round(target,7),'old',round(old,7),'new',round(best,7),'q',where,'oldwhere',oldwhere,flush=True)
