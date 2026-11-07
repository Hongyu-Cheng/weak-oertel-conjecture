from fractions import Fraction as F
from itertools import combinations
h=F(8,5)
fibers=[(p,q,h+(h-1)*q) for q in (-1,0,1) for p in range(-4+3*q,5-3*q)]
j=1
lines=set((F(p-j),F(q),sign*w) for p,q,w in fibers for sign in(-1,1) if(p-j,q)!=(0,0))
points=set()
for (a,b,c),(d,e,f) in combinations(lines,2):
 det=a*e-b*d
 if det:
  aa,bb=(c*e-b*f)/det,(a*f-c*d)/det
  if aa>=0: points.add((aa,bb))
def mass(a,b):return sum(max(F(0),min(2*w,w+a*(p-j)+b*q)) for p,q,w in fibers)
xs=sorted({a for a,b in points}|{F(0)})
print('unique a:',len(xs))
for a in xs:
 bs={a*(p-j)+e*w for p,q,w in fibers if q==-1 for e in(-1,1)}|{-a*(p-j)+e*w for p,q,w in fibers if q==1 for e in(-1,1)}
 vals=[(mass(a,b),b) for b in bs]
 m=min(t[0] for t in vals)
 print(a, m, 'b',next(bb for vv,bb in sorted(vals) if vv==m))
