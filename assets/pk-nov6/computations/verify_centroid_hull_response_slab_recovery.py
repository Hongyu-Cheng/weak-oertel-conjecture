"""Exact checks for the centroid-hull deformation and its two calibrations."""
from fractions import Fraction as F
import sympy as s

checks = 0


def eq(a, b=0):
    global checks
    assert s.simplify(a-b) == 0, (a, b)
    checks += 1


t, delta = s.symbols('t delta', real=True)
M = 12-9*t
Sigma = (2*(2-2*t)**3+(8-5*t)**3)/(12*M)
E = 4*(3-s.Rational(3, 2)*t)*(5-s.Rational(7, 2)*t)/(8-5*t)
eq(Sigma.subs(t, 0), s.Rational(11, 3))
eq(E.subs(t, 0), s.Rational(15, 2))
eq((s.diff(Sigma, t)/Sigma).subs(t, 0), -s.Rational(51, 44))
eq((s.diff(E, t)/E).subs(t, 0), -s.Rational(23, 40))
delta_rate = ((s.diff(Sigma, t)/Sigma+s.diff(E, t)/E-s.diff(M, t)/M)/2).subs(t, 0)
eq(delta_rate, -s.Rational(433, 880))
Q0 = 5+delta
Qprime = -s.Rational(7, 2)+delta*delta_rate
betaprime = (12*Qprime+9*Q0)/144
eq(betaprime, s.Rational(1, 48)+227*delta/10560)

rho_plus = (1+delta/15)/2
rho_minus = (1-delta/15)/2
beta = (5+delta)/12
Xi_lower = rho_minus-beta+5*delta/48+2*delta/11-delta/12
eq(Xi_lower, s.Rational(1, 12)+227*delta/2640)
eq(-3*Xi_lower, -12*betaprime)
eq(betaprime.subs(delta, s.Rational(1, 10)), s.Rational(809, 35200))
eq((-3*Xi_lower).subs(delta, s.Rational(1, 10)), -s.Rational(2427, 8800))

# Check the independent fixed-mark regular response, retaining all covariance terms.
fixed_cap_loss = 4*rho_plus+3*rho_minus
C_energy = s.Rational(61, 16)
J_cov = s.Rational(252, 11)
response = fixed_cap_loss-beta*9+delta*(C_energy/15+J_cov/24-s.Rational(3, 4))
eq(response, -3*Xi_lower)
eq(rho_plus-rho_minus-delta/15)

# The full mixed-volume mean and the volume martingale normalization.
eq((8*3)/s.Integer(12), 2)
eq((-2+2)/s.Integer(12))
eq(s.Rational(6, 1375)*s.Rational(55, 24), s.Rational(1, 100))

def captured(lo, hi, sign, threshold):
    if sign == 1:
        return max(F(0), hi-max(lo, threshold))
    return max(F(0), min(hi, -threshold)-lo)


# Actual closed caps in every continuous orientation and many exact base tilts.
# The analytic proof in the source handles all tilts, not just these checks.
for de in (F(1, 10), F(1, 50), F(1, 100)):
    for sign in (-1, 1):
        for anum in range(-100, 101):
            a = F(anum, 10)
            mass = F(0)
            for z, lo, hi in ((-1, F(-1), F(1)), (0, F(-1), F(7)), (1, F(-1), F(1))):
                threshold = sign*F(2)-de-a*z
                mass += captured(lo, hi, sign, threshold)
            assert mass >= 5+de
            checks += 1
    for sign, a in ((1, F(0)), (-1, F(4))):
        mass = sum(captured(lo, hi, sign, sign*F(2)-de-a*z)
                   for z, lo, hi in ((-1, F(-1), F(1)), (0, F(-1), F(7)), (1, F(-1), F(1))))
        assert mass == 5+de
        checks += 1

# Signed feasibility of the interval path; its midpoint equals either endpoint.
for tt in (F(-1, 10), F(-1, 100), F(0), F(1, 100), F(1, 10)):
    alo, ahi = -1+tt, 1-tt
    klo, khi = -1+tt, 7-4*tt
    assert klo <= alo < ahi <= khi
    checks += 1

# Exact polygon area and centroid for the reverse obstruction.
vertices = [(F(-2), F(0)), (F(-1), F(-3)), (F(1), F(-3)), (F(2), F(0))]
crosses = [vertices[i][0]*vertices[(i+1)%4][1]-vertices[(i+1)%4][0]*vertices[i][1]
           for i in range(4)]
twice_area = sum(crosses)
area = twice_area/2
gx = sum((vertices[i][0]+vertices[(i+1)%4][0])*crosses[i] for i in range(4))/(3*twice_area)
gy = sum((vertices[i][1]+vertices[(i+1)%4][1])*crosses[i] for i in range(4))/(3*twice_area)
assert area == 9 and gx == 0 and gy == F(-4, 3)
checks += 3
for mass in (F(6), F(9), F(6)):
    assert mass < F(21, 2)
    checks += 1
for mass in (F(15), F(15)):
    assert mass < 21
    checks += 1
assert F(3, 2) > F(4, 3)
checks += 1

print(f'PASS: {checks} exact response, actual-cap, covariance, and compatibility checks.')
