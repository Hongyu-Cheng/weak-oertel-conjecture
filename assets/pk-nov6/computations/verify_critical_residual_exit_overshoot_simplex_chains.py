"""Exact rational planar calibration of the critical overshoot source."""
from fractions import Fraction as F

eps = F(1, 10)
gamma = F(4, 9)
endpoint_volume = eps**2
total_volume = 2 + endpoint_volume
budget = gamma + endpoint_volume
h_squared = 1 - gamma

# The proved exact-depth source applies: eps^2 < rho_2, using its
# equivalent squared rational comparison to sqrt(10).
assert 10 > (3 + F(9, 2)*endpoint_volume)**2
assert budget == F(409, 900)
assert budget > gamma*total_volume/2
assert 3*h_squared == F(5, 3)

# KKT quantities divided by the positive common height h.
s = (F(2),)*3
lam = (F(0), F(6), F(0))
mu = {(1, 0): F(2), (1, 2): F(2)}
base = (-1, 0, 1)
for i in range(3):
    out = sum(v for (a,b),v in mu.items() if a == i)
    incoming = sum(v for (a,b),v in mu.items() if b == i)
    assert lam[i] == s[i] + out - incoming
    assert sum(v*(base[b]-base[a]) for (a,b),v in mu.items() if a == i) == 0

for L in (F(2), F(7,2), F(10), F(1000)):
    # All canonical P caps include A, have their centroid cap at0, and
    # exclude +1; Q caps isolate the +1 canonical cap.
    assert L > F(1, 3)
    assert 1-L < F(1, 3)
    assert endpoint_volume + gamma == budget
    t = 1/(3*L)
    radius = 1-(1-eps)*t
    assert 0 < t < 1 and radius > 0
    assert F(1,3)-L*t == 0
    assert F(1,3)-L*t/2 > 0
    assert F(1,3)-L*(t+1)/2 < 0
    c = 1+(1/t-1)/3
    assert c == L+F(2,3)
    # Reweighted probabilities and the truncated base barycenter.
    w_left = 1/(3*c*t)
    w_center = 1/(3*c)
    w_right = 1/(3*c)
    assert w_left+w_center+w_right == 1
    assert -t*w_left+w_right == 0

print('PASS: exact critical-budget calibration, KKT row, exit fractions, '
      'and reweighted martingale; overshoot is symbolically L+2/3.')
