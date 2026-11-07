"""Exact arithmetic diagnostics; the all-dimensional proof is in the note."""
from fractions import Fraction as F
from math import factorial

assert F(11, 20)**2 + F(1, 10)**2 == F(5, 16)
assert F(5, 16) < F(1, 3)
assert F(609, 200)**2 == F(370881, 40000) < 10

checks = 3
for d in range(2, 151):
    eps = F(1, 10)
    gamma = F(d, d+1)**d
    v = F(1, factorial(d))
    a = eps**d
    r = (1+eps)/2
    assert r**d + a <= F(5, 16) < F(1, 3) < gamma
    assert F(d, d+1) > r
    assert gamma * v < gamma * (2+a)*v/2
    assert max(v, a*v) < (2+a)*v/2
    checks += 4

d = 2
v = F(1, 2)
a = F(1, 100)
gamma = F(4, 9)
m = (2+a)*v
assert m == F(201, 200)
assert gamma*m/2 == F(67, 300)
assert gamma*m/2-gamma*v == F(1, 900)
assert (gamma+a)*v == F(409, 1800)
assert (gamma+a)*v-gamma*m/2 == F(7, 1800)
checks += 5
print(f"PASS: {checks} exact arithmetic checks")
