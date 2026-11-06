import numpy as np
from scipy.optimize import minimize_scalar

def triangle_tail(p,t):
 a,b,c=sorted(p)
 if t<=a:return 1.
 if t>=c:return 0.
 if t>=b:return (c-t)**2/((c-a)*(c-b))
 return 1-(t-a)**2/((c-a)*(b-a))
def pair_at_u(A,C,y,u):
 p=A@u;q=C@u;v=2*y@u
 pts=sorted(set(list(p)+[v-t for t in q]))
 f=lambda t:triangle_tail(p,t)+triangle_tail(q,v-t)
 vals=[f(t) for t in pts]+[1.]
 best=(min(vals),pts[np.argmin(vals[:len(pts)])] if min(vals)<1 else pts[0])
 for l,r in zip(pts,pts[1:]):
  m=(l+r)/2; fl,fm,fr=f(l),f(m),f(r)
  aa=2*(fl+fr-2*fm)/(r-l)**2
  bb=(fr-fl)/(r-l)-aa*(l+r)
  if aa>1e-12:
   t=-bb/(2*aa)
   if l<t<r:
    val=f(t)
    if val<best[0]:best=(val,t)
 return best

def depth(A,C,y,N=120):
 ang=np.linspace(0,2*np.pi,N,endpoint=False)
 vals=[pair_at_u(A,C,y,np.array([np.cos(a),np.sin(a)]))[0] for a in ang]
 ids=[i for i in range(N) if vals[i]<=vals[(i-1)%N] and vals[i]<=vals[(i+1)%N]]
 best=(min(vals),ang[np.argmin(vals)])
 for i in ids:
  fun=lambda a:pair_at_u(A,C,y,np.array([np.cos(a),np.sin(a)]))[0]
  fit=minimize_scalar(fun,bounds=(ang[i]-2*np.pi/N,ang[i]+2*np.pi/N),method='bounded',options={'xatol':1e-11})
  if fit.fun<best[0]:best=(fit.fun,fit.x)
 return best
if __name__=='__main__':
 rng=np.random.default_rng(661)
 A=np.array([[0.,0.],[1,0],[0,1]])
 for it in range(300):
  L=rng.normal(size=(2,2));L/=np.sqrt(abs(np.linalg.det(L)));C=np.array([[0.,0.],L[:,0],L[:,1]])
  pts=[]
  for j in range(2):
   ra=rng.dirichlet([2,2,2]);rc=rng.dirichlet([2,2,2]);pts.append((ra@A+rc@C)/2)
  y0,y1=pts; ym=(y0+y1)/2
  d0,_=depth(A,C,y0);d1,_=depth(A,C,y1);dm,theta=depth(A,C,ym)
  gap=np.sqrt(dm)-(np.sqrt(d0)+np.sqrt(d1))/2
  if gap<-.00001:
   print('FAIL',it,'gap',gap,'C',C.tolist(),'points',[p.tolist() for p in [y0,ym,y1]],'depths',[d0,dm,d1],'midnormal',theta,flush=True)
   np.savez('./two_layer_depth_root_concavity_best.npz',A=A,C=C,y0=y0,y1=y1,d0=d0,dm=dm,d1=d1)
   break
  if it%25==0:print('tested',it,'lastgap',gap,flush=True)
