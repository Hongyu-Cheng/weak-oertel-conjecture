from fractions import Fraction as F
from math import comb
checks=0
def ck(p,msg):
 global checks
 assert p,msg
 checks+=1
# The exact cone realizes the complete binomial formula in every tested d.
for d in range(2,13):
 for r in [F(1,5),F(1,2),F(1),F(3,2),F(4)]:
  P=F(7,3);U=P*r**(d-1)/d
  expansion=P*sum(F(comb(d-1,p),p+1)*r**p for p in range(d))
  closed=P*((1+r)**d-1)/(d*r)
  ck(expansion==closed,'exact full binomial cone identity')
  ck(expansion>=U+P,'nonnegative dimensional reserve')
  if d==3:ck((expansion-U-P)**2==3*U*P,'exact three-dimensional cone reserve')
# Exact moment integrals for several concave piecewise affine sections.
def moment(vals,p):
 out=F(0)
 for x,y in zip(vals,vals[1:]):
  out+=x**p if x==y else (y**(p+1)-x**(p+1))/((p+1)*(y-x))
 return out
for vals in [[F(0),F(2),F(3),F(3),F(0)],
             [F(1),F(3),F(4),F(4),F(2)],
             [F(0),F(1),F(2),F(3)],
             [F(4),F(3),F(2),F(1)]]:
 L=F(len(vals)-1)
 ck(all(vals[j+1]-vals[j]>=vals[j+2]-vals[j+1] for j in range(len(vals)-2)), 'section concavity')
 for m in range(1,9):
  im=moment(vals,m)
  for p in range(1,m+1):
   ip=moment(vals,p)
   ck(((p+1)*ip/L)**m>=((m+1)*im/L)**p,'root-free concave moment inequality')
# A certified formal menu shows that the listed scalar consequences
# do not by themselves prove the d=3 closure. It is NOT an actual body.
g=F(27,64);kap=F(10,27);a=F(1,80);b=F(1);k=F(99,100);Q=F(4223,10000)
roots=[F(2,5),F(3,4),F(7,8),F(8,9)]
t=[r**3 for r in roots];U=[a*x for x in t]
P=[F(3,10),F(309,100),F(601,200),F(601,200)]
H=[4*p/3 for p in P];q=[Q-u for u in U]
ck(U==sorted(U) and all(0<u<a for u in U),'proper positive formal caps')
ck(Q<g*(a+b+k)/2,'formal mass is strictly below proposed target')
ck(2*max(a,b,k)<a+b+k,'formal strict no-heavy')
Fprof=U[0]+U[1]+kap*U[2]
ck(k<=Q/g-Fprof,'middle cap profile')
ck(a<=U[3]+U[2]+kap*U[1],'opposite cap profile')
ck(Fprof<a,'positive two-residual overlap budget')
ck(P[2]+P[3]>3*b,'shared two-residual support budget')
for u,p in zip(U,P):
 spare=8*Q-9*u-p
 ck(spare>0 and spare*spare>3*u*p,'strict full d3 extrusion bound')
ck(sum(p*u for p,u in zip(P,U))>4*b*a,'strict weighted centroid incidence')
G=[1+x/2-F(3,4)/r for x,r in zip(t,roots)]
ck(sum(h*gg for h,gg in zip(H,G))>4,'coupled residual-moment condition')
X=sum(P)-3*b
spare=8*k-a-b-X
ck(spare>0 and spare*spare>3*a*X,'strict global AF binomial bound')
ck((X/(3*b))**3>a/b,'global first mixed-volume minimum')
ck(all(sum(P)-p>3*b for p in P),'each proper residual support condition')
# A nonnegative abstract incidence measure meets all memberships exactly.
single4=2*a-sum(U)
edge14=U[0]
d2=U[1];d3=U[2];d4=U[3]-single4-edge14
edge23=(d2+d3-d4)/2
edge24=(d2+d4-d3)/2
edge34=(d3+d4-d2)/2
patterns=[((3,),single4),((0,3),edge14),((1,2),edge23),((1,3),edge24),((2,3),edge34)]
ck(all(w>0 for inds,w in patterns),'positive formal membership masses')
ck(sum(w for inds,w in patterns)==a,'membership total mass')
for i in range(4):ck(sum(w for inds,w in patterns if i in inds)==U[i],'membership marginal')
for inds,w in patterns:ck(sum(P[i] for i in inds)>3*b,'every used pattern passes actual support obstruction')
# The above certificate checks necessary scalar consequences only.
print(f'{checks} exact rational checks passed.')
print('formal target gap =',g*(a+b+k)/2-Q)
print('global AF squared slack =',spare*spare-3*a*X)
print('residual-moment slack =',sum(h*gg for h,gg in zip(H,G))-4)
print('formal incidence atoms =',[(inds,str(w)) for inds,w in patterns])
