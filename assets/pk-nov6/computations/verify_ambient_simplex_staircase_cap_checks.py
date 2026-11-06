"""Exact staircase decomposition and bounded oblique-cap checks.

The nearby floating search result was a numerical artifact. No assertion
about an all-normal minimum is made.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial,comb
exec(open('./verify_simplex_endpoint_centroid_midpoint_failure.py').read().split('h=list(map')[0])
h=list(map(F,[0,4,0,0,1,3,3]));vs=[(F(0),)*5]*2+[tuple(F(i==j) for i in range(5)) for j in range(5)]
def detfast(A):
 A=[list(row) for row in A];ret=F(1);n=len(A)
 for k in range(n):
  p=next((i for i in range(k,n) if A[i][k]),None)
  if p is None:return F(0)
  if p!=k:A[k],A[p]=A[p],A[k];ret=-ret
  v=A[k][k];ret*=v
  for i in range(k+1,n):
   q=A[i][k]/v
   for j in range(k+1,n):A[i][j]-=q*A[k][j]
 return ret

def pieces(z):
 lo=[i for i in range(7) if h[i]<z];hi=[i for i in range(7) if h[i]>z];eq=[i for i in range(7) if h[i]==z]
 n=len(lo)+len(hi)-2
 out=[]
 for rights in combinations(range(n),len(lo)-1):
  path=[(0,0)];a=b=0
  for k in range(n):
   if k in rights:a+=1
   else:b+=1
   path.append((a,b))
  pp=[]
  for a,b in path:
   i,j=lo[a],hi[b]
   pp.append(tuple(((h[j]-z)*vs[i][k]+(z-h[i])*vs[j][k])/(h[j]-h[i]) for k in range(5)))
  pp += [vs[i] for i in eq]
  assert len(pp)==6
  vol=abs(detfast([[pp[i+1][k]-pp[0][k] for k in range(5)] for i in range(5)]))/120
  out.append((pp,vol))
 return out
P={z:pieces(F(z)) for z in (1,2,3)}
for z,ss in P.items():
 assert sum(vol for pp,vol in ss)==density(h,F(z))/180
print('pieces',[len(P[z]) for z in P])
g=[F(25,243),F(25,243),F(7,54),F(61,324),F(61,324)]
M=F(73,72)/180
def cap(n):
 out=F(0)
 for z,ss in P.items():
  for pp,vol in ss:
   knots=[n[0]*(z-2)+sum(n[k+1]*(p[k]-g[k]) for k in range(5)) for p in pp]
   if min(knots)>=0:frac=F(1)
   elif max(knots)<=0:frac=F(0)
   else:frac=dd(knots,F(0),5)
   assert 0<=frac<=1,(knots,frac)
   out+=vol*frac
 return out/M
normals=[[1,0,0,1,12,1],[1,0,0,1,12,0],[1,0,0,1,1,12],
         [1,0,0,1,1,1],[F(102,1000),0,F(75,1000000),F(103,1000),
                       F(1255,1000),F(121,1000)]]
for n in normals:
 r=cap(n)
 assert r>F(5,6)**5/2
 print(n, float(r),r,flush=True)
assert cap(normals[0])==F(22871381014142276443,99086463923756728320)
assert cap(normals[2])==cap(normals[0])
assert cap(normals[4])==F(
 40785603200965569268246734952488254693,
 176707994235590558388120820688145530880)
print("PASS: 17 exact slice simplices, three volume sums, five oblique caps.")
