"""Exact certificates used in shared-facet-projective-moment-consequence.md."""
from fractions import Fraction as F


def integral_monomial(power):
    return F(0) if power % 2 else F(2, power + 1)


# Signed density sign*x1 on x2=z, for the two integer facet traces.
mass = z_moment = x1_moment = x2_moment = F(0)
zx1 = zx2 = F(0)
for z, sign in [(0, 1), (1, -1)]:
    density_mass = sign * integral_monomial(1)
    density_x1 = sign * integral_monomial(2)
    mass += density_mass
    z_moment += z * density_mass
    x1_moment += density_x1
    x2_moment += z * density_mass
    zx1 += z * density_x1
    zx2 += z * z * density_mass
assert (mass, z_moment, x1_moment, x2_moment) == (0, 0, 0, 0)
assert (zx1, zx2) == (F(-2, 3), 0)


def area(poly):
    return abs(sum(x * v - y * u for (x, y), (u, v) in
                   zip(poly, poly[1:] + poly[:1]))) / 2


diamond = [(F(1), F(0)), (F(0), F(1)),
           (F(-1), F(0)), (F(0), F(-1))]
right = [(F(0), F(-1)), (F(1), F(0)), (F(0), F(1))]
left = [(F(0), F(1)), (F(-1), F(0)), (F(0), F(-1))]
M = area(diamond)
assert M == 2
assert area(right) == area(left) == 1
beta = F(1, 2)
lam = F(1)
rho = F(1, 2)
section = F(2)
stress = F(4)
assert 2 * lam == 1 / beta
assert lam * section == rho * stress
support = F(1)
proposed_bound_left = 2 * lam * section * support
assert proposed_bound_left == 4 > M

# Exact coefficients of sqrt(3) in the nonzero covariance example.
zx1_sqrt3 = F(0)
zx2_sqrt3 = F(0)
for z in [-1, 1]:
    zx1_sqrt3 += z * z
    zx2_sqrt3 += z * F(-z, 2)
assert (zx1_sqrt3, zx2_sqrt3) == (2, -1)
v = F(1, 2)
assert (-v * zx1_sqrt3, -v * zx2_sqrt3) == (-1, F(1, 2))

print("All shared-facet moment countercertificates passed exactly.")
