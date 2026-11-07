#!/usr/bin/env python3
import sympy as S
from fractions import Fraction as F
from itertools import product
checks=0
def ok(x):
 global checks
 assert x
 checks+=1
for d in range(1,9):
 r=S.symbols('r:'+str(d+1));y=[(1-t)/d for t in r];lam=S.symbols('l:'+str(d+1))
 # Linear algebra identities tested modulo sum r=1; raw margins/circuit.
 rr=list(r[:-1])+[1-sum(r[:-1])];yy=[(1-t)/d for t in rr]
 fj=[lam[j]/(d*yy[j])-sum(rr[k]*lam[k]/(d*yy[k]) for k in range(d+1)) for j in range(d+1)]
 ok(S.factor(sum(rr[j]*fj[j] for j in range(d+1)))==0)
 for j in range(d+1):ok(S.factor(fj[j].subs(dict(zip(lam,yy))))==0)
 # Beta transformation needs no product expansion.
 ok(S.factor(1-d*sum(t*t for t in yy)-(1-sum(t*t for t in rr))/d)==0)
 gamma=F(d,d+1)**d
 uni=F(1,d+1);val=(1-uni)**(d+1)/(1-(d+1)*uni*uni)
 ok(val==gamma)
# General pair-bracket identity, retaining the sum of the other coordinates.
a,b,s,q=S.symbols('a b s q')
num=2*(1-a)*(1-b)-(1-a*a-b*b-q)
ok(S.expand(num.subs(b,1-a-s)-(s*s+q))==0)
# Exact all-d positive rational examples, actual cap fractions and source centroid equations.
for d in range(1,8):
 for pattern in range(1,17):
  vals=[F(1+((j+2)*pattern)%11) for j in range(d+1)];r=[t/sum(vals) for t in vals]
  y=[(1-t)/d for t in r];q=[S.prod(d*y[k] for k in range(d+1) if k!=j) for j in range(d+1)]
  den=sum(rj/qj for rj,qj in zip(r,q));theta=[(rj/qj)/den for rj,qj in zip(r,q)]
  beta=1/den;f=S.prod(1-t for t in r)/(1-sum(t*t for t in r))
  ok(sum(y)==1);ok(sum(theta)==1);ok(beta==sum(t*qj for t,qj in zip(theta,q)))
  ok(beta==f);ok(beta>=F(d,d+1)**d)
  for j in range(d+1):
   ts=[d*y[k] for k in range(d+1) if k!=j]
   ok(all(0<t<1 for t in ts));ok(1-sum(ts)/d==y[j])
  if d>=2:
   i=max(range(d+1),key=lambda i:r[i]);j=min(range(d+1),key=lambda i:r[i]);new=list(r);new[i]=new[j]=(r[i]+r[j])/2
   fn=S.prod(1-t for t in new)/(1-sum(t*t for t in new))
   ok(fn<=f);ok((fn<f)==(r[i]!=r[j]))
print(f'PASS: {checks} exact symbolic/rational checks.')
