import numpy as np
from scipy.optimize import minimize
from pathlib import Path
import json

def cons(z,j):
 A,a,B,b,r,t=z[:6];C=(A*B+a*t+b*r)/2
 cs=[r*(A+b)-A*b,t*(a+B)-a*B,A*(B+r)-B*r,a*(b+t)-b*t,B*(A+t)-A*t,b*(a+r)-a*r,B+b-A-a,B+b-r-t]
 p=1/(B+b)/(1/(B+b)+1/(A+a)+1/(r+t));cs.append(2/9-p)
 for i,(args,y) in enumerate(zip([(r,A,B,b),(B,t,a,A),(a,b,r,t)],[a*t/2,b*r/2,A*B/2])):
  u,v,rh,ta=args;D=rh*u+ta*v-u*v;N=u*v*(u*ta+v*rh)-rh*ta*(u-v)**2
  cs.append(N-2*D*(y+z[6+i]*C) if D>0 else 1.)
  if i==j:cs.append(N-2*D*(y+C/3) if D>0 else 1.)
 return np.array(cs)
rng=np.random.default_rng(2930);best=-1
for j in range(3):
 for it in range(35):
  B=rng.uniform(.25,.75);x=rng.uniform(.43,.59);y=rng.uniform(.43,.59)
  A=x*rng.uniform(.3,.7);r=y*rng.uniform(.3,.7)
  z=np.array([A,x-A,B,1-B,r,y-r,.25,.25,.25])
  ss=minimize(lambda z:-sum(z[6:]),z,method='SLSQP',bounds=[(.002,1)]*6+[(.001,1/3)]*3,constraints=[{'type':'ineq','fun':lambda z:cons(z,j)},{'type':'eq','fun':lambda z:z[2]+z[3]-1}],options={'maxiter':1200,'ftol':2e-12})
  if ss.success and min(cons(ss.x,j))>-1e-8 and sum(ss.x[6:])>best:
   best=sum(ss.x[6:]);q={'score':float(best),'j':j,'x':ss.x.tolist(),'slack':float(min(cons(ss.x,j)))};print(q,flush=True);Path('./clipped_sector_credit_root_best.json').write_text(json.dumps(q,indent=2))
print('DONE',best,'target',29/32,flush=True)
