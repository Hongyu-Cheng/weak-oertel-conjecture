"""Standalone exact full-cover and power-coefficient verifier.
No optimizer, numerical geometry, or import of the proof-search implementation.
"""
from pathlib import Path
from itertools import permutations,combinations_with_replacement,combinations,product
from fractions import Fraction
from functools import reduce
from math import gcd
import json,time
checks=0
def ck(t):
 global checks
 assert t
 checks+=1

def determinant(M):
 n=len(M);ans=0
 for p in permutations(range(n)):
  sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
  ans+=sign*reduce(lambda a,b:a*b,(M[i][p[i]] for i in range(n)),1)
 return ans

def primitive(v):
 g=reduce(gcd,(abs(x) for x in v));ck(g>0)
 return tuple(x//g for x in v)
def dot(v,w):return sum(x*y for x,y in zip(v,w))
def volume(T):return Fraction(abs(determinant(T)),reduce(lambda a,b:a*b,(sum(v) for v in T),1))
def facet_plane(T,i):
 rows=[v for j,v in enumerate(T) if j!=i]
 n=tuple((-1)**j*determinant([r[:j]+r[j+1:] for r in rows]) for j in range(4))
 if dot(n,T[i])<0:n=tuple(-a for a in n)
 ck(dot(n,T[i])>0)
 return n

def split_exact(T,f):
 vals=[dot(f,v) for v in T];ck(min(vals)<0<max(vals))
 pos=[i for i,q in enumerate(vals) if q>0];neg=[i for i,q in enumerate(vals) if q<=0]
 def meet(i,j):return primitive(tuple(vals[i]*T[j][k]-vals[j]*T[i][k] for k in range(4)))
 if len(pos)==3:return split_exact(T,tuple(-q for q in f))
 if len(pos)==1:
  p=pos[0];a,b,c=neg;A,B,C=meet(p,a),meet(p,b),meet(p,c)
  out=[(T[p],A,B,C),(T[a],T[b],T[c],A),(T[b],T[c],A,B),(T[c],A,B,C)]
 else:
  p,q=pos;a,b=neg;A,B,C,D=meet(p,a),meet(p,b),meet(q,a),meet(q,b)
  out=[(T[p],A,B,T[q]),(A,B,T[q],C),(B,T[q],C,D),
       (T[a],A,C,T[b]),(A,C,T[b],B),(C,T[b],B,D)]
 return [U for U in out if determinant(U)]

def verify_cover(T,children):
 parent_planes=[facet_plane(T,i) for i in range(4)]
 # Each child vertex is in the parent, including every degeneracy.
 allvertices=set(v for U in children for v in U)
 for v in allvertices:
  ck(min(v)>=0 and sum(v)>0)
  for f in parent_planes:ck(dot(f,v)>=0)
 ck(sum(volume(U) for U in children)==volume(T))
 # Explicit face separators prove pairwise disjoint interiors.
 cp=[[facet_plane(U,i) for i in range(4)] for U in children]
 for i,j in combinations(range(len(children)),2):
  separate=any(all(dot(f,v)<=0 for v in children[j]) for f in cp[i]) or any(all(dot(f,v)<=0 for v in children[i]) for f in cp[j])
  ck(separate)

points=[(x,y) for x in range(-4,5) for y in range(-4,5) if min(-x-y,2*x-y,2*y-x)>=-4]
rows=[((2,2,2*x-y,2*x+2*y),(-1,2,2*x-y,2*x+2*y),(-1,-4,2*x-y,2*x+2*y)) for x,y in points]
global_g=[(0,6,0,0),(3,6,0,0),(3,0,0,0)]
monomials=list(combinations_with_replacement(range(4),3))
def power_coefficients(T):
 """Expand the LOWER homogeneous cubic in local barycentric variables.
 Positive vertex denominators divide each monomial by one common factor,
 so the signs of these integer coefficients equal the normalized signs.
 """
 G=[[dot(g,v) for v in T] for g in global_g]
 ck(all(min(g)>=0 for g in G))
 squares=[{pair:0 for pair in combinations_with_replacement(range(4),2)} for _ in range(3)]
 for row in rows:
  for typ,f in enumerate(row):
   w=[dot(f,v) for v in T]
   # Direct sign-justified lower bound for each positive-part term.
   include=(min(w)>=0) if typ!=1 else (max(w)>0)
   if include:
    for i,j in squares[typ]:squares[typ][i,j]+=(1 if i==j else 2)*w[i]*w[j]
 coeff={mon:0 for mon in monomials}
 for typ in range(3):
  sign=-1 if typ==1 else 1
  for (i,j),value in squares[typ].items():
   for k in range(4):coeff[tuple(sorted((i,j,k)))]+=3*sign*G[typ][k]*value
 for i,j,k in product(range(4),repeat=3):coeff[tuple(sorted((i,j,k)))]-=40*G[0][i]*G[1][j]*G[2][k]
 return coeff

cert=json.loads(Path(__file__).with_name('r4_exact_bernstein_tetra_attempt_slab_recovery.json').read_text())
ck(cert['complete'] is True);ck(not cert['pending'] and not cert['hard'])
records={}
for path,record in cert['records']:
 path=tuple(path);ck(path not in records);records[path]=record
planes=[tuple(f) for f in cert['planes']]
for f in planes:ck(len(f)==4 and min(f)<0<max(f))
ROOT=tuple(tuple(int(i==j) for i in range(4)) for j in range(4))
stack=[((),ROOT)];visited=set();proved=0;splits=0;start=time.time();maxdepth=0
while stack:
 path,T=stack.pop();ck(path in records and path not in visited);visited.add(path);maxdepth=max(maxdepth,len(path))
 record=records[path]
 if record=='proved':
  coeff=power_coefficients(T)
  for value in coeff.values():ck(value>=0)
  proved+=1
 else:
  ck(isinstance(record,list) and record[0]=='plane')
  ck(0<=record[1]<len(planes))
  children=split_exact(T,planes[record[1]])
  verify_cover(T,children);splits+=1
  for i,U in enumerate(children):stack.append((path+(i,),U))
ck(visited==set(records));ck(proved==11188);ck(splits==3911)
ck(len(visited)==15099);ck(maxdepth<71)
print(f'PASS: {checks} exact checks; {proved} complete nonnegative power/Bernstein leaves; {splits} verified disjoint covering splits; max depth {maxdepth}; seconds {time.time()-start:.2f}')
