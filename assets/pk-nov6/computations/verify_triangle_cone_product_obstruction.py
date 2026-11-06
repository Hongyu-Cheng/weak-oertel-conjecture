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

caps=[((-1,-1),F(-2)),((1,0),F(1)),((0,1),F(1))]
for epsilon in [F(1,2),F(1,10),F(1,100)]:
 Q=[(F(0),F(0)),(F(3),F(0)),(1-epsilon,1+2*epsilon)]
 ds={(i,j):area(clip(clip(Q,*caps[i]),*caps[j])) for i,j in combinations(range(3),2)}
 es=[area(clip(Q,*caps[i]))-sum(ds[tuple(sorted((i,j)))] for j in range(3) if j!=i) for i in range(3)]
 ratio=es[0]*es[1]*es[2]/(ds[(0,1)]*ds[(0,2)]*ds[(1,2)])
 js=[es[i]-2*sum(ds[tuple(sorted((i,j)))] for j in range(3) if j!=i) for i in range(3)]
 print('epsilon',epsilon,'E',es,'D',ds,'ratio',ratio,'fixed signed caps',js)
 assert ratio>8
