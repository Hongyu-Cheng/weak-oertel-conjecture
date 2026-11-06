"""Bounded falsification of diagonal spectral quasiconvexity; no theorem from screens."""
import numpy as np
from scipy.spatial import ConvexHull
rng=np.random.default_rng(773108)
vs=np.array([[1.,0.],[0.,1.],[-1.,-1.]])
def area(P): return abs(np.sum(P[:,0]*np.roll(P[:,1],-1)-P[:,1]*np.roll(P[:,0],-1)))/2
def clip(P,v):
 out=[]
 for p,q in zip(P,np.roll(P,-1,axis=0)):
  a,b=p@v,q@v
  if a>=0:out.append(p)
  if a*b<0:out.append(p+a/(a-b)*(q-p))
 return np.array(out)
def val(P):
 k=area(P);Q=[];S=[]
 for v in vs:
  C=clip(P,v)
  if len(C)<3:return None
  q=area(C)
  ss=[]
  for p,r in zip(P,np.roll(P,-1,axis=0)):
   a,b=p@v,r@v
   if a*b<0:ss.append(p+a/(a-b)*(r-p))
  if len(ss)!=2:return None
  Q.append(q);S.append(np.linalg.norm(ss[0]-ss[1])/np.linalg.norm(v))
 Q=np.array(Q);S=np.array(S);M=np.sum(Q/S);f=2*np.sqrt(k*Q)/(S*M)
 B=np.array([[0,f[0]/2,f[2]/2],[f[0]/2,0,f[1]/2],[f[2]/2,f[1]/2,0]])
 return (np.linalg.eigvalsh(B)[-1],np.sum(f*f)+np.prod(f),Q/k)

for it in range(3000):
 p=rng.integers(-10,11,(4,2)).astype(float)
 try:h=ConvexHull(p)
 except:continue
 if len(h.vertices)!=4:continue
 p=p[h.vertices]
 if not all(np.linalg.det(np.stack([q-r,-r]))>0 for r,q in zip(p,np.roll(p,-1,axis=0))):continue
 k=area(p);Q=[];S=[]
 for v in vs:
  Q.append(area(clip(p,v)));ss=[]
  for a,b in zip(p,np.roll(p,-1,axis=0)):
   x,y=a@v,b@v
   if x*y<0:ss.append(a+x/(x-y)*(b-a))
  if len(ss)!=2:break
  S.append(np.linalg.norm(ss[0]-ss[1])/np.linalg.norm(v))
 if len(S)!=3:continue
 Q=np.array(Q);S=np.array(S);M=np.sum(Q/S)
 if M*M*np.prod(S)**2 <16*k*np.prod(Q)-1e-7:
  print('SCALE COUNTER',p.tolist(),k,Q,S);break
else:print('NO SCALE COUNTER IN BOUNDED SCREEN')
