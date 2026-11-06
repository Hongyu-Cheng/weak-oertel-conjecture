import numpy as np
from scipy.optimize import linprog
best=(1,None)
for d in range(1,41):
  N=300
  edges=np.linspace(0,1,N+1)
  masses=(1-edges[:-1])**d-(1-edges[1:])**d
  # exact cell first moments for f=d(1-x)^(d-1)
  def F(x):return -(1-x)**d+d/(d+1)*(1-x)**(d+1)
  moments=F(edges[1:])-F(edges[:-1]); xs=np.divide(moments,masses,out=(edges[:-1]+edges[1:])/2,where=masses>1e-16)
  gamma=(d/(d+1))**d
  for j in range(1,N):
    g=edges[j];h=(xs<=g).astype(float)
    for sign in (1,-1):
      H=h if sign==1 else 1-h
      obj=H-gamma
      res=linprog(obj,A_eq=[2*(xs-g)],b_eq=[g-1/(d+1)],bounds=list(zip(np.zeros(N),masses)),method='highs')
      if res.success:
        gap=np.dot(H,masses)-gamma/2+res.fun
        if gap<best[0]:
          best=(float(gap),(d,float(g),sign,float(sum(res.x))))
          print(best,flush=True)
print('FINAL',best)
