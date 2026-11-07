# Falsification only. Feasibility uses the exact simultaneous PSD criterion.
import json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
c=128/279

def mat(z):
 A,a,B,b,r,t=z[:6];X=z[6:9];Y=z[9:12]
 R=np.array([A,B,t,a,b,r]);S=np.array([Y[2],X[1],Y[0],X[2],Y[1],X[0]])
 M=np.zeros((6,6))
 for i in range(6):
  M[i,i]=R[i]**2*(1/(2*S[i-1])+1/(2*S[i]))-1
  j=(i+1)%6;M[i,j]=M[j,i]=R[i]*R[j]/(2*S[i])-1
 return M

def cons(z):
 A,a,B,b,r,t=z[:6];X=z[6:9];Y=z[9:12]
 q=X+Y.sum()-Y
 return np.r_[X-np.array([A*r,B*t,a*b])/2,Y-np.array([a*t,b*r,A*B])/2,c-q,1-(q.sum()-.75*q.max()),B+b-A-a,B+b-r-t,np.linalg.eigvalsh(mat(z))]
def obj(z):
 A,a,B,b,r,t=z[:6];s=np.array([B+b,A+a,r+t]);return (1/s[0])/np.sum(1/s)
seed=np.array(json.loads(Path('./six_sector_ordinary_relaxation_root_best.json').read_text())['x'])
rng=np.random.default_rng(2026092917);best=1
for it in range(100):
 if it%3==0:
  z=seed.copy()
  if it:z[:6]*=np.exp(rng.normal(0,.20,6));z[6:]*=np.exp(rng.normal(0,.14,6));z[6:]/=z[6:].sum()
 else:
  z=np.r_[np.full(6,np.sqrt(2/9)),np.full(3,2/9),np.full(3,1/9)]
  z[:6]*=np.exp(rng.normal(0,.30,6));z[6:]*=np.exp(rng.normal(0,.22,6));z[6:]/=z[6:].sum()
 sol=minimize(obj,z,method='SLSQP',bounds=[(.005,3)]*6+[(1e-6,1)]*6,constraints=[{'type':'ineq','fun':cons},{'type':'eq','fun':lambda z:sum(z[6:])-1}],options={'maxiter':1200,'ftol':1e-11})
 cs=cons(sol.x)
 if min(cs)>=-2e-7 and abs(sum(sol.x[6:])-1)<1e-7 and sol.fun<best:
  best=sol.fun
  rec={'iteration':it,'objective':float(best),'x':sol.x.tolist(),'minimum_constraint':float(min(cs)),'success':bool(sol.success),'eigenvalues':np.linalg.eigvalsh(mat(sol.x)).tolist()}
  Path('./exact_psd_ordinary_weight_slab_recovery_best.json').write_text(json.dumps(rec,indent=2));print(json.dumps(rec),flush=True)
 if best<2/9-1e-6:break
print('DONE',best,flush=True)
