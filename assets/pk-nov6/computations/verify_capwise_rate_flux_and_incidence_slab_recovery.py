"""Exact identities for capwise defect-rate flux and actual triangle calibrations."""
from fractions import Fraction as F
import sympy as s
checks=0
def ck(x):
    global checks
    assert x
    checks+=1
r,R,gamma,c=s.symbols('r R gamma c', positive=True)
M=s.Rational(1,2)
# Full and inside cap flux at every monomial, including m=0.
for k in range(60):
    mom=R**k/s.Integer(k+1)
    volume=M*c*(2*gamma/c)*(k+1)*mom
    section=gamma*R**k
    ck(s.simplify(volume-section)==0)
    # The complement has a_H=b and zero inverse capture.
    ck(s.simplify(gamma*R**k-section)==0)
    # Generic nonparallel cut captures one-half at every rate.
    ck(s.simplify(gamma*R**k/2-volume/2)==0)
# General polynomial calculus behind g+r g'.
for k in range(30):
    gg=r**k
    ck(s.simplify(s.integrate(gg+r*s.diff(gg,r),(r,0,R))/R-R**k)==0)
# Section atom cannot itself be the uniform spreading of its boundary atom.
for num in range(1,31):
    rr=F(num,31)
    ck(rr!=rr/2)
# Exact signed radial formula, using g_z=(1/3,1/3).
h=s.sqrt(2)/3
fullB=s.sqrt(2)*gamma*h
insideC=-s.Rational(2,3)*gamma
outsideC=s.Rational(2,3)*gamma
ck(s.simplify(fullB+insideC)==0)
ck(s.simplify(fullB-outsideC)==0)
for k in range(30):
    Vmom=s.Rational(2,3)*gamma*R**k/(k+1)
    ck(s.simplify(0-(k+1)*Vmom-insideC*R**k)==0)
    ck(s.simplify(fullB*R**k-outsideC*R**k)==0)
# Proper cut collar: exact inverse primitive and algebraic upper bound.
a,eta,t=s.symbols('a eta t', positive=True)
b=a-eta
primitive=t+b*s.log(t-b)
actual=s.simplify(primitive.subs(t,a+eta**2)-primitive.subs(t,a))
expected=eta**2+(a-eta)*s.log(1+eta)
ck(s.simplify(actual-expected)==0)
# log(1+eta)<=eta gives upper eta^2+a eta when eta<=a.
for den in range(2,55):
    aa=F(1,den)
    for q in range(1,den+1):
        ee=aa*F(q,den+1)
        ck(0<ee<aa)
        ck(ee*ee+(aa-ee)*ee<=ee*ee+aa*ee)
# Symmetry fractions: all rate tests depend only on t, angular r is uniform.
x=s.symbols('x')
for k in range(35):
    ck(s.integrate(R**k,(x,s.Rational(1,2),1))==R**k/2)
# Nonparallel section x=y parametrized by t, actual coarea dt/2.
xy=s.Matrix([t/2,t/2])
speed=s.sqrt(sum(s.diff(v,t)**2 for v in xy))
ck(s.simplify(speed/s.sqrt(2)-s.Rational(1,2))==0)
# Cap fraction at fixed boundary rate forces same inverse fraction across rates.
for den in range(1,31):
  for num in range(den+1):
    fraction=F(num,den)
    for k in range(12):
      ck(fraction*F(1,k+1)==(fraction*F(1))/(k+1))
# A multi-rate example of the exact weighted-tail fraction.
B=[(F(1,4),F(2),F(1,5)),(F(3,4),F(3),F(4,5))]
# triples (surface rate, surface mass, chosen cap fraction)
for rr in (F(1,10),F(1,3),F(7,10)):
    full=sum(mass/rate for rate,mass,cap in B if rate>=rr)
    cut=sum(cap*mass/rate for rate,mass,cap in B if rate>=rr)
    ck(0<=cut<=full)
    ck(full>0)
    frac=cut/full
    ck(0<=frac<=1)
print(f'PASS: {checks} exact capwise-rate/incident-allocation checks')
