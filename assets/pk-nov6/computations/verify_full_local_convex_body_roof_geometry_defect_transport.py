"""Exact polygon consistency checks for the proved local arbitrary-body argument.
Finite examples are not used to infer a neighborhood or a global inequality.
"""
exec(open('./verify_fixed_endpoint_sector_polygon_replacement_slab_recovery.py').read().split('def verify(')[0])
from math import isqrt
normals=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]
def replacement(K,seed):
 pp=[];nn=[]
 for i,e in enumerate(rays):
  p,n=ray_endpoint(K,e);pp.append(p);nn.append(n[(seed+i)%len(n)])
 vv=[]
 for i in range(6):
  P,Q=pp[i],pp[(i+1)%6];D=cross(P,Q);alpha=area(sector(K,P,Q))/D
  p,q=dot(nn[i],Q),dot(nn[(i+1)%6],P)
  if alpha==F(1,2):u=v=F(1,2)
  elif 1-p*q>0:
   ex,ey=(1-p)/(1-p*q),(1-q)/(1-p*q);t=(2*alpha-1)/(ex+ey-1)
   u=(1-t)/2+t*ex;v=(1-t)/2+t*ey
  else:
   t=(2*alpha-1)/(1-p);u=F(1,2)-p*t;v=F(1,2)+t
  ck=u+v==2*alpha and u>0 and v>0 and u+p*v<=1 and q*u+v<=1
  check(ck);vv.append(add(mul(u,P),mul(v,Q)))
 Q=hull(pp+vv)
 return Q,pp,vv,nn

def baryforms(T):
 out=[]
 for i in range(3):
  A,B=T[(i+1)%3],T[(i+2)%3];e=sub(B,A)
  n=(-e[1],e[0]);z=dot(n,sub(T[i],A))
  out.append((mul(1/z,n),-dot(n,A)/z))
 return out

def sqrt_upper(q,scale=10**30):
 z=isqrt(q.numerator*scale**2//q.denominator)
 check(F(z,scale)**2<=q<F(z+1,scale)**2)
 return F(z+1,scale)

def phi_upper(P):
 k=area(P);q=[area(clip(P,n)) for n in normals]
 pp=[ray_endpoint(P,e)[0] for e in rays]
 ss=[pp[1][1]-pp[4][1],pp[0][0]-pp[3][0],pp[5][0]-pp[2][0]]
 M=sum(qi/si for qi,si in zip(q,ss))
 f=[2*sqrt_upper(k*qi)/(si*M) for qi,si in zip(q,ss)]
 return [f[i]+(f[(i+1)%3]+f[(i+2)%3])**2/4 for i in range(3)]

rng=Random(301009)
max_vertices=0
for case in range(40):
 x,s,v=[F(rng.randint(2,8),4) for _ in range(3)];w=F(case%4,4)
 T=[(2*v+w,-v-w),(-x,x+s),(-x,-s-w)]
 eps=F(1,10000)
 pts=[mul(1-eps,p) for p in T]
 for p in T:
  for _ in range(4):pts.append(add(p,(eps*rng.randint(-3,3),eps*rng.randint(-3,3))))
 for j in range(3):
  A,B=T[j],T[(j+1)%3];e=sub(B,A);out=(e[1],-e[0]);out=mul(1/dot(e,e),out)
  for t in [F(1,50),F(1,5),F(2,5),F(3,5),F(4,5),F(49,50)]:
   pts.append(add(add(A,mul(t,e)),mul(eps*rng.randint(0,5),out)))
 K=hull(pts);max_vertices=max(max_vertices,len(K))
 Q,pp,vv,nn=replacement(K,case)
 T0=[vv[5],vv[1],vv[3]];check(area(T0)>0)
 check(area(Q)==area(K));check(len(Q)<=12)
 for i in range(6):
  check(ray_endpoint(Q,rays[i])[0]==pp[i])
  check(area(sector(Q,pp[i],pp[(i+1)%6]))==area(sector(K,pp[i],pp[(i+1)%6])))
  check(all(dot(nn[i],p)<=1 for p in Q))
 for n in normals:check(area(clip(Q,n))==area(clip(K,n)))
 forms=baryforms(T0)
 for p in Q:check(sum(dot(n,p)+c<0 for n,c in forms)<=1)
 for i in range(3):
  for j in range(i):
   ni,ci=forms[i];nj,cj=forms[j]
   check(area(clip(clip(Q,mul(-1,ni),ci),mul(-1,nj),cj))==0)
 Etotal=F(0)
 for i,(n,c) in enumerate(forms):
  cap=hull(clip(Q,mul(-1,n),c))
  if area(cap)==0:continue
  A,B=T0[(i+1)%3],T0[(i+2)%3];e=sub(B,A)
  coords=[(dot(e,sub(p,A))/dot(e,e),-cross(e,sub(p,A))) for p in cap]
  check(all(0<=t<=1 and h>=0 for t,h in coords))
  tops=[]
  for p in sorted(set(coords)):
   if tops and p[0]==tops[-1][0]:tops[-1]=max(p,tops[-1],key=lambda z:z[1]);continue
   while len(tops)>1 and cross(sub(tops[-1],tops[-2]),sub(p,tops[-1]))>=0:tops.pop()
   tops.append(p)
  check(tops[0]==(0,0) and tops[-1]==(1,0))
  E=sum((a[1]+b[1])*(b[0]-a[0])/2 for a,b in zip(tops,tops[1:]));H=max(p[1] for p in tops)
  check(E==area(cap));check(H/2<=E<=H)
  coeff=[]
  for j in range(1,len(tops)-1):
   t,h=tops[j];left=(h-tops[j-1][1])/(t-tops[j-1][0]);right=(tops[j+1][1]-h)/(tops[j+1][0]-t)
   cr=t*(1-t)*(left-right);check(cr>0);coeff.append((t,cr))
  check(sum(a for t,a in coeff)==2*E)
  for tt,hh in tops:
   val=sum(a*(tt/t if tt<=t else (1-tt)/(1-t)) for t,a in coeff)
   check(val==hh)
  Etotal+=E
 check(Etotal==area(Q)-area(T0)>0)
 check(all(z<2 for z in phi_upper(K)))
print(f'PASS: {checks:,} exact support-replacement, many-roof, coarea-data and row checks; input polygons up to {max_vertices} vertices')
