"""Exact symbolic checks for the sampled projective Ball-body example."""
import sympy as sp

s = sp.symbols('s', real=True)
g = (1+s) / sp.sqrt((1+s)**2+1)
assert sp.simplify(sp.diff(g, s, 2) +
                   3*(1+s)/(((1+s)**2+1)**sp.Rational(5, 2))) == 0
assert sp.simplify(g.subs(s, 0)-1/sp.sqrt(2)) == 0
assert sp.simplify(g.subs(s, 1)-2/sp.sqrt(5)) == 0
assert sp.simplify(g.subs(s, sp.Rational(1, 2))-3/sp.sqrt(13)) == 0
assert sp.Rational(36, 13)-sp.Rational(13, 10) == sp.Rational(191, 130)
assert 191**2 > 16*1690
assert 191**2 == 36481
assert 16*1690 == 27040

t = sp.symbols('t', nonnegative=True)
ball_square = 2*sp.integrate(t, (t, 0, 1))
ball_diamond = 2*4*sp.integrate(t, (t, 0, 1/(2*(1+s))))
assert sp.simplify(ball_square+ball_diamond-1-1/(1+s)**2) == 0
assert 2+4+4+4+2 == 16
assert 4+4*sp.Rational(1, 2) == 6
print('PASS: exact Jacobian weights, Ball ray integral, strict curvature, '
      'midpoint gauge certificate, and source masses.')
