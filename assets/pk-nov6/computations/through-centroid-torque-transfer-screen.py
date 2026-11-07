"""Search actual lower-certified cellwise torque couplings for transfer failure.
Only wholly included pair-cell rectangles earn cost, so positive failures
can subsequently be rationalized to exact certificates.
"""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import kron,eye,csr_matrix,vstack
import json
rng=np.random.default_rng(539915)
best=-1.;tested=0
for it in range(5000):
 N=int(rng.integers(3,10));z=np.arange(N+1,dtype=float);k=int(rng.integers(1,N))
 curv=rng.exponential(1,size=N-1)*(rng.random(N-1)<.5)
 shape=-np.array([sum(curv[j-1]*max(0,i-j) for j in range(1,N)) for i in range(N+1)])
 aa=rng.uniform(.1,30);D=np.dot(z-k,z)
 if abs(D)<1e-9:continue
 bb=-np.dot(z-k,shape+aa)/D
 lengths=shape+aa+bb*z
 if min(lengths)<=1e-6:continue
 bc=curv*rng.random(N-1)
 low=np.array([sum(bc[j-1]*max(0,i-j) for j in range(1,N)) for i in range(N+1)])
 M=lengths.sum();gx=np.dot(lengths,low+lengths/2)/M
 slopes=[0.]
 for i in range(N+1):
  if i!=k:slopes +=[(low[i]-gx)/(i-k),(low[i]+lengths[i]-gx)/(i-k)]
 caps=[]
 for s in slopes:
  thresh=gx+s*(z-k);up=np.maximum(0,np.minimum(lengths,low+lengths-thresh)).sum()
  caps.extend([(up,s,1),(M-up,s,-1)])
 for mass,s,orientation in sorted(caps)[:3]:
  if 2*mass>=M-lengths[k]:continue
  bins=14
  def source(indices):
   records=[]
   for i in indices:
    kk=abs(i-k)
    for j in range(bins):
     ends=low[i]+lengths[i]*np.array([j,j+1])/bins
     f=orientation*(ends-gx-s*(i-k))/kk
     records.append((kk,float(min(f)),float(max(f)),kk*lengths[i]/bins))
   return np.array(records)
  L=source(range(k));R=source(range(k+1,N+1));nl=len(L);nr=len(R)
  # Pair output sign is the sign of the sum of these torque-normalized values.
  cost=(1/L[:,0,None]+1/R[None,:,0])*(L[:,1,None]+R[None,:,1]>=1e-12)
  eq=vstack([kron(eye(nl),csr_matrix(np.ones((1,nr)))),kron(csr_matrix(np.ones((1,nl))),eye(nr))],format='csr')
  rhs=np.r_[L[:,3],R[:,3]]
  opt=linprog(-cost.ravel(),A_eq=eq[:-1],b_eq=rhs[:-1],bounds=(0,None),method='highs')
  if not opt.success:continue
  tested+=1;value=-opt.fun;gap=(value-2*mass)/M
  if gap>best:
   best=gap;data={'case':it,'tested':tested,'N':N,'k':k,'lengths':lengths.tolist(),'lower':low.tolist(),'gx':gx,'M':M,'cap_mass':mass,'slope':s,'orientation':orientation,'target_lower':value,'gap_over_M':gap}
   print(json.dumps(data),flush=True)
   with open('./through-centroid-torque-transfer-best.json','w') as f:json.dump(data,f,indent=2)
  if gap>1e-5:break
 if best>1e-5 or tested>=120:break
print('finished',tested,best,flush=True)
