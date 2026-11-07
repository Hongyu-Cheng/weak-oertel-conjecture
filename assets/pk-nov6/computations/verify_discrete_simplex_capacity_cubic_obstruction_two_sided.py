from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json
D=json.loads(Path('./beta_coupling_exact_certificate_root.json').read_text())
n=D['n']; triples=D['triples']; weights=list(map(F,D['mass'])); count=0
def check(q):
 global count
 assert q
 count+=1
check(n==200 and D['Mn']==273 and D['Md']==100)
check(len(triples)==len(weights)==399)
check(all(p>0 for p in weights))
check(sum(weights)==1)
phi=(F(200,273),F(100,273),F(100,273))
mu=defaultdict(F)
margins=[defaultdict(F) for _ in range(3)]
for (i,j,k),p in zip(triples,weights):
 check(0<=i<n and 0<=j<n and 0<=k<n)
 check(2*(i+1)+(j+1)+(k+1)<=546)
 for jj,kk in ((j,k),(k,j)):
  u=(F(i+1,n),F(jj+1,n),F(kk+1,n))
  z=tuple(phi[q]*u[q] for q in range(3))
  x=(1-z[1]-z[2],z[1],z[2])
  check(x[0]>=z[0])
  check(sum(x)==1 and min(x)>=0)
  mu[x]+=p/2
  for q in range(3): margins[q][u[q]]+=p/2
for q in range(3):
 for i in range(n):check(margins[q][F(i+1,n)]==F(2*i+1,n*n))
check(sum(mu.values())==1)
actual=[]
for q in range(3):
 m=defaultdict(F)
 for x,p in mu.items():m[x[q]]+=p
 cumulative=F(0); ratios=[]
 for t,p in sorted(m.items()):
  cumulative+=p
  check(cumulative<=t*t/(phi[q]*phi[q]))
  ratios.append(t*t/cumulative)
 actual.append(min(ratios))
check(actual==[x*x for x in phi])
check(sum(x*x for x in phi)+2*phi[0]*phi[1]*phi[2]-1==F(33583,273**3))
print('PASS',count,'exact checks;',len(mu),'simplex atoms')
print('capacity squares:',*[str(x) for x in actual])
print('guaranteed cubic excess:',F(33583,273**3))
