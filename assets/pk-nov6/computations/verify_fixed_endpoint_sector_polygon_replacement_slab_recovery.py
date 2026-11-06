from fractions import Fraction as F
from random import Random

checks=0
branches={'core':0,'bounded':0,'unbounded':0}
def check(b):
 global checks
 assert b
 checks+=1
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(t,a):return(t*a[0],t*a[1])
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(P):return sum(cross(a,b) for a,b in zip(P,P[1:]+P[:1]))/2 if len(P)>2 else F(0)
def hull(points):
 P=sorted(set(points))
 def half(P):
  H=[]
  for p in P:
   while len(H)>1 and cross(sub(H[-1],H[-2]),sub(p,H[-1]))<=0:H.pop()
   H.append(p)
  return H
 return half(P)[:-1]+half(P[::-1])[:-1]
def clip(P,n,b=F(0)):
 R=[]
 for a,c in zip(P,P[1:]+P[:1]):
  fa,fc=dot(n,a)-b,dot(n,c)-b
  if fa>=0:R.append(a)
  if (fa<0<fc) or (fc<0<fa):R.append(add(a,mul(fa/(fa-fc),sub(c,a))))
 return R
rays=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(1)),(F(-1),F(0)),(F(0),F(-1)),(F(1),F(-1))]
def sector(P,a,b):
 return clip(clip(P,(-a[1],a[0])),(b[1],-b[0]))
def supports(P):
 out=[]
 for a,b in zip(P,P[1:]+P[:1]):
  e=sub(b,a);n=(e[1],-e[0]);h=dot(n,a)
  check(h>0)
  out.append(mul(1/h,n))
 return out
def ray_endpoint(P,d):
 ns=supports(P)
 t=min(1/dot(n,d) for n in ns if dot(n,d)>0)
 p=mul(t,d)
 return p,[n for n in ns if dot(n,p)==1]
def verify(K,index):
 check(area(K)>0)
 eps=[];ns=[]
 for i,d in enumerate(rays):
  p,nn=ray_endpoint(K,d);eps.append(p);ns.append(nn[(index+i)%len(nn)])
 vertices=[]
 targets=[]
 us=[];vs=[]
 for i in range(6):
  P,Q=eps[i],eps[(i+1)%6];det=cross(P,Q)
  check(det>0)
  target=area(sector(K,P,Q));targets.append(target)
  alpha=target/det
  p=dot(ns[i],Q);q=dot(ns[(i+1)%6],P)
  check(p<=1 and q<=1 and alpha>=F(1,2))
  if p==1 or q==1:
   branches['core']+=1;check(alpha==F(1,2));u=v=F(1,2)
  elif 1-p*q>0:
   branches['bounded']+=1
   D=1-p*q;Ex=(1-p)/D;Ey=(1-q)/D
   th=(2*alpha-1)/(Ex+Ey-1)
   check(0<=th<=1)
   u=(1-th)/2+th*Ex;v=(1-th)/2+th*Ey
  else:
   branches['unbounded']+=1
   check(p<0 and q<0)
   tt=(2*alpha-1)/(1-p)
   u=F(1,2)-tt*p;v=F(1,2)+tt
  check(u>0 and v>0 and u+v==2*alpha)
  check(u+p*v<=1 and q*u+v<=1)
  pp=(1-u)/v;qq=(1-v)/u
  check(pp>=p and qq>=q)
  V=add(mul(u,P),mul(v,Q))
  vertices.extend([P,V]);us.append(u);vs.append(v)
  check(area([(F(0),F(0)),P,V,Q])==target)
 Ds=[cross(eps[i],eps[(i+1)%6]) for i in range(6)]
 aa=[2*targets[i]/Ds[i]-1 for i in range(6)]
 Es=[cross(eps[i-1],eps[(i+1)%6]) for i in range(6)]
 kk=[Ds[i-1]+Ds[i]-Es[i] for i in range(6)]
 for i in range(6):
  lhs=Ds[i]*aa[i-1]/us[i-1]+Ds[i-1]*aa[i]/vs[i]
  check(lhs<=kk[i])
  join=cross(sub(eps[i],vertices[2*((i-1)%6)+1]),sub(vertices[2*i+1],eps[i]))
  check(join==us[i-1]*vs[i]*(kk[i]-lhs))
  if aa[i]>0:
   check(kk[i]>0 and kk[(i+1)%6]>0)
   check(us[i]>=Ds[(i+1)%6]*aa[i]/kk[(i+1)%6])
   check(vs[i]>=Ds[i-1]*aa[i]/kk[i])
  ri=aa[i]/(Ds[i]*us[i]);si=aa[i]/(Ds[i]*vs[i]);hi=aa[i]/(Ds[i]*(us[i]+vs[i]))
  check(ri*si==hi*(ri+si))
 check(sum(1/a for a in targets)>=sum(1/d for d in Ds)+sum(Es[i]/(Ds[i-1]*Ds[i]) for i in range(6))/2)
 for i in range(len(vertices)):

  a,b,c=vertices[i-1],vertices[i],vertices[(i+1)%len(vertices)]
  check(cross(sub(b,a),sub(c,b))>=0)
 Q=hull(vertices)
 check(len(Q)<=12)
 check(area(Q)==area(K))
 for i,(d,n) in enumerate(zip(rays,ns)):
  check(all(dot(n,p)<=1 for p in Q))
  check(ray_endpoint(Q,d)[0]==eps[i])
  check(area(sector(Q,eps[i],eps[(i+1)%6]))==targets[i])
 for n in [(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]:
  for sign in [-1,1]:check(area(clip(Q,mul(sign,n)))==area(clip(K,mul(sign,n))))

examples=[
 [(F(-1),F(-1)),(F(1),F(-1)),(F(1),F(1)),(F(-1),F(1))],
 [(F(-1,10),F(-1,10)),(F(10),F(1)),(F(1),F(10))],
 [(F(-1),F(-1)),(F(3),F(-1)),(F(-1),F(4))],
]
rng=Random(29303)
for _ in range(160):
 pts=[(F(-1),F(-1)),(F(1),F(-1)),(F(1),F(1)),(F(-1),F(1))]
 pts += [(F(rng.randrange(-80,81),10),F(rng.randrange(-80,81),10)) for _ in range(14)]
 examples.append(hull(pts))
for i,K in enumerate(examples):verify(hull(K),i)
check(all(branches[k]>0 for k in branches))
print(f'PASS: {checks} exact actual-polygon checks; wedge branches {branches}')
