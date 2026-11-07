"""Exact identities for the complete direct low-sector proof.

No floating-point arithmetic, search tolerance, or sampled sign inference.
"""
import sympy as s
from fractions import Fraction as Q

k,v=s.symbols('k v')
beta=k*v/3
t=s.Rational(1,3)
P=t-2*beta
Im=2*t**3/(k-2*beta)-2*beta*t**3/(3*(k-2*beta)**2)
Ip=2*(t+beta)*P**2/(k+2*beta)+2*beta*P**3/(3*(k+2*beta)**2)
Om=s.Rational(4,9)
Op=4*(t+beta)*P
H=s.factor(Im+Ip+(Om+Op)/2-3*beta*P/4+s.Rational(4,81)
           -s.Rational(4,9)*(1/(3*k)+s.Rational(1,2)+3*k/16))
N=(k**3*(96*v**6-1152*v**5-432*v**4+7776*v**3-7290*v**2)
   +k**2*(-432*v**5-3888*v**4+9720*v**3+1944*v**2-8019*v-2187)
   +k*(-896*v**4+4320*v**3-3744*v**2-5832*v+7128)
   -768*v**4+1152*v**2)
assert s.cancel(H-N/(324*k*(2*v-3)**2*(2*v+3)**2))==0
P3=4*v**2*(16*v**4-192*v**3-72*v**2+1296*v-1215)
P2=144*v**5+1296*v**4-3240*v**3-648*v**2+2673*v+729
derivative=(k**3*P3-k**2*P2-128*v**2*(3-2*v**2))/(108*k**2*(2*v-3)**2*(2*v+3)**2)
assert s.cancel(s.diff(H,k)-derivative)==0
Qpoly=48*v**6-1008*v**5-8968*v**4+22248*v**3-4581*v**2-19683*v+12069
assert s.cancel(H.subs(k,s.Rational(1,2))-Qpoly/(648*(2*v-3)**2*(2*v+3)**2))==0


def expansion(coeff):
    degree=len(coeff)-1
    return sum(s.Rational(c.numerator,c.denominator)*s.binomial(degree,j)
               *v**j*(1-v)**(degree-j) for j,c in enumerate(coeff))


coeff2=list(map(Q,['729','6318/5','8667/5','9072/5','7209/5','954']))
coeffQ=list(map(Q,['12069','17577/2','26013/5','24237/10','2899/3','3475/6','125']))
assert all(c>0 for c in coeff2+coeffQ)
assert s.expand(P2-expansion(coeff2))==0
assert s.expand(Qpoly-expansion(coeffQ))==0

# Reconstruct the sharp equality directly from the finite original sums.
kk=Q(2,3);bb=Q(1,6);tt=Q(1,3)
W=sum(max(1-kk*h,0)**2 for h in range(4))
K=sum(4*(tt-bb*h)*max(tt-(kk-2*bb)*h,0)
      +4*(tt+bb*(h+1))*max(tt-2*bb-(kk+2*bb)*h,0) for h in range(4))
assert K-Q(4,9)*W == -Q(4,81)
print('PASS: all rational identities, all 13 positive Bernstein coefficients, exact sharp equality')
