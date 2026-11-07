"""Exact actual-polygon first variations for every edge and unique-tip regime."""
import sympy as S
from fractions import Fraction as F
from random import Random
checks=0
def ck(x):
 global checks
 assert x
 checks+=1
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(c,a):return tuple(c*x for x in a)
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def area(P):return S.factor(sum(det(a,b) for a,b in zip(P,P[1:]+P[:1]))/2)
eps=S.symbols('eps',positive=True)
def sign0(f):
 f=S.factor(f)
 if f==0:return 0
 num,den=f.as_numer_denom()
 def sg(poly):
  pp=S.Poly(poly,eps)
  return S.sign(pp.nth(min(k[0] for k in pp.monoms())))
 return sg(num)*sg(den)
def clipped(P,n):
 out=[]
 for a,b in zip(P,P[1:]+P[:1]):
  fa,fb=dot(n,a),dot(n,b);sa,sb=sign0(fa),sign0(fb)
  if sa>=0:out.append(a)
  if sa*sb<0:out.append(add(a,mul(S.factor(fa/(fa-fb)),sub(b,a))))
 return out
normals=[(1,0),(0,1),(-1,-1)]
def section(P,n):
 out=[]
 for a,b in zip(P,P[1:]+P[:1]):
  fa,fb=dot(n,a),dot(n,b);sa,sb=sign0(fa),sign0(fb)
  if sa==0:out.append(a)
  if sa*sb<0:out.append(add(a,mul(S.factor(fa/(fa-fb)),sub(b,a))))
 out=list(dict.fromkeys(out));ck(len(out)==2)
 idx=1 if n[0] else 0
 z=S.factor((out[1][idx]-out[0][idx])/(abs(n[0]) if n[0] else abs(n[1])))
 return z*sign0(z)
def deriv(f):return S.factor(S.diff(f,eps).subs(eps,0))

x,s,v,w=S.symbols('x s v w',positive=True)
p=2*v+w;b=x+s;c=x+s+w;e=s+w;L=x+w+2*v;B=x+2*s+w;H=x+s+w+v
r=L/H;eta=4-r;k=L*B/2
q=[p*p*B/(2*L),L*b*b/(2*H),L*c*c/(2*H)]
sig=[p*B/L,L*b/H,L*c/H];ee=[r,B/H,B/H]
c0=eta/(L*B)
cs=[ee[i]/(2*q[i])-eta/(H*sig[i]) for i in range(3)]
ds=[-ee[i]/sig[i]+eta*q[i]/(H*sig[i]**2) for i in range(3)]
alpha=[S.factor(c0+z) for z in cs]
a=p/L
claimed=[(eta*(a-r/2)**2+r*(r-2)**2/4)/(L*B*a*a),
 (b*b+e*e-(B/H)*b*e)/(L*B*b*b),
 (c*c+s*s-(B/H)*c*s)/(L*B*c*c)]
for z,zz in zip(alpha,claimed):ck(S.factor(z-zz)==0)
ck(S.factor(sum(qi/si for qi,si in zip(q,sig))-H)==0)

rng=Random(290929)
for it in range(12):
 X,SS,V=[S.Rational(rng.randint(1,15),rng.randint(1,9)) for _ in range(3)]
 W=S.Rational(0) if it%3==0 else S.Rational(rng.randint(1,13),rng.randint(1,9))
 subvars={x:X,s:SS,v:V,w:W}
 P=[(2*V+W,-V-W),(-X,X+SS),(-X,-SS-W)]
 K0=area(P);ck(K0==k.subs(subvars))
 c00=c0.subs(subvars);cc=[z.subs(subvars) for z in cs];dd=[z.subs(subvars) for z in ds]
 al=[z.subs(subvars) for z in alpha];ck(all(z>0 for z in al))
 for j in range(3):
  j2=(j+1)%3;edge=sub(P[j2],P[j]);n0=(edge[1],-edge[0]);n0=mul(1/dot(edge,edge),n0)
  ck(det(edge,n0)==-1)
  psi=-dot(normals[j],P[j])/dot(normals[j],edge)
  theta=-dot(normals[j2],P[j])/dot(normals[j2],edge)
  ck(0<theta<psi<1)
  for t in [theta/2,theta,psi,(1+psi)/2]:
   tip=add(add(P[j],mul(t,edge)),mul(eps,n0))
   poly=P[:j+1]+[tip]+P[j+1:]
   kk=area(poly);qq=[area(clipped(poly,n)) for n in normals];ss=[section(poly,n) for n in normals]
   kd=deriv(kk);qd=list(map(deriv,qq));sd=list(map(deriv,ss))
   ck(kd==S.Rational(1,2))
   ph=S.factor(c00*kd+sum(cc[i]*qd[i]+dd[i]*sd[i] for i in range(3)))
   expect=-al[j]*t/(2*(1-t)) if t<=theta else -al[j2]*(1-t)/(2*t)
   ck(S.factor(ph-expect)==0);ck(ph<0)
   # All unperturbed cap and section data match the actual formulas.
   for i in range(3):
    ck(S.factor(qq[i].subs(eps,0)-q[i].subs(subvars))==0)
    ck(S.factor(ss[i].subs(eps,0)-sig[i].subs(subvars))==0)
print(f'PASS: {checks:,} exact symbolic and all-edge actual-polygon derivative checks')
