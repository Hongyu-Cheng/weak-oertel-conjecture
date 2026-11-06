import numpy as np
from scipy.spatial import ConvexHull
import random,json
rng=random.Random(988431)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def intercepts(V,axis):
 vals=[]
 for A,B in zip(V,np.roll(V,-1,axis=0)):
  if A[axis]*B[axis]<0:
   t=A[axis]/(A[axis]-B[axis]);vals.append((A+t*(B-A))[1-axis])
  elif A[axis]==0:vals.append(A[1-axis])
 if len(vals)!=2:return None
 return min(vals),max(vals)
def clip(V,axis):
 out=[]
 for A,B in zip(V,np.roll(V,-1,axis=0)):
  if A[axis]>=0:out.append(A)
  if A[axis]*B[axis]<0:
   t=A[axis]/(A[axis]-B[axis]);out.append(A+t*(B-A))
 return out

def mass(V,h):
 if len(V)<3:return 0.
 total=0.
 for j in range(1,len(V)-1):
  tri=np.array([V[0],V[j],V[j+1]]);a=abs(cross(tri[1]-tri[0],tri[2]-tri[0]))/2
  total+=a*np.sum(1+tri@h)/3
 return total

gamma=27/64;best=-1e99;valid=0
for trial in range(300000):
 ints=np.array([[rng.randint(-30,30),rng.randint(-30,30)] for _ in range(rng.randint(5,12))],float)

 try: ints=ints[ConvexHull(ints).vertices]
 except: continue
 w=np.array([rng.randint(1,40) for _ in range(len(ints))],float);w/=sum(w);V=ints-w@ints
 xi=intercepts(V,1);yi=intercepts(V,0)
 if xi is None or yi is None:continue
 slopes=[]
 for lo,hi in [xi,yi]:slopes.append(-1.5*(lo+hi)/(lo*lo+lo*hi+hi*hi))
 h=np.array(slopes);hs=1+V@h
 if min(hs)<0:continue
 valid+=1;M=0.;mom=np.zeros(2)
 for j in range(1,len(V)-1):
  tri=V[[0,j,j+1]];area=abs(cross(tri[1]-tri[0],tri[2]-tri[0]))/2;hh=1+tri@h
  M+=area*sum(hh)/3;mom+=area*(np.sum(tri,axis=0)*sum(hh)+tri.T@hh)/12
 S=np.array([(yi[1]-yi[0])*(1+h[1]*sum(yi)/2),(xi[1]-xi[0])*(1+h[0]*sum(xi)/2)])
 p=np.array([mass(clip(V,0),h)/M,mass(clip(V,1),h)/M]);s=S*mom/M**2
 for j in range(2):
  if s[j]<0:s[j]=-s[j];p[j]=1-p[j]
 if min(s)<1e-11:continue
 lows=(p-1+gamma)/s; highs=(p-gamma)/s;gap=max(lows)-min(highs)
 if gap>best:
  best=gap
  if trial<10000 or gap>0:print('best',trial,'valid',valid,'gap',gap,'p',p,'s',s,flush=True)
 if gap>1e-8:
  rec={'integervertices':ints.tolist(),'barycentricweights':w.tolist(),'vertices':V.tolist(),'slopes':h.tolist(),'p':p.tolist(),'s':s.tolist(),'gap':gap}
  open('./affine-polygon-profile-numerical-candidate.json','w').write(json.dumps(rec,indent=2));print('NUMERICAL CANDIDATE; rational certification needed',flush=True);break
 if trial and trial%100000==0:print('trial',trial,'valid',valid,'best',best,flush=True)
else:print('finished',valid,'best',best,flush=True)
