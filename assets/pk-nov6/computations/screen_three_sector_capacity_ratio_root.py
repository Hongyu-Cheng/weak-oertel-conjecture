import numpy as np
from scipy.optimize import minimize
import json
from pathlib import Path

def data(z):
 A,a,B,b,r,t=z[:6];C=(A*B+a*t+b*r)/2
 cs=[r*(A+b)-A*b,t*(a+B)-a*B,A*(B+r)-B*r,a*(b+t)-b*t,B*(A+t)-A*t,b*(a+r)-a*r,B+b-A-a,B+b-r-t]
 p=1/(B+b)/(1/(B+b)+1/(A+a)+1/(r+t))
 cs.append(2/9-p)
 for args,y in zip([(r,A,B,b),(B,t,a,A),(a,b,r,t)],[a*t/2,b*r/2,A*B/2]):
  u,v,rh,ta=args;D=rh*u+ta*v-u*v;N=u*v*(u*ta+v*rh)-rh*ta*(u-v)**2
  cs.append(N-2*D*(y+z[6]*C) if D>0 else 1.)
 return np.array(cs)
rng=np.random.default_rng(22);best=-1
for i in range(90):
 B=rng.uniform(.2,.8);x=rng.uniform(.35,.58);y=rng.uniform(.35,.58)
 A=x*rng.uniform(.2,.8);r=y*rng.uniform(.2,.8)
 z=np.array([A,x-A,B,1-B,r,y-r,.1])
 s=minimize(lambda z:-z[6],z,method='SLSQP',bounds=[(.002,1)]*6+[(0,3)],constraints=[{'type':'ineq','fun':data},{'type':'eq','fun':lambda z:z[2]+z[3]-1}],options={'maxiter':1000,'ftol':1e-11})
 if s.success and min(data(s.x))>-1e-7 and s.x[6]>best:
  best=s.x[6];q={'ratio':float(best),'x':s.x.tolist(),'slack':float(min(data(s.x)))};print(q,flush=True);Path('./three_sector_capacity_ratio_root_best.json').write_text(json.dumps(q,indent=2))
print('DONE',best,'threshold',23/96)
