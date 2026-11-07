"""Standalone rational verification; no numerical solver and no SymPy dependency."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json
checks=0
def ck(t):
 global checks
 assert t
 checks+=1
P=[(x,y) for x in range(-4,5) for y in range(-4,5) if min(-x-y,2*x-y,2*y-x)>=-4]
ck(len(P)==31)
ck(Counter(tuple(t%2 for t in p) for p in P)=={(0,0):10,(0,1):7,(1,0):7,(1,1):7})
H=[];L=[]
for x,y in P:
 e=(-x-y,2*x-y,2*y-x)
 for s in range(3):
  W=sum(t>0 for t in e)+(e[1]==0 and s>=1)+(e[2]==0 and s<=1)
  ck(W in [1,2])
  (H if W==2 else L).append((x,y,s))
ck(len(H)==27);ck(len(L)==66)
cert=json.loads(Path(__file__).with_name('r4_facet_martingale_exact_slab_recovery.json').read_text())
ck([list(h) for h in H]==cert['high']);ck([list(l) for l in L]==cert['low'])
ck(cert['source_mass']==22);ck(cert['target_mass']==9)
row=[F(0)]*len(H);col=[F(0)]*len(L);mom=[[F(0)]*3 for _ in H];seen=set()
for i,j,num,den in cert['edges']:
 ck((i,j) not in seen);seen.add((i,j))
 ck(0<=i<len(H) and 0<=j<len(L));ck(num>0 and den>0)
 mass=F(num,den);row[i]+=mass;col[j]+=mass
 for k in range(3):mom[i][k]+=mass*L[j][k]
for i,h in enumerate(H):
 ck(row[i]==22)
 for k in range(3):ck(mom[i][k]==22*h[k])
for v in col:ck(v==9)
ck(22*len(H)==9*len(L))
ck(F(40,93)-F(1,3)==F(9,93));ck(F(2,3)-F(40,93)==F(22,93))
ck(F(40,93)<F(4,9));ck(F(4,9)-F(40,93)==F(4,279))
for j in range(3):
 plus=sum((-x-y,2*x-y,2*y-x)[j]>0 for x,y in P)
 zero=sum((-x-y,2*x-y,2*y-x)[j]==0 for x,y in P)
 ck((plus,zero)==(12,3));ck(F(plus)+F(4,9)*zero==F(40,3))
 # All actual proper sections occur on a balanced zero slice.
 Z=[p for p in P if (-sum(p),2*p[0]-p[1],2*p[1]-p[0])[j]==0]
 ck(all(sum(p[i] for p in Z)==0 for i in range(2)))
for k,size in [(1,1),(2,9),(3,23),(4,30)]:ck(F(k,4)-F(size,31)>=F(1,124))
# Exposed edge z1+z2=4: all-facet profile constant in x with central doubling.
edge=[(r,4-r) for r in range(5)]
vals=[]
for x,y in edge:
 e=(-x-y,2*x-y,2*y-x);ck(all(t!=0 for t in e))
 vals.append(F(sum(t>0 for t in e),3))
ck(vals==[F(1,3),F(1,3),F(2,3),F(1,3),F(1,3)])
ck(sum(vals)/5==F(2,5)<F(4,9))
print(f'PASS: {checks} exact martingale, profile, critical-stationarity and quota checks')
