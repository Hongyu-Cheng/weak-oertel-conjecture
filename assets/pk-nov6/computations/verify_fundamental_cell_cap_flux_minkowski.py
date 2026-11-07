"""Exact rational calibration of the cap identities and obstructions."""
from fractions import Fraction as F
from math import floor, ceil

checks = 0


def check(value):
    global checks
    assert value
    checks += 1


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(a[0]*b[1]-a[1]*b[0]
                   for a, b in zip(poly, poly[1:]+poly[:1]))) / 2


def clip(poly, normal, threshold):
    output = []
    for a, b in zip(poly, poly[1:]+poly[:1]):
        fa = sum(c*d for c, d in zip(normal, a))-threshold
        fb = sum(c*d for c, d in zip(normal, b))-threshold
        if fa >= 0:
            output.append(a)
        if (fa < 0 < fb) or (fb < 0 < fa):
            t = fa/(fa-fb)
            output.append(tuple(a[i]+t*(b[i]-a[i]) for i in range(2)))
    clean = []
    for p in output:
        if not clean or p != clean[-1]:
            clean.append(p)
    if len(clean) > 1 and clean[0] == clean[-1]:
        clean.pop()
    return clean


def section(poly, z):
    values = []
    for a, b in zip(poly, poly[1:]+poly[:1]):
        if a[0] == b[0]:
            if a[0] == z:
                values.extend((a[1], b[1]))
        elif min(a[0], b[0]) <= z <= max(a[0], b[0]):
            values.append(a[1]+(z-a[0])*(b[1]-a[1])/(b[0]-a[0]))
    return F(0) if not values else max(values)-min(values)


def mixed(poly):
    return sum((section(poly, F(k)) for k in range(ceil(min(p[0] for p in poly)),
                                                   floor(max(p[0] for p in poly))+1)), F(0))


def saw(z):
    return F(0) if z.denominator == 1 else z-floor(z)-F(1, 2)


def flux(poly):
    # Polygons are counterclockwise. For an edge (dz,dx), N_z ds=dx.
    total = F(0)
    for a, b in zip(poly, poly[1:]+poly[:1]):
        dz, dx = b[0]-a[0], b[1]-a[1]
        if not dz:
            total += dx*saw(a[0])
            continue
        knots = {F(0), F(1)}
        for k in range(ceil(min(a[0], b[0])), floor(max(a[0], b[0]))+1):
            t = (k-a[0])/dz
            if 0 < t < 1:
                knots.add(t)
        knots = sorted(knots)
        total += dx*sum((saw(a[0]+dz*(s+t)/2)*(t-s)
                         for s, t in zip(knots, knots[1:])), F(0))
    return total


def check_flux(poly):
    if area(poly) == 0:
        return
    a, b = min(p[0] for p in poly), max(p[0] for p in poly)
    endpoint = (section(poly, a) if a.denominator == 1 else F(0)) / 2
    endpoint += (section(poly, b) if b.denominator == 1 else F(0)) / 2
    check(mixed(poly) == area(poly)-flux(poly)+endpoint)


triangle = [(F(-1, 2), F(-1)), (F(3, 2), F(-1)), (F(1, 2), F(3))]
normals = [(-F(4, 3), F(1)), (-F(4, 3), F(-1)),
           (F(4, 3), F(1)), (F(4, 3), F(-1))]
thresholds = [-F(1, 3), -F(1, 3), F(1), F(1)]
caps = [clip(triangle, normal, threshold)
        for normal, threshold in zip(normals, thresholds)]
check(area(triangle) == mixed(triangle) == 4)
check([area(cap) for cap in caps] == [F(2), F(9, 8), F(2), F(9, 8)])
check([mixed(cap) for cap in caps] == [F(4, 3)]*4)
check(sum(flux(cap) for cap in caps) == F(11, 12))
check(sum(mixed(cap)/4-area(cap)/4 for cap in caps) == -F(11, 48))
check(tuple(sum(normal[i] for normal in normals) for i in range(2)) == (0, 0))
for cap in caps:
    check_flux(cap)

for numerator in range(5, 81):
    R = F(numerator, 2)
    body = [(-1/(R-1), F(-1)), (1+1/(R-1), F(-1)), (F(1, 2), R)]
    cap = clip(body, (F(-1), F(1)), F(0))
    check(mixed(body) == 4)
    check(mixed(cap) == 1)
    check(area(body) == (R+1)**2/(2*(R-1)))
    check(area(cap) == (R-1)*(2*R-1)/(2*(2*R-3)))
    check_flux(body)
    check_flux(cap)

for numerator in range(3, 101):
    L = F(numerator, 2)
    def total_slice(z):
        return (2*L*(1-z)+z)*(2*(1-z)+2*L*z)
    def cap_slice(z):
        return L*(1-z)*(2*(1-z)+2*L*z)
    total = (total_slice(F(0))+4*total_slice(F(1, 2))+total_slice(F(1)))/6
    retained = (cap_slice(F(0))+4*cap_slice(F(1, 2))+cap_slice(F(1)))/6
    check(total == (2*L*L+6*L+1)/3)
    check(retained == L*(L+2)/3)
    check(retained/total-F(1, 3) == (L*L-1)/(3*(2*L*L+6*L+1)))
    check((cap_slice(F(0))+cap_slice(F(1))) /
          (total_slice(F(0))+total_slice(F(1))) == F(1, 3))

# Endpoint/boundary calibrations of (5), including integer vertical facets.
base_polygons = [triangle,
    [(F(-1), F(-1)), (F(2), F(-1)), (F(2), F(2)), (F(-1), F(2))],
    [(F(-2, 3), F(-1)), (F(7, 3), F(0)), (F(0), F(3))]]
for body in base_polygons:
    check_flux(body)
    for a in range(-3, 4):
        for b in range(-3, 4):
            if not (a or b):
                continue
            for c in range(-5, 6):
                cap = clip(body, (F(a), F(b)), F(c, 2))
                if len(cap) >= 3:
                    check_flux(cap)

print(f"PASS: {checks} exact rational checks")
