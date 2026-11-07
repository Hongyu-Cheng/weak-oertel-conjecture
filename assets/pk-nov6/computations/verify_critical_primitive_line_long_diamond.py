"""Exact diagnostics for the all-dimension long-diamond counterexample.

The theorem is proved in the companion Markdown file.  These checks
use only rational arithmetic and do not stand in for the all-halfspace
or all-dimensional proof.
"""

from fractions import Fraction as F
from random import Random


checks = 0


def check_equal(left, right):
    global checks
    assert left == right, (left, right)
    checks += 1


def check_positive(value):
    global checks
    assert value > 0, value
    checks += 1


def clip(poly, ux, uy, threshold):
    if not poly:
        return []
    result = []
    previous = poly[-1]
    old = ux*previous[0]+uy*previous[1]-threshold
    for point in poly:
        new = ux*point[0]+uy*point[1]-threshold
        if (old >= 0) != (new >= 0):
            t = old/(old-new)
            result.append(tuple(previous[j]+t*(point[j]-previous[j]) for j in (0, 1)))
        if new >= 0:
            result.append(point)
        previous, old = point, new
    return result


def area(poly):
    if not poly:
        return F(0)
    return abs(sum(poly[j-1][0]*poly[j][1]-poly[j-1][1]*poly[j][0]
                   for j in range(len(poly))))/2


# General explicit rational parameters: root inequalities are compared by
# taking the same positive integer power, so no radicals are approximated.
for d in range(2, 201):
    gamma = F(d, d+1)**d
    a = F(1, 2*d)
    b = 2-a
    N = 3*2**(d-1)
    q = (2*N+1)*gamma+a**d
    mass = 2*N+1+a**d+b**d
    check_equal(a+b, F(2))
    check_positive(gamma-F(1, 3))
    assert gamma <= F(4, 9)
    checks += 1
    check_positive((b/2)**d-(1-gamma))
    check_positive(b-d*a)
    check_positive(F(2*N+1)-3*b**d)
    check_positive(mass/4-b**d)
    check_positive(q-gamma*b**d)
    check_positive(q/mass-gamma/4)


d, N = 2, 4
a, b = F(2, 5), F(8, 5)
gamma = F(4, 9)
triangle = [(F(-1, 3), F(-2, 3)),
            (F(2, 3), F(-2, 3)),
            (F(-1, 3), F(4, 3))]
check_equal(area(triangle), F(1))
check_equal(tuple(sum(p[j] for p in triangle)/3 for j in (0, 1)), (F(0), F(0)))

fibers = {(0, j): triangle for j in range(-N, N+1)}
fibers[(-1, 0)] = [(a*x, a*y) for x, y in triangle]
fibers[(1, 0)] = [(b*x, b*y) for x, y in triangle]
complete_base = {(x, y) for x in range(-1, 2) for y in range(-N, N+1)
                 if F(abs(x))+F(abs(y), N) <= 1}
check_equal(set(fibers), complete_base)
mass = sum(area(poly) for poly in fibers.values())
q = (2*N+1)*gamma+a*a
check_equal(q, F(104, 25))
check_equal(mass, F(293, 25))
check_equal(max(area(poly) for poly in fibers.values()), F(64, 25))
check_positive(mass/4-F(64, 25))
check_positive((b/2)**2-(1-gamma))


def masses(alpha1, alpha2, ux, uy, threshold=F(0)):
    return {z: area(clip(poly, ux, uy, threshold-alpha1*z[0]-alpha2*z[1]))
            for z, poly in fibers.items()}


canonical = [(F(1), F(0)), (F(0), F(1, 2)), (F(-1), F(-1, 2))]
for ux, uy in canonical:
    actual = masses(F(-2), F(0), ux, uy)
    check_equal(sum(actual.values()), q)
    check_equal(actual[(-1, 0)], a*a)
    check_equal(actual[(1, 0)], F(0))
    for j in range(-N, N+1):
        check_equal(actual[(0, j)], gamma)
    # Strict endpoint statuses, not merely vanishing volume.
    for x, y in fibers[(-1, 0)]:
        check_positive(ux*x+uy*y+2)
    for x, y in fibers[(1, 0)]:
        check_positive(2-ux*x-uy*y)
    for sign, scale in ((-1, a), (1, b)):
        isolated = masses(F(3*sign), F(0), ux, uy, F(3))
        check_equal(sum(isolated.values()), gamma*scale*scale)
        check_equal(isolated[(sign, 0)], gamma*scale*scale)
        check_equal(sum(v for z, v in isolated.items() if z != (sign, 0)), F(0))

# Purely integer normals retain whole boundary fibers; their exact masses
# satisfy the same lower bound at the actual point y.
for alpha1 in range(-4, 5):
    for alpha2 in range(-4, 5):
        if alpha1 == alpha2 == 0:
            continue
        value = sum(masses(F(alpha1), F(alpha2), F(0), F(0)).values())
        assert value >= q
        checks += 1

# Independent exact cap diagnostics in coupled integer/continuous directions.
rng = Random(20260929)
for _ in range(2500):
    alpha1, alpha2, ux, uy = [F(rng.randint(-15, 15), rng.randint(1, 7))
                            for _ in range(4)]
    if ux == uy == 0:
        ux = F(1)
    value = sum(masses(alpha1, alpha2, ux, uy).values())
    assert value >= q, (alpha1, alpha2, ux, uy, value, q)
    checks += 1

print(f"PASS: {checks} exact rational checks")
