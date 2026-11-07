"""Parse the printed coefficient table and check the geometric identities independently."""
from submission_text import read_submission
from pathlib import Path
import re
import sympy as s
p,q,r,w=s.symbols('p q r w')
source=read_submission('fa0b1651cc72d020')
N=0;rows=0
for line in source.splitlines():
 match=re.fullmatch(r'    C(\d)(\d) = (.+)',line)
 if not match:continue
 i,j=int(match[1]),int(match[2]);parts=match[3].rstrip('.').replace(' ','').split('+');poly=0
 for part in parts:
  term=re.fullmatch(r'(\d*)M(\d)(\d)',part);assert term
  coefficient=int(term[1] or '1');a,b=int(term[2]),int(term[3]);assert a>=b
  poly+=coefficient*(r**a*w**b+(r**b*w**a if a>b else 0))
 N+=p**i*q**j*poly;rows+=1
assert rows==33
D=p*q*(r+w)+r*w*(p+q);theta=p*w*(q+r)/D
b=[(r/(p+r)+theta*w/(p+w))/3,(w/(q+w)+(1-theta)*r/(q+r))/3,
   (p/(p+r)+(1-theta)*q/(q+r))/3,(q/(q+w)+theta*p/(p+w))/3]
x,y,z,t=1/p,1/q,1/r,1/w;L=x+y+z+t
ind=[(x/(x+z)+x/(x+t)-x/L)/3,(y/(y+z)+y/(y+t)-y/L)/3,
     (z/(z+x)+z/(z+y)-z/L)/3,(t/(t+x)+t/(t+y)-t/L)/3]
for u,v in zip(b,ind):assert s.cancel(u-v)==0
F=(p*p*q*q+p*q*(p+q)*(r+w)+r*w*(p*p+p*q+q*q))/((p+r)*(p+w)*(q+r)*(q+w))
DEN=(p+r)**2*(p+w)**2*(q+r)**2*(q+w)**2*D**3
assert s.cancel((27*b[1]*b[2]*b[3]-F*(1-F))*DEN-N)==0
poly=s.Poly(N,p,q,r,w);assert len(poly.terms())==100
assert all(c>0 for c in poly.coeffs())
a0,a1,a2=s.symbols('a0 a1 a2')
assert s.expand(1-a0*a1*a2-((1-a0)+a0*(1-a1)+a0*a1*(1-a2)))==0
print('PASS: 33 printed coefficient rows; 100 positive monomials; 6 exact geometric/algebraic identities')
