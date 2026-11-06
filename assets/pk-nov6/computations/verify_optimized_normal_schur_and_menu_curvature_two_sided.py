"""Exact identities for the two cap-curvature notes.

All global extrema, status cases, compatibility, and normal-gap claims
are proved in their Markdown sources rather than inferred from this file.
"""

import sympy as s

checks = 0


def eq(left, right):
    global checks
    assert s.factor(left-right) == 0
    checks += 1


eps, r, a, alpha, theta, t = s.symbols('eps r a alpha theta t')
lam = s.Rational(3, 2)/eps
threshold = 2-eps
level = s.Rational(9, 4)*(2-eps)
eq(s.Rational(9, 2)*r*r-s.Rational(3, 2)*lam*(2*r-threshold)**2,
   level-s.Rational(9, 2)*(2-eps)/eps*(r-1)**2)
eq(level-s.Rational(9, 2)*(threshold/2)**2,
   s.Rational(9, 8)*eps*(2-eps))
eq(3*lam*(3*eps**2/2)+3*level, s.Rational(27, 2))

indices = [-1, 0, 1]
rho = s.symbols('rho0:3')
p = s.symbols('p0:3')
q = s.symbols('q0:3')
phi = sum((2*(1+t*rho[k])+t*p[k]+alpha*j
           +theta*(t*q[k]-(1+t*rho[k])))**2
          for k, j in enumerate(indices))/(2*(1-theta))
base = {t: 0, alpha: 0, theta: 0}
eq(phi.subs(base), 6)
eq(s.diff(phi, alpha).subs(base), 0)
eq(s.diff(phi, theta).subs(base), 0)
eq(s.diff(phi, alpha, 2).subs(base), 2)
eq(s.diff(phi, theta, 2).subs(base), 3)
eq(s.diff(phi, alpha, theta).subs(base), 0)
eq(s.diff(phi, t, 2).subs(base), sum((2*rho[k]+p[k])**2 for k in range(3)))
eq(s.diff(phi, t, alpha).subs(base),
   sum(j*(2*rho[k]+p[k]) for k, j in enumerate(indices)))
eq(s.diff(phi, t, theta).subs(base), sum(p[k]+2*q[k] for k in range(3)))

affine = sum((2*(1+a*j)+alpha*j-theta*(1+a*j))**2 for j in indices)/(2*(1-theta))
eq(affine, 6+s.Rational(3, 2)*theta**2/(1-theta)
   +(2*a+alpha-a*theta)**2/(1-theta))
eq(affine.subs({alpha: -2*a, theta: 0}), 6)
eq(s.diff(affine, alpha).subs({alpha: -2*a, theta: 0}), 0)
eq(s.diff(affine, theta).subs({alpha: -2*a, theta: 0}), 0)
normal_hessian = s.hessian(affine, (alpha, theta)).subs({alpha: -2*a, theta: 0})
eq(normal_hessian[0, 0], 2)
eq(normal_hessian[0, 1], -2*a)
eq(normal_hessian[1, 1], 3+2*a*a)
eq(normal_hessian.det(), 6)
eq(affine.subs(alpha, 0),
   6+4*a*a+(s.Rational(3, 2)+a*a)*theta*theta/(1-theta))
eq(s.Rational(4, 9)*(s.Rational(27, 2)+9*a*a), 6+4*a*a)
eq((6*a)**2/s.Rational(3, 2), 24*a*a)
eq(s.Rational(3, 4)*24*a*a, 18*a*a)
eq(2+s.Rational(9, 2)*(1-s.Rational(1, 2))**2, s.Rational(25, 8))
eq(2*(1+s.Rational(1, 2))**2, s.Rational(9, 2))

# Two-group ownership: middle group owns {-1,0}, endpoint group owns {1}.
eq(affine.subs({alpha: -2*a, theta: 0}), 6)
eq(affine.subs({alpha: 0, theta: 0}), 6+4*a*a)
eq(sum(2*(2*a)**2 for _ in range(3)), 24*a*a)
eq(s.Rational(3, 4)*sum(2*(2*a)**2 for _ in range(3)), 18*a*a)
for av in [s.Rational(1, 20), s.Rational(1, 10), s.Rational(-1, 20)]:
    al = -2*av if av >= 0 else s.Integer(0)
    assert 3*al <= 0
    checks += 1
    eq(affine.subs({a: av, alpha: al, theta: 0}),
       6+4*min(av, 0)**2)
    assert 2*(1+av)**2 < 6
    checks += 1
print(f'PASS {checks} exact symbolic checks')
