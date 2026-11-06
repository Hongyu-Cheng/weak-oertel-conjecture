"""Exact calibrations for the sampled-majorant theorem; not its analytic proof."""
from fractions import Fraction as Q
import sympy as s

checks = 0

def check(ok):
    global checks
    assert ok
    checks += 1

x, t, h, c = s.symbols('x t h c', positive=True)
l3 = s.log(3)
rho = 1 / (2*l3*(1+x/2))
y = 2/l3-2
check(s.simplify(s.integrate(rho, (x, -1, 1))-1) == 0)
check(s.simplify(s.integrate(x*rho, (x, -1, 1))-y) == 0)
check(s.simplify(1+y/2-1/l3) == 0)
check(s.simplify(s.integrate(c*(1+x/2)*rho, (x, -1, 1))-c/l3) == 0)
check(s.simplify(rho/(c/l3)-1/(2*c*(1+x/2))) == 0)
source_log = s.log((c*(1+(y-t*h)/2))/(c/l3))
check(s.simplify(s.diff(source_log, t).subs(t, 0)+h*l3/2) == 0)
check(s.simplify((s.log(c/2)-s.log(3*c/2))/2+l3/2) == 0)

# Exact log normalization of the downward boundary layer.
layer_integral = s.integrate(s.log(s.Rational(1, 2)+x/(2*t)), (x, 0, t))
check(s.simplify(layer_integral-t*(s.log(2)-1)) == 0)
check(s.simplify(layer_integral+t*(1-s.log(2))) == 0)

# Sampled sqrt-base plane: equality at 0,1; strict failure at interior 1/4.
check(1+s.sqrt(0) == 1)
check(1+s.sqrt(1) == 2)
check(1+s.Rational(1, 4) < 1+s.sqrt(s.Rational(1, 4)))

# Actual compatible product fibers with positive concave quadratic parameters.
# The finite base slope is the closest point to 0 in its exact feasible interval.
P = tuple(range(-2, 3))
for a in (Q(1, 4), Q(1, 2), Q(1)):
    for e in (Q(-2), Q(-1, 3), Q(0), Q(2, 3), Q(2)):
        for p in P:
            lower = [e-a*(z+p) for z in P if z > p]
            upper = [e-a*(z+p) for z in P if z < p]
            lo = max(lower) if lower else None
            hi = min(upper) if upper else None
            alpha = Q(0)
            if lo is not None and alpha < lo:
                alpha = lo
            if hi is not None and alpha > hi:
                alpha = hi
            check(lo is None or alpha >= lo)
            check(hi is None or alpha <= hi)
            for yy in (Q(-1, 2), Q(0), Q(2, 3)):
                b = Q(1, 3)
                f = Q(1, 5)
                cc = f-2*b*yy
                source = Q(20)-a*p*p-b*yy*yy+e*p+f*yy
                check(source > 0)
                for z in P:
                    residual = alpha*(z-p)+a*(z*z-p*p)-e*(z-p)
                    check(residual >= 0)
                    for xx in (Q(-1), Q(-2, 5), Q(0), Q(3, 7), Q(1)):
                        U = Q(20)-a*z*z-b*xx*xx+e*z+f*xx
                        A = source+cc*(xx-yy)+alpha*(z-p)
                        check(U > 0)
                        check(A-U == residual+b*(xx-yy)**2)
                        check(A >= U)
                check(source+cc*(yy-yy)+alpha*(p-p) == source)

# Signed sharp coefficient for both directions and zero speed.
for hh in (Q(k, 7) for k in range(-14, 15)):
    check(s.simplify((-s.Rational(hh.numerator, hh.denominator)*l3/2)
                     -(s.Rational(hh.numerator, hh.denominator)/2)
                      *s.log(s.Rational(1, 3))) == 0)

print(f"PASS: {checks} exact sampled-majorant calibration checks")
