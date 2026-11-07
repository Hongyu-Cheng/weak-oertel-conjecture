"""Exact algebra for the active-cap integer-flux obstruction."""
from fractions import Fraction as Q
import sympy as s

t = (4 - s.sqrt(7)) / 3
delta = t - s.Rational(4, 9)
D = 2*t-t*t
V0 = s.Rational(3, 2)
V1 = delta**2/4
M = V0+V1
g0 = s.Rational(4, 9)
c = g0+delta/2
eps = delta/4

def zero(expr):
    assert s.simplify(expr) == 0, s.simplify(expr)

# Elementary square comparisons prove 5/2 < sqrt(7) < 8/3,
# hence 4/9 < t < 1/2 and 0 < delta < 1/18.
assert Q(5, 2)**2 < 7 < Q(8, 3)**2
assert Q(64, 81) > Q(3, 4)
assert Q(1, 2592) < Q(2, 3)
zero(3*t*t-8*t+3)
zero(D-(1+2*s.sqrt(7))/9)
zero(V0-(2*t-t*t/2)-D)
zero(c+eps-(t-delta/4))

# Trapezoid area and centroid, from its horizontal section lengths.
y = s.symbols('y')
zero(s.integrate(2-y, (y, 0, 1))-V0)
zero(s.integrate(y*(2-y), (y, 0, 1))/V0-g0)

# Right-cap triangle formula and derivative factorization.
q, T = s.symbols('q T', positive=True)
A = (1+q*T)**2/(2*(q+s.Rational(1, 2)))
zero(s.diff(A, q)-(1+q*T)*(q*T+T-1)/(2*(q+s.Rational(1, 2))**2))
qstar = 1/t-1
zero(A.subs({q:qstar,T:t})-D)
zero((1-T)**2-T/2-(T-s.Rational(1, 2))*(T-2))

# Each transition agrees with the adjacent horizontal integration formula.
q1 = s.Rational(1, 2)/(1-T)
zero(A.subs(q,q1)-(s.Rational(3, 4)-q1*(s.Rational(1, 2)-T)))
zero(s.integrate(2-y, (y, t, 1))-D)

# Exact divergence, closed-cap probabilities, and negative flux.
mean = (V0*g0+V1*c)/M
flow = V0*(mean-g0)
zero(flow-V0*V1*delta/(2*M))
zero(flow-V1*(c-mean))
flux = flow*(-D/V0)
zero(flux+delta**3*D/(8*M))

# Direct cap-centered decomposition agrees with the tree formula.
global_centered_tail = s.integrate((y-mean)*(2-y), (y,t,1))
fiber_centered_tail = s.integrate((y-g0)*(2-y), (y,t,1))
zero(global_centered_tail-fiber_centered_tail-flux)

# The complete active trapezoid circuit has positive flux after isolation.
R = 4*(1-t)/(2-t)
zero(2*(2*t)*qstar-R*(2-t))
zero(2*(5*qstar+1)-3*R-(20*t*t-38*t+20)/(t*(2-t)))
assert 19**2-4*10*10 < 0
C0 = D*V1*delta/(2*M)
side_mean_difference = -qstar*delta-qstar*delta/2
zero(-(D*V1/M)*side_mean_difference-3*qstar*C0)
zero(6*qstar-R-2*(1-t)*(6-5*t)/(t*(2-t)))

# Mean-only outside-fiber control cannot replace zero outside cap mass.
def two_equal_fiber_flux(mean0, mean1, prob0, prob1):
    mean = (mean0+mean1)/2
    return (mean0-mean)*prob0+(mean1-mean)*prob1
jplus = two_equal_fiber_flux(Q(-97,4),Q(-1,2),Q(3,4),Q(1,4))
jminus = two_equal_fiber_flux(Q(97,4),Q(-1,2),Q(1,4),Q(3,4))
assert jplus == Q(-95,16) and jminus == Q(-99,16)
assert jplus+jminus == Q(-97,8)

print('PASS: exact center, cap regimes, flow divergence, single negative flux, and positive isolated active-circuit flux')
