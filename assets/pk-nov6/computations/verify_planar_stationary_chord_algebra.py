"""Exact checks for the proved planar weighted stationary-chord theorem.

These verify the displayed identities; the mathematical proof is in the
companion Markdown note and does not rely on enumerated test cases.
"""
from fractions import Fraction as F


def det(x, y):
    return x[0] * y[1] - x[1] * y[0]


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(det(x, y) for x, y in
                   zip(poly, poly[1:] + poly[:1]))) / 2


def clip_cap(poly, p):
    out = []
    for x, y in zip(poly, poly[1:] + poly[:1]):
        dx, dy = det(p, x), det(p, y)
        if dx >= 0:
            out.append(x)
        if (dx < 0 < dy) or (dy < 0 < dx):
            alpha = dx / (dx - dy)
            out.append(tuple(x[k] + alpha * (y[k] - x[k]) for k in [0, 1]))
    return out


count = 0
for denom in range(3, 51):
    for a in range(1, denom - 1):
        for b in range(1, denom - a):
            t = [F(a, denom), F(b, denom), F(denom - a - b, denom)]
            e = sum(t[i] * t[j] for i in range(3) for j in range(i + 1, 3))
            theta = [x * (1 - x) / (2 * e) for x in t]
            assert sum(theta) == 1
            assert all(0 < x < F(1, 2) for x in theta)
            E = []
            for mask in range(8):
                num = 2 * e * e + sum(t[i] ** 2 *
                    (9 * t[i] * (1 - t[i]) - 8 * e)
                    for i in range(3) if mask & (1 << i))
                assert num >= 0
                E.append(num)
            assert E[7] == e - 9 * t[0] * t[1] * t[2]
            for i in range(3):
                x = t[i]
                s = 1 - x
                others = [t[j] for j in range(3) if j != i]
                v = others[0] * others[1]
                A = x * s
                assert E[1 << i] == 2 * (v + A - 2 * x*x)**2 + x**3 * (9 - 17*x)
                assert E[7 ^ (1 << i)] == s * (x*s*(1+x)+(1-8*x)*v)
            count += 1

# Exact geometry and orientation checks for several asymmetric triangles.
for t in [[F(1, 3)] * 3, [F(3, 5), F(1, 5), F(1, 5)],
          [F(1, 10), F(3, 10), F(3, 5)],
          [F(1, 101), F(1, 101), F(99, 101)]]:
    l = [(1 - x) / 2 for x in t]
    center = (l[1], l[2])
    vertices = [(-center[0], -center[1]),
                (1-center[0], -center[1]),
                (-center[0], 1-center[1])]
    p = []
    for i in range(3):
        k = (i + 2) % 3
        p.append(tuple(t[k] * vertices[i][j] +
                       (1-t[k]) * vertices[k][j] for j in [0, 1]))
    e = sum(t[i]*t[j] for i in range(3) for j in range(i+1, 3))
    theta = [x*(1-x)/(2*e) for x in t]
    assert all(sum(theta[i]*p[i][j] for i in range(3)) == 0 for j in [0, 1])
    for i in range(3):
        assert det(p[i], vertices[i]) > 0
        assert all(det(p[i], vertices[j]) < 0 for j in range(3) if j != i)
    weighted = sum(theta[i]*area(clip_cap(vertices, p[i])) for i in range(3))
    formula = (e + sum(theta[i]*t[i]**2 for i in range(3))) / (2*e + sum(x*x for x in t))
    assert weighted / area(vertices) == formula >= F(4, 9)

print(f"Verified all eight exact subset inequalities and identities on {count} rational triples; geometry checks passed.")
