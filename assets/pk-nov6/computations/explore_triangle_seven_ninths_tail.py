import sympy as s
x,q=s.symbols('x q',real=True)
u=1-x;D=x*u*(1-2*x)
F=[s.Integer(1),1-q*q/(x*u),(u-q)**2/(u*(1-2*x)),s.Integer(0)]
def branch(t,xx):
 if t<=0:return 0
 if t<=xx:return 1
 if t<=1-xx:return 2
 return 3
for lo,hi in [(s.Rational(0),s.Rational(1,3)),(s.Rational(1,3),s.Rational(1,2))]:
 xx=(lo+hi)/2
 breaks=sorted([s.Integer(0),x,u,s.Rational(2,3),s.Rational(2,3)-x,x-s.Rational(1,3)],key=lambda v:v.subs(x,xx))
 own=F[branch(s.Rational(1,3),xx)].subs(q,s.Rational(1,3))
 print('XRANGE',lo,hi,'breaks',breaks)
 for L,H in zip(breaks,breaks[1:]):
  qq=((L+H)/2).subs(x,xx)
  i=branch(qq,xx);j=branch(s.Rational(2,3)-qq,xx)
  W=s.factor(D*(9*F[i]+7*F[j].subs(q,s.Rational(2,3)-q)+9*own-11))
  A=s.expand(W).coeff(q,2);B=s.expand(W).coeff(q,1);C=s.expand(W).coeff(q,0)
  print('interval',L,H,'branches',i,j,'A',s.factor(A))
  print(' endpoints',s.factor(W.subs(q,L)),s.factor(W.subs(q,H)))
  if A!=0:
   v=s.factor(-B/(2*A));G=s.factor(4*A*C-B*B)
   print(' vertex',v,'v-L',s.factor(v-L),'H-v',s.factor(H-v),'discGap',G)
