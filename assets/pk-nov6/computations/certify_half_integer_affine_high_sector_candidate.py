import sympy as s
from fractions import Fraction
from math import comb
from itertools import product
import json
from pathlib import Path
b,z,k,x,y,w=s.symbols('b z k x y w')
P=1-b
A=1/(2-3*b)
# convex combination of two unconditional arithmetic-sum lower bounds
f=lambda p,l:(1-k)*(p**3/(3*l)+p*p/2)+k*p*p
H=s.factor(A*(f(P,k*(1-z))+f(P-k*z,k*(1+z)))-s.Rational(4,9)*(1/(3*k)+s.Rational(1,2)+k/s.Integer(5)))
num,den=s.fraction(H)
print('den',s.factor(den),flush=True)
print('num=',s.factor(num),flush=True)
# Use explicit positive denominator to avoid a hidden sign convention.
D=270*k*(2-3*b)*(1-z*z)
pol=s.Poly(s.cancel(H*D),b,z,k).as_expr()
assert s.cancel(H-pol/D)==0
q=s.Rational

def bern(poly):
 pp=s.Poly(poly,x,y,w); ns=tuple(pp.degree(v) for v in (x,y,w)); C={ijk:Fraction(c) for ijk,c in pp.terms()}
 bs={}
 for ijk in product(*(range(n+1) for n in ns)):
  total=Fraction(0)
  for jjj,c in C.items():
   if all(j<=i for j,i in zip(jjj,ijk)):
    ratio=Fraction(1)
    for j,i,n in zip(jjj,ijk,ns): ratio*=Fraction(comb(i,j),comb(n,j))
    total+=c*ratio
  bs[ijk]=total
 return min(bs.values()),ns,bs

base=s.Poly(s.expand(pol.subs(z,b*z)),b,z,k).as_expr()
queue=[((q(1,3),q(1,2)),(q(0),q(1)),(q(0),q(1)),0)]
passes=[]
certificate=[]
while queue:
 bb,vv,kk,depth=queue.pop()
 mapped=s.expand(base.subs({b:bb[0]+(bb[1]-bb[0])*x,z:vv[0]+(vv[1]-vv[0])*y,k:kk[0]+(kk[1]-kk[0])*w},simultaneous=True))
 mn,degs,coeffs=bern(mapped)
 if mn>=0:
  passes.append((bb,vv,kk,mn,degs))
  certificate.append({'b_interval':list(map(str,bb)), 'v_interval':list(map(str,vv)),
                      'k_interval':list(map(str,kk)), 'degrees':degs,
                      'minimum':str(mn),
                      'coefficients': [{'index':ijk,'value':str(value)}
                                       for ijk,value in sorted(coeffs.items())]})
  print('PASS',bb,vv,kk,mn,degs,flush=True);continue
 if depth>=8:
  print('FAIL',bb,vv,kk,mn,flush=True);break
 # cycle dimensions, prioritizing k then v then b
 axis=[2,1,0][depth%3]
 bounds=[bb,vv,kk]; lo,hi=bounds[axis];mid=(lo+hi)/2
 for interval in [(lo,mid),(mid,hi)]:
  child=bounds.copy();child[axis]=interval;queue.append((*child,depth+1))
else:
 print('CERTIFIED',len(passes),'boxes',sum((r[4][0]+1)*(r[4][1]+1)*(r[4][2]+1) for r in passes),'coefficients',flush=True)
 artifact={'positive_denominator':str(D), 'numerator':str(pol),
           'substitution':'z=b*v', 'boxes':certificate}
 Path('./half-integer-affine-high-sector-bernstein.json').write_text(json.dumps(artifact,indent=2)+'\n')
