"""Bounded falsification screen only; never used as a proof."""
import numpy as np, math
from scipy.spatial import ConvexHull
from scipy.optimize import differential_evolution
normals=np.array([[1.,0.],[0.,1.],[-1.,-1.]])
def area(p):return abs(sum(np.cross(x,y) for x,y in zip(p,p[1:]+p[:1])))/2 if len(p)>2 else 0.
def clip(p,n):
 o=[]
 for x,y in zip(p,p[1:]+p[:1]):
  a,b=x@n,y@n
  if a>=0:o.append(x)
  if a*b<0:o.append(x+a/(a-b)*(y-x))
 return o

def data(P):
 if any(np.cross(y-x,-x)<=1e-8 for x,y in zip(P,P[1:]+P[:1])):return None
 k=area(P);q=[];s=[]
 for n in normals:
  points=[]
  for x,y in zip(P,P[1:]+P[:1]):
   a,b=x@n,y@n
   if a*b<0:points.append(x+a/(a-b)*(y-x))
  if len(points)!=2:return None
  q.append(area(clip(P,n)));s.append(np.linalg.norm(points[1]-points[0])/np.linalg.norm(n))
 q=np.array(q);s=np.array(s);M=sum(q/s)
 f=2*np.sqrt(k*q)/(s*M);ph=np.array([f[i]+(sum(f)-f[i])**2/4 for i in range(3)])
 return k,q,s,f,ph
rng=np.random.default_rng(9713);best=(-1,None)
for _ in range(2500):
 P=rng.uniform(-3,3,size=(4,2))
 try:h=ConvexHull(P)
 except:continue
 if len(h.vertices)!=4:continue
 P=[P[i] for i in h.vertices];D=data(P)
 if D is None:continue
 if max(D[-1])>best[0]:best=(max(D[-1]),(P,D))
print('screen max',best[0])
print('points',best[1][0]);print('data',best[1][1])
