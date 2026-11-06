from itertools import combinations
from fractions import Fraction
import random
import numpy as np
from scipy.optimize import linprog
ns={};exec(open('./parity-center-search.py').read().split('random.seed')[0],ns)
hull=ns['hull'];points_in=ns['points_in'];cross=ns['cross']

def pair(z,a,b):
 return cross(z,a,b)==0 and (a[0]-z[0])*(b[0]-z[0])+(a[1]-z[1])*(b[1]-z[1])<=0
def triple(z,a,b,c):
 ss=[cross(a,b,z),cross(b,c,z),cross(c,a,z)]
 return (all(s>=0 for s in ss) or all(s<=0 for s in ss)) and cross(a,b,c)!=0
def edges(pts,z):
 ids=[i for i,p in enumerate(pts) if p!=z]
 pp=[e for e in combinations(ids,2) if pair(z,pts[e[0]],pts[e[1]])]
 pset={frozenset(e) for e in pp}
 tt=[e for e in combinations(ids,3) if not any(frozenset(p) in pset for p in combinations(e,2)) and triple(z,*[pts[i] for i in e])]
 return [(pts.index(z),)]+pp+tt
def dual(pts,z,weights):
 es=edges(pts,z)
 mat=np.zeros((len(es),len(pts)))
 for j,e in enumerate(es):mat[j,list(e)]=-1
 result=linprog(weights,A_ub=mat,b_ub=-np.ones(len(es)),bounds=(0,None),method='highs')
 vals=[Fraction(float(v)).limit_denominator(360) for v in result.x]
 if not all(sum(vals[i] for i in e)>=1 for e in es):raise RuntimeError('bad rationalization')
 obj=sum(Fraction(w)*v for w,v in zip(weights,vals))
 return obj,vals

if __name__=='__main__':
 pts=[(-3,-1),(-2,0),(-1,1),(-1,2),(0,1),(0,2),(1,2),(1,3),(2,3),(3,3)]
 print('known polygon',[(z,dual(pts,z,[1]*len(pts))) for z in pts],flush=True)
 random.seed(18123)
 for it in range(10000):
  h=hull([(random.randrange(-4,5),random.randrange(-4,5)) for _ in range(random.randrange(3,8))])
  if len(h)<3:continue
  pts=points_in(h)
  if not 5<=len(pts)<=24:continue
  weights=[1]*len(pts) if it%2==0 else [random.randrange(1,11) for _ in pts]
  target=Fraction(sum(weights),4)
  cert=[]
  for z in pts:
   obj,vals=dual(pts,z,weights)
   if obj>=target:break
   cert.append((z,obj,vals))
  else:
   print('COUNTEREXAMPLE',h,'points',pts,'weights',weights,'target',target,'certificate',cert,flush=True)
   break
  if it%100==0:print('checked',it,flush=True)
 else:print('none found',flush=True)
