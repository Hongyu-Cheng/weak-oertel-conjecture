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
for it in range(2000):
 p=rng.integers(-10,11,(4,2)).astype(float)
 try:h=ConvexHull(p)
 except:continue
 if len(h.vertices)!=4:continue
 p=p[h.vertices]
 if not all(np.linalg.det(np.stack([q-r,-r]))>0 for r,q in zip(p,np.roll(p,-1,axis=0))):continue
 if any(np.sign((p[2]+.9*(p[0]-p[2]))@v)!=np.sign((p[2]+1.1*(p[0]-p[2]))@v) for v in vs):continue
 out=[]
 for t in [.9,1,1.1]:
  z=p.copy();z[0]=p[2]+t*(p[0]-p[2]);out.append(val(z))
 if any(x is None for x in out):continue
 if out[1][0]>max(out[0][0],out[2][0])+1e-7:
  print('SPECTRAL PEAK',p.tolist(),out,flush=True);break
else:print('NO SCREENED PEAK')
