"""Exact algebra checks of the one-sided jet formulas; not an OC proof."""

import sympy as s

t, x = s.symbols("t x", real=True)


def check_profile(d, knots, pieces):
    assert len(pieces) == len(knots) + 1
    checks = 0
    for k, T in enumerate(knots):
        left, right = pieces[k], pieces[k + 1]
        F = left.subs(x, T)
        assert F == right.subs(x, T)
        fminus = s.diff(left, x).subs(x, T)
        fplus = s.diff(right, x).subs(x, T)
        hminus = s.diff(left, x, 2).subs(x, T)
        hplus = s.diff(right, x, 2).subs(x, T)
        for q in map(s.Rational, [-2, -1, 0, 1, 2]):
            for r in map(s.Rational, [-3, -1, 0, 1, 3]):
                side = s.sign(q) if q else s.sign(r)
                chosen = right if side >= 0 else left
                D = fplus * q if q >= 0 else fminus * q
                if q > 0:
                    E = hplus * q * q + fplus * r
                elif q < 0:
                    E = hminus * q * q + fminus * r
                else:
                    E = fplus * r if r >= 0 else fminus * r
                for A, B in [(s.Rational(2, 3), s.Rational(-5, 7)),
                             (s.Rational(-4, 5), s.Rational(3, 2)),
                             (s.Integer(0), s.Integer(0))]:
                    density = (1 + t * A + t * t * B / 2) ** (-d)
                    expression = density * chosen.subs(x, T + t*q + t*t*r/2)
                    actual = s.series(expression, t, 0, 3).removeO().expand()
                    first = D - d * A * F
                    second = E - 2*d*A*D + (d*(d+1)*A*A-d*B)*F
                    expected = F + t*first + t*t*second/2
                    assert s.expand(actual - expected) == 0, (d, T, q, r, A, B)
                    checks += 1
    return checks


total = 0
# Interval [0,1]: nonzero boundary-area jumps at both endpoints.
total += check_profile(1, [s.Integer(0), s.Integer(1)],
                       [s.Integer(1), 1-x, s.Integer(0)])
# Unit triangle, cut by x_1: an inside facet and outside vertex.
total += check_profile(2, [s.Integer(0), s.Rational(1, 3), s.Integer(1)],
                       [s.Rational(1, 2), (1-x)**2/2,
                        (1-x)**2/2, s.Integer(0)])
# Unit square, raw cut x_1+x_2>=x: F'' jumps at a proper section.
# This checks scalar-profile algebra, so normalization of that raw normal
# has no role; rescaling the scalar threshold gives the unit-normal version.
total += check_profile(2, [s.Integer(0), s.Integer(1), s.Integer(2)],
                       [s.Integer(1), 1-x*x/2, (2-x)**2/2, s.Integer(0)])
# Tetrahedron, cut by x_1, including a proper section and a support vertex.
total += check_profile(3, [s.Integer(0), s.Rational(1, 4), s.Integer(1)],
                       [s.Rational(1, 6), (1-x)**3/6,
                        (1-x)**3/6, s.Integer(0)])
print(f"PASS: {total} exact one-sided weighted-profile expansions")
