import json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
x=json.loads(Path(__file__).with_name('r4_facet_martingale_exact_slab_recovery.json').read_text())
checks=0
def ck(v):
 global checks
 assert v
 checks+=1
sets=[]
for ih,h in enumerate(x['high']):
 edges=[(j,F(num,den)) for i,j,num,den in x['edges'] if i==ih]
 ck(all(w>0 for j,w in edges));ck(sum(w for j,w in edges)==22)
 for c in range(3):ck(sum(w*x['low'][j][c] for j,w in edges)==22*h[c])
 sets.append(set([tuple(h[:2])]+[tuple(x['low'][j][:2]) for j,w in edges]))
def rank(pts):
 if not pts:return 0
 p=next(iter(pts))
 if len(pts)==1:return 1
 return 3 if any((q[0]-p[0])*(r[1]-p[1])!=(q[1]-p[1])*(r[0]-p[0]) for q,r in combinations(pts,2)) else 2
seq=[0,1,2,7,9,16,17,18,20,24,5,6,10,13]
bases=[((-4,-4),(-3,-3),(-2,-1)),((-4,-4),(-3,-3),(-2,-1)),((-4,-4),(-1,2)),((-4,-4),(-2,-2),(0,2)),((-2,-1),(-1,-1),(-1,0)),((-1,-1),(0,0),(0,1)),((0,0),(0,3),(1,0)),((0,1),(0,4),(1,0)),((0,3),(2,0),(2,1)),((0,4),(1,3)),((-4,-4),(-2,-2),(2,0)),((-3,-3),(-2,-2),(-1,-2)),((-4,-4),(-2,-3)),((-3,-3),(-1,-2),(-1,-1))]
covered=set()
for i,basis in zip(seq,bases):
 basis=set(basis);ck(basis<=sets[i]);ck(rank(basis)==len(basis)==rank(sets[i]))
 if covered:ck(basis<=covered)
 covered|=sets[i]
P={(z,y) for z in range(-4,5) for y in range(-4,5) if min(-z-y,2*z-y,2*y-z)>=-4}
ck(covered==P);ck(len(P)==31)
for f in [lambda z:1,lambda z:z[0],lambda z:z[1]]:
 ck(9*sum(f(z) for z in x['low'])-22*sum(f(z) for z in x['high'])==0)
print('PASS:',checks,'exact Jensen-support, affine-basis propagation and full-base coverage checks')
