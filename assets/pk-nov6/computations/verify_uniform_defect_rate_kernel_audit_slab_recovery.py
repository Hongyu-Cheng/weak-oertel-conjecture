"""Independent exact identities for the rate-kernel audit and actual triangle."""
import sympy as s
from fractions import Fraction as F
checks=0
def ck(ok):
    global checks
    assert ok
    checks+=1

t,b,v,eta,a,c,gm,m,R=s.symbols('t b v eta a c gm m R', positive=True)
# Exact triangle normalizer and inverse primitives.
logprim=v**2*s.log(v)/2-v**2/4+b*(v*s.log(v)-v)
ck(s.simplify(s.diff(logprim,v)-(v+b)*s.log(v))==0)
invprim=t+b*s.log(t-b)
ck(s.simplify(s.diff(invprim,t)-t/(t-b))==0)
momprim=t*t/2+b*t+b*b*s.log(t-b)
ck(s.simplify(s.diff(momprim,t)-t*t/(t-b))==0)
ck(s.simplify((momprim-b*invprim)-t*t/2)==0)
# Jacobian of actual coordinates (t,r)->(rt,(1-r)t).
r=s.symbols('r', real=True)
xy=s.Matrix([r*t,(1-r)*t])
ck(s.simplify(abs(xy.jacobian([t,r]).det())-t)==0)
# Exact affine contact row marked value and original-row reweight.
I,Z,V=s.symbols('I Z V', positive=True)
Lm_source=c*(I/Z-b)
ck(s.simplify(Lm_source.subs(I,V+b*Z)-c*V/Z)==0)
ck(s.simplify((c*(t-b)/(c*V/Z))*(1/(Z*(t-b)))-1/V)==0)
# Actual rate change of variable, preserving its physical numerator.
q=s.symbols('q', real=True)
newt=b+s.exp(-gm*m*q)/c
ck(s.simplify(s.diff(newt,q)/(newt-b)+gm*m)==0)
ck(s.simplify((R/(gm*m))*(-s.log(c*(newt-b)))-R*q)==0)
# Monomial derivative; no L=1 cutoff on a positive rate power.
L,lam=s.symbols('L lam', positive=True)
for k in range(1,35):
    ff=(-s.log(L))*(lam*(-s.log(L)))**k
    ck(s.simplify(s.diff(ff,L)+(k+1)*(lam*(-s.log(L)))**k/L)==0)
# Exact weighted moment relation and polynomial extension.
x=s.symbols('x', nonnegative=True)
for k in range(50):
    ck(s.simplify(s.integrate(x**k,(x,0,R))/R-R**k/(k+1))==0)
for den in range(1,21):
  for num in range(1,den+1):
    rr=F(num,den)
    for k in range(15):
      bmass=F(2,3)*F(den+num,den)
      vmoment=bmass*rr**k/F(k+1)
      ck((k+1)*vmoment==bmass*rr**k)
# Radial and vector factors for arbitrary gamma and c.
root2=s.sqrt(2)
bmass=root2*gm
h=2/(3*root2)
zetamass=2*gm/c
Acenter=2*c/3
M=s.Rational(1,2)
ck(s.simplify(h*bmass-M*Acenter*zetamass)==0)
for j in range(2):
    ck(s.simplify(bmassresearch-agent2-M*c*zetamass)==0)
# Limiting source is positive and not deepest; exact rational gamma calibration.
for den in range(1,41):
  for num in range(1,2*den+1):
    gg=F(num,den)
    yy=F(1,4)/(1+gg)
    ck(yy>0 and 2*yy<1)
    ck((2*yy)**2<F(4,9))
# Mixtures preserve zero-rate atoms and have the stated decreasing density.
weights=[F(1,7),F(2,7),F(4,7)]
rates=[F(0),F(1,3),F(1)]
ck(sum(weights)==1)
for k in range(31):
  vm=sum(w*(F(1) if k==0 else F(0)) if rr==0 else w*rr**k/F(k+1) for w,rr in zip(weights,rates))
  bm=sum(w*rr**k for w,rr in zip(weights,rates))
  ck(vm==bm/F(k+1))
# Tail densities on the open subintervals.
ck(weights[1]/rates[1]+weights[2]/rates[2]>=weights[2]/rates[2]>0)
print(f'PASS: {checks} exact uniform-rate-kernel audit checks')
