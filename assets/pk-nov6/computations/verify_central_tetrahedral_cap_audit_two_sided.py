import sympy as s
from fractions import Fraction as Q
from itertools import product
from math import prod
checks=0
def ck(x):
 global checks
 assert x;checks+=1
x,y,z,w=s.symbols('x y z w',positive=True)
S=x+y+z+w;R=z+w;bb=z*w
lam=[a*(1/(a+b)+1/(a+c)-1/S)/3 for a,b,c in [(x,z,w),(y,z,w),(z,x,y),(w,x,y)]]
F=bb*((x+y)*S-x*y+bb)/((x+z)*(x+w)*(y+z)*(y+w))
c=bb*(S+y)-x*y*y
B=R*(x+y)+x*x+x*y+y*y
A=R**3+2*R**2*x+3*R**2*y+R*x*x+5*R*x*y+3*R*y*y+2*x*x*y+2*x*y*y+y**3
ck(s.factor(1-3*lam[1]-c/((y+z)*(y+w)*S))==0)
ck(s.factor(F-27*lam[1]*lam[2]*lam[3]-bb*(c*B+bb*A+bb**2*y)/(S**3*(y+z)**2*(y+w)**2))==0)
heights=[-1/x,-1/y,1/z,1/w]
Fcdf=sum((-heights[i])**3/prod(heights[j]-heights[i] for j in range(4) if j!=i) for i in (0,1))
ck(s.factor(F-Fcdf)==0)
ck(s.factor(sum(lam)-1)==0)
# Actual section vertices and diagonal area weights reproduce all coordinates.
AA=s.Matrix([x,0,z,0])/(x+z);BB=s.Matrix([x,0,0,w])/(x+w)
CC=s.Matrix([0,y,0,w])/(y+w);DD=s.Matrix([0,y,z,0])/(y+z)
e=s.Matrix([x,y,z,w])/S
cent=(AA+CC+(y+z)*BB/S+(x+w)*DD/S)/3
for j in range(4):
 ck(s.factor(cent[j]-lam[j])==0)
 ck(s.factor(((x+z)*AA/S+(y+w)*CC/S-e)[j])==0)
 ck(s.factor(((x+w)*BB/S+(y+z)*DD/S-e)[j])==0)
for xv,yv,zv,wv in product(range(1,6),repeat=4):
 sub={x:xv,y:yv,z:zv,w:wv}
 ll=[Q(v.subs(sub)) for v in lam];ff=Q(F.subs(sub))
 for r in (0,1):
  if ll[1-r]<=Q(1,3):ck(ff>27*prod(ll[j] for j in range(4) if j!=r))
# All boundary triangular incidences, including a captured boundary vertex.
for eta in product([Q(1,5),Q(1,2),Q(4,5),Q(1)],repeat=3):
 l=[1-sum(eta)/3]+[v/3 for v in eta];f=prod(eta)
 ck(f==27*prod(l[1:]))
 if max(l)<=Q(1,3):
  for j in range(1,4):
   if eta[j-1]==1:ck(f>=27*prod(l[h] for h in range(4) if h!=j))
# Exact two-coordinate face construction, powers remove fractional exponents.
for d in range(2,10):
 for a in range(0,11):
  theta=Q(a,10);m=d+1
  Y=[[Q(0)]*m for _ in range(m)];Y[0][1]=Y[1][0]=1
  for j in range(2,m):Y[0][j]=theta;Y[1][j]=1-theta
  for j in range(m):ck(sum(Y[i][j] for i in range(m))==1 and Y[j][j]==0)
  ck(prod(Y[0][j] for j in range(m) if j!=0)==theta**(d-1))
  ck(prod(Y[1][j] for j in range(m) if j!=1)==(1-theta)**(d-1))
print('PASS',checks,'exact checks; printed cap identity, actual section centroids, boundary incidences, and all-d two-face construction')
