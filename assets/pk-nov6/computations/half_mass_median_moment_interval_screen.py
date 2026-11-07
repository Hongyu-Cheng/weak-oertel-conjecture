import numpy as np,json
rng=np.random.default_rng(394221)
def qopt(p,lo,hi):
 l=max(lo,min(hi,p/6));return p*l-3*l*l

def check(a,c,e):
 b=1.;M=a+c+1;t=M/2; l=[e-a/2,-.5,e-c/2];u=[e+a/2,.5,e+c/2];w=[a,1,c]
 cand=[]
 if a>=t-1e-12:cand.append((a-t,0,e,a/(2*M)))
 if c>=t-1e-12:cand.append((c-t,2,e,c/(2*M)))
 lo=max(0,(t-1)/2);hi=min(a,c,t/2)
 if lo<=hi+1e-12 and a<=t+1e-12 and c<=t+1e-12:
  du=1-2*e-(a+c)/2;dl=1+2*e-(a+c)/2
  qp=qopt(2*t-du,lo,hi);qm=qopt(2*t-dl,lo,hi)
  length=1-t+(qp+qm)/t;y=(qp-qm)/(2*t)
  slopes=[-1e8,1e8]+[(q-y)/z for i,z in [(0,-1),(2,1)] for q in [l[i],u[i]]]
  vals=[sum(max(0,min(wi,y+s*z-li)) for wi,li,z in zip(w,l,[-1,0,1])) for s in slopes]
  depth=min(min(vals),M-max(vals))/M
  cand.append((length,1,y,depth))
 best=max(x[0] for x in cand)
 winners=[x for x in cand if abs(x[0]-best)<1e-10]
 return min(x[3] for x in winners),cand
best=1
for it in range(1000000):
 a=rng.uniform(.001,1.999);c=rng.uniform(.001,2-a); e=(2-a-c)/4*rng.uniform(-1,1)
 if it%3==0:e=(2-a-c)/4*rng.choice([-1,1])
 dep,cand=check(a,c,e)
 if dep<best:
  best=dep;ans=dict(a=a,c=c,e=e,depth=dep,candidates=cand)
  print(it,json.dumps(ans),flush=True);json.dump(ans,open('./half_mass_median_moment_interval_best.json','w'),indent=2)
 if dep<.25-1e-7:break
