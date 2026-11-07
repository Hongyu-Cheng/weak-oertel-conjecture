from fractions import Fraction as Q
from itertools import combinations,product
from math import prod

def cdf_b(x,t=Q(0)):
 d=len(x)-1;F=Q(0);Ft=Q(0);grad=[Q(0)]*(d+1)
 for i in range(d+1):
  if x[i]>=t:continue
  term=(t-x[i])**d/prod(x[j]-x[i] for j in range(d+1) if i!=j)
  F+=term;Ft+=d*term/(t-x[i])
  for j in range(d+1):
   grad[j]+=term*(-d/(t-x[i])+sum(1/(x[l]-x[i]) for l in range(d+1) if i!=l)) if i==j else -term/(x[j]-x[i])
 return F,tuple(-g/Ft for g in grad),Ft
worst=(Q(100),None);count=0
for x in combinations([Q(j) for j in range(-7,8) if j],4):
 if min(x)>0 or max(x)<0:continue
 F,b,Ft=cdf_b(x)
 for r in range(4):
  if x[r]>=0 or max(b)>Q(1,3) or min(x)+3*F/Ft<=0:continue
  count+=1;val=F/(27*prod(b[j] for j in range(4) if j!=r))
  if val<worst[0]:worst=(val,(x,r,F,b))
print('tests',count,'min',worst)
