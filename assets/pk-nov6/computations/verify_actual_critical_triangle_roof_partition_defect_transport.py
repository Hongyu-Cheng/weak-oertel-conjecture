from fractions import Fraction as F
from itertools import product
import sympy as s

count=0
def ck(b):
    global count
    assert b
    count+=1
P=list(product(range(-2,3),repeat=2))
q=lambda p:2*p[0]+p[1]
r=lambda p:7-abs(q(p))
par=lambda p:(p[0]%2,p[1]%2)
ck(len(P)==25);ck(len(set(map(par,P)))==4)
ck(min(map(r,P))==1);ck(sum(map(r,P))==109)
ck(sum(r(p)**2 for p in P)==551)
ck(F(9,2)*551==F(4959,2));ck(F(4,9)*F(4959,2)==1102)
for p in P:
    ck(r(p)==r((-p[0],-p[1])))
    ck(r(p)>0)
for j in (0,1): ck(sum(r(p)*p[j] for p in P)==0)
left=[p for p in P if q(p)<0];right=[p for p in P if q(p)>0]
ck(len(set(map(par,left)))==4);ck(len(set(map(par,right)))==4)
for p in [(-2,0),(-2,-1),(-1,0),(-1,-1)]:
    ck(q(p)<0);ck(q((-p[0],-p[1]))>0)
    ck(par(p)==par((-p[0],-p[1])))
# All real cell vertices are sampled, and the affine formulas agree there.
for poly in [[(-2,-2),(-2,2),(-1,2),(1,-2)],[(2,-2),(2,2),(-1,2),(1,-2)]]:
    for p in poly: ck(p in P)
for p in P:
    ck(r(p)==min(7-q(p),7+q(p)))
# Canonical through-(p,0) small-tilt exact polynomial has a negative derivative.
t=s.symbols('t',real=True)
for p in P:
    if p==(0,0): continue
    poly=sum((2*r(z)+t*sum(p[j]*(z[j]-p[j]) for j in (0,1)))**2 for z in P)
    ck(s.expand(poly).coeff(t,1)==-4*109*(p[0]**2+p[1]**2))
# Exact edge kernel mass/mean and target densities.
x=s.symbols('x',real=True)
ck(F(2,3)+F(1,6)+F(1,6)==1)
ck(s.expand(F(2,3)*x+F(1,6)*(x-F(1,3))+F(1,6)*(x+F(1,3)))==x)
ck(F(3,2)*F(2,3)==1);ck(F(3,4)+F(3,2)*F(1,6)==1)
# Compare output polynomial moments to uniform length; this is independent of edge size.
for k in range(10):
    out=s.integrate(F(3,4)*x**k,(x,0,F(1,3)))+s.integrate(F(3,4)*x**k,(x,F(2,3),1))
    out+=s.integrate(F(3,2)*(F(2,3)*x**k+F(1,6)*(x-F(1,3))**k+F(1,6)*(x+F(1,3))**k),(x,F(1,3),F(2,3)))
    ck(s.simplify(out-F(1,k+1))==0)
# The canonical paired tail is strictly above 8/9 away from its zero shift.
for j in range(1,101):
    a=F(j,100)
    ck(F(8,9)+F(2,9)*a*a>F(8,9))
    ck(1+F(1,9)*(2-(1+a))**2>F(8,9))
print(f'{count} exact checks PASS')
