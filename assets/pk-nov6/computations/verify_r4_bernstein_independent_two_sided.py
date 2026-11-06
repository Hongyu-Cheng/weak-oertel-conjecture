"""Independent exact replay: raw monomial coefficients, projective vertices, coverage volumes."""
from fractions import Fraction as Q
from itertools import permutations
from functools import reduce
from math import gcd
from pathlib import Path
import json,time
HERE=Path(__file__).parent
J=json.loads((HERE/'r4_exact_bernstein_tetra_attempt_slab_recovery.json').read_text())
assert J['complete'] and not J['hard'] and not J['pending']
P=[(x,y) for x in range(-4,5) for y in range(-4,5) if min(-x-y,2*x-y,2*y-x)>=-4]
assert len(P)==31
rows=[[(2,2,2*x-y,2*x+2*y),(-1,2,2*x-y,2*x+2*y),(-1,-4,2*x-y,2*x+2*y)] for x,y in P]
gs=[(0,6,0,0),(3,6,0,0),(3,0,0,0)]
perms=list(permutations(range(4)))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(T):return sum((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))*reduce(lambda a,b:a*b,(T[i][p[i]] for i in range(4)),1) for p in perms)
def vol(T):return Q(abs(det(T)),reduce(lambda a,b:a*b,(sum(v) for v in T),1))
def prim(v):
 g=reduce(gcd,map(abs,v));assert g>0
 return tuple(x//g for x in v)
def split(T,f):
 vals=[dot(v,f) for v in T];I=[i for i,v in enumerate(vals) if v>0];N=[i for i,v in enumerate(vals) if v<=0]
 assert min(vals)<0<max(vals)
 if len(I)==3:return split(T,tuple(-x for x in f))
 def cut(i,j):
  v=prim(tuple(vals[i]*T[j][k]-vals[j]*T[i][k] for k in range(4)))
  assert min(v)>=0 and dot(f,v)==0
  # independent normalized Euclidean edge interpolation
  x=[Q(t,sum(T[i])) for t in T[i]];y=[Q(t,sum(T[j])) for t in T[j]]
  fx=Q(vals[i],sum(T[i]));fy=Q(vals[j],sum(T[j]))
  assert [Q(t,sum(v)) for t in v]==[(fx*y[k]-fy*x[k])/(fx-fy) for k in range(4)]
  return v
 if len(I)==1:
  i=I[0];j,k,l=N;v,w,x=cut(i,j),cut(i,k),cut(i,l)
  children=[(T[i],v,w,x),(T[j],T[k],T[l],v),(T[k],T[l],v,w),(T[l],v,w,x)]
 else:
  i,j=I;k,l=N;v,w,x,y=cut(i,k),cut(i,l),cut(j,k),cut(j,l)
  children=[(T[i],v,w,T[j]),(v,w,T[j],x),(w,T[j],x,y),(T[k],v,x,T[l]),(v,x,T[l],w),(x,T[l],w,y)]
 children=[t for t in children if det(t)]
 assert sum(map(vol,children))==vol(T)
 for t in children:
  vv=[dot(v,f) for v in t];assert min(vv)>=0 or max(vv)<=0
 return children
# Compute coefficients by multiplication, independently of the search polarization formula.
units=[tuple(int(i==j) for j in range(4)) for i in range(4)]
def mul(A,B):
 C={}
 for a,x in A.items():
  for b,y in B.items():
   ab=tuple(a[i]+b[i] for i in range(4));C[ab]=C.get(ab,0)+x*y
 return C
def lin(v):return {units[i]:x for i,x in enumerate(v) if x}
def leaf(T):
 G=[lin([dot(g,v) for v in T]) for g in gs];out={}
 for rr in rows:
  for j,f in enumerate(rr):
   vals=[dot(f,v) for v in T]
   included=(min(vals)>=0) if j!=1 else (max(vals)>0)
   if included:
    W=lin(vals);pol=mul(G[j],mul(W,W));fac=-3 if j==1 else 3
    for a,x in pol.items():out[a]=out.get(a,0)+fac*x
 for a,x in mul(G[0],mul(G[1],G[2])).items():out[a]=out.get(a,0)-40*x
 assert all(x>=0 for x in out.values()),(T,out)
 return len(out),sum(x==0 for x in out.values())
records={tuple(p):r for p,r in J['records']};assert len(records)==len(J['records'])
root=tuple(units);stack=[((),root)];seen=set();nv=nc=nz=0;total=Q(0);start=time.time()
while stack:
 path,T=stack.pop();assert path in records and path not in seen;seen.add(path);r=records[path]
 assert det(T)!=0 and all(min(v)>=0 and sum(v)>0 for v in T)
 if r=='proved':
  c,z=leaf(T);nv+=1;nc+=c;nz+=z;total+=vol(T)
 else:
  assert r[0]=='plane';children=split(T,J['planes'][r[1]])
  stack.extend((path+(i,),U) for i,U in enumerate(children))
assert seen==set(records) and total==1
assert nv==J['stats']['proved']==11188
print('PASS: 31 actual bases;',len(seen),'nodes;',nv,'leaf tetrahedra;',nc,'independent raw coefficients;',nz,'zero coefficients; exact total volume',total,'seconds',round(time.time()-start,2))
