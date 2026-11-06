"""Exact checks for the block normalization and dense-lattice constants.

The dimension-independent proof is in the companion Markdown note.
This checks a nontrivial triangle normalization, its fiber/covolume
Jacobians, its exact sampled mass, and the stated n=d=1 threshold.
"""

from fractions import Fraction as Q
import sympy as sp

W, H = sp.symbols("W H", positive=True)
z, x = sp.symbols("z x", real=True)

# Start with C=conv((0,0),(W,0),(W,H)).  The inverse simplex map
# does not preserve the vertical direction.  The displayed orthogonal
# rotation restores it after centroid translation and inradius scaling.
simplex_linear = sp.Matrix([[1 / W, -1 / H], [0, 1 / H]])
rotation = sp.Matrix([[1, 1], [-1, 1]]) / sp.sqrt(2)
g_delta = sp.Matrix([sp.Rational(1, 3), sp.Rational(1, 3)])
image = sp.simplify(
    rotation * (3 * sp.sqrt(2))
    * (simplex_linear * sp.Matrix([z, x]) - g_delta)
)
assert image == sp.Matrix([3 * z / W - 2, -3 * z / W + 6 * x / H])
linear = image.jacobian([z, x])
assert linear[0, 1] == 0
assert sp.simplify(linear.det() - 18 / (W * H)) == 0
assert sp.simplify(linear[0, 0] * linear[1, 1] - linear.det()) == 0

vertices = [sp.Matrix([0, 0]), sp.Matrix([W, 0]), sp.Matrix([W, H])]
images = [image.subs({z: v[0], x: v[1]}) for v in vertices]
assert images == [sp.Matrix([-2, 0]), sp.Matrix([1, -3]), sp.Matrix([1, 3])]
assert sum(images, sp.zeros(2, 1)) == sp.zeros(2, 1)

# K={Z<=1, X-Z<=2, -X-Z<=2}: support distances of these defining
# planes from 0 are 1,sqrt(2),sqrt(2), hence B_2 is contained in K.
for normal, offset in [(sp.Matrix([1, 0]), 1),
                       (sp.Matrix([-1, 1]), 2),
                       (sp.Matrix([-1, -1]), 2)]:
    assert offset**2 >= normal.dot(normal)
    assert all(normal.dot(v) <= offset for v in images)
assert max(v.dot(v) for v in images) == 10 < 8**2

# For an integer W, original fiber lengths are H*k/W, k=0,...,W.
# The zero-length boundary fiber contributes zero, without being
# replaced by a positive fiber.  The weighted sampled total is exact.
original_mass = H * (W + 1) / 2
sampled_mass = sp.factor(linear.det() * original_mass)
assert sp.simplify(sampled_mass - 9 * (W + 1) / W) == 0
assert sp.simplify(sampled_mass - 9 - 9 / W) == 0
cover_radius = 3 / (2 * W)
assert sp.simplify(cover_radius - linear[0, 0] / 2) == 0
assert sp.simplify(8 / W - cover_radius) == sp.Rational(13, 2) / W

# n=d=1: R=8, Gamma_2=4/9, alpha=1/4, S=16, E=36.
gap = Q(4, 9) - Q(1, 4)
denominator = Q(16) + (1 + Q(1, 4)) * 36
assert gap == Q(7, 36)
assert denominator == 61
assert gap / denominator == Q(7, 2196)
assert Q(1, 128) < Q(7, 2196) * 3  # pi>3 suffices.
assert Q(8) / Q(1, 128) == 1024

# A finite arithmetic consistency check of the dimension conventions;
# positivity in every dimension is proved by the binomial estimate.
def gamma(k):
    return Q(1) if k == 0 else Q(k, k + 1) ** k

for n in range(1, 13):
    for d in range(13):
        gap_nd = gamma(n + d) - gamma(d) / 2**n
        if (n, d) == (1, 0):
            assert gap_nd == 0
        else:
            assert gap_nd > 0

print("PASS: exact block triangle, Jacobians, sampled mass, and mesh constants")
