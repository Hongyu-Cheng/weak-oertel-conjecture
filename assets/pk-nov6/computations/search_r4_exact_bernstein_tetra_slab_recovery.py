"""Bounded exact Bernstein proof search; COMPLETE is required for a theorem."""
from itertools import combinations_with_replacement, permutations
from math import gcd
from functools import reduce
from fractions import Fraction as Q
from pathlib import Path
import json,time,sys
P=[(x,y) for x in range(-4,5) for y in range(-4,5) if min(-x-y,2*x-y,2*y-x)>=-4]
rows=[]
for x,y in P:
 rows.append(((2,2,2*x-y,2*x+2*y),(-1,2,2*x-y,2*x+2*y),(-1,-4,2*x-y,2*x+2*y)))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def primitive(v):
 g=reduce(gcd,(abs(x) for x in v));return tuple(x//g for x in v)
planes=[]
for row in rows:
 for f in row:
  if min(f)<0<max(f):
   f=primitive(f)
   if next(x for x in f if x)!=abs(next(x for x in f if x)):f=tuple(-x for x in f)
   if f not in planes:planes.append(f)
ROOT=tuple(tuple(int(i==j) for i in range(4)) for j in range(4))
triples=list(combinations_with_replacement(range(4),3));perms=list(permutations(range(4)))
def det(T):
 return sum(((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)))*reduce(lambda a,b:a*b,(T[i][p[i]] for i in range(4)),1) for p in perms)
def volume(T):return Q(abs(det(T)),reduce(lambda a,b:a*b,(sum(v) for v in T),1))
def clean(tets):return [tuple(t) for t in tets if det(t)]
def split(T,f):
 vals=[dot(f,v) for v in T];pos=[i for i,x in enumerate(vals) if x>0];neg=[i for i,x in enumerate(vals) if x<=0]
 assert pos and any(v<0 for v in vals)
 def I(i,j):return primitive(tuple(vals[i]*T[j][k]-vals[j]*T[i][k] for k in range(4)))
 if len(pos)==1:
  p=pos[0];a,b,c=neg;A,B,C=I(p,a),I(p,b),I(p,c)
  out=[[T[p],A,B,C],[T[a],T[b],T[c],A],[T[b],T[c],A,B],[T[c],A,B,C]]
 elif len(pos)==3:
  # Reverse the normal so that this is a one-positive split.
  return split(T,tuple(-x for x in f))
 else:
  p,q=pos;a,b=neg;A,B,C,D=I(p,a),I(p,b),I(q,a),I(q,b)
  out=[[T[p],A,B,T[q]],[A,B,T[q],C],[B,T[q],C,D],
       [T[a],A,C,T[b]],[A,C,T[b],B],[C,T[b],B,D]]
 return clean(out)
def bisect(T,i,j):
 a,b=T[i],T[j];v=primitive(tuple(sum(b)*a[k]+sum(a)*b[k] for k in range(4)))
 U=list(T);V=list(T);U[i]=v;V[j]=v
 return [tuple(U),tuple(V)]

g0=(0,6,0,0);g1=(3,6,0,0);g2=(3,0,0,0)
def bernstein_lower(T):
 G=[[dot(g,v) for v in T] for g in [g0,g1,g2]]
 active=[[],[],[]]
 for row in rows:
  for j,f in enumerate(row):
   w=[dot(f,v) for v in T]
   if (j!=1 and min(w)>=0) or (j==1 and max(w)>0):active[j].append(w)
 answer=[]
 for i,j,k in triples:
  # This is three times the degree-three Bernstein coefficient.
  tot=0
  for typ in range(3):
   sign=-1 if typ==1 else 1;g=G[typ]
   tot+=3*sign*sum(g[i]*w[j]*w[k]+g[j]*w[i]*w[k]+g[k]*w[i]*w[j] for w in active[typ])
  # sum over all six permutations, repeated indices intentionally retained
  abc=[i,j,k]
  tot-=20*sum(G[0][abc[p[0]]]*G[1][abc[p[1]]]*G[2][abc[p[2]]] for p in permutations(range(3)))
  answer.append(tot)
 return answer

def unresolved_plane(T):
 best=None
 sums=[sum(v) for v in T]
 for j,f in enumerate(planes):
  vals=[dot(f,v) for v in T]
  if min(vals)<0<max(vals):
   ff=[v/s for v,s in zip(vals,sums)]
   score=min(-min(ff),max(ff))
   if best is None or score>best[0]:best=(score,j)
 return None if best is None else best[1]
def longest(T):
 points=[[x/sum(v) for x in v] for v in T]
 return max(((sum((points[i][k]-points[j][k])**2 for k in range(4)),i,j) for i in range(4) for j in range(i+1,4)))[1:]

# Validate all generic and boundary clipping patterns, with exact volume.
for f in [(1,-1,-1,-1),(1,1,-1,-1),(1,1,1,-1),(0,1,-1,-1),(0,0,1,-1),(1,0,0,-1),(2,3,-5,-7)]:
 out=split(ROOT,f);assert sum(map(volume,out))==volume(ROOT)
print('unique intersecting planes',len(planes),'root coeff min',min(bernstein_lower(ROOT)),flush=True)
limit=int(sys.argv[1]) if len(sys.argv)>1 else 20000
maxdepth=int(sys.argv[2]) if len(sys.argv)>2 else 65
stack=[(ROOT,0,[])];records=[];stats={'visited':0,'proved':0,'plane_splits':0,'bisections':0,'unresolved':0};start=time.time();hard=[]
while stack and stats['visited']<limit:
 T,dep,path=stack.pop();stats['visited']+=1
 B=bernstein_lower(T)
 if min(B)>=0:
  stats['proved']+=1;records.append([path,'proved']);continue
 if dep>=maxdepth:
  stats['unresolved']+=1;hard.append({'tet':T,'path':path,'coefficients':B});continue
 j=unresolved_plane(T)
 if j is not None:
  out=split(T,planes[j]);stats['plane_splits']+=1;record=['plane',j]
 else:
  i,j=longest(T);out=bisect(T,i,j);stats['bisections']+=1;record=['edge',i,j]
 records.append([path,record])
 for k,U in reversed(list(enumerate(out))):stack.append((U,dep+1,path+[k]))
 if stats['visited']%1000==0:print(stats,'pending',len(stack),'seconds',round(time.time()-start,2),flush=True)
print(stats,'pending',len(stack),'seconds',round(time.time()-start,2),'COMPLETE',not stack and not hard,flush=True)
output={'stats':stats,'planes':planes,'records':records,'hard':hard,'pending':[{'tet':T,'depth':dep,'path':path} for T,dep,path in stack],'complete':not stack and not hard}
Path(__file__).with_name('r4_exact_bernstein_tetra_attempt_slab_recovery.json').write_text(json.dumps(output,separators=(',',':')))
