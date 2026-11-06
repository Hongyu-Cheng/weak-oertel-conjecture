"""Exact algebra checks for the proved tilt identities and shortcut obstruction.

These identities supplement, rather than replace, the all-phase proof.
"""
import sympy as s

t, p = s.symbols("t p", real=True)
checks = 0


def zero(x):
    global checks
    assert s.factor(x) == 0, s.factor(x)
    checks += 1


# f(v)=(2 exp(-|v|/2)-exp(-|v|))/6.
A = (2 / (s.Rational(1, 2) - t) - 1 / (1 - t)) / 6
B = A.subs(t, -t)
Z = (1 - t) * (1 - 2 * t) * (1 + 2 * t) * (1 + t)
zero(A + B - 1 / Z)
F = s.factor(Z * A)
G = s.factor(A * B / (A + B))
zero(F.subs(t, 0) - s.Rational(1, 2))
zero(Z.subs(t, -s.Rational(1, 4)) - s.Rational(45, 64))
zero(F.subs(t, -s.Rational(1, 4)) - s.Rational(7, 32))
zero(G.subs(t, -s.Rational(1, 4)) - s.Rational(35, 144))
zero(B.subs(t, s.Rational(1, 2)) / (2 * s.Rational(1, 6)) - s.Rational(2, 3))
zero(B.subs(t, 1) / s.Rational(1, 6) - s.Rational(5, 6))
zero(s.Rational(2, 3) * (1 - 2 * (-s.Rational(1, 4))) - 1)
assert s.Rational(35, 144) < s.Rational(1, 4)
checks += 1

# Common reciprocal difference of forward-tilted opposite pairs.
P = p / (1 - t * p)
R = p / (1 + t * p)
zero(1 / P - 1 / R + 2 * t)
zero(2 / (1 / P + 1 / R) - p)

# The derivative numerator for the tilted omitted-coordinate gauge.
H = s.Function("H")(t)
beta = 1 - p * t
N = beta * s.diff(H, t) + p * H
zero(s.diff(H / beta, t) - N / beta**2)
zero(s.diff(N, t) - beta * s.diff(H, t, 2))

# General two-positive positive-half transform, used only as an identity.
q, X, Y, f0, rho, bb = s.symbols("q X Y f0 rho bb")
AA = (X / bb - q * Y / (1 - q + q * bb)) / (1 - q)
delta = (1 - q) / q
LL = delta / (1 - rho)
zero((bb * AA).subs({X: f0 * (1 - q) / (1 - rho), Y: rho * f0 * (1 - q) / (1 - rho)})
     - f0 * (bb + LL) / (bb + delta))

print(f"{checks} exact tilt identities and rational certificates PASS")
