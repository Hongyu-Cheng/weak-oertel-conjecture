"""Exact countercertificate to unrestricted diagonal quasiconvexity."""
from fractions import Fraction as F
checks=0
def ck(z):
 global checks
 assert z
 checks+=1
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def area(P):return abs(sum(det(p,q) for p,q in zip(P,P[1:]+P[:1])))/2
def clip(P,v):
 out=[]
 for p,q in zip(P,P[1:]+P[:1]):
  a,b=dot(p,v),dot(q,v)
  if a>=0:out.append(p)
  if a*b<0:
   t=a/(a-b);out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
 return out
normals=[(1,0),(0,1),(-1,-1)]
def data(t):
 P=[(7-17*t,-6+15*t),(F(1),F(-5)),(F(7),F(-6)),(F(2),F(4))]
 ck(all(det(sub(P[(i+1)%4],P[i]),sub(P[(i+2)%4],P[(i+1)%4]))>0 for i in range(4)))
 ck(all(det(sub(q,p),(-p[0],-p[1]))>0 for p,q in zip(P,P[1:]+P[:1])))
 k=area(P);Q=[];sigma=[]
 for v in normals:
  Q.append(area(clip(P,v)));Z=[]
  for p,q in zip(P,P[1:]+P[:1]):
   a,b=dot(p,v),dot(q,v)
   if a*b<0:
    u=a/(a-b);Z.append((p[0]+u*(q[0]-p[0]),p[1]+u*(q[1]-p[1])))
  ck(len(Z)==2)
  d=sub(Z[0],Z[1]);sig=abs(d[1]) if v==(1,0) else abs(d[0])
  sigma.append(sig)
 M=sum(q/z for q,z in zip(Q,sigma));f2=[4*k*q/(z*M)**2 for q,z in zip(Q,sigma)]
 return k,Q,sigma,f2
r=F(9353,10000)
for t in [F(9,10),F(1),F(11,10)]:
 k,Q,sigma,f2=data(t)
 S=sum(f2);P2=f2[0]*f2[1]*f2[2]
 A=4*r**3-r*S
 ck(A>0)
 ck(all(r*r>x/4 for x in f2))
 # det(rI-B)=(A-sqrt(P2))/4.
 if t==1:ck(A*A<P2)
 else:ck(A*A>P2)
 # No cubic violation: 4-S>0 and (4-S)^2>P2.
 ck(4-S>0);ck((4-S)**2>P2)
 print('t=',t,' k=',k,' Q=',Q,' sigma=',sigma,' f^2=',f2)
# Vertex signs are constant on the interval, since each affine endpoint value
# has the same nonzero sign.
for v in normals:
 ck(dot((7-17*F(9,10),-6+15*F(9,10)),v)*dot((7-17*F(11,10),-6+15*F(11,10)),v)>0)
print(f'PASS: {checks} exact checks')
