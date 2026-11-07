"""Exact rational check of the actual q=2 obstruction; no numerical search."""
from fractions import Fraction as F

q = 2
a = F(1, 2)
bases = (-1, 0, 1)
V = F(2)**q
root_plus = tuple(1 + a*z for z in bases)
root_minus = tuple(1 - a*z for z in bases)
residual_plus = tuple(r**q for r in root_plus)
residual_minus = tuple(r**q for r in root_minus)
residual_zero = (V - 1,) * 3
e_power = tuple(min(A, B, C) for A, B, C in zip(
    residual_plus, residual_minus, residual_zero))
assert e_power == (F(1, 4), F(1), F(1, 4))

h = (F(1),)*3
s = (F(2),)*3
lam = (F(0), F(6), F(0))
mu = {(1, 0): F(2), (1, 2): F(2)}
pi = {(1, j): F(2) for j in range(3)}
for i in range(3):
    outgoing = sum(value for (ii, j), value in mu.items() if ii == i)
    incoming = sum(value for (j, ii), value in mu.items() if ii == i)
    assert lam[i] == s[i] + outgoing - incoming
    assert sum(value*(bases[j]-bases[i]) for (ii, j), value in mu.items()
               if ii == i) == 0
    assert sum(value for (ii, j), value in pi.items() if ii == i) == lam[i]
    assert sum(value*(bases[j]-bases[i]) for (ii, j), value in pi.items()
               if ii == i) == 0
for j in range(3):
    assert sum(value for (i, jj), value in pi.items() if jj == j) == s[j]
for (i, j), value in mu.items():
    assert value*(h[i]-h[j]) == 0

assert sum(root_plus)/3 == 1
assert sum(residual_plus)/3 == F(7, 6)
captured_plus = tuple(V - r for r in residual_plus)
assert captured_plus[1] == 3
assert sum(captured_plus)/3 == F(17, 6)
assert sum(captured_plus) == F(17, 2)
assert 3*V == 12
assert sum(hh**q for hh in h) == 3

# In barycentric-height coordinates, all cap traces are exact intervals in
# height, and their minimum upper threshold is never above H_0's threshold.
for z in bases:
    assert min(1+a*z, 1-a*z) <= 1
    assert 0 < 1+a*z < 2
    assert 0 < 1-a*z < 2

print('PASS: exact KKT, affine row, positive residuals, root equality, '
      'strict volume defect, and actual global cap masses.')
