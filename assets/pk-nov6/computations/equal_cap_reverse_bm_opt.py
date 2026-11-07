exec(open('./equal_cap_exclusive_search.py').read().split('best=')[0])
from scipy.optimize import differential_evolution
from math import sqrt
import sys
N=int(sys.argv[1]) if len(sys.argv)>1 else 5
tau=float(sys.argv[2]) if len(sys.argv)>2 else .47
record=[1,None]
def objective(v):
 P=hull([(float(v[2*j]),float(v[2*j+1])) for j in range(N)])
 if len(P)<3 or area(P)<1e-7:return 100
 M=area(P);bs=[quantile(P,a,b,tau) for a,b in norms]
 if sum(bs)>=0:return 1+sum(bs)
 Q=P
 for j,(a,b) in enumerate(norms):Q=clip(Q,a,b,bs[j])
 ratio=area(Q)/M/(3*sqrt(tau)-2)**2
 val=1-ratio
 if val<record[0]:
  record[:]=[val,(P,bs,area(Q)/M)]
  if val<-.000001:print('COUNTER',tau,record,flush=True)
 return val
res=differential_evolution(objective,[(-1,1)]*(2*N),popsize=10,maxiter=250,tol=1e-8,seed=49,polish=False)
print('DONE',N,tau,record,res.fun,flush=True)
