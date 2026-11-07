from fractions import Fraction as F
import sys
sys.path.insert(0,'.')
from minkowski_depth_search import best,depth
import numpy as np
A=[(F(0),F(12)),(F(-3),F(24)),(F(-1),F(28)),(F(6),F(32))]
B=[(F(0),F(21)),(F(-9),F(24)),(F(-3),F(21)),(F(7),F(14))]
C=[(a+c,b+d) for (a,b),(c,d) in zip(A,B)]
def exact(D,k,x):
 M=sum(u-l for l,u in D); data=[]
 for j,I in enumerate(D):
  if j==k:continue
  for e in I:
   a=(e-x)/(j-k)
   mass=sum(max(F(0),min(u-l,u-x-a*(i-k))) for i,(l,u) in enumerate(D))
   data.extend([(mass,1,a,j,e),(M-mass,-1,a,j,e)])
 return sorted(data)
for name,D,k,x in [('A',A,2,F(14)),('B',B,1,F(33,4)),('C',C,1,F(18))]:
 print(name,'M',sum(u-l for l,u in D),'best cap',exact(D,k,x)[:5])
for k in [1,2]:
 from scipy.optimize import minimize_scalar
 DD=np.array(C,float); sol=minimize_scalar(lambda x:-depth(DD,k,x),bounds=DD[k],method='bounded')
 x=F(float(sol.x)).limit_denominator(10000)
 print('C',k,x,exact(C,k,x)[:5])
