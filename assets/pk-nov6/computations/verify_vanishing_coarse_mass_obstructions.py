"""Exact arithmetic checks for the null-coarse-mass examples.

The all-cap and weak-convergence arguments are in the companion note.
No finite numerical optimization is used in those proofs.
"""

from fractions import Fraction as F
import sympy as sp

eps = sp.symbols("eps", positive=True)
v, x, z = sp.symbols("v x z", real=True)

# Two triangle areas, the full-dimensional tetrahedral hull limit,
# and conditional weak-limit normalization and median.
assert sp.integrate(eps * (v + 1), (v, -1, 1)) == 2 * eps
assert sp.integrate(4 * z * (1 - z), (z, 0, 1)) == sp.Rational(2, 3)
assert sp.integrate((v + 1) / 4, (v, -1, 1)) == sp.Rational(1, 2)
median = sp.sqrt(2) - 1
assert sp.simplify((median + 1)**2 / 4 - sp.Rational(1, 2)) == 0
assert F(4, 9) / 2 == F(2, 9) < F(1, 4)

# Tetrahedron support distances after translation: each of the four
# normals has squared norm 2 and support offset 1/2.
for normal in [sp.Matrix([1, 1, 0]), sp.Matrix([1, -1, 0]),
               sp.Matrix([-1, 0, 1]), sp.Matrix([-1, 0, -1])]:
    assert normal.dot(normal) == 2
assert sp.simplify((2 * sp.sqrt(2)) * (sp.Rational(1, 2) / sp.sqrt(2))) == 1

# Closed cap x-2z>=0 captures exactly half of the first triangle and
# nothing at the other base: normalize its area eps by total 4eps.
assert sp.simplify(sp.integrate(eps * (v + 1) / 2, (v, -1, 1)) / (4 * eps)) == sp.Rational(1, 4)

# Exact fine-grid masses, including zero-length endpoint fibers.
for ell in range(1, 31):
    h = F(1, ell**2)
    e = F(1, ell)
    mass0 = h * sum(e * (k * h + 1) for k in range(-ell**2, ell**2 + 1))
    mass1 = h * sum(2 - F(2 * abs(k), ell) for k in range(-ell, ell + 1))
    assert mass0 == F(2, ell) + F(1, ell**3)
    assert mass1 == F(2, ell)
    assert F(1, ell) + F(1, 4 * ell**2) + F(1, 2 * ell**3) <= F(2, ell)
    for vertex_v in [-1, 0, 1, -e, e]:
        assert (F(vertex_v) / h).denominator == 1

# Rank-two box fibers at every integer point of the side-two triangle.
integer_bases = [(i, j) for i in range(3) for j in range(3 - i)]
assert len(integer_bases) == 6
volumes = []
for i, j in integer_bases:
    bary = [1 - sp.Rational(i + j, 2), sp.Rational(i, 2), sp.Rational(j, 2)]
    volume = sp.factor(8 * sp.prod(eps + (1 - eps) * b for b in bary))
    if 1 in bary:
        assert sp.simplify(volume - 8 * eps**2) == 0
    else:
        assert sp.simplify(volume - 2 * eps * (1 + eps)**2) == 0
    volumes.append(volume)
total = sp.factor(sum(volumes))
edge = 16 * eps**2 + 2 * eps * (1 + eps)**2
assert sp.factor(total - 2 * edge) == 2 * eps * (eps - 1)**2
assert sp.limit((2 * eps * (1 + eps)**2) / total, eps, 0, dir="+") == sp.Rational(1, 3)
assert sp.limit((8 * eps**2) / total, eps, 0, dir="+") == 0

# Same-parity crossing rectangles: an actual midpoint fiber absorbs
# the relative mass, as required by the separate comparability note.
middle_area = (1 + eps)**2
three_fiber_mass = sp.expand(8 * eps + middle_area)
assert three_fiber_mass == 1 + 10 * eps + eps**2
assert sp.limit(4 * eps / three_fiber_mass, eps, 0, dir="+") == 0
assert sp.limit(middle_area / three_fiber_mass, eps, 0, dir="+") == 1
sum_to_endpoint_ratio = (2 + 2 * eps)**2 / (4 * eps)
assert sp.limit(sum_to_endpoint_ratio, eps, 0, dir="+") == sp.oo

print("PASS: depth constants, normalization, sampled masses, hollow-face budget, and midpoint domination")
