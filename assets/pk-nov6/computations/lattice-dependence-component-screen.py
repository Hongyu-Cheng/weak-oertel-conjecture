from itertools import combinations,product
from fractions import Fraction as F
from math import gcd
from functools import reduce
import random

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def facets(V):
 fs=set()
 for a,b,c in combinations(V,3):
  u=cross(sub(b,a),sub(c,a))
  if not any(u):continue
  h=dot(u,a); vals=[dot(u,x)-h for x in V]
  if min(vals)<0<max(vals):continue
  if min(vals)==max(vals)==0:continue
  if max(vals)>0:u=tuple(-x for x in u);h=-h
  g=reduce(gcd,[abs(x) for x in u]+[abs(h)])
  fs.add(tuple(x//g for x in u)+(h//g,))
 return sorted(fs)
def rank(rows):
 mat=[list(map(F,r)) for r in rows];k=0
 if not mat:return 0
 for j in range(len(mat[0])):
  i=next((i for i in range(k,len(mat)) if mat[i][j]),None)
  if i is None:continue
  mat[k],mat[i]=mat[i],mat[k];a=mat[k][j];mat[k]=[x/a for x in mat[k]]
  for i in range(k+1,len(mat)):
   a=mat[i][j]
   if a:mat[i]=[x-a*y for x,y in zip(mat[i],mat[k])]
  k+=1
  if k==len(mat):break
 return k

def relations(P,inds):
 # Null vectors of the affine-coordinate matrix supported on this face.
 m=len(inds);mat=[[F(1) for i in inds]]+[[F(P[i][j]) for i in inds] for j in range(3)]
 piv=[];k=0
 for j in range(m):
  i=next((i for i in range(k,4) if mat[i][j]),None)
  if i is None:continue
  mat[k],mat[i]=mat[i],mat[k];a=mat[k][j];mat[k]=[x/a for x in mat[k]]
  for i in range(4):
   if i!=k:
    a=mat[i][j]
    if a:mat[i]=[x-a*y for x,y in zip(mat[i],mat[k])]
  piv.append(j);k+=1
  if k==4:break
 for j in range(m):
  if j in piv:continue
  r=[F(0)]*len(P);r[inds[j]]=1
  for i,l in enumerate(piv):r[inds[l]]=-mat[i][j]
  yield r

random.seed(72713)
templates=[(2,3,6),(2,4,4),(3,3,3)]
for it in range(5000):
 abc=random.choice(templates)
 grid=[p for p in product(*(range(a+1) for a in abc)) if sum(F(p[i],abc[i]) for i in range(3))<=1]
 V=random.sample(grid,random.randrange(5,13));fs=facets(V)
 if len(fs)<4:continue
 P=[p for p in grid if all(dot(f[:3],p)<=f[3] for f in fs)]
 if any(all(dot(f[:3],p)<f[3] for f in fs) for p in P):raise RuntimeError('template was not hollow')
 sets=[]
 for z in P:
  active=[f for f in fs if dot(f[:3],z)==f[3]]
  face=tuple(i for i,p in enumerate(P) if all(dot(f[:3],p)==f[3] for f in active))
  if len(face)>1:sets.append(face)
 parent=list(range(len(P)))
 def find(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 for S in sets:
  for i in S[1:]:parent[find(i)]=find(S[0])
 if len({find(i) for i in range(len(P))})>1:continue
 rows=[r for S in set(sets) for r in relations(P,S)]
 dim=len(P)-rank(rows)
 if dim>4:
  print('EXACT CANDIDATE',it,'dim',dim,'P',P,'facets',fs,'face_sets',sorted(set(sets)),flush=True);break
 if it%100==0:print('screen',it,'P',len(P),'dim',dim,flush=True)
else:print('no counter found',flush=True)
