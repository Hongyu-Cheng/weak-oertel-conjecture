"""Exact arithmetic checks for the regression-sharpness certificate."""
import sympy as sp

L = sp.symbols('L', positive=True)
a0, a1, a2 = sp.symbols('a0 a1 a2')
bases = [(0, 0), (1, 0), (0, 1), (1, 1)]
signs = [1, -1, -1, 1]
features = [sp.Matrix([1, z[0], z[1]]) for z in bases]

G = sp.zeros(3, 3)
B = sp.zeros(1, 3)
Q = sp.Integer(0)
R = sp.Integer(0)
for z, e, q in zip(bases, signs, features):
    G += q * q.T
    B += e * L * q.T
    Q += e * e * L
    R += L**2 + sp.Rational(1, 12)

assert G.det() == 4
assert B == sp.zeros(1, 3)
assert Q == 4 * L
assert sp.simplify(R - Q**2 / 4) == sp.Rational(1, 3)
assert sp.simplify(R / (Q**2 / 4) - 1) == 1 / (12 * L**2)
assert sp.expand(sum(e * (a0 + a1*z[0] + a2*z[1])
                     for z, e in zip(bases, signs))) == 0
for e in [-1, 1]:
    selected = [z for z, eps in zip(bases, signs) if eps == e]
    assert len(selected) == 2
    assert [sum(z[j] for z in selected) for j in range(2)] == [1, 1]
    assert sum(sp.Rational(1, 2) for z in bases) == 2
    assert [sum(sp.Rational(1, 2)*z[j] for z in bases)
            for j in range(2)] == [1, 1]

print('PASS: affine cancellation, exact normal stress moments, '
      'regression covariance, and sharp limiting coefficient.')
