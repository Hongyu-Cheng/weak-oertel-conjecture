#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
checks=0
def ok(x):
 global checks
 assert x
 checks+=1

# Common boundary-square cone law: each of four line segments has mass1/4.
faces=[((F(-1),F(-1)),(F(1),F(-1))),((F(1),F(-1)),(F(1),F(1))),((F(1),F(1)),(F(-1),F(1))),((F(-1),F(1)),(F(-1),F(-1)))]
n1=[(F(5,2),F(7,4)),(F(-5,2),F(7,4)),(F(0),F(-7,4))]
n2=[(F(2),F(3,2)),(F(-2),F(3,2)),(F(0),F(-3,2))]
table={}
for P,Q in faces:
 cuts={F(0),F(1)}
 for a,b in n1+n2:
  v=a*P[0]+b*P[1];dv=a*(Q[0]-P[0])+b*(Q[1]-P[1])
  ok(dv!=0 or v!=0) # No entire face lies on a cap boundary.
  if dv and 0<-v/dv<1:cuts.add(-v/dv)
 cuts=sorted(cuts)
 for lo,hi in zip(cuts,cuts[1:]):
  t=(lo+hi)/2;X=(P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1]))
  states=[tuple(int(a*X[0]+b*X[1]>0) for a,b in ns) for ns in (n1,n2)]
  key=tuple(states);table[key]=table.get(key,F(0))+(hi-lo)/4
ok(sum(table.values())==1)
Bs=[]
for i in range(3):
 p=sum(v for (s,t),v in table.items() if s[i]);q=sum(v for (s,t),v in table.items() if t[i]);o=sum(v for (s,t),v in table.items() if s[i] and t[i])
 ok(p==q==F(1,2));ok(min(p,q)-o==([F(1,160),F(1,160),F(0)][i]))
 B=35*p+8*q-8*o;Bs.append(B)
 ok(B==([F(351,20),F(351,20),F(35,2)][i]))

hx=[F(1),F(5,2),F(3),F(5,2),F(1)];hy=[F(1),F(7,4),F(2),F(7,4),F(1)]
V=[4*x*y for x,y in zip(hx,hy)]
ok(V==[4,F(35,2),24,F(35,2),4]);ok(sum(V)==67)
selected={1,3,4}
expected_x=[(F(-1),F(5)),(F(-1),F(-5)),(F(-1),F(4))]
expected_y=[(F(-1,2),F(7,2)),(F(-1,2),F(-7,2)),(F(-1,2),F(5,2))]
for vals,exps in [(hx,expected_x),(hy,expected_y)]:
 for i in range(1,4):
  const=vals[i-1]-2*vals[i]+vals[i+1]
  vel=[-vals[j] if j in selected else F(0) for j in range(5)]
  rate=vel[i-1]-2*vel[i]+vel[i+1]
  ok((const,rate)==exps[i-1]);ok(const<0);ok(const+rate/F(7)<=0)
# Unit-normal normalization cancels in rho/S; raw circuit checks.
rho=[F(1),F(1),F(2)];normals=[(1,1),(-1,1),(0,-1)]
ok(all(sum(r*n[j] for r,n in zip(rho,normals))==0 for j in range(2)))
S=[2*sum(hy),2*sum(hy),2*sum(hx)];ok(S==[15,15,20])
ratios=[r/s for r,s in zip(rho,S)];theta=[v/sum(ratios) for v in ratios]
ok(theta==[F(2,7),F(2,7),F(3,7)])
ok(sum(t*b for t,b in zip(theta,Bs))==F(1227,70))
rate=2*sum(V[j] for j in selected);ok(rate==78)
ok(F(1227,70)<rate/2);ok(sum(theta)*39==rate/2)
# Shell coefficients and exact finite contraction area formula at rational values.
for eps in [F(1,100),F(1,20),F(1,8)]:
 tau=1-(1-eps)**2
 for j in selected:ok(V[j]-(1-eps)**2*V[j]==tau*V[j])
# Relations and barycentric output diagonal maps.
ok(F(1,2)*(-1)+F(1,2)==0);ok(F(2,3)*(-1)+F(1,3)*2==0)
ok(F(2,3)*F(5,2)+F(1,3)==2)
ok(F(2,3)*F(7,4)+F(1,3)==F(3,2))
# Genuine selected-menu switch.
Sprime=[F(4),F(4),F(6)]
rprime=[r/s for r,s in zip(rho,Sprime)]
tprime=[r/sum(rprime) for r in rprime]
ok(tprime==[F(3,10),F(3,10),F(2,5)])
ok(sum(t*b for t,b in zip(tprime,Bs))==F(1753,100))
ok(F(1753,100)<39<43)
for eps in [F(0),F(1,100),F(1,20),F(1,8),F(1,7)]:
 tau=1-(1-eps)**2
 Meps=67-39*tau;Qeps=F(67,2)-F(43,2)*tau
 ok(Qeps==Meps/2-2*tau);ok(Qeps>F(51,4))
 for z,x,y in zip(range(-2,3),hx,hy):
  if z:ok(10*abs(z)>x+y)
ok(F(24,2)+F(35,2)+4==F(67,2))
ok(2*(F(35,2)+4)==43)
print(f'PASS: {checks} exact checks. Common shell three-bit signature cells:')
for (s,t),v in sorted(table.items()):print(''.join(map(str,s)),''.join(map(str,t)),str(v))
print('Critical response weights:',theta,'adaptive weighted lower bound:',F(1227,70),'required threshold:',39)
