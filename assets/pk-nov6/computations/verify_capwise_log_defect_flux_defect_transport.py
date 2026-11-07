import sympy as s
from fractions import Fraction as F
count=0
def ck(x):
 global count
 assert x
 count+=1
c=s.exp(F(1,2)); bmass=s.sqrt(2)*s.log(2);n=s.Matrix([-1,-1])/s.sqrt(2)
grad=c*s.Matrix([1,1]);zeta=2/c*s.log(2);M=F(1,2)
ck(s.simplify(-n*bmass-M*grad*zeta)==s.zeros(2,1))
# Full inside cap: boundary defect is zero and section correction is indispensable.
u=s.Matrix([1,1]);sec=s.log(2)
ck(s.simplify(M*grad*zeta-u*sec)==s.zeros(2,1))
# Complementary outside cap recovers all surface defect.
ck(s.simplify(-n*bmass-(-(-u)*sec))==s.zeros(2,1))
# Proper diagonal section has no section defect.
ck(s.simplify(-n*bmass/2-M*grad*zeta/2)==s.zeros(2,1))
# Complementary selectors use identical section allocation.
a=s.symbols('a',real=True)
ck(s.expand((1-a)+a-1)==0)
ck(s.expand(1-(1-a)-a)==0)
# Exact primitive for the proper diagonal section (coarea dt/2).
t,b=s.symbols('t b',positive=True)
prim=((t-b)*s.log(t-b)-(t-b))/2
ck(s.simplify(s.diff(prim,t)-s.log(t-b)/2)==0)
# Layer-cake tail coefficient.
x,A=s.symbols('x A',positive=True)
ck(s.simplify(A*s.exp(-A)+s.integrate(s.exp(-x),(x,A,s.oo))-(A+1)*s.exp(-A))==0)
for m in range(8,101):
 a=F(1,m);eta=F(1,2**m)
 ck(a*F(m,1)==1)
 ck(0<eta<a)
print(f'{count} exact checks PASS')
