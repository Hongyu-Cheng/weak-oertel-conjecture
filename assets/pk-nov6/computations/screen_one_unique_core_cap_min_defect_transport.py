# Bounded falsification screen only; output is not an exact certificate.
exec(open('./screen_exact_psd_ordinary_weight_slab_recovery.py').read().split('seed=np.array')[0])
rng=np.random.default_rng(490631)
h=.7;AA=100/89;k=62339/17800
Y=np.array([AA/2,h*h/2,AA/2]); X=np.array([(k-.5-AA-h*h/2)/2,.5,(k-.5-AA-h*h/2)/2])
seed=np.r_[np.array([AA,AA,1,h,h,1])/np.sqrt(k),X/k,Y/k,1700/3667]
def feas(z):
 A,a,B,b,r,t=z[:6];X=z[6:9];Y=z[9:12];q=X+sum(Y)-Y
 return np.r_[X-np.array([A*r,B*t,a*b])/2,Y-np.array([a*t,b*r,A*B])/2,z[12]-q,np.linalg.eigvalsh(mat(z[:12]))]
def eql(z): return np.array([sum(z[6:12])-1,2*z[7]-z[2]*z[5]])
best=1
for it in range(12):
 z=seed.copy()
 if it:
  z[:6]*=np.exp(rng.normal(0,.15,6));z[6:12]*=np.exp(rng.normal(0,.12,6));z[6:12]/=sum(z[6:12])
 sol=minimize(lambda z:z[12],z,method='SLSQP',bounds=[(.01,3)]*6+[(1e-5,1)]*6+[(.4,.6)],constraints=[{'type':'ineq','fun':feas},{'type':'eq','fun':eql}],options={'maxiter':900,'ftol':1e-11})
 if min(feas(sol.x))>=-1e-7 and max(abs(eql(sol.x)))<1e-7 and sol.fun<best:
  best=sol.fun
  rec={'value':float(best),'x':sol.x.tolist(),'residual':float(min(feas(sol.x))),'success':bool(sol.success)}
  print(json.dumps(rec),flush=True)
  Path('./one_unique_core_cap_min_defect_transport_screen.json').write_text(json.dumps(rec,indent=2))
print('DONE',best,flush=True)
