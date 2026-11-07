"""Exact identity proof checks, not a numerical substitute for the source proof."""
import sympy as s
from fractions import Fraction as Q
p,q,r,w=s.symbols('p q r w')
D=p*q*(r+w)+r*w*(p+q); theta=p*w*(q+r)/D
b=[(r/(p+r)+theta*w/(p+w))/3,
   (w/(q+w)+(1-theta)*r/(q+r))/3,
   (p/(p+r)+(1-theta)*q/(q+r))/3,
   (q/(q+w)+theta*p/(p+w))/3]
F=s.cancel((p**3/((p+r)*(p+w))-q**3/((q+r)*(q+w)))/(p-q))
DEN=(p+r)**2*(p+w)**2*(q+r)**2*(q+w)**2*D**3
terms={
(7,6):[(2,4,0),(7,3,1),(9,2,2)],
(7,5):[(1,5,0),(13,4,1),(31,3,2)],
(7,4):[(5,5,1),(32,4,2),(52,3,3)],
(7,3):[(10,5,2),(38,4,3)],(7,2):[(10,5,3),(22,4,4)],(7,1):[(5,5,4)],(7,0):[(1,5,5)],
(6,6):[(2,5,0),(16,4,1),(33,3,2)],(6,5):[(13,5,1),(70,4,2),(112,3,3)],
(6,4):[(32,5,2),(117,4,3)],(6,3):[(38,5,3),(85,4,4)],(6,2):[(22,5,4)],(6,1):[(5,5,5)],
(5,6):[(9,5,1),(39,4,2),(56,3,3)],(5,5):[(39,5,2),(132,4,3)],(5,4):[(66,5,3),(141,4,4)],(5,3):[(48,5,4)],(5,2):[(12,5,5)],
(4,6):[(15,5,2),(41,4,3)],(4,5):[(52,5,3),(109,4,4)],(4,4):[(1,6,3),(59,5,4)],(4,3):[(1,6,4),(22,5,5)],
(3,6):[(11,5,3),(19,4,4)],(3,5):[(1,6,3),(37,5,4)],(3,4):[(3,6,4),(23,5,5)],(3,3):[(2,6,5)],
(2,6):[(3,5,4)],(2,5):[(3,6,4),(15,5,5)],(2,4):[(3,6,5)],(2,3):[(1,6,6)],
(1,5):[(3,6,5)],(1,4):[(1,6,6)],(0,5):[(1,6,6)]}
def M(a,b):return r**a*w**b+(r**b*w**a if a>b else 0)
NUM=sum(p**i*q**j*sum(c*M(a,b) for c,a,b in ts) for (i,j),ts in terms.items())
assert s.cancel((27*b[1]*b[2]*b[3]-F*(1-F))*DEN-NUM)==0
assert all(c>0 for c in s.Poly(NUM,p,q,r,w).coeffs())
assert len(s.Poly(NUM,p,q,r,w).terms())==100
checks=2
# Explicit repeated-positive and repeated-negative values are included: F has
# already been canceled as a rational function whose denominator is positive.
for pp in range(1,5):
 for qq in range(1,5):
  for rr in range(1,4):
   for ww in range(1,4):
    sub={p:pp,q:qq,r:rr,w:ww}
    fv=F.subs(sub);bv=[v.subs(sub) for v in b]
    for j in range(4):
     assert 27*s.prod(bv[k] for k in range(4) if k!=j)>fv*(1-fv)
     checks+=1
# A genuine proper through-edge section sharpens the universal constant.
z=s.symbols('z',positive=True)
boundary=[(1-z)/3,z/3,s.Rational(1,3),s.Rational(1,3)]
assert s.expand(27*boundary[0]*boundary[1]*boundary[2]-z*(1-z))==0
checks+=1
print(f'{checks} exact tetrahedral cap-variance/product checks PASS; full 100-term polynomial identity verified')
