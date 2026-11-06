from submission_text import read_submission
import sympy as s
from pathlib import Path
import re
p,q,r,w=s.symbols('p q r w')
D=p*q*(r+w)+r*w*(p+q);th=p*w*(q+r)/D
mu=[r/(p+r)+th*w/(p+w),w/(q+w)+(1-th)*r/(q+r),p/(p+r)+(1-th)*q/(q+r),q/(q+w)+th*p/(p+w)]
F=(p*p*q*q+p*q*(p+q)*(r+w)+r*w*(p*p+p*q+q*q))/((p+r)*(p+w)*(q+r)*(q+w))
text=read_submission('628a958af5b83522')
rows=[tuple(map(int,m)) for m in re.findall(r'\b([0-9])([0-9]),([0-9])([0-9]): ([0-9]+)',text)]
assert len(rows)==23

def M(a,b,u,v):return u**a*v**b+(u**b*v**a if a>b else 0)
def S(a,b,c,d):
 val=M(a,b,p,q)*M(c,d,r,w)
 if (a,b)!=(c,d):val+=M(c,d,p,q)*M(a,b,r,w)
 return val
NUM=sum(co*S(a,b,c,d) for a,b,c,d,co in rows)
E=(p+r)**2*(p+w)**2*(q+r)**2*(q+w)**2*D**4
assert s.cancel((s.prod(mu)-F*(1-F))*E-NUM)==0
poly=s.Poly(NUM,p,q,r,w)
assert len(poly.terms())==129 and all(c>0 for c in poly.coeffs())
print('23 source-parsed symmetric entries, full 129-positive-monomial identity PASS')
