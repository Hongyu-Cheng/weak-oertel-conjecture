from fractions import Fraction as F
import random
random.seed(8207)
def profile(points):
 pts=[(F(x),F(y)) for x,y in points]
 # Upper concave hull, preserving nonnegative endpoints.
 P=[]
 for p in sorted(pts):
  while len(P)>1 and (P[-1][1]-P[-2][1])*(p[0]-P[-1][0]) <= (p[1]-P[-1][1])*(P[-1][0]-P[-2][0]):P.pop()
  P.append(p)
 return P

def evaluate(P):
 M=F(0);J=F(0)
 for (a,fa),(b,fb) in zip(P,P[1:]):
  w=b-a
  M+=w*(fa+fb)/2
  J+=a*w*(fa+fb)/2+w*w*(fa+2*fb)/6
 if M==0:return
 mean=J/M
 Q=[(x-mean,y) for x,y in P]
 def density(x):
  if x<Q[0][0] or x>Q[-1][0]:return F(0)
  for (a,fa),(b,fb) in zip(Q,Q[1:]):
   if a<=x<=b:return fa+(fb-fa)*(x-a)/(b-a)
  return F(0)
 def cdf(x):
  out=F(0)
  for (a,fa),(b,fb) in zip(Q,Q[1:]):
   if x<=a:break
   e=min(x,b);l=e-a
   out+=fa*l+(fb-fa)*l*l/(2*(b-a))
  return out
 cuts=sorted({F(0)}|{abs(x) for x,y in Q})
 cands=cuts[:]
 for a,b in zip(cuts,cuts[1:]):
  p=(2*a+b)/3;q=(a+2*b)/3
  hp=density(p)-density(-p);hq=density(q)-density(-q)
  if hp!=hq:
   r=p-hp*(q-p)/(hq-hp)
   if a<r<b:cands.append(r)
 vals=[(cdf(-s)-(M-cdf(s)),s) for s in cands]
 v,s=max(vals)
 return v/M,s,mean,M,P
best=(F(-100),None)
for it in range(60000):
 L=random.randint(2,12)
 P=profile([(i,random.randint(0,30)) for i in range(L+1)])
 v=evaluate(P)
 if not v:continue
 if v[0]>best[0]:
  best=(v[0],v)
 if v[0]>F(1,9):
  print('FOUND',v,flush=True);break
else:print('NONE; best',best,flush=True)
