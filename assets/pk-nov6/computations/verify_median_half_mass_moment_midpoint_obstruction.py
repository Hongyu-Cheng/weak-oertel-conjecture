from fractions import Fraction as F
w=list(map(F,[9,75,140,200,25]));z=list(range(5));j=3;M=sum(w);t=M/2
assert [w[i+1]-w[i] for i in range(4)]==[66,65,60,-175]
assert M==449 and t==F(449,2) and max(w)<t
eligible=[k for k in z if min(sum(w[:k+1]),sum(w[k:]))>=t]
assert eligible==[3] and min(sum(w[:4]),sum(w[3:]))==225>t
m=[F(0),F(0),F(25),F(349,2),F(25)]
assert sum(m)==t and sum((i-j)*v for i,v in zip(z,m))==0
assert all(0<=v<=wi for v,wi in zip(m,w))
for gradient,lam,nu,expected in [([-x for x in m],-F(349,2),-F(299,2),[-F(274),-F(249,2),0,0,299]),([wi-x for wi,x in zip(w,m)],F(51,2),-F(179,2),[-285,-F(259,2),0,0,64])]:
 residual=[g-lam-nu*(i-j) for i,g in zip(z,gradient)]
 assert residual==expected
 for mi,wi,r in zip(m,w,residual):
  if mi==0:assert r<=0
  elif mi==wi:assert r>=0
  else:assert r==0
upper=-sum(x*x for x in m)/(2*t)
lower=-sum(wi*x-x*x/2 for wi,x in zip(w,m))/t
y=(upper+lower)/2;length=upper-lower
assert (lower,upper)==(-F(185399,1796),-F(126801,1796))
assert y==-F(39025,449) and length==F(29299,898)>0
assert -w[j]<y<0
thresholds=[y-100*(i-j) for i in z]
assert all(thresholds[i]>0 for i in [0,1,2]) and thresholds[4]<-w[4]
cap=-y+w[4]
assert cap==F(50250,449) and M/4-cap==F(601,1796)>0
escape=-F(175,2)
assert min(140,25,-2*escape)==25
escape_cap=-escape+25
assert escape_cap==F(225,2) and escape_cap/M==F(225,898)>F(1,4)
print('PASS: convex fibers, unique strict median, exact source optimizers, positive interval, bad cap, and explicit deep escape point.')
