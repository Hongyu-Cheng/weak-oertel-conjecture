from fixed_width_true_centroid_cap_lp import solve_widths
import numpy as np, json, sys
rng=np.random.default_rng(91357)
best=1; bestgap=1
for trial in range(int(sys.argv[1]) if len(sys.argv)>1 else 500):
 N=int(rng.integers(3,15)); anchor=int(rng.integers(max(1,(N-1)//3),min(N-1,(2*(N-1)+2)//3)+1)); z=np.arange(N)-anchor
 # sparse nonnegative tent combination plus constant; affine adjustment enforces true base mean
 v=np.zeros(N); idx=np.arange(N)
 for j in rng.choice(np.arange(1,N-1),size=int(rng.integers(1,min(N-2,4)+1)),replace=False):
  v+=rng.uniform(.1,2)*np.minimum(idx/j,(N-1-idx)/(N-1-j))
 denom=z@z; base=v-z*(z@v)/denom; scale=1-z*z.sum()/denom
 lo=0.;hi=float('inf')
 for b,s in zip(base,scale):
  if s>1e-12:lo=max(lo,-b/s)
  elif s< -1e-12:hi=min(hi,-b/s)
  elif b<=0:hi=-1
 if hi<=lo+1e-8:continue
 A=lo+rng.uniform(.00001,.7)*max(v.max(),.1)
 if A>=hi:A=(lo+hi)/2
 w=base+A*scale
 if min(w)<=0:continue
 ans=solve_widths(w,z,tail_filter=lambda p,q,l,r,N: l==r==1 and p>0 and q<N-1)
 if ans is None:continue
 gap=ans['value']-ans['Qover2mM']
 if ans['value']<best or gap<bestgap:
  best=min(best,ans['value']);bestgap=min(bestgap,gap)
  print(trial,'best',best,'gap',bestgap,json.dumps(ans),flush=True)
  if ans['value']==best:json.dump(ans,open('./fixed_width_true_centroid_cap_best.json','w'),indent=2)
  if gap==bestgap:json.dump(ans,open('./fixed_width_true_centroid_cap_gap_best.json','w'),indent=2)
 if ans['value']<.5-1e-7:
  print('STRONGER_BOUND_COUNTER',flush=True);break
