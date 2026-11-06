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
assert len(out)==1999
assert sum(map(len,reps))==110
w=list(map(F,['3/140','1179/14560','37/520','893/14560','75/1456','297/3640','513/7280','58/455','1051/10920','13/168','3/65','79/910','58/455']))
assert sum(w)==1 and min(w)>0
checks=2
for p,ids,lam in rep_rows:
 assert w[p]>=sum(F(l)*w[j] for j,l in zip(ids,lam));checks+=1
gaps=[]
for _,mask,_,k in out:
 gap=F(k,7)-sum(w[j] for j in range(N) if mask>>j&1)
 assert gap>0;gaps.append(gap);checks+=1
assert min(gaps)==F(1,65);checks+=1
print('PASS',checks,'exact arithmetic checks;1999 proper closed minors,110 extreme anchored representations;minimum quota slack1/65')
