"""Exact symbolic calibration; the transport theorem has a prose proof."""
import sympy as S

s, e, l, t = S.symbols("s e l t", positive=True)
V = l**2 / 2 + 2 * l * t + t**2
J = l**3 / 6 + l**2 * t + S.Rational(3, 2) * l * t**2 + t**3 / 2

# Independent square-minus-triangle moments.
assert S.expand((l + t)**2 - l**2 / 2 - V) == 0
assert S.expand((l + t)**3 / 2 - l**2 / 2 * (2*l/3 + t) - J) == 0

g = J / V
defect = g.subs({l: (1+s)/2, t: e/2}) - (S.Rational(1, 3) + g.subs({l: s, t: e}))/2
factor = (
    e**2 * (2*e**2 + 2*e*s + e + s**2 + s)
    / (6*(2*e**2 + 4*e*s + s**2)*(2*e**2 + 4*e*s + 4*e + s**2 + 2*s + 1))
)
assert S.cancel(defect - factor) == 0
assert S.simplify(S.diff(factor, e).subs(e, 0)) == 0
assert S.simplify(S.diff(factor, e, 2).subs(e, 0)/2 - 1/(6*s*(s+1))) == 0

vA = S.Rational(1, 2)
vB = V.subs({l: s, t: e})
vC = V.subs({l: (1+s)/2, t: e/2})
delta = 1 - ((S.sqrt(vA) + S.sqrt(vB))/2)**2/vC
assert S.simplify(delta.subs(e, 0)) == 0
assert S.simplify(S.diff(delta, e).subs(e, 0)) == 0
assert S.simplify(S.diff(delta, e, 2).subs(e, 0)/2 - 2/(s*(s+1)**2)) == 0
assert S.simplify((1/(6*s*(s+1))) / ((2/(s*(s+1)**2))*((1+s)/2)) - S.Rational(1, 6)) == 0

print("PASS 9 exact symbolic identities for arbitrary positive s")
