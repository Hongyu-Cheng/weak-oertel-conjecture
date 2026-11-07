"""Independent clipping and exact certificate identity audit; no floating point."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
from flint import fmpz_mpoly as P
import re
checks=0
def ck(x):
 global checks
 assert x
 checks+=1

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def area(poly):return sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1]))/2

def clip(poly,v):
 out=[];points=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  fa=dot(v,a);fb=dot(v,b)
  if fa>=0:out.append(a)
  if fa==0:points.append(a)
  if fa*fb<0:
   q=tuple(a[j]+fa/(fa-fb)*(b[j]-a[j]) for j in range(2))
   out.append(q);points.append(q)
 return out,list(dict.fromkeys(points))

for a in [F(1,5),F(2,3),F(1),F(3)]:
 for b in [F(1,7),F(1),F(7,2)]:
  for t in [F(1,9),F(1),F(5)]:
   for u in [F(0),F(1,4),F(1),F(7)]:
    for branch in ['double','unique']:
     X=(1+t)*u/(1+u) if branch=='double' else -a*u/(1+u)
     Y=1+t-X;L=a+b+1
     poly=[(-a,-b),(b+1,-b),(X,Y),(-a,a+1)]
     ck(area(poly)==L*(L+t)/2)
     sig=[b+1+a*t/(a+X),a+1+b*t/(b+Y),a+b]
     q=[((b+1)**2+t*(L-a*a/(a+X)))/2,((a+1)**2+t*(L-b*b/(b+Y)))/2,(a+b)**2/2]
     if branch=='unique':
      sig[0]=(b+1)*(Y+b)/(b+1-X);q[0]=sig[0]*(b+1)/2
     for j,v in enumerate([(1,0),(0,1),(-1,-1)]):
      out,points=clip(poly,v)
      ck(len(points)==2);ck(area(out)==q[j])
      sigma=abs(points[1][0]-points[0][0])/abs(v[1]) if v[1] else abs(points[1][1]-points[0][1])/abs(v[0])
      ck(sigma==sig[j])
     M=sum(x/y for x,y in zip(q,sig));T=sum(x/y**2 for x,y in zip(q,sig));U=F(1)
     for x,y in zip(q,sig):U*=x/y**2
     k=area(poly);E=M*M-k*T;R=M*M*E*E-4*k**3*U
     ck(E>0);ck(R>0)
print(f'Actual clipping: {checks} checks',flush=True)

a,b,t,u=s.symbols('a b t u');variables=(a,b,t,u);gens=P.gens(4)
def fp(expr):
 ans=P(0,4)
 for mon,coef in s.Poly(expr,*variables).terms():
  ck(coef.is_Integer)
  term=P(int(coef),4)
  for g,e in zip(gens,mon):term*=g**e
  ans+=term
 return ans

def load_large(path):
 # Printed Flint polynomials have integer coefficients and x1,...,x4 variables.
 text=Path(path).read_text().split('  (nvars=')[0].strip();terms={}
 for term in text.replace(' - ',' + -').split(' + '):
  coefficient=1;mon=[0]*4
  for factor in term.split('*'):
   if factor.startswith('x'):
    m=re.fullmatch(r'x([1-4])(?:\^(\d+))?',factor);ck(m is not None)
    mon[int(m[1])-1]=int(m[2] or 1)
   else:coefficient*=int(factor)
  mon=tuple(mon);ck(mon not in terms);terms[mon]=coefficient
 powers=[[g**j for j in range(max(m[i] for m in terms)+1)] for i,g in enumerate(gens)]
 ans=P(0,4)
 for mon,coefficient in terms.items():
  term=P(coefficient,4)
  for i,e in enumerate(mon):term*=powers[i][e]
  ans+=term
 return ans,terms

for branch in ['double','unique']:
 L=a+b+1
 X=(1+t)*u/(1+u) if branch=='double' else -a*u/(1+u)
 Y=1+t-X
 sig=[b+1+a*t/(a+X),a+1+b*t/(b+Y),a+b]
 q=[((b+1)**2+t*(L-a*a/(a+X)))/2,((a+1)**2+t*(L-b*b/(b+Y)))/2,(a+b)**2/2]
 if branch=='unique':sig[0]=(b+1)*(Y+b)/(b+1-X);q[0]=sig[0]*(b+1)/2
 M=s.cancel(sum(qi/si for qi,si in zip(q,sig)));T=s.cancel(sum(qi/si**2 for qi,si in zip(q,sig)))
 U=s.cancel(s.prod(qi/si**2 for qi,si in zip(q,sig)))
 E=s.cancel(M*M-L*(L+t)*T/2)
 en,ed=s.fraction(E)
 base=Path(__file__).with_name('parallel_cut_ear_'+branch+'_')
 En=s.sympify(Path(str(base)+'E_num_root.txt').read_text(),locals=dict(zip(map(str,variables),variables)))
 Ed=s.sympify(Path(str(base)+'E_den_root.txt').read_text(),locals=dict(zip(map(str,variables),variables)))
 ck(s.expand(en*Ed-En*ed)==0)
 for expr in [En,Ed]:
  terms=s.Poly(expr,*variables).terms();ck(all(coef>0 for _,coef in terms))
  ck(any(mon[3]==0 for mon,_ in terms))
 Rn,nt=load_large(str(base)+'R_num_root.txt');Rd,dt=load_large(str(base)+'R_den_root.txt')
 for terms in [nt,dt]:
  ck(all(c>0 for c in terms.values()));ck(any(mon[3]==0 for mon in terms))
 ck(min(mon[2] for mon in nt)==1);ck(min(mon[2] for mon in dt)==0)
 mn,md=s.fraction(M);un,ud=s.fraction(U)
 rawN=P(2,4)*fp(mn)**2*fp(En)**2*fp(ud)-fp(L*(L+t))**3*fp(un)*fp(md)**2*fp(Ed)**2
 rawD=P(2,4)*fp(md)**2*fp(Ed)**2*fp(ud)
 ck(Rn*rawD==Rd*rawN)
 print(branch,'exact polynomial identity PASS; numerator terms',len(nt),'denominator terms',len(dt),flush=True)
print(f'PASS: {checks} exact clipping, identity and individual-coefficient checks')
