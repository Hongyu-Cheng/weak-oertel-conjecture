from fractions import Fraction as F
w=list(map(F,[2,16,17,1]));M=sum(w)
assert all(w[i+1]-w[i]>=w[i+2]-w[i+1] for i in range(2))
rows=[(1,[F(2),F(31,4),F(2),F(0)],[F(7,4),F(33,4),F(7,4),F(0)],F(-31,4),F(23,4),F(15,2),F(753,8),F(-2595,376)),(2,[F(0),F(1),F(8),F(1)],[F(0),F(1,2),F(9),F(1,2)],F(-8),F(-7),F(-15,2),F(351,4),F(-123,16))]
for j,p,q,lam,nu,omega,score,y in rows:
 assert all(0<=v<=wi for mass in [p,q] for v,wi in zip(mass,w))
 assert sum(p)==sum(q)>0
 assert all(sum(F(i-j)*mass[i] for i in range(4))==0 for mass in [p,q])
 for mass,grad,offset,slope in [(p,[-v for v in p],lam,nu),(q,[wi-v for wi,v in zip(w,q)],-lam,omega)]:
  residual=[g-offset-slope*(i-j) for i,g in enumerate(grad)]
  for v,wi,r in zip(mass,w,residual):
   assert (r==0) or (r>0 and v==wi) or (r<0 and v==0)
 A=-sum(v*v for v in p)/2; B=sum(wi*v-v*v/2 for wi,v in zip(w,q))
 assert A+B==score and (A-B)/(2*sum(p))==y
 tilt=F(-100) if j==1 else F(100)
 caps=[max(F(0),min(wi,-y+tilt*(i-j))) for i,wi in enumerate(w)]
 assert sum(caps)<M/4
 assert sum(caps)==(F(3347,376) if j==1 else F(139,16))
assert F(753,8)>F(351,4)>1>F(1,4)
assert sum(w[:2])==sum(w[2:])==M/2
print('PASS: exact QP certificates, unique selector, median eligibility and bad caps')
