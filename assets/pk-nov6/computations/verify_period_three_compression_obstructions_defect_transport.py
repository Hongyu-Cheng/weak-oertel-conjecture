"""Exact actual-body certificate; no floating point computations."""
from fractions import Fraction as F
import sympy as s
checks=0
def ck(v):
 global checks
 assert v
 checks+=1
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def sub(p,q):return (p[0]-q[0],p[1]-q[1])
def dot(p,q):return p[0]*q[0]+p[1]*q[1]
def area(P):return abs(sum(det(p,q) for p,q in zip(P,P[1:]+P[:1])))/2
def clip(P,n):
 out=[]
 for p,q in zip(P,P[1:]+P[:1]):
  a,b=dot(p,n),dot(q,n)
  if a>=0:out.append(p)
  if a*b<0:
   t=a/(a-b);out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
 return out
e=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def data(P):
 R=[]
 for v in e:
  vals=[]
  for p,q in zip(P,P[1:]+P[:1]):
   h=sub(q,p);D=det(v,h)
   if D:
    r=det(p,h)/D;t=det(p,v)/D
    if r>0 and 0<=t<=1:vals.append(r)
  ck(len(set(vals))==1);R.append(vals[0])
 W=[area(clip(clip(P,(-a[1],a[0])),(b[1],-b[0]))) for a,b in zip(e,e[1:]+e[:1])]
 return R,W
def compressed(R,W):
 c=[1/(2*w) for w in W];N=s.zeros(3)
 for i in range(3):
  N[i,i]=R[i]**2*(c[(i-1)%6]+c[i])+R[i+3]**2*(c[i+2]+c[i+3])-2
  j=(i+1)%3
  N[i,j]=N[j,i]=c[i]*R[i]*R[(i+1)%6]+c[i+3]*R[i+3]*R[(i+4)%6]-2
 return N
P=[(F(87,100),F(-49,100)),(F(-1,200),F(1,100)),(F(-1,200),F(-23,200))]
ck(all(det(sub(q,p),(-p[0],-p[1]))>0 for p,q in zip(P,P[1:]+P[:1])))
R,W=data(P)
ck(R==[F(1,80),F(1,140),F(1,200),F(1,200),F(41,350),F(41,200)])
ck(W==[F(1,22400),F(17,560000),F(1,80000),F(13,22400),F(1681,140000),F(3361,80000)])
k=area(P);Q=[area(clip(P,n)) for n in [(1,0),(0,1),(-1,-1)]]
sigma=[R[1]+R[4],R[0]+R[3],R[2]+R[5]]
M=sum(q/z for q,z in zip(Q,sigma))
f2=[4*k*q/(z*M)**2 for q,z in zip(Q,sigma)]
ck(f2==[F(49,16),F(1,4),F(1,4)])
ck(sum(f2)+F(7,16)==4)
N=compressed(R,W)
ck(N==s.Matrix([[s.Rational(844802,1092325),s.Rational(-161,325),s.Rational(-6517,6722)],[s.Rational(-161,325),s.Rational(65226,5525),s.Rational(-7,17)],[s.Rational(-6517,6722),s.Rational(-7,17),s.Rational(379827,228548)]]))
ck([N[:j,:j].det() for j in [1,2,3]]==[s.Rational(844802,1092325),s.Rational(164990791,18569525),s.Rational(9338175,2971124)])
ck((F(1,200)*F(23,200)*F(19,50))/(F(1,200)*F(1,200)*F(49,100))==F(874,49))
T=[(F(2),F(-1)),(F(-1),F(2)),(F(-1),F(-1))]
R,W=data(T);ck(R==[F(1)]*6);ck(W==[F(1,2),F(1)]*3)
ck(compressed(R,W)==s.Matrix([[1,s.Rational(-1,2),s.Rational(-1,2)],[s.Rational(-1,2),1,s.Rational(-1,2)],[s.Rational(-1,2),s.Rational(-1,2),1]]))
ck(3*F(2,3)-3*F(4,3)==-2)
print(f'PASS: {checks} exact actual geometry and matrix checks')
