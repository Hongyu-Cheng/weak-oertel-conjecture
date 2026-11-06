"""Exact planar calibration of the analytically classified critical menu."""
from fractions import Fraction as F

d = 2
b = F(1, d+1)
gamma = (1-b)**d
eps = F(1, 10)
a = eps**d
Q = gamma+a
M = 2+a

# Strict rho_2 applicability: 3+(9/2)a < sqrt(10).
assert (3+F(9,2)*a)**2 < 10
assert a < (1-2*b)**d
L_min = 1-b

def tail_T(threshold):
    if threshold <= 0:
        return F(1)
    if threshold >= 1:
        return F(0)
    return (1-threshold)**d

def tail_A_nonorigin(threshold):
    if threshold <= 0:
        return a
    if threshold >= eps:
        return F(0)
    return (eps-threshold)**d

for L in (L_min, F(1), F(2), F(10)):
    endpoint_mass = tail_A_nonorigin(b-L)+tail_T(b+L)
    assert endpoint_mass == a
    assert gamma+endpoint_mass == Q
    t = b/L
    cost = (1/t+2)/3
    assert cost >= F(d+2,3)
    origin_cost = ((L+1-eps)/b+2)/3
    assert origin_cost-cost == (1-eps)/(3*b)
assert (L_min/b+2)/3 == F(4,3)
assert b/L_min == F(1,2)

# The analytic proof divides every excluded tilt at L=b-min_A lambda_i.
# Before that threshold the right cap has at least this STRICTLY greater
# mass; afterward A is full and the right cap remains positive until L_min.
assert tail_T(2*b) > a
assert Q/M-gamma/2 == a*(2-gamma)/(2*(2+a)) > 0
assert Q == F(409,900)
assert M == F(201,100)

print('PASS: strict profile range, exact canonical menu masses, '
      'optimal L=2/3, exit1/2, cost4/3, and above-OC gap.')
