"""Exact finite arithmetic for the n=4 section and depth obstruction."""
from fractions import Fraction as F
from itertools import product

Z = list(product(range(-2, 3), repeat=4))
I = [z for z in Z if max(map(abs, z)) <= 1]
J = [z for z in Z if max(map(abs, z)) == 2]
assert (len(Z), len(I), len(J)) == (625, 81, 544)
theta = {z: F(375, 397) if z[0] == 2 else
            F(1, 2) if z[0] == 1 else F(22, 397) for z in J}
weight = len(I) + sum(theta.values())
mom = [sum(z[k] for z in I) + sum(theta[z]*z[k] for z in J)
       for k in range(4)]
assert sum(theta.values()) == F(73390, 397)
assert weight == F(105547, 397)
assert mom == [weight, 0, 0, 0]

# Four actual sign patterns through j=e1 yield the exact trace vector.
eps = F(1, 1000)
normals = [(F(1), eps, 10*eps, 100*eps),
           (F(1), -eps, -10*eps, -100*eps)]
normals += [tuple(-x for x in a) for a in normals]
coeff = [F(375, 794), F(375, 794), F(11, 397), F(11, 397)]
assert sum(coeff) == 1
for z in J:
    margins = [sum(a[k]*(z[k]-(k == 0)) for k in range(4))
               for a in normals]
    assert all(m != 0 for m in margins)
    assert sum(w for w, m in zip(coeff, margins) if m > 0) == theta[z]

# Exact maximum of the unclipped small-box hinge on coefficient vertices.
hinges = []
for a in product((-1, 1), repeat=4):
    h = sum(max(0, a[0]-sum(a[k]*z[k] for k in range(4))) for z in I)
    assert h == (102 if a[0] == 1 else 21)
    hinges.append(h)
assert max(hinges) == 102
assert 125 - 102 - 1 == 22
assert sum(2-max(map(abs,z)) for z in I) == 82

for T in (1, 5):
    mass = sum(T + 2 - max(map(abs,z)) for z in Z)
    assert mass == 82 + 625*T
    assert F(625*T, 2*mass) > F(82, mass)
assert F(82, 3207) < F(1, 32)
print("PASS: exact fibers/layers, proper and supporting counts, trace barycenters,")
print("      four consistent sign patterns, hinge constant102, and below-OC mass.")
