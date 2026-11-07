from fractions import Fraction as F

def cross(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(P):
 P=sorted(set(P));L=[]
 for p in P:
  while len(L)>1 and cross(L[-2],L[-1],p)<=0:L.pop()
  L.append(p)
 U=[]
 for p in reversed(P):
  while len(U)>1 and cross(U[-2],U[-1],p)<=0:U.pop()
  U.append(p)
 return L[:-1]+U[:-1]
def area(P):return abs(sum(x[0]*y[1]-x[1]*y[0] for x,y in zip(P,P[1:]+P[:1])))/2

def dot(n,p):return n[0]*p[0]+n[1]*p[1]
def clip(P,n,b):
 R=[]
 for x,y in zip(P,P[1:]+P[:1]):
  a=dot(n,x)-b;c=dot(n,y)-b
  if a>=0:R.append(x)
  if a*c<0:
   t=a/(a-c);R.append((x[0]+t*(y[0]-x[0]),x[1]+t*(y[1]-x[1])))
 return R
V=[(F(2),F(-1)),(F(-1),F(23,16)),(F(-1),F(-7,16))]
y=(F(-1,32),F(1,64));ns=[(1,0),(0,1),(-1,-1)]
for name,pts in [('triangle',V),('pentagon',V+[(F(1999,1000),F(-1)),(F(1999,1000),F(-999,1000))])]:
 P=hull(pts);k=area(P);qs=[area(clip(P,n,dot(n,y))) for n in ns];qsS=sorted(qs);pr=qsS[0]+qsS[1]+qsS[2]/4
 print(name,'P',P,'k',k,'theta',k/F(9,2),'qs',[q/k for q in qs],'profile',pr/k,'slacks',[F(128,279)-q/k for q in qs],1-pr/k)
 assert all(q/k<F(128,279) for q in qs)
 assert pr<k and k/F(9,2)<F(11,16)
