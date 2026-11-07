import numpy as np
from scipy.optimize import differential_evolution, minimize_scalar
ns={};src=open('./screen_fixed_shape_center_deformation_two_sided.py').read().split('for it in range(1200):')[0];exec(src,ns)
qpoint=ns['qpoint']
best=0

def arrays(p):
 r0,r3,a,b,ca,cb=p;ca*=a;cb*=b
 r=np.array([r0,(2*r0+r3+2*a+b)/3,(r0+2*r3+a+2*b)/3,r3])
 c=np.array([0,(2*ca+cb)/3,(ca+2*cb)/3,0])
 return r,c

def Q(r,c,t):
 lo=t*c-r;hi=t*c+r
 best=max(r[0],r[-1])
 for k in [1,2]:
  z=minimize_scalar(lambda x:-qpoint(lo,hi,k,x),bounds=(lo[k],hi[k]),method='bounded',options={'xatol':1e-8})
  best=max(best,-z.fun)
 return best

def fun(p):
 global best
 r,c=arrays(p);diff=(Q(r,c,1)-Q(r,c,.5))/(2*r.sum())
 if diff>best+1e-7:
  best=diff;print('gain',best,'p',p.tolist(),flush=True)
 return -diff
res=differential_evolution(fun,[(.001,1)]*4+[(-1,1)]*2,popsize=8,maxiter=40,polish=False,seed=733,tol=0,atol=0)
print('final',res.fun,res.x,arrays(res.x),flush=True)
