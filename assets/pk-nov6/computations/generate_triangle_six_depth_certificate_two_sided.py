from fractions import Fraction as Q
import sympy as sp
from math import comb
T,X=sp.symbols('t L')
D=(T+1)*(2-T)*(1-2*T)
# vertices are (t,L)
polys=[[(-Q(1),Q(0)),(Q(1,2),Q(0)),(Q(1,2),Q(2)),(-Q(1),Q(2))]]
lines={(Q(1),Q(0),Q(0))}
for k in [-2,-1,1,2,3]:
 for vals in [(0,k,1),(-1,k,0),(1,k,-1)]:
  vals=tuple(Q(v) for v in vals)
  p=next(v for v in vals if v)
  lines.add(tuple(v/p for v in vals))
def val(p,line):return line[0]*p[0]+line[1]*p[1]+line[2]
def clean(p):
 q=[]
 for x in p:
  if not q or q[-1]!=x:q.append(x)
 if len(q)>1 and q[-1]==q[0]:q.pop()
 return q
def clip(poly,line,sgn):
 out=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  va=sgn*val(a,line);vb=sgn*val(b,line)
  if va>=0:out.append(a)
  if (va>0 and vb<0) or (va<0 and vb>0):
   k=va/(va-vb);out.append((a[0]+k*(b[0]-a[0]),a[1]+k*(b[1]-a[1])))
 return clean(out)
def area(p):return sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1]))
for line in sorted(lines):
 nxt=[]
 for p in polys:
  for s in [-1,1]:
   q=clip(p,line,s)
   if len(q)>=3 and area(q)>0:nxt.append(q)
 polys=nxt
print('cells',len(polys),flush=True)
def numerator(p):
 t=sum(x[0] for x in p)/len(p);l=sum(x[1] for x in p)/len(p)
 f=sp.Rational(-22,9)*D
 for k in [-2,-1,0,1,2,3]:
  xx=k*l
  if xx<=-1:f+=D
  elif xx>=1-t:pass
  elif xx<t:f+=D-(k*X+1)**2*(1-2*T)
  else:f+=(1-T-k*X)**2*(T+1)
 return sp.Poly(sp.expand(9*f),T,X)
U,V=sp.symbols('u v')
def bern(P,tri):
 a,b,c=tri
 tt=a[0]+(b[0]-a[0])*U+(c[0]-a[0])*V
 ll=a[1]+(b[1]-a[1])*U+(c[1]-a[1])*V
 tr=sp.Poly(P.as_expr().subs({T:tt,X:ll}),U,V)
 deg=3
 out=[]
 for i in range(deg+1):
  for j in range(deg+1-i):
   v=0
   for (aa,bb),cc in tr.terms():
    if aa<=i and bb<=j:
     v+=cc*sp.Rational(comb(i,aa)*comb(j,bb),comb(deg,aa+bb)*comb(aa+bb,aa))
   out.append(v)
 return out
cnt=0;maxdepth=0;bad=[];certificate=[]
for idx,p in enumerate(polys):
 P=numerator(p)
 record={"polygon":[[[v.numerator,v.denominator] for v in z] for z in p],"polynomial":[[int(a),int(b),str(c)] for (a,b),c in P.terms()],"triangles":[]}
 stack=[((p[0],p[i],p[i+1]),0) for i in range(1,len(p)-1)]
 while stack:
  tri,depth=stack.pop();bs=bern(P,tri)
  if min(bs)>=0:
   cnt+=1;maxdepth=max(maxdepth,depth);record["triangles"].append({"vertices":[[[v.numerator,v.denominator] for v in z] for z in tri],"bernstein":[str(x) for x in bs]});continue
  if depth>=14:
   bad.append((idx,tri,sp.factor(P.as_expr()),min(bs)));break
  edges=[((tri[a][0]-tri[b][0])**2+(tri[a][1]-tri[b][1])**2,a,b) for a,b in [(0,1),(1,2),(2,0)]]
  _,a,b=max(edges);c=3-a-b
  mid=((tri[a][0]+tri[b][0])/2,(tri[a][1]+tri[b][1])/2)
  stack.append(((tri[a],mid,tri[c]),depth+1));stack.append(((mid,tri[b],tri[c]),depth+1))
 certificate.append(record)
 print(idx,'factor',sp.factor(P.as_expr()),'bad',len(bad),'cert',cnt,'depth',maxdepth,flush=True)
print('TOTAL',cnt,maxdepth,'bad',bad)

import json
assert not bad
with open("./triangle-six-fiber-depth-bernstein-certificate.json","w") as out:json.dump({"degree":3,"cells":certificate},out,indent=2)
