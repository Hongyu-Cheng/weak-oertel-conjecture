# Exploratory screen only; never a proof.
import numpy as np
from scipy.interpolate import BSpline
from random import Random
rng=Random(319)

def den(h,x):
 h=np.array(sorted(h)); n=len(h); x=np.asarray(x)
 b=BSpline.basis_element(h,extrapolate=False)(x)*(n-1)/(h[-1]-h[0])
 return np.nan_to_num(b,nan=0.0)
best=(1e9,None)
for trial in range(12000):
 d=rng.choice([5,6,7,8,10]);n=d+2
 # Several exact rational knot families in [0,4].
 h=[0.,4.]+[rng.randrange(1,16)/4 for _ in range(d)]
 w=den(h,[1.,2.,3.]);M=sum(w)
 if M<=0 or max(w)>=M/2-1e-10:continue
 j=next(k+1 for k in range(3) if sum(w[:k+1])>=M/2)
 G=(d/(d+1))**d/2
 for i in range(n):
  c=den([*h,h[i]],float(j))/n/w[j-1]
  if not (0<c<1):continue
  mass=(1-c)**d*sum(den(h,(np.arange(5)-c*h[i])/(1-c)))/M
  ratio=mass/G
  if ratio<best[0]:
   best=(ratio,(d,h,w.tolist(),j,i,float(c),float(mass),G))
   if ratio<1: print('FOUND',best,flush=True);raise SystemExit
print('BEST',best)
