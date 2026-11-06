from fractions import Fraction as F
from itertools import combinations
h=F(8,5)
fibers=[(p,q,h+(h-1)*q) for q in (-1,0,1) for p in range(-4+3*q,5-3*q)]
for j in (0,1,-1,2):
 lines=set((F(p-j),F(q),sign*w) for p,q,w in fibers for sign in(-1,1) if(p-j,q)!=(0,0))
 points=set()
 for (a,b,c),(d,e,f) in combinations(lines,2):
  det=a*e-b*d
  if det: points.add(((c*e-b*f)/det,(a*f-c*d)/det))
 def mass(a,b):return sum(max(F(0),min(2*w,w+a*(p-j)+b*q)) for p,q,w in fibers)
 vals=[(mass(a,b),a,b) for a,b in points]
 m=min(t[0] for t in vals)
 print(j, 'min',m,'T',13*h,'at', [v for v in vals if v[0]==m][:12],len(points))
