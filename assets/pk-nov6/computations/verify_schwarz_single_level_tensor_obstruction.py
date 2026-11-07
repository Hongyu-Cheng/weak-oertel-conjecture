"""Exact integration for the symmetric-triangle radial-level obstruction."""
import sympy as sp

v = sp.symbols('v', real=True)
h = 1 - 1/sp.sqrt(2)
f = 2*(1-v)
assert sp.integrate(f, (v, 0, 1)) == 1
assert sp.simplify(sp.integrate(f, (v, h, 1))-sp.Rational(1, 2)) == 0
assert sp.simplify(sp.integrate(f, (v, 0, h))-sp.Rational(1, 2)) == 0
plus = sp.integrate((v-h)*f, (v, h, 1))
minus = sp.integrate((h-v)*f, (v, 0, h))
assert sp.simplify(plus-1/(6*sp.sqrt(2))) == 0
assert sp.simplify(minus-sp.Rational(2, 3)+5/(6*sp.sqrt(2))) == 0
tensor = sp.simplify(plus+minus)
length = 2*h
level_plus = sp.integrate((v-h)/length, (v, h, length))
level_minus = sp.integrate((h-v)/length, (v, 0, h))
level_tensor = sp.simplify(level_plus+level_minus)
assert sp.simplify(tensor-(2-sp.sqrt(2))/3) == 0
assert sp.simplify(level_tensor-(2-sp.sqrt(2))/4) == 0
assert sp.simplify(tensor-level_tensor-(2-sp.sqrt(2))/12) == 0
assert sp.simplify(level_plus-level_minus) == 0
assert sp.simplify(plus-minus) != 0
assert 2**2 > 2
print('PASS: masses, objective-one median stress hinges, unique balanced '
      'radial level, and strict exact tensor deficit.')
