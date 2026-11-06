"""Independent exact polygon boundary integration for the support-gap identities."""
from fractions import Fraction as F
checks=0
def ck(v):
 global checks
 assert v
 checks+=1

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def area(poly):return sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1]))/2

def clip(poly,v,c):
 out=[];cuts=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  fa=dot(v,a)-c;fb=dot(v,b)-c
  if fa>=0:out.append(a)
  if fa*fb<0:
   p=tuple(a[j]+fa/(fa-fb)*(b[j]-a[j]) for j in range(2))
   out.append(p);cuts.append(p)
 return out,cuts

def edge_fraction(a,b,v,c):
 fa=dot(v,a)-c;fb=dot(v,b)-c
 if fa>=0 and fb>=0:return F(1)
 if fa<=0 and fb<=0:return F(0)
 return fa/(fa-fb) if fa>0 else fb/(fb-fa)

g=(F(1,3),F(1,3));K=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
A=[(F(1,6),F(1,4)),(F(1,2),F(1,4)),(F(1,2),F(5,12)),(F(1,6),F(5,12))]
fibers={-1:A,0:K,1:A}
vectors=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]
thresholds=[dot(v,g) for v in vectors]
theta=[F(4,11),F(3,11),F(4,11)]
ck(area(K)==F(1,2));ck(area(A)==F(1,18));ck(sum(theta)==1)
for p in A:ck(min(p)>0 and sum(p)<1)
Q=F(5,18);V=F(11,18)
capmass=[F(0)]*3;S=[F(0)]*3;sectionmom=[[F(0)]*3 for _ in range(3)]
C={};T={};B={};sigmas={}
for z,poly in fibers.items():
 C[z]=F(0);T[z]=[F(0),F(0)];B[z]=F(0);sigmas[z]=[]
 for j,(v,c) in enumerate(zip(vectors,thresholds)):
  cut,ends=clip(poly,v,c)
  ck(len(ends)==2)
  sig=abs(ends[1][0]-ends[0][0])/abs(v[1]) if v[1] else abs(ends[1][1]-ends[0][1])/abs(v[0])
  sigmas[z].append(sig)
  q=area(cut);capmass[j]+=q;S[j]+=sig
  C[z]+=theta[j]*q;B[z]+=theta[j]*sig*c
  for l in range(2):T[z][l]+=theta[j]*sig*v[l]
  midpoint=(F(z),*(sum(e[l] for e in ends)/2 for l in range(2)))
  for l in range(3):sectionmom[j][l]+=sig*midpoint[l]
  ck(q==(F(2,9) if z==0 else F(1,36)))
ck(capmass==[Q]*3);ck(S==[F(1),F(4,3),F(1)])
ck(sigmas[-1]==[F(1,6),F(1,3),F(1,6)])
ck(sigmas[0]==[F(2,3)]*3);ck(sigmas[1]==sigmas[-1])
for j in range(3):
 for l,e in enumerate((F(0),*g)):ck(sectionmom[j][l]==S[j]*e)
ck(T[-1]==T[1]==[F(0),F(1,33)]);ck(T[0]==[F(0),F(-2,33)])
ck(sum(B.values())==0);ck(sum(C.values())==Q)
ck(B[-1]==B[1]==F(1,99));ck(B[0]==F(-2,99))
formal={z:2*C[z]+B[z]+max(dot(tuple(-a for a in T[z]),p) for p in poly) for z,poly in fibers.items()}
ck(formal[-1]==formal[1]==F(23,396));ck(formal[0]==F(16,33))
m=(F(1,3),F(1,4));r=(F(0),F(1));D=sub(r,m)
G=dot(T[-1],D);ck(G==F(1,44));ck(sum(formal.values())==2*Q+2*G==F(119,198))
# Direct edge integrals: outward normal times edge length is (dy,-dx).
J=F(0);Lp=F(0);Lm=F(0);den=F(0);num=F(0);base_den=F(0);base_num=F(0)
means=[]
for z,poly in fibers.items():
 own_den=F(0);own_num=F(0)
 for a,b in zip(poly,poly[1:]+poly[:1]):
  dx,dy=sub(b,a);N=(dy,-dx)
  radial=dot(N,sub(a,m))
  mean=sum(w*edge_fraction(a,b,v,c) for w,v,c in zip(theta,vectors,thresholds))
  correction=max(F(0),dot(N,D)) if z==0 else F(0)
  ck(radial>=correction)
  den+=radial-correction;num+=(radial-correction)*mean
  base_den+=radial;base_num+=radial*mean
  own_den+=radial;own_num+=radial*mean
  if z==0:
   means.append(mean);J+=correction;Lp+=correction*mean;Lm+=max(F(0),-dot(N,D))*mean
 if z!=0:
  ck(own_den==2*area(A));ck(own_num==formal[z]);ck(own_num/own_den==F(23,44))
ck(means==[F(16,33),F(14,33),F(14,33)])
ck(base_den==2*V);ck(base_num==2*Q)
ck(J==F(3,4));ck(Lp==F(7,22));ck(Lm==F(4,11));ck(Lm-Lp==2*G)
ck(den==2*V-J);ck(num==2*Q-Lp);ck(num/den==F(94,187)>F(4,9))
ck(F(23,44)>F(4,9));ck(F(16,33)>F(4,9));ck(Q/V==F(5,11))
# Middle-slack area measure at bottom normal, including exact endpoint vanishing.
n=(F(0),F(-1));hA=max(dot(n,p) for p in A);hK=max(dot(n,p) for p in K)
ck(hK-hA==F(1,4))
# Strict midpoint inclusion with completely zero support-slack measure.
for h in [F(1,100),F(1,3),F(1,2),F(99,100)]:
 M=[(h,F(0)),(F(1),F(0)),(F(0),F(1)),(F(0),h)]
 ck(F(0)<area(M)<area(K))
 for a,b in zip(K,K[1:]+K[:1]):
  dx,dy=sub(b,a);N=(dy,-dx)
  ck(max(dot(N,p) for p in M)==dot(N,a))
print(f'PASS: {checks} exact polygon cap, coarea, flux, support and potential checks')
