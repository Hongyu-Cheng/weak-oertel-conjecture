"""Exact finite calibrations for the full-shape intrinsic component lift."""
from fractions import Fraction as F
from itertools import product


def rank(rows):
    a = [[F(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((j for j in range(r, len(a)) if a[j][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        divisor = a[r][c]
        a[r] = [x / divisor for x in a[r]]
        for j in range(len(a)):
            if j != r and a[j][c]:
                factor = a[j][c]
                a[j] = [x - factor * y for x, y in zip(a[j], a[r])]
        r += 1
        if r == len(a):
            break
    return r


bases = [(0, 0), (1, 0), (0, 1), (1, 1)]
for j, (x, y) in enumerate(bases):
    g = x * y
    chi = [1 - x - y + g, x - g, y - g, g]
    assert chi == [int(i == j) for i in range(4)]

offsets = [(1, 2), (3, 5), (7, 11), (13, 17)]
for j, (x, y) in enumerate(bases):
    recovered = tuple(
        offsets[0][c]
        + x * (offsets[1][c] - offsets[0][c])
        + y * (offsets[2][c] - offsets[0][c])
        + x * y * (offsets[3][c] - offsets[1][c]
                   - offsets[2][c] + offsets[0][c])
        for c in range(2)
    )
    assert recovered == offsets[j]

epsilon = F(1, 7)
mass = 8 * epsilon
transforms = [(F(1, 2), 1 / (4 * epsilon)),
              (1 / (2 * epsilon), F(1, 4))]
halfsides = [(F(1), epsilon), (epsilon, F(1))]
for transform, sides in zip(transforms, halfsides):
    assert transform[0] * transform[1] == 1 / mass
    image = tuple(t * s for t, s in zip(transform, sides))
    assert image == (F(1, 2), F(1, 4))
    assert 4 * image[0] * image[1] == F(1, 2)
    for corner in product((-1, 1), repeat=2):
        original = tuple(sign * s for sign, s in zip(corner, sides))
        normalized = tuple(t * v for t, v in zip(transform, original))
        assert tuple(v / t for t, v in zip(transform, normalized)) == original

# k=2, s=4, m=2, t=1: the total affine dimension must be 11.
vertices = []
for i, (z1, z2) in enumerate(bases):
    for x, y in product((F(-1, 2), F(1, 2)),
                        (F(-1, 4), F(1, 4))):
        blocks = [F(0)] * 8
        blocks[2 * i:2 * i + 2] = [x, y]
        vertices.append([F(z1), F(z2), *blocks, F(z1 * z2)])
differences = [[x - y for x, y in zip(v, vertices[0])]
               for v in vertices[1:]]
assert rank(differences) == 11

print("PASS: component indicators, offset features, common Jacobians, "
      "exact inverse maps, intrinsic masses, and full affine dimension")
