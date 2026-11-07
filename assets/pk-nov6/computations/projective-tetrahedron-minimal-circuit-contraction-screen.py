import sys

import numpy as np
from fractions import Fraction as F
from random import Random
from math import prod
from itertools import combinations
rng=Random(74162)
def cap(t):
 pp=[z for z in t if z>0];nn=[-z for z in t if z<0]
 if len(pp)==1:return pp[0]**3/prod(pp[0]+z for z in nn)
 if len(nn)==1:return 1-nn[0]**3/prod(nn[0]+z for z in pp)
 if len(pp)!=2 or len(nn)!=2:raise ValueError(t)
 p,q=pp;r,s=nn;a=p*s/((p+r)*(p+s)*(q+s));b=q*r/((p+r)*(q+s)*(q+r));return p*(a+b)+q*q/((q+s)*(q+r))
def solve(A,b):
 a=[list(row)+[rhs] for row,rhs in zip(A,b)];n=len(a)
 for j in range(n):
  z=next(i for i in range(j,n) if a[i][j]);a[j],a[z]=a[z],a[j];v=a[j][j];a[j]=[x/v for x in a[j]]
  for i in range(n):
   if i==j:continue
   v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
 return [r[-1] for r in a]
for trial in range(10000):
 p,q,r,s=[F(rng.randint(1,30)) for _ in range(4)];t=[p,q,-r,-s]
 aa=p*s/((p+r)*(p+s)*(q+s));bb=q*r/((p+r)*(q+s)*(q+r));tau=aa/(aa+bb)
 la=[(r/(p+r)+tau*s/(p+s))/3,(s/(q+s)+(1-tau)*r/(q+r))/3,(p/(p+r)+(1-tau)*q/(q+r))/3,(q/(q+s)+tau*p/(p+s))/3]
 S=3*(aa+bb);records=[('quad',t,S)]
 for i in range(4):
  if any(la[j]>=F(1,3) for j in range(4) if j!=i):continue
  tt=[F(3) if j==i else 3-1/la[j] for j in range(4)];co=27*prod(la[j] for j in range(4) if j!=i);records.append(('vertex'+str(i),tt,co))
 records += [('negative '+name,[-x for x in tt],co) for name,tt,co in list(records)]
 normals=[[co*(tt[j]-tt[0]) for j in range(1,4)] for name,tt,co in records]
 before=[cap(tt) for name,tt,co in records];after=[cap([4*la[j]*tt[j] for j in range(4)]) for name,tt,co in records]
 for inds in combinations(range(len(records)),4):
  A=[[normals[i][j] for i in inds] for j in range(3)]+[[F(1)]*4];An=np.array(A,dtype=float)
  try:w=np.linalg.solve(An,np.array([0,0,0,1.]))
  except np.linalg.LinAlgError:continue
  if min(w)<1e-8:continue
  bef=sum(w[j]*float(before[i]) for j,i in enumerate(inds));aft=sum(w[j]*float(after[i]) for j,i in enumerate(inds))
  if abs(bef-.5)<=abs(aft-.5)+1e-8:continue
  ww=solve(A,[F(0),F(0),F(0),F(1)])
  be=sum(w*before[i] for w,i in zip(ww,inds));af=sum(w*after[i] for w,i in zip(ww,inds))
  if min(ww)>0 and abs(be-F(1,2))>abs(af-F(1,2)):
   rec={'params':(p,q,r,s),'lambda':la,'indices':inds,'records':[records[i] for i in inds],'normals':[normals[i] for i in inds],'weights':ww,'beforecaps':[before[i] for i in inds],'aftercaps':[after[i] for i in inds],'before':be,'after':af}
   print('EXACT CONTRACTION FAILURE',trial,'params',(p,q,r,s),'names',[records[i][0] for i in inds],'means',float(be),float(af),'exact',repr(rec),flush=True)
   open('./projective-minimal-circuit-contraction-counter.txt','w').write(repr(rec));raise SystemExit
 if trial%500==0:print(trial,'no exact contraction failure',flush=True)
