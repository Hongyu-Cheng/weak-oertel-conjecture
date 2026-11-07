import numpy as np
from scipy.optimize import minimize

def phi3(v):
 x,y,w,z=sorted(v)
 if x<=1e-14:return (y*w*z)**(1/3)
 D=(z-x)*(z-y)*(z-w)
 h=z-np.sqrt(max(0,D/z))
 if h>=w and D>0:return (z*h*h)**(1/3)
 if y-x<1e-13 or w-y<1e-13:
  from scipy.optimize import minimize_scalar
  # Random screening does not use repeated entries.
  raise ValueError('repeated knot')
 A=(y-x)*(w-x)*(z-x)
 B=(y-x)*(w-y)*(z-y)
 return ((y**1.5*np.sqrt(A)-x**1.5*np.sqrt(B))**2/(y-x)**3)**(1/3)

def value(phi,l):
 return 3*sum(phi[i]*np.prod(np.delete(l,i))**(1/3) for i in range(4))

def optimize_l(phi):
 r=minimize(lambda l:-value(phi,l),np.full(4,.25),method='SLSQP',bounds=[(1e-12,1)]*4,constraints=[{'type':'eq','fun':lambda l:sum(l)-1}],options={'ftol':1e-11,'maxiter':100})
 return -r.fun,r.x

if __name__=='__main__':
 rng=np.random.default_rng(90631);best=(0,None,None,None)
 for i in range(5000):
  alpha=[.08,.2,.5,1,3][i%5]
  X=rng.dirichlet(np.full(4,alpha),size=4).T
  try:ph=np.array([phi3(row) for row in X])
  except ValueError:continue
  score,l=optimize_l(ph)
  if score>best[0]:
   best=(score,X,ph,l)
   if score>1+1e-7:
    print('VIOLATION',score,X.tolist(),ph.tolist(),l.tolist(),flush=True);break
  if i%1000==0:print(i,best[0],flush=True)
 print('BEST',best[0],best[1].tolist(),best[2].tolist(),best[3].tolist(),flush=True)
