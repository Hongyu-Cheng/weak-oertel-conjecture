# Falsification only; use exact-feasibility formula numerically.
exec(open('./screen_exact_psd_ordinary_weight_slab_recovery.py').read().split('seed=np.array')[0])
rng=np.random.default_rng(376511)
def base(z):
 A,a,B,b,r,t=z[:6];X=z[6:9];Y=z[9:12]
 return np.r_[X-np.array([A*r,B*t,a*b])/2,Y-np.array([a*t,b*r,A*B])/2,np.linalg.eigvalsh(mat(z))]
def vals(z):
 A,a,B,b,r,t=z[:6];X=z[6:9];Y=z[9:12];q=X+sum(Y)-Y
 sig=np.array([B+b,A+a,r+t]); aa=q/sig;aa/=sum(aa);ff=2*aa/np.sqrt(q)
 return ff+(sum(ff)-ff)**2/4
best=-1
for it in range(100):
 z=np.r_[np.full(6,.45)*np.exp(rng.normal(0,.30,6)),np.full(3,2/9),np.full(3,1/9)]
 z[6:]*=np.exp(rng.normal(0,.3,6));z[6:]/=sum(z[6:])
 sol=minimize(lambda z:-vals(z)[0],z,method='SLSQP',bounds=[(.005,4)]*6+[(1e-5,1)]*6,constraints=[{'type':'ineq','fun':base},{'type':'eq','fun':lambda z:sum(z[6:])-1}],options={'maxiter':1200,'ftol':1e-11})
 if min(base(sol.x))>=-2e-7 and abs(sum(sol.x[6:])-1)<1e-7 and -sol.fun>best:
  best=-sol.fun;rec={'value':float(best),'x':sol.x.tolist(),'values':vals(sol.x).tolist(),'resid':float(min(base(sol.x))),'success':bool(sol.success)}
  Path('./general_lorentz_exact_sector_psd_slab_recovery_best.json').write_text(json.dumps(rec,indent=2));print(json.dumps(rec),flush=True)
 if best>2.005:break
print('DONE',best,flush=True)
