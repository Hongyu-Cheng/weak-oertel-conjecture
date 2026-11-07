#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
import sympy as S
checks=0
def ok(x):
 global checks
 assert x
 checks+=1

def zero(x):ok(S.factor(x)==0)
b,c=S.symbols('b c',positive=True);D=b+c+2*b*c
x=c*(1+b)**2/D;y=b*(1+c)**2/D
zero(x/(1+b)+y/(1+c)-1)
zero(x*b/(1+b)**2-y*c/(1+c)**2)
zero(1-x-b*(1-b*c)/D)
zero(1-y-c*(1-b*c)/D)
u,v=S.symbols('u v',positive=True);w=(1-u*v)/(u+v)
r=[u,v,w];P=sum(r);R=S.prod(r)
zero(sum(r[i]*r[j] for i in range(3) for j in range(i+1,3))-1)
zero(S.prod(1+t*t for t in r)-(P-R)**2)
zero(sum((1+r[i]**2)*(1+r[j]**2) for i in range(3) for j in range(i+1,3))-2*P*(P-R))
# Dense rational family, with exact geometry, first moments and interval signs.
for a,b in product([F(i,8) for i in range(1,13)],repeat=2):
 if a*b>=1:continue
 r=[a,b,(1-a*b)/(a+b)];P=sum(r);R=r[0]*r[1]*r[2]
 beta=(P-R)/(2*P);x=[1/(1+t*t) for t in r];theta=[beta*t for t in x]
 yy=[r[j]*(P-r[j])/2 for j in range(3)]
 tt={(j,k):r[k]*(1+r[j]*r[j])/(r[j]+r[k]) for j in range(3) for k in range(3) if j!=k}
 bb={(j,k):(1-t)/t for (j,k),t in tt.items()}
 ok(sum(theta)==1);ok(sum(yy)==1);ok(beta>=F(4,9));ok(all(0<t<1 for t in tt.values()))
 for j in range(3):
  ok(yy[j]==sum(bb[j,k]*yy[k] for k in range(3) if k!=j))
  ok(sum(yy[k]/tt[j,k] for k in range(3) if k!=j)==1)
 for j in range(3):
  for k in range(j+1,3):
   s=tt[j,k];t=tt[k,j]
   ok(theta[j]*s+theta[k]*t==beta)
   ok(theta[j]*s*(1-s)==theta[k]*t*(1-t))
   ok(s+t>1);ok(theta[j]<beta and theta[k]<beta and theta[j]+theta[k]>beta)
   # Exact hinge integral: each cap interval separately, for rational hinge points.
   for h in [F(i,12) for i in range(13)]:
    ij=max(s-h,0)**2/2
    ik=((1-h)**2-max(1-t-h,0)**2)/2
    full=(1-h)**2/2
    ok(theta[j]*ij+theta[k]*ik<=beta*full)
# Exact noncanonical example.
r=[F(1,2),F(1,2),F(3,4)];P=sum(r);R=S.prod(r)
beta=(P-R)/(2*P)
ok(beta==F(25,56));ok(beta-F(4,9)==F(1,504))
theta=[beta/(1+t*t) for t in r]
ok(theta==[F(5,14),F(5,14),F(2,7)])
yy=[t*(P-t)/2 for t in r];ok(yy==[F(5,16),F(5,16),F(3,8)])
print(f'PASS: {checks} exact symbolic/rational checks.')
