"""Exact standard-library certificate; no random or numerical geometry input."""
from itertools import product, permutations
J=4
e=[tuple(int(i==j) for i in range(J)) for j in range(J)]
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
levels=[{e[0]}]
for ell in range(3): levels.append({sub(scale(2,k),e[c]) for k in levels[-1] for c in (1,2,3)})
S=set(e[1:]).union(*levels)
assert list(map(len,levels))==[1,3,9,27] and len(S)==43
for k in S:
 assert sum(k)==1 and sum(x>0 for x in k)==1
 odd=[i for i,x in enumerate(k) if x%2]
 assert len(odd)==1
 c=odd[0];par=tuple(x//2 for x in add(k,e[c]))
 assert par in S and dot(k,k)>=dot(e[c],e[c])
 if k not in e:
  assert dot(k,k)>1 and k[0]>=2 and par[0]==k[0]//2
  m=[-k[i] for i in range(1,4)]
  for i,j in ((0,1),(0,2),(1,2)):assert m[i]&m[j]==0
  assert tuple(-par[i] for i in range(1,4))==tuple(x//2 for x in m)
 # Unit linear radius, positive powers, exact radius edge, and root domination.
 assert sum(k)==sum(par)==sum(e[c])==1
rows=[
 ((0,1,0,0),(1,0,0),1),
 ((1,0,0,0),(1,1,1),4),
 ((2,-1,0,0),(-2,11,11),5),
 ((4,-3,0,0),(-11,12,12),4),
 ((4,-2,-1,0),(-2,1,10),7),
 ((8,-7,0,0),(-12,-11,-11),1),
 ((8,-6,-1,0),(-12,-11,-10),2),
 ((8,-5,-2,0),(-12,-11,-9),3),
 ((8,-4,-3,0),(-12,-11,-8),4),
 ((8,-4,-2,-1),(-12,-10,-9),7),
]
covered=set()
for k,u,count in rows:
 assert k in S and any(u)
 b=dot(u,k[1:]);parts=[]
 for group in [set(e[1:])]+levels:
  parts.append(sum(dot(u,l[1:])>=b for l in group))
 assert sum(parts)==count
 formula=sum(u[i]>=b for i in range(3))+int(0>=b)
 for ell in (1,2,3):
  formula+=sum(-sum(2**h*u[word[h]] for h in range(ell))>=b for word in product(range(3),repeat=ell))
 assert formula==count
 print(k,u,'threshold',b,'parts',parts,'total',count)
 for perm in permutations(range(3)):
  kp=(k[0],)+tuple(k[1+i] for i in perm)
  up=tuple(u[i] for i in perm)
  assert kp in S
  assert sum(dot(up,sub(l[1:],kp[1:]))>=0 for l in S)==count
  covered.add(kp)
assert covered==S and max(x[2] for x in rows)==7 and 4*7<43
# Exact missing lattice point in the standard-square projection.
rootbase=((0,0),(1,0),(0,1),(1,1))
def project(k):return tuple(sum(k[i]*rootbase[i][j] for i in range(4)) for j in range(2))
P={project(k) for k in S}
assert (-2,-2) not in P
assert (0,0) in P and (-7,0) in P and (0,-7) in P
# (-2,-2)=3/7*(0,0)+2/7*(-7,0)+2/7*(0,-7).
assert tuple(3*(0,0)[i]+2*(-7,0)[i]+2*(0,-7)[i] for i in range(2))==(-14,-14)
print('PASS: coefficient conditions, all ten orbit caps, 43-point coverage, and projection gap')
