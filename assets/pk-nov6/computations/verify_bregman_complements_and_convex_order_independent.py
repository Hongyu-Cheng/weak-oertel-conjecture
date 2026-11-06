"""Exact algebra certificates; analytical attainment proof is in the note."""
from fractions import Fraction as F
import sympy as s

checks = 0


def check(a, b):
    global checks
    assert s.simplify(a - b) == 0, (a, b)
    checks += 1


def psi(q):
    return min(F(1), max(F(0), 1 + q))


def J(q):
    return (max(F(0), q + 1) ** 2 - max(F(0), q) ** 2) / 2


def B(q, v):
    return J(q + v) - J(q) - psi(q) * v


for i in range(-18, 19):
    q = F(i, 4)
    check(psi(-1 - q), 1 - psi(q))
    for j in range(-18, 19):
        v = F(j, 5)
        check(B(-1 - q, -v), B(q, v))
        assert B(q, v) >= 0

p = [(1, 0), (0, 1), (-1, -1)]
neg = [(-x, -y) for x, y in p]
complete = {(x, y) for x in range(-1, 2) for y in range(-1, 2)
            if abs(x - y) <= 1}
assert complete == {(0, 0), *p, *neg}
checks += 1
for coord in range(2):
    check(sum(v[coord] for v in p), 0)
    check(sum(v[coord] for v in neg), 0)

for sign in [-1, 1]:
    out = sum(F(1, 2) * max(0, sign * (x + y) - 1) for x, y in p)
    inside = sum(F(1, 2) * max(0, sign * (x + y) - 1) for x, y in neg)
    check(out, F(1, 2) if sign == -1 else 0)
    check(inside, F(1, 2) if sign == 1 else 0)

for a in range(-4, 5):
    for b in range(-4, 5):
        for t in [F(-7, 3), F(1, 4), F(5, 2)]:
            vo = [t * (a * x + b * y) for x, y in p]
            vi = [t * (a * x + b * y) for x, y in neg]
            check(sum(B(F(-1, 2), v) for v in vo),
                  sum(B(F(-1, 2), v) for v in vi))
            check(sum(v * v for v in vo), sum(v * v for v in vi))
            check(sum(abs(v) for v in vo), sum(abs(v) for v in vi))

x, R, H = s.symbols('x R H', positive=True)
check(s.integrate(1 - x*x, (x, -1, 1)), s.Rational(4, 3))
check(s.integrate(x*x, (x, -1, 1)), s.Rational(2, 3))
check(s.integrate(1 - x*x, (x, 0, 1)), s.Rational(2, 3))
variance_t = (4*R**2 * R**2/3 + 4*R/12) / (4*R**2 + 4*R)
check(variance_t, (4*R**3 + 1)/(12*(R+1)))
check((R**2/3)/variance_t, 4*R**2*(R+1)/(4*R**3+1))
check(4*R**2*(R+1)/(4*R**3+1)-1,
      (4*R**2-1)/(4*R**3+1))

# The rectangle projection bound on its sloping interval is affine;
# checking its two endpoints proves it on that interval.
m, ell = s.symbols('m ell', positive=True)
f_ratio = (m + ell - x)/(2*ell)
lower = 1 - x/m
check((f_ratio - lower).subs(x, m-ell), (m-ell)/m)
check((f_ratio - lower).subs(x, m), s.Rational(1, 2))
w, f0 = s.symbols('w f0', positive=True)
check(s.integrate(f0*(1-x/m)*(1-x/w), (x, 0, w)),
      f0*(w/2-w*w/(6*m)))
print(f'PASS: {checks} exact Bregman, lattice, complement, and normal-bound certificates')
