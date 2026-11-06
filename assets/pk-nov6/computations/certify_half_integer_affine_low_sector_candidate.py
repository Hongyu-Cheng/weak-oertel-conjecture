import sympy as s
from fractions import Fraction
from math import comb
from itertools import product
import json
from pathlib import Path
a,beta,k,x,y,w=s.symbols('a beta k x y w')
q=s.Rational
c=1-a;t=q(1,3)
Ileft=s.cancel(((a-t)**3/(3*a*(k*a-beta))-(c-t)**3/(3*c*(k*c-beta)))/(2*a-1))
Irightlow=s.cancel(((a-t-beta)**3/(3*a*(k*a+beta))-(c-t-beta)**3/(3*c*(k*c+beta)))/(2*a-1))
Irightup=(a-t-beta)**3/(3*a*(2*a-1)*(k*a+beta))
Ownleft=1-t*t/(a*c)
Ownrightlow=1-(t+beta)**2/(a*c)
Ownrightup=(a-t-beta)**2/(a*(2*a-1))
print('Ileft=',s.factor(Ileft),flush=True)
print('Irightlow=',s.factor(Irightlow),flush=True)
raw=[]
for region,(Ir,Or,bm) in enumerate([
 (Irightlow,Ownrightlow,(q(2,3)-a)*y),
 (Irightup,Ownrightup,q(2,3)-a+(2*a-1)*y),
 (s.Integer(0),s.Integer(0),a-q(1,3)+(q(2,3)-a)*y)]):
 H=s.factor((1-k)*(Ileft+Ir)+(1+k)*(Ownleft+Or)/2-q(4,9)*(1/(3*k)+q(1,2)+k/5))
 hh=s.factor(H.subs(beta,bm).subs(k,3*bm+(1-3*bm)*w))
 km=3*bm+(1-3*bm)*w
 # These denominators are positive by the strict geometric parameter
 # conditions k>3*beta and a<2/3, not by evaluating a sample point.
 D0=810*a*c*km*(a*km-bm)*(a*km+bm)*(c*km-bm)*(c*km+bm)
 D1=810*a*c*km*(a*km-bm)*(a*km+bm)*(c*km-bm)
 D2=810*a*c*km*(a*km-bm)*(c*km-bm)
 den=s.factor([27*D0,9*D1,D2/(q(2,3)-a)][region])
 assert s.fraction(s.cancel(den))[1]==1
 num=s.cancel(hh*den)
 assert s.fraction(num)[1]==1
 assert s.cancel(hh-num/den)==0
 print('region',region,'positive denominator',den,flush=True)
 raw.append((s.Poly(num,a,y,w).as_expr(),den))

def bern(poly):
 pp=s.Poly(poly,x,y,w); ns=tuple(pp.degree(v) for v in (x,y,w)); C={ijk:Fraction(c) for ijk,c in pp.terms()}
 bs={}
 for ijk in product(*(range(n+1) for n in ns)):
  total=Fraction(0)
  for jjj,c in C.items():
   if all(j<=i for j,i in zip(jjj,ijk)):
    ratio=Fraction(1)
    for j,i,n in zip(jjj,ijk,ns):ratio*=Fraction(comb(i,j),comb(n,j))
    total+=c*ratio
  bs[ijk]=total
 return min(bs.values()),ns,bs

cert=[]
for region,(base,den) in enumerate(raw):
 queue=[((q(1,2),q(2,3)),(q(0),q(1)),(q(0),q(1)),0)]
 passes=[]
 while queue:
  aa,vv,ww,depth=queue.pop()
  poly=s.expand(base.subs({a:aa[0]+(aa[1]-aa[0])*x,y:vv[0]+(vv[1]-vv[0])*y,w:ww[0]+(ww[1]-ww[0])*w},simultaneous=True))
  mn,degs,coeffs=bern(poly)
  if mn>=0:
   passes.append((aa,vv,ww,mn,degs));print('PASS',region,aa,vv,ww,mn,degs,flush=True)
   cert.append({'region':region,'a_interval':list(map(str,aa)), 'v_interval':list(map(str,vv)),
                'w_interval':list(map(str,ww)), 'degrees':degs,'minimum':str(mn),
                'coefficients':[{'index':ijk,'value':str(val)} for ijk,val in sorted(coeffs.items())]})
   continue
  if depth>=9:
   print('FAIL',region,aa,vv,ww,mn,flush=True);break
  axis=[2,1,0][depth%3]
  bounds=[aa,vv,ww];lo,hi=bounds[axis];mid=(lo+hi)/2
  for interval in [(lo,mid),(mid,hi)]:
   child=bounds.copy();child[axis]=interval;queue.append((*child,depth+1))
 else:
  print('REGION CERTIFIED',region,len(passes),'boxes',flush=True);continue
 print('REGION INCOMPLETE',region,flush=True)
Path('./half-integer-affine-low-sector-bernstein-candidate.json').write_text(json.dumps({'raw':[{'numerator':str(n),'denominator':str(d)} for n,d in raw], 'boxes':cert},indent=2)+'\n')
