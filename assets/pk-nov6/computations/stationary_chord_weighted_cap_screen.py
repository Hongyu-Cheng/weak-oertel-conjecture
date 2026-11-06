import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog

def area(P):
 return abs(np.sum(np.cross(P,np.roll(P,-1,axis=0))))/2 if len(P)>2 else 0.
def clip(P,u):
 Q=[]
 for a,b in zip(P,np.roll(P,-1,axis=0)):
  va,vb=np.dot(u,a),np.dot(u,b)
  if va>=-1e-10:Q.append(a)
  if (va>1e-10 and vb < -1e-10) or (va < -1e-10 and vb>1e-10):Q.append(a+va/(va-vb)*(b-a))
 return np.array(Q)
def calc(P):
 roots=[]
 for a,b in zip(P,np.roll(P,-1,axis=0)):
  for c,d in zip(-P,np.roll(-P,-1,axis=0)):
   A=np.stack((b-a,c-d),axis=1)
   if abs(np.linalg.det(A))<1e-10:continue
   s,t=np.linalg.solve(A,c-a)
   if min(s,t)>-1e-9 and max(s,t)<1+1e-9:
    x=a+s*(b-a)
    if all(np.linalg.norm(x-y)>1e-7 for y in roots):roots.append(x)
 if len(roots)<2:return None
 roots=np.array(roots)
 vals=np.array([area(clip(P,np.array([-p[1],p[0]])))/area(P) for p in roots])
 sol=linprog(vals,A_eq=np.vstack((np.ones(len(roots)),roots.T)),b_eq=np.array([1,0,0]),bounds=(0,None),method='highs')
 return (sol.fun,roots,vals,sol.x) if sol.success else None
rng=np.random.default_rng(617493)
best=1.
for it in range(3000):
 pts=rng.integers(-20,21,size=(rng.integers(4,16),2)).astype(float)
 try:P=pts[ConvexHull(pts).vertices]
 except:continue
 weights=rng.dirichlet(np.ones(len(P))*rng.choice([.25,1.,3.]))
 center=weights@P
 Q=P-center
 r=calc(Q)
 if r and r[0]<best:
  best=r[0]
  if best<4/9-1e-7:
   np.savez('./stationary_chord_weighted_cap_candidate.npz',P=P,center=center,roots=r[1],vals=r[2],weights=r[3]);print('VIOLATION',it,best,'P',P.tolist(),'center',center.tolist(),'theta',r[3].tolist(),flush=True);break
else: print('NO VIOLATION; best',best,flush=True)
