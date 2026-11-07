"""Exact support-kernel and first-variation certificates (no depth search)."""
from fractions import Fraction as F

N = [(-3, 1), (-1, -2), (1, 0), (1, 1)]
L = [(0, 1, -1, 2), (2, 1, 7, 0)]
checks = 0

def dot(x, y):
    return sum(a*b for a, b in zip(x, y))

for row in L:
    for j in range(2):
        assert sum(row[i]*N[i][j] for i in range(4)) == 0
        checks += 1
assert L[0][0]*L[1][1]-L[0][1]*L[1][0] == -2
assert N[2][0]*N[3][1]-N[2][1]*N[3][0] == 1
checks += 2  # Both matrices have rank two, so im N=ker L exactly.

A = [(-1, 2), (-2, -1), (2, -3), (2, -1)]
B = [(F(-13, 8), F(17, 8)), (F(-5, 2), F(-1, 2)),
     (F(3, 2), F(-5, 2)), (F(3, 2), -1)]
A = [tuple(map(F, p)) for p in A]
B = [tuple(map(F, p)) for p in B]
a, b = list(map(F, (5, 4, 2, 1))), [F(7), F(7, 2), F(3, 2), F(1, 2)]
delta = [y-x for x, y in zip(a, b)]
assert [dot(row, delta) for row in L] == [F(-1), F(0)]
checks += 1

def section(poly, normal):
    pts = set()
    for p, q in zip(poly, poly[1:]+poly[:1]):
        hp, hq = dot(normal, p), dot(normal, q)
        if hp == 0:
            pts.add(p)
        if hp*hq < 0:
            pts.add(tuple((hq*x-hp*y)/(hq-hp) for x, y in zip(p, q)))
    assert len(pts) == 2
    return sorted(pts)

normals = [(1, 0), (0, 1), (-1, -1)]
# Section length divided by norm of its normal: rational in these directions.
def normalized_area(seg, normal):
    tangent = (-normal[1], normal[0])
    return abs(dot(tangent, tuple(y-x for x, y in zip(*seg))))/dot(normal, normal)

expected = [(F(3), F(9, 4)), (F(8, 3), F(17, 6)), (F(13, 4), F(13, 4))]
derivatives = []
for normal, expect in zip(normals, expected):
    got = tuple(normalized_area(section(poly, normal), normal) for poly in (A, B))
    assert got == expect
    derivatives.append(got[1]-got[0])
    checks += 1
assert derivatives == [F(-3, 4), F(1, 6), F(0)]
checks += 1

for poly, support in ((A, a), (B, b)):
    assert poly[3][1]-poly[2][1] == (support[1]+2*support[3]-support[2])/2
    assert poly[2][0]-poly[1][0] == support[2]+(2*support[0]+support[1])/7
    checks += 2

print(f"PASS: {checks} exact kernel, edge, and cap-variation checks")
