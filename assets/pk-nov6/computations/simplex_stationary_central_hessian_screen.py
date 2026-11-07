import numpy as np,json
class J:
 def __init__(self,v,g,h):self.v,self.g,self.h=v,g,h
 def __add__(a,b):
  if not isinstance(b,J):return J(a.v+b,a.g,a.h)
  return J(a.v+b.v,a.g+b.g,a.h+b.h)
 __radd__=__add__
 def __neg__(a):return J(-a.v,-a.g,-a.h)
 def __sub__(a,b):return a+-b
 def __mul__(a,b):
  if not isinstance(b,J):return J(a.v*b,a.g*b,a.h*b)
  return J(a.v*b.v,a.g*b.v+b.g*a.v,a.h*b.v+b.h*a.v+np.outer(a.g,b.g)+np.outer(b.g,a.g))
 __rmul__=__mul__
 def inv(a):return J(1/a.v,-a.g/a.v**2,2*np.outer(a.g,a.g)/a.v**3-a.h/a.v**2)
 def __truediv__(a,b):return a*b.inv() if isinstance(b,J) else a*(1/b)
def jet(c,p):
 n=len(c);z=np.zeros(n);hh=np.zeros((n,n));vv=[J(c[i],np.eye(n)[i],hh) for i in range(n)];x=vv[:p];y=[-v for v in vv[p:]];q=n-p
 tab=[[J(0.,z,hh) for j in range(q+1)] for i in range(p+1)]
 for i in range(p):tab[i][q]=J(1.,z,hh)
 for i in range(p-1,-1,-1):
  for j in range(q-1,-1,-1):tab[i][j]=(y[j]*tab[i+1][j]+x[i]*tab[i][j+1])/(x[i]+y[j])
 return tab[0][0]
if __name__=='__main__':
 rng=np.random.default_rng(21372);count=0;best=-1e20;info=None
 for it in range(30000):
  n=int(rng.integers(4,10));p=int(rng.integers(2,n-1));c=np.exp(rng.uniform(-3,3,n));c[p:]*=-1
  j=jet(c,p);lam=j.g/j.g.sum()
  if lam.min()<=0 or lam.max()>1/(n-1)+1e-10:continue
  count+=1;basis=np.linalg.svd(np.stack([lam,c]))[2][2:].T
  eig=np.linalg.eigvalsh(basis.T@j.h@basis)*np.linalg.norm(c)**2
  if eig[0]>best:
   best=float(eig[0]);info=dict(it=it,p=p,c=c.tolist(),lam=lam.tolist(),eig=eig.tolist(),P=j.v)
  if eig[0]>1e-7:
   print('COUNTER',json.dumps(info),flush=True);break
 else:print('DONE',count,'BEST',json.dumps(info),flush=True)
