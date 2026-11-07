from fractions import Fraction as Q
from itertools import combinations
from math import prod
import sympy as s
checks=0
def ck(x):
 global checks
 assert x;checks+=1

def cdf_b(x,t=Q(0)):
 d=len(x)-1;F=Q(0);Ft=Q(0);grad=[Q(0)]*(d+1)
 for i in range(d+1):
  if x[i]>=t:continue
  z=(t-x[i])**d/prod(x[j]-x[i] for j in range(d+1) if i!=j)
  F+=z;Ft+=d*z/(t-x[i])
  for j in range(d+1):
   grad[j]+=z*(-d/(t-x[i])+sum(1/(x[l]-x[i]) for l in range(d+1) if i!=l)) if i==j else -z/(x[j]-x[i])
 return F,tuple(-g/Ft for g in grad),Ft

def facet_cap(a):
 P=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(0),Q(1))]
 val=lambda p:a[0]+(a[1]-a[0])*p[0]+(a[2]-a[0])*p[1]
 R=[]
 for p,q in zip(P,P[1:]+P[:1]):
  f,g=val(p),val(q)
  if f<=0:R.append(p)
  if (f<0<g) or (g<0<f):
   r=f/(f-g);R.append(tuple(p[j]+r*(q[j]-p[j]) for j in range(2)))
 if not R:return Q(0),None
 twice=sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(R,R[1:]+R[:1]))
 if not twice:return Q(0),None
 c=[sum((p[j]+q[j])*(p[0]*q[1]-p[1]*q[0]) for p,q in zip(R,R[1:]+R[:1]))/(3*twice) for j in range(2)]
 return abs(twice),(1-c[0]-c[1],c[0],c[1])

cases=0
for a in combinations([Q(i) for i in range(-7,8) if i],4):
 if min(a)>0 or max(a)<0:continue
 F,b,Ft=cdf_b(a);t=3*F/Ft;x=tuple(v+t for v in a)
 if min(x)<=0:continue
 cases+=1
 ck(sum(b)==1 and sum(x[j]*b[j] for j in range(4))==t)
 for j in range(4):
  ids=[l for l in range(4) if l!=j]
  Fj,cj=facet_cap([a[l] for l in ids])
  ck(Fj>0 and Fj==x[j]*F/t)
  for l,v in zip(ids,cj):
   ck(v==(t+3*(x[j]-x[l])*b[l])/(3*x[j]))
   ck(v>0)
  ck(sum(x[l]*v for l,v in zip(ids,cj))<t)
  ck(3*sum(x[l]**2*b[l] for l in range(4))>t*sum(x[l] for l in ids))

# Missing-entry derivative after raising to the d-th power.
e,b,c,z=s.symbols('e b c z',positive=True)
ck(s.simplify(s.diff(c*(b+e)-b*e,e)-b*c*(2/b-1/b-1/c))==0)
leading=b**3*(c-e)*(z-e)/(b-e)**2
ck(s.simplify(s.diff(leading,e).subs(e,0)-b*c*z*(3/b-1/b-1/c-1/z))==0)

# Exact one-full-row stationary saddle.
X=[[Q(1,5),Q(1,5),Q(3,5),Q(3,5)],[Q(0)]*4,[Q(2,5),Q(2,5),Q(0),Q(2,5)],[Q(2,5),Q(2,5),Q(2,5),Q(0)]]
for j in range(4):ck(sum(X[i][j] for i in range(4))==1)
t=Q(2,5);F=Q(1,2);B=[Q(1,4)]*4;mu=[Q(0),Q(0),Q(1,10),Q(1,10)]
for j in range(4):
 ck((1-X[0][j])*B[j]/(1-t)<=Q(1,3))
 ck(B[j]*(1-X[0][j])==sum(mu)-mu[j])
ck((1-X[0][0])*B[0]/(1-t)==Q(1,3))
ck(F>Q(27,64))
u=s.symbols('u');L=s.Rational(2,5)
Fuu=s.diff(2*u*(1-u)**3/L,u)/L
ck(Fuu.subs(u,s.Rational(1,2))==-s.Rational(25,8))
full=-s.Rational(2,5)*Fuu.subs(u,s.Rational(1,2))/(3*s.Rational(1,2))
ck(full==s.Rational(5,6))
fund=s.Rational(3,10)*(1-s.Rational(25,16)*e**2)**s.Rational(1,3)
ck(s.diff(fund,e,2).subs(e,0)==-s.Rational(5,16))
ck(full+2*s.diff(fund,e,2).subs(e,0)==s.Rational(5,24))
print('PASS',checks,'exact checks;',cases,'regular full-positive stationary cuts with actual clipped facet-centroid verification')
