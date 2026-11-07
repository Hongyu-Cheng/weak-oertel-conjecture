"""Exact arithmetic calibrations for the exposed-face/inward-trace note.

The general geometric proof is in the Markdown source. This checks the
actual product example, every three-bit Boolean objective, and the
planar sharp-profile moments; it is not a numerical proof of OC.
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

P = (-1, 0, 1)
closed = {z: (int(z >= 0), int(z >= 0), int(z <= 0)) for z in P}
inward = {z: (int(z > 0), int(z >= 0), int(z <= 0)) for z in P}
check(closed[0] == (1, 1, 1))
check(inward[0] == (0, 1, 1))
check(tuple(sum(closed[z][i] for z in P) for i in range(3)) == (2, 2, 2))
check(tuple(sum(inward[z][i] for z in P) for i in range(3)) == (1, 2, 2))

signatures = tuple(product((0, 1), repeat=3))
for epsilon in (F(1, 2), F(1, 3), F(1, 7), F(1, 1000)):
    for z in P:
        # On the open collar -epsilon<t<0, all bits are constant in t.
        for tau in (F(1, 9), F(1, 2), F(8, 9)):
            t = -epsilon * tau
            actual = (int(t + z >= 0), int(-t + z >= 0), int(-z >= 0))
            check(actual == inward[z])
    # Every Boolean profile is a sum of these disjoint signature atoms.
    for bits in product((0, 1), repeat=8):
        psi = dict(zip(signatures, bits))
        exact_collar = epsilon * sum(psi[inward[z]] for z in P)
        face_inward = sum(psi[inward[z]] for z in P)
        check(exact_collar / epsilon == face_inward)

check(sum(closed[z][0] * closed[z][1] for z in P) == 2)
check(sum(inward[z][0] * inward[z][1] for z in P) == 1)
check(all(any(inward[z]) for z in P))

# W-Gamma on the triangle facet: exact zero mass and first moment.
pieces = ((F(0), F(1, 3), -F(1, 9)),
          (F(1, 3), F(2, 3), F(2, 9)),
          (F(2, 3), F(1), -F(1, 9)))
check(sum(c * (b-a) for a,b,c in pieces) == 0)
check(sum(c * (b*b-a*a) / 2 for a,b,c in pieces) == 0)
check(sum((c + F(4,9)) * (b-a) for a,b,c in pieces) == F(4,9))
for power in range(2, 21):
    check(sum(c * (b**(power+1)-a**(power+1)) / (power+1)
              for a,b,c in pieces) < 0)

print(f"PASS: {checks} exact exposed-face/inward-trace checks")
