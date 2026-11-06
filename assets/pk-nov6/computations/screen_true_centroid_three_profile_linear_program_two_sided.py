"""Exact finite formulation, floating LP only for candidate discovery."""
import numpy as np
from scipy.optimize import linprog
import json
rng=np.random.default_rng(93491)

def weights(xs):
 n=len(xs);mass=np.zeros(n);moment=np.zeros(n);cap=np.zeros(n)
 for i,(l,r) in enumerate(zip(xs[:-1],xs[1:])):
  D=r-l
  mass[i]+=D/2;mass[i+1]+=D/2
  moment[i]+=D*(2*l+r)/6;moment[i+1]+=D*(l+2*r)/6
  if l>=0:cap[i]+=D/2;cap[i+1]+=D/2
  elif r>0:
   cap[i]+=r*r/(2*D);cap[i+1]+=(r*r/2-l*r)/D
 return mass,moment,cap

def solve(grids):
 ns=list(map(len,grids));offs=np.cumsum([0]+ns);N=offs[-1]
 arr=[weights(x) for x in grids]
 Ae=[];be=[];Au=[];bu=[]
 for j in [0,1]:
  row=np.zeros(N);row[offs[j]:offs[j+1]]=arr[j][0];Ae.append(row);be.append(1)
 row=np.zeros(N)
 for j in range(3):row[offs[j]:offs[j+1]]=arr[j][1]
 Ae.append(row);be.append(0)
 for j in range(3):
  xs=grids[j]
  for i in range(1,ns[j]-1):
   row=np.zeros(N);L=xs[i]-xs[i-1];R=xs[i+1]-xs[i]
   row[offs[j]+i-1]=1/L;row[offs[j]+i]=-1/L-1/R;row[offs[j]+i+1]=1/R
   Au.append(row);bu.append(0)
 for i,x in enumerate(grids[0]):
  for j,y in enumerate(grids[1]):
   s=(x+y)/2;zs=grids[2]
   if s<zs[0]-1e-10 or s>zs[-1]+1e-10:return None
   ii=min(len(zs)-2,np.searchsorted(zs,s,side='right')-1);ii=max(0,ii)
   u=(s-zs[ii])/(zs[ii+1]-zs[ii]);row=np.zeros(N)
   row[i]=.5;row[offs[1]+j]=.5;row[offs[2]+ii]=-(1-u);row[offs[2]+ii+1]=-u
   Au.append(row);bu.append(0)
 row=np.zeros(N);row[offs[2]:]=arr[2][0];Au.append(row);bu.append(3);Au.append(-row);bu.append(-1)
 obj=np.concatenate([a[2] for a in arr]);obj[offs[2]:]-=arr[2][0]/3
 res=linprog(obj,A_ub=Au,b_ub=bu,A_eq=Ae,b_eq=be,bounds=(0,None),method='highs')
 if res.success:return res.fun-1/3,res.x,offs
 return None
best=(1e9,None)
for it in range(10000):
 # Both endpoint supports may be one-sided relative to the tested centroid.
 aa=rng.integers(-12,7);ab=aa+rng.integers(2,16)
 ba=rng.integers(-12,7);bb=ba+rng.integers(2,16)
 ka=min((aa+ba)/2,rng.integers(-15,1));kb=max((ab+bb)/2,rng.integers(1,16))
 grids=[np.linspace(aa,ab,5),np.linspace(ba,bb,5),np.linspace(ka,kb,9)]
 ret=solve(grids)
 if ret is None:continue
 gap,hs,offs=ret
 if gap<best[0]:
  data={'it':it,'gap':gap,'knots':[x.tolist() for x in grids],'heights':[hs[offs[j]:offs[j+1]].tolist() for j in range(3)]}
  print(json.dumps(data),flush=True);best=(gap,data)
  open('./screen_true_centroid_three_profile_linear_program_two_sided_best.json','w').write(json.dumps(data,indent=2))
 if gap< -1e-5:break
