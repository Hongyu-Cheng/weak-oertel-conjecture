"""Falsification only: exact corner-loss data, no global theorem inferred."""
import numpy as np
from math import sqrt
rng=np.random.default_rng(293001)
norms=np.array([[1.,0.],[0.,1.],[-1.,-1.]])
best=(-1,None)
low=(1e100,None)
for it in range(10000):
 x,s,v=np.exp(rng.uniform(-3,3,3));w=0. if it%7==0 else np.exp(rng.uniform(-3,3))
 P=np.array([[2*v+w,-v-w],[-x,x+s],[-x,-s-w]])
 p=2*v+w;b=x+s;c=x+s+w;L=x+w+2*v;B=x+2*s+w;H=x+s+w+v
 k=L*B/2;q=np.array([p*p*B/(2*L),L*b*b/(2*H),L*c*c/(2*H)]);sig=np.array([p*B/L,L*b/H,L*c/H])
 emax=[]
 for j in range(3):
  ends=[]
  for other in range(3):
   if j==other:continue
   # Along j->other the other cap switches from negative to positive.
   fj,fo=norms[other]@P[j],norms[other]@P[other]
   ends.append(P[j]+fj/(fj-fo)*(P[other]-P[j]))
  emax.append(abs(np.linalg.det(np.stack([ends[0]-P[j],ends[1]-P[j]])))/2)
 ee=np.array(emax)[None,:]*rng.random((30,3))
 if it%5==0:ee=np.array(emax)[None,:]*np.array([[i>>j&1 for j in range(3)] for i in range(8)])
 kk=k-ee.sum(axis=1);qq=q[None,:]-ee;M=(qq/sig).sum(axis=1)
 f=2*np.sqrt(kk[:,None]*qq)/(sig*M[:,None]);phi=f[:,0]+(f[:,1]+f[:,2])**2/4
 C=f[:,0]+(f[:,1]+f[:,2])**2/2
 ei=np.column_stack([f[:,0],(f[:,1]+f[:,2])*f[:,1]/2,(f[:,1]+f[:,2])*f[:,2]/2])
 al=C[:,None]/(2*kk[:,None])+ei/(2*qq)-C[:,None]/(M[:,None]*sig)
 jj=np.unravel_index(np.argmin(al),al.shape)
 if al[jj]<low[0]:low=(al[jj],(it,x,s,v,w,ee[jj[0]].tolist(),jj))
 j=phi.argmax();gap=phi[j]-2
 if gap>best[0]:best=(gap,(it,x,s,v,w,ee[j].tolist(),emax,phi[j]))
 if gap>1e-8:print('COUNTER',best);break
else:print('No violation in screen. best=',best);print('minimum derivative alpha=',low)
