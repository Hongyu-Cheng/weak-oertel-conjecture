from fractions import Fraction as F
from itertools import product,combinations
ns={};exec(open('./lattice-dependence-component-screen.py').read().split('random.seed')[0],ns)
rank,relations,dot=ns['rank'],ns['relations'],ns['dot']
P=[(0,0,1),(0,0,2),(0,0,3),(0,1,1),(0,1,2),(0,1,3),(0,2,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1),(1,2,0),(2,0,0)]
fs=[(-1,0,-1,-1),(-1,0,0,0),(0,-1,0,0),(0,0,-1,0),(1,2,1,5),(2,1,1,4),(3,0,2,6)]
assert [p for p in product(range(3),range(3),range(4)) if all(dot(f[:3],p)<=f[3] for f in fs)]==P
def solve3(rows):
 a=[list(map(F,row[:3]))+[F(row[3])] for row in rows]
 for j in range(3):
  i=next((i for i in range(j,3) if a[i][j]),None)
  if i is None:return None
  a[j],a[i]=a[i],a[j];q=a[j][j];a[j]=[v/q for v in a[j]]
  for i in range(3):
   if i!=j:
    q=a[i][j];a[i]=[x-q*y for x,y in zip(a[i],a[j])]
 return tuple(row[-1] for row in a)
exact_vertices=set()
for triple in combinations(fs,3):
 p=solve3(triple)
 if p is not None and all(dot(f[:3],p)<=f[3] for f in fs):exact_vertices.add(p)
vertices=[i for i,p in enumerate(P) if rank([f[:3] for f in fs if dot(f[:3],p)==f[3]])==3]
assert exact_vertices=={P[i] for i in vertices}
print('vertices',[(i,P[i]) for i in vertices])
sets=[]
for z in P:
 active=[f for f in fs if dot(f[:3],z)==f[3]]
 face=tuple(i for i,p in enumerate(P) if all(dot(f[:3],p)==f[3] for f in active))
 if len(face)>1:sets.append(face)
sets=sorted(set(sets));print('faces',sets)
mat=[r for S in sets for r in relations(P,S)]
k=0;piv=[]
for j in range(len(P)):
 i=next((i for i in range(k,len(mat)) if mat[i][j]),None)
 if i is None:continue
 mat[k],mat[i]=mat[i],mat[k];a=mat[k][j];mat[k]=[x/a for x in mat[k]]
 for i in range(len(mat)):
  if i!=k:
   a=mat[i][j]
   if a:mat[i]=[x-a*y for x,y in zip(mat[i],mat[k])]
 piv.append(j);k+=1
print('rank',k,'Ldim',len(P)-k)
assert len(P)-k==5
g=[F(v) for v in [0,0,0,3,3,3,6,0,0,0,1,0,0]]
assert all(dot(row,g)==0 for S in sets for row in relations(P,S))
assert rank([[1]+list(p)+[g[i]] for i,p in enumerate(P)])==5
for j in range(len(P)):
 if j in piv:continue
 g=[F(0)]*len(P);g[j]=1
 for i,l in enumerate(piv):g[l]=-mat[i][j]
 print('g',g)
 print('nonaff',rank([[1]+list(p)+[g[i]] for i,p in enumerate(P)])>4)
