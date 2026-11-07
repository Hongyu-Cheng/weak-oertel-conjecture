from random import Random
r=Random(73291)
def hull(P):
 P=sorted(set(P))
 def cr(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
 L=[]
 for p in P:
  while len(L)>=2 and cr(L[-2],L[-1],p)<=0:L.pop()
  L.append(p)
 U=[]
 for p in P[::-1]:
  while len(U)>=2 and cr(U[-2],U[-1],p)<=0:U.pop()
  U.append(p)
 return L[:-1]+U[:-1]
def area(P):return abs(sum(x*y2-y*x2 for (x,y),(x2,y2) in zip(P,P[1:]+P[:1])))/2
def clip(P,a,b,c=0):
 R=[]
 for A,B in zip(P,P[1:]+P[:1]):
  f=a*A[0]+b*A[1]-c;g=a*B[0]+b*B[1]-c
  if f>=0:R.append(A)
  if (f<0<g) or (g<0<f):
   t=f/(f-g);R.append((A[0]+t*(B[0]-A[0]),A[1]+t*(B[1]-A[1])))
 return R
norms=[(1,0),(0,1),(-1,-1)]
for it in range(100000):
 P=hull([(r.randrange(-100,101),r.randrange(-100,101)) for k in range(r.randrange(3,10))])
 if len(P)<3:continue
 M=area(P);caps=[area(clip(P,*v))/M for v in norms]
 Es=[]
 for i in range(3):
  Q=P
  for j,(a,b) in enumerate(norms):Q=clip(Q,a if i==j else -a,b if i==j else -b)
  Es.append(area(Q)/M)
 if min(Es)>1e-5 and max(caps)<=.5+1e-8 and sum(Es)>.5*sum(caps)+1e-5:
  print('COUNTER',it,P,caps,Es,flush=True);break
else:print('NO COUNTER')
