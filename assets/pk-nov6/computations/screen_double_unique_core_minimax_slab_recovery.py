exec(open('./screen_exact_psd_ordinary_weight_slab_recovery.py').read().split('seed=np.array')[0])
rng=np.random.default_rng(591294)
def base(z):
 A,a,B,b,r,t=z[:6];X=z[6:9];Y=z[9:12];q=X+sum(Y)-Y
 return np.r_[X-np.array([A*r,B*t,a*b])/2,Y-np.array([a*t,b*r,A*B])/2,z[12]-q,np.linalg.eigvalsh(mat(z[:12]))]
def eq(z):return np.array([sum(z[6:12])-1,2*z[7]-z[2]*z[5],2*z[8]-z[1]*z[3]])
best=1
for it in range(20):
 z=np.r_[np.full(6,.45)*np.exp(rng.normal(0,.3,6)),np.full(3,.20),np.full(3,2/15),.49]
 sol=minimize(lambda z:z[12],z,method='SLSQP',bounds=[(.01,3)]*6+[(1e-6,1)]*6+[(.3,.9)],constraints=[{'type':'ineq','fun':base},{'type':'eq','fun':eq}],options={'maxiter':1500,'ftol':1e-11})
 if min(base(sol.x))>=-1e-7 and max(abs(eq(sol.x)))<1e-7 and sol.fun<best:
  best=sol.fun;print(json.dumps({'value':float(best),'x':sol.x.tolist(),'success':bool(sol.success),'resid':float(min(base(sol.x)))}),flush=True)
print('DONE',best,flush=True)
