from fractions import Fraction as F
import random
random.seed(9125)
def profile(points):
 P=[]
 for p in sorted((F(x),F(y)) for x,y in points):
  while len(P)>1 and (P[-1][1]-P[-2][1])*(p[0]-P[-1][0]) <= (p[1]-P[-1][1])*(P[-1][0]-P[-2][0]):P.pop()
  P.append(p)
 return P

def evaluate(P,d):
 p=d-1;M=F(0);J=F(0)
 for (a,fa),(b,fb) in zip(P,P[1:]):
  w=b-a;dh=fb-fa
  if dh:
   area=w*(fb**(p+1)-fa**(p+1))/(dh*(p+1))
   mom=w*w*((fb**(p+2)-fa**(p+2))/(p+2)-fa*(fb**(p+1)-fa**(p+1))/(p+1))/(dh*dh)
  else:area=w*fa**p;mom=w*w*fa**p/2
  M+=area;J+=a*area+mom
 if M==0:return
 mean=J/M;Q=[(x-mean,y) for x,y in P]
 def root(x):
  if x<Q[0][0] or x>Q[-1][0]:return F(0)
  for (a,fa),(b,fb) in zip(Q,Q[1:]):
   if a<=x<=b:return fa+(fb-fa)*(x-a)/(b-a)
  return F(0)
 def cdf(x):
  out=F(0)
  for (a,fa),(b,fb) in zip(Q,Q[1:]):
   if x<=a:break
   e=min(x,b);w=e-a;s=(fb-fa)/(b-a)
   if s:out+=((fa+s*w)**(p+1)-fa**(p+1))/(s*(p+1))
   else:out+=w*fa**p
  return out
 cuts=sorted({F(0)}|{abs(x) for x,y in Q});cands=cuts[:]
 for a,b in zip(cuts,cuts[1:]):
  x=(2*a+b)/3;y=(a+2*b)/3
  hx=root(x)-root(-x);hy=root(y)-root(-y)
  if hx!=hy:
   rr=x-hx*(y-x)/(hy-hx)
   if a<rr<b:cands.append(rr)
 val,s=max((cdf(-s)-(M-cdf(s)),s) for s in cands)
 return val/M,s,mean,M,P
for d in (3,4,5,8,12,20):
 target=1-2*F(d,d+1)**d
 best=F(-10)
 for it in range(20000):
  L=random.randint(2,10)
  P=profile([(i,random.randint(0,25)) for i in range(L+1)])
  v=evaluate(P,d)
  if not v:continue
  best=max(best,v[0])
  if v[0]>target:
   print('FOUND d',d,'target',target,'record',v,flush=True);raise SystemExit
 print('DONE',d,'best',float(best),'target',float(target),flush=True)
