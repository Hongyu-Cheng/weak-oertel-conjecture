"""Exact certificates for the strict five-fiber two-dimensional motion."""

from fractions import Fraction as F
import sympy as s

checks = 0


def ck(condition):
    global checks
    assert condition
    checks += 1


def eq(left, right):
    ck(s.factor(left-right) == 0)


indices = [-2, -1, 0, 1, 2]
radii = [F(4, 5), F(19, 20), F(1), F(19, 20), F(4, 5)]
mode = [F(1), F(0), -F(8, 5), F(0), F(1)]
for k in range(1, 4):
    ck(radii[k-1]-2*radii[k]+radii[k+1] == -F(1, 10))
R = sum(x*x for x in radii)
E = sum(x*x for x in mode)
ck(R == F(817, 200))
ck(E == F(114, 25))
ck(sum(j*j for j in indices) == 10)
ck(sum(r*j for r, j in zip(radii, indices)) == 0)
ck(sum(r*e for r, e in zip(radii, mode)) == 0)
ck(sum(j*e for j, e in zip(indices, mode)) == 0)
for parity in [0, 1]:
    ck(sum(r*j for r, j in zip(radii, indices) if j % 2 == parity) == 0)
    ck(sum(r*e for r, e, j in zip(radii, mode, indices) if j % 2 == parity) == 0)
Q = 2*R
U = 2*radii[3]**2+F(9, 2)*radii[4]**2
lower = 2*sum(x*x for x in radii[:4])
ck(Q == F(817, 100))
ck(U == F(937, 200))
ck(lower == F(689, 100))
ck(lower > U and Q > U)
ck(F(9, 2) < F(9, 4)*R)

a, b, alpha, theta, A, B = s.symbols('a b alpha theta A B')
rs = [s.Rational(r.numerator, r.denominator)+a*j
      +b*s.Rational(e.numerator, e.denominator)
      for r, j, e in zip(radii, indices, mode)]
RR = s.Rational(R.numerator, R.denominator)
EE = s.Rational(E.numerator, E.denominator)
eq(sum(x*x for x in rs), RR+10*a*a+EE*b*b)
eq(sum(j*x for j, x in zip(indices, rs)), 10*a)
phi = sum(((2-theta)*x+alpha*j)**2
          for x, j in zip(rs, indices))/(2*(1-theta))
eq(phi, (2-theta)**2*(RR+EE*b*b)/(2*(1-theta))
   +5*(alpha+(2-theta)*a)**2/(1-theta))
eq(phi.subs({alpha: -2*a, theta: 0}), 2*RR+2*EE*b*b)
eq(phi.subs({alpha: 0, theta: 0}), 2*RR+20*a*a+2*EE*b*b)
for var in [alpha, theta]:
    eq(s.diff(phi, var).subs({alpha: -2*a, theta: 0}), 0)
normal_hessian = s.hessian(phi, (alpha, theta)).subs({a: 0, b: 0, alpha: 0, theta: 0})
eq(normal_hessian[0, 0], 10)
eq(normal_hessian[0, 1], 0)
eq(normal_hessian[1, 1], RR)
mass = s.Rational(9, 2)*(RR+10*a*a+EE*b*b)
eq(mass, s.Rational(7353, 400)+45*a*a+s.Rational(513, 25)*b*b)
normalized_mass = mass*RR/(RR+EE*b*b)
eq(normalized_mass-s.Rational(9, 2)*RR, 45*RR*a*a/(RR+EE*b*b))
eq(s.Rational(3, 4)*3*40*A*A, 90*A*A)
eq(s.Rational(3, 4)*3*4*EE*B*B, 9*EE*B*B)
print(f'PASS {checks} exact arithmetic and symbolic checks')
