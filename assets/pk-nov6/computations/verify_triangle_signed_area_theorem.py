"""Exact checks of sharpness and the new wing/application constants.
The general geometric and matching proofs are in the companion notes.
"""
from fractions import Fraction as F
from itertools import combinations

def clip(P,a,b):
 if not P:return []
 out=[]
 for p,q in zip(P,P[1:]+P[:1]):
  s=sum(v*w for v,w in zip(a,p))-b;t=sum(v*w for v,w in zip(a,q))-b
  if s>=0:out.append(p)
  if s*t<0:out.append(tuple(x+s/(s-t)*(y-x) for x,y in zip(p,q)))
 return out

def area(P):return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(P,P[1:]+P[:1])))/2 if P else F(0)

K=[(F(0),F(0)),(F(3),F(0)),(F(0),F(3))]
caps=[((-1,-1),F(-2)),((1,0),F(1)),((0,1),F(1))]

def overlap(P):return sum(area(clip(clip(P,*caps[i]),*caps[j])) for i,j in combinations(range(3),2))
def J(P):return area(P)-3*overlap(P)

square=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
trap=[(F(0),F(0)),(F(3),F(0)),(F(2),F(1)),(F(0),F(1))]
assert area(K)==F(9,2) and overlap(K)==F(3,2) and J(K)==0
assert area(square)==1 and overlap(square)==0 and J(square)==1
assert area(trap)==F(5,2) and overlap(trap)==F(1,2) and J(trap)==1
assert F(2,9)*area(K)==1

for cn in range(1,9):
 for cd in range(1,7):
  c=F(cn,cd)
  for mn in range(10):
   M=F(mn,7)
   positive_bound=F(5,2)*M*c*c
   negative_constructed=F(3,2)*M*c*c
   assert negative_constructed==F(3,5)*positive_bound
  for W in [F(0),F(1,10),F(2),F(17,3)]:
   E=c*c+W;Dlower=c*c+F(3,5)*W
   assert E-2*Dlower==-c*c-W/5<0

for k in [F(1,24),F(1),F(37,3)]:
 for b in [F(1,100),F(1),F(17,2)]:
  a=k+b
  neighbor=4*(a/4-F(2,9)*k)/3
  assert neighbor==b/3+k/27>b/3
  assert b+min(b,neighbor)>F(4,3)*b
  assert F(4,3)*k+b+min(b,neighbor)>F(4,3)*a
print('PASS: exact equality bodies, wing constants, and arbitrary-endpoint matching constants.')
