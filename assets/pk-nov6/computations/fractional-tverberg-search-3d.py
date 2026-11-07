from itertools import combinations,product
from fractions import Fraction
import random
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def contains(z,ps):
 if len(ps)==1:return z==ps[0]
 a,b=ps[:2]
 if len(ps)==2:return cross(sub(a,z),sub(b,z))==(0,0,0) and dot(sub(a,z),sub(b,z))<=0
 c=ps[2];normal=cross(sub(b,a),sub(c,a))
 if len(ps)==3:
  if normal==(0,0,0) or dot(sub(z,a),normal):return False
  signs=[dot(cross(sub(b,a),sub(z,a)),normal),dot(cross(sub(c,b),sub(z,b)),normal),dot(cross(sub(a,c),sub(z,c)),normal)]
  return all(s>=0 for s in signs)
 d=ps[3];D=det(sub(b,a),sub(c,a),sub(d,a))
 if D==0:return False
 vals=[det(sub(b,z),sub(c,z),sub(d,z)),det(sub(z,a),sub(c,a),sub(d,a)),det(sub(b,a),sub(z,a),sub(d,a)),det(sub(b,a),sub(c,a),sub(z,a))]
 return all(v*D>=0 for v in vals)

def edges(vs,z):
 es=[]
 for k in range(1,5):
  for e in combinations(range(len(vs)),k):
   if any(set(ee).issubset(e) for ee in es):continue
   if contains(z,[vs[i] for i in e]):es.append(e)
 return es
def solve(vs,z):
 es=edges(vs,z)
 if any(not set(a).intersection(b) for a,b in combinations(es,2)):
  return Fraction(2),None
 mat=np.zeros((len(es),len(vs)))
 for i,e in enumerate(es):mat[i,list(e)]=-1
 r=linprog(np.ones(len(vs)),A_ub=mat,b_ub=-np.ones(len(es)),bounds=(0,1),method='highs')
 vals=[Fraction(float(v)).limit_denominator(1000) for v in r.x]
 if not all(sum(vals[i] for i in e)>=1 for e in es):raise RuntimeError('bad rationalization')
 return sum(vals),vals

random.seed(44271)
for it in range(3000):
 raw=list(set(tuple(random.randrange(-2,3) for _ in range(3)) for j in range(random.randrange(11,24))))
 if len(raw)<4:continue
 try:h=ConvexHull(np.array(raw))
 except Exception:continue
 vs=[raw[i] for i in h.vertices]
 if not 9<=len(vs)<=15:continue
 pts=[p for p in product(range(-2,3),repeat=3) if np.all(np.dot(h.equations[:,:3],p)+h.equations[:,3]<=1e-8)]
 avg=np.mean(np.array(vs),axis=0)
 pts.sort(key=lambda p:sum((x-y)**2 for x,y in zip(p,avg)))
 target=Fraction(len(vs),8)
 cert=[]
 for z in pts:
  val,dual=solve(vs,z)
  if val>=target:break
  cert.append((z,val,dual))
 else:
  print('COUNTEREXAMPLE vertices',vs,'lattice points',pts,'target',target,'cert',cert,flush=True)
  break
 if it%20==0:print('checked',it,'vertices',len(vs),'points',len(pts),flush=True)
else:print('none found',flush=True)
