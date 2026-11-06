# Falsification/calibration only, not proof.
exec(open('./screen_exact_psd_ordinary_weight_slab_recovery.py').read().split('seed=np.array')[0])
seed=np.array(json.loads(Path('./exact_psd_ordinary_weight_slab_recovery_best.json').read_text())['x'])
rng=np.random.default_rng(928173)
def sat(z,ee):
 A,a,B,b,r,t=z[:6];X=z[6:9];Y=z[9:12]
 R=np.array([A,B,t,a,b,r]);W=np.array([Y[2],X[1],Y[0],X[2],Y[1],X[0]])
 return np.r_[sum(W)-1,[2*W[i]-R[i]*R[(i+1)%6] for i in ee]]
for ee in [(0,3),(0,4),(1,3),(1,4)]:
 best=1; rec=None
 for it in range(25):
  z=seed.copy() if it%2==0 else np.r_[np.full(6,np.sqrt(2/9)),np.full(3,2/9),np.full(3,1/9)]
  z[:6]*=np.exp(rng.normal(0,.25,6));z[6:]*=np.exp(rng.normal(0,.25,6));z[6:]/=z[6:].sum()
  sol=minimize(obj,z,method='SLSQP',bounds=[(.003,3)]*6+[(1e-6,1)]*6,constraints=[{'type':'ineq','fun':cons},{'type':'eq','fun':lambda z:sat(z,ee)}],options={'maxiter':1200,'ftol':1e-11})
  if min(cons(sol.x))>=-2e-7 and max(abs(sat(sol.x,ee)))<2e-7 and sol.fun<best:
   best=sol.fun;rec={'pattern':ee,'objective':float(best),'x':sol.x.tolist(),'minimum_constraint':float(min(cons(sol.x))),'success':bool(sol.success),'eigenvalues':np.linalg.eigvalsh(mat(sol.x)).tolist()}
 print(json.dumps(rec),flush=True)
