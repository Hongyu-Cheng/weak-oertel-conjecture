"""Exact source/reflection certificates for nonsymmetric flat rounding.

The C2/IFT escape is justified by the audited analytic proof. This script
checks the new geometry, affine symmetries, and baseline cap cancellation.
"""
from fractions import Fraction as F


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def apply(A, x):
    return tuple(dot(row, x) for row in A)


def transpose(A):
    return tuple(zip(*A))


def mul(A, B):
    return tuple(tuple(dot(row, col) for col in transpose(B)) for row in A)


def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                   -poly[(i+1) % len(poly)][0]*poly[i][1]
                   for i in range(len(poly))))/2 if poly else F(0)


def clip(poly, normal, threshold):
    out = []
    for a, b in zip(poly, poly[1:]+poly[:1]):
        ha, hb = dot(normal, a)-threshold, dot(normal, b)-threshold
        if ha >= 0:
            out.append(a)
        if (ha < 0 < hb) or (hb < 0 < ha):
            t = ha/(ha-hb)
            out.append(tuple(x+t*(y-x) for x, y in zip(a, b)))
    return out


K = [(F(-1, 3), F(-1, 3)), (F(2, 3), F(-1, 3)),
     (F(-1, 3), F(2, 3))]
B = [(F(1), F(-1)), (F(0), F(1)), (F(-1), F(0))]
minusK = [tuple(-x for x in p) for p in K]
assert area(K) == F(1, 2)
assert area(B) == F(3, 2)
M = 2*area(K)+area(B)
assert M == F(5, 2)
facets = [(F(2), F(1)), (F(-1), F(1)), (F(-1), F(-2))]
assert all(dot(u, b) <= 1 for u in facets for b in B)
differences = {tuple((x-y)/2 for x, y in zip(a, b)) for a in K for b in K}
assert len(differences) == 7
assert all(dot(u, v) <= 1 for u in facets for v in differences)
contacts = [(F(1, 2), F(0)), (F(-1, 2), F(1, 2)), (F(0), F(-1, 2))]
assert all(dot(u, v) == 1 for u, v in zip(facets, contacts))
assert dot(facets[1], tuple(-x for x in B[0])) == 2 > 1
# Endpoint translation in the first supporting direction breaks compatibility.
for denominator in range(10, 110):
    t = F(1, denominator)
    moved = tuple(x+t*u/2 for x, u in zip(contacts[0], facets[0]))
    assert dot(facets[0], moved) == 1+F(5, 2)*t > 1

normals = [(F(-1), F(-1)), (F(1), F(0)), (F(0), F(1))]
Rs = [((F(0), F(-1)), (F(-1), F(0))),
      ((F(-1), F(0)), (F(1), F(1))),
      ((F(1), F(1)), (F(0), F(-1)))]
I = ((F(1), F(0)), (F(0), F(1)))
Q = ((F(1), F(1, 2)), (F(1, 2), F(1)))
for normal, R in zip(normals, Rs):
    assert mul(R, R) == I
    assert R[0][0]*R[1][1]-R[0][1]*R[1][0] == -1
    assert {apply(R, p) for p in B} == set(B)
    assert apply(transpose(R), normal) == tuple(-x for x in normal)
    assert mul(mul(transpose(R), Q), R) == Q
    assert area(clip(B, normal, F(0))) == area(B)/2
# Q eigenvalues are 1/2 and 3/2, so E contains ball sqrt(2/3).
assert apply(Q, (F(1), F(1))) == (F(3, 2), F(3, 2))
assert apply(Q, (F(1), F(-1))) == (F(1, 2), F(-1, 2))

cap_checks = 0
for normal in normals:
    for j in range(-20, 41):
        threshold = F(j, 30)
        plus = area(clip(K, normal, threshold))
        minus = area(clip(minusK, normal, -threshold))
        assert plus+minus == area(K)
        assert plus+minus+area(clip(B, normal, F(0))) == M/2
        cap_checks += 1

# The group has zero sum margin for every a summing to one.
for a0, a1 in [(F(1, 3), F(1, 3)), (F(1, 4), F(1, 2)),
               (F(2, 5), F(1, 5)), (F(7, 20), F(3, 10))]:
    a = [a0, a1, 1-a0-a1]
    assert all(x > 0 for x in a)
    rows = [tuple(normal)+(F(1, 3)-ai,) for normal, ai in zip(normals, a)]
    assert tuple(sum(row[j] for row in rows) for j in range(3)) == (0, 0, 0)

other = (F(-2), F(-1))
other_mass = (area(clip(K, other, F(0)))+
              area(clip(minusK, other, F(0)))+
              area(clip(B, other, F(0))))
assert area(clip(B, other, F(0))) == F(2, 3)
assert other_mass == F(7, 6) < M/2

print(f"PASS: exact active compatibility, 100 forbidden free translations, "
      f"three cap/ellipsoid reflections, {cap_checks} moving-threshold identities, "
      "and nonselected cap mass 7/6<5/4.")
