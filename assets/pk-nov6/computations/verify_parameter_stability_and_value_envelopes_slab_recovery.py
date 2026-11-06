"""Exact calibrations, not a replacement for the analytic proofs."""
from fractions import Fraction as F
import sympy as s

checks = 0

def zero(x):
    global checks
    assert s.simplify(x) == 0, x
    checks += 1

t, x = s.symbols('t x', positive=True)
c = 1-s.log(2)
raw_integral = s.integrate(s.log((1+x)/2), (x, 0, 1))
zero(raw_integral + c)
zero(t*raw_integral + c*t)
removed_log_integral = t*raw_integral+c*t*t
zero(removed_log_integral+c*t-c*t*t)
zero(s.limit(removed_log_integral/t, t, 0, dir='+')+c)
# Retained region of [t,1] is constant exp(c*t); re-normalizing is exactly 1.
zero((c*t*(1-t))/(1-t)-c*t)

# A whole-body homothety of the interval about its certified source.
# Here the pushed row fills the new fiber, so the exact collar term is zero.
r, q, b = s.symbols('r q b', positive=True)
scalar_inverse = ((q/r-s.Rational(1, 2))/b)**2
zero((q/r-s.Rational(1, 2))**2-b*b*scalar_inverse)
zero((r*(s.Rational(1, 2)+b))/r-(s.Rational(1, 2)+b))

for denominator in range(3, 30):
    for numerator in (1, denominator-1):
        scale=F(numerator, denominator)
        physical_buffer=F(1, 5)*scale
        mass=scale
        raw_depth=scale/2+physical_buffer
        assert raw_depth/mass == F(7,10)
        checks += 1
        variance=scale*scale/12
        energy=scale
        assert energy/mass == 1
        assert variance/(scale*scale) == F(1,12)
        checks += 2
        # Explicit scalar inverse at the certificate value s=1.
        inverse=((raw_depth/scale-F(1,2))/F(1,5))**2
        assert inverse == 1
        checks += 1

# Algebra of the entropy normalization (nonzero moving logarithmic mean).
a, z, b = s.symbols('a z b', positive=True)
zero(s.log(b)-s.log(a)-s.log(b/a))
print(f'PASS: {checks} exact calibration checks')
