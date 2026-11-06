from fractions import Fraction as F
from itertools import combinations
import sympy as s
from collections import Counter
P=[(-1,3,0),(0,-2,0),(0,-1,0),(0,0,0),(0,1,0),(1,-1,0),(1,0,0),(1,0,1),(1,1,1),(1,2,2),(2,-2,-1),(2,-1,0),(2,0,1)]
N=len(P); reps=[set() for _ in P]; rep_rows=[]
for size in (2,3,4):
 for ids in combinations(range(N),size):
  M=s.Matrix([[1]*size]+[[P[j][k] for j in ids] for k in range(3)])
  rows=M.T.rref()[1]
  if len(rows)!=size:continue
  Minv=M[list(rows),:].inv()
  for p,x in enumerate(P):
   if p in ids:continue
   y=s.Matrix([1,*x]); lam=Minv*y[list(rows),:]
   if min(lam)>0 and M*lam==y:
    reps[p].add(sum(1<<j for j in ids));rep_rows.append((p,ids,list(lam)))
colors=[tuple(x%2 for x in p) for p in P]; out=[]
for mask in range(1,(1<<N)-1):
 if any(any(mask&r==r for r in reps[p]) for p in range(N) if not(mask>>p&1)):continue
 ids=[j for j in range(N) if mask>>j&1]; k=len({colors[j] for j in ids})
 out.append((F(len(ids),k),mask,len(ids),k))
a=max(out);print('closed minors',len(out),'max cardinality/parity',a[0],'global',F(13,7),'indices',[j for j in range(N) if a[1]>>j&1]); print('strict uniform quotas',all(x[0]<F(13,7) for x in out)); print('reps',sum(map(len,reps)))

import numpy as np
from scipy.optimize import linprog
A=[];b=[]
for _,mask,_,k in out:
 A.append([int(bool(mask>>j&1)) for j in range(N)]+[1]);b.append(k/7)
for j in range(N):
 row=[0.]*(N+1);row[j]=-1;row[-1]=1;A.append(row);b.append(0)
for p,ids,lam in rep_rows:
 row=[0.]*(N+1);row[p]=-1
 for j,l in zip(ids,lam):row[j]=float(l)
 A.append(row);b.append(0)
c=[0.]*N+[-1.]
res=linprog(c,A_ub=A,b_ub=b,A_eq=[[1.]*N+[0.]],b_eq=[1.],bounds=[(0,None)]*(N+1),method='highs')
print('concave quota maxmargin',res.success, res.fun, res.x if res.success else res.message)
if res.success:
 w=[F(float(x)).limit_denominator(1000000) for x in res.x[:-1]]
 print('rational',w,'sum',sum(w))
 print('quota gap',min(F(k,7)-sum(w[j] for j in range(N) if mask>>j&1) for _,mask,_,k in out))
 print('minradius',min(w))
 print('minconcavity',min(w[p]-sum(F(l)*w[j] for j,l in zip(ids,lam)) for p,ids,lam in rep_rows))
