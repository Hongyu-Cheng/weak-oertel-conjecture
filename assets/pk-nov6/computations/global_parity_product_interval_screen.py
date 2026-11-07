import numpy as np
from scipy.optimize import minimize_scalar
from fractions import Fraction
import random,json
rng=random.Random(9103)

def depth1(j,x,lo,hi):
 n=len(lo);z=np.arange(n)-j
 slopes=[0.]
 for i in range(n):
  if z[i]: slopes += [(lo[i]-x)/z[i],(hi[i]-x)/z[i]]
 slopes=np.array(slopes)
 f=np.clip(x+slopes[:,None]*z[None,:]-lo,0,hi-lo).sum(axis=1)
 return min(f.min(),(hi-lo).sum()-f.max())
def opt1(lo,hi):
 best=(-1,None,None)
 for j in range(len(lo)):
  o=minimize_scalar(lambda x:-depth1(j,x,lo,hi),bounds=(lo[j],hi[j]),method='bounded',options={'xatol':1e-10})
  x=float(Fraction(float(o.x)).limit_denominator(100000));v=depth1(j,x,lo,hi)
  if v>best[0]:best=(v,j,x)
 return best

def depth2(R,j,x,lo,hi):
 z=np.array([(r-1,w-j) for r in range(-R,R+1) for w in range(len(lo))],float)
 l=np.tile(lo,2*R+1);h=np.tile(hi,2*R+1)
 A=np.repeat(z,2,axis=0);b=np.column_stack((l-x,h-x)).ravel()
 ii,jj=np.triu_indices(len(b),1)
 det=A[ii,0]*A[jj,1]-A[ii,1]*A[jj,0]
 mask=np.abs(det)>1e-10;ii,jj,det=ii[mask],jj[mask],det[mask]
 aa=(b[ii]*A[jj,1]-A[ii,1]*b[jj])/det
 bb=(A[ii,0]*b[jj]-b[ii]*A[jj,0])/det
 vals=np.clip(x+aa[:,None]*z[:,0]+bb[:,None]*z[:,1]-l,0,h-l).sum(axis=1)
 k1=vals.argmin();k2=vals.argmax();M=(h-l).sum()
 if vals[k1]<=M-vals[k2]:return vals[k1],(aa[k1],bb[k1],1)
 return M-vals[k2],(aa[k2],bb[k2],-1)

bestgap=1
for trial in range(400):
 n=rng.randrange(3,8)
 slopes=sorted([rng.randrange(-8,9) for _ in range(n-1)],reverse=True)
 hi=np.r_[0,np.cumsum(slopes)].astype(float);hi+=rng.randrange(1,8)-hi.min()
 # independent convex lower sequence, with global affine shifts removed
 ls=sorted([rng.randrange(-4,5) for _ in range(n-1)])
 lo=np.r_[0,np.cumsum(ls)].astype(float)
 lo-=lo.max()+rng.randrange(0,5)
 v,j,x=opt1(lo,hi)
 for R in (1,2,3,5):
  v2,cut=depth2(R,j,x,lo,hi);target=(2*R+1)*v
  gap=(target-v2)/target
  if gap<bestgap:
   bestgap=gap
   print('best',trial,R,gap,lo.tolist(),hi.tolist(),v,j,x,v2,cut,flush=True)
  if gap<1e-8:
   out=dict(R=R,lo=lo.tolist(),hi=hi.tolist(),v=v,j=j,x=x,v2=v2,cut=cut)
   open('./global_parity_product_candidate.json','w').write(json.dumps(out));print('CANDIDATE',out,flush=True);raise SystemExit
print('done bestgap',bestgap)
