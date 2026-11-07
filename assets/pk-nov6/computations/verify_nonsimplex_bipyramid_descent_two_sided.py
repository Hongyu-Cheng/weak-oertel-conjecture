"""Exact slice integration and actual rational 3D clipping certificates."""

from fractions import Fraction as F
from itertools import product
from math import factorial
import sympy as s

checks = 0


def ck(condition):
    global checks
    assert condition
    checks += 1


def eq(a, b):
    ck(s.factor(a-b) == 0)


rho, r, q, h = s.symbols('rho r q h', positive=True)
for p in range(2, 10):
    d = p+1
    Vp = s.Rational((p+1)**p, factorial(p))
    delta = s.Rational(p, p+1)**p
    V = 2*Vp/d
    positive = 2*s.integrate(delta*Vp*(rho-h/p)**p, (rho, h/p, r))
    eq(positive, delta*V*(r-h/p)**d)
    negative = (2*s.integrate(Vp*rho**p, (rho, 0, q))
                +2*s.integrate(delta*Vp*(rho+q/p)**p, (rho, q, r)))
    eq(negative, delta*V*(r+q/p)**d-V*q**d/p)
    eq(delta*((p+1)/s.Integer(p))**d, s.Rational(p+1, p))
    eq((delta*V*(r+q/p)**d-V*q**d/p).subs(q, r), V*r**d)
    ck(2*delta < 1)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def subtract(a, b):
    return tuple(x-y for x, y in zip(a, b))


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def clip_face(face, threshold):
    output = []
    for a, b in zip(face, face[1:]+face[:1]):
        da, db = a[0]-threshold, b[0]-threshold
        if da >= 0:
            output.append(a)
        if (da < 0 < db) or (db < 0 < da):
            t = da/(da-db)
            output.append(tuple(x+t*(y-x) for x, y in zip(a, b)))
    # Consecutive duplicate or repeated support vertices do not contribute.
    return list(dict.fromkeys(output))


def planar_hull(points):
    points = sorted(set(points))
    if len(points) < 3:
        return points
    def cross(a, b, c):
        return ((b[0]-a[0])*(c[1]-a[1])
                -(b[1]-a[1])*(c[0]-a[0]))
    lower, upper = [], []
    for sequence, target in [(points, lower), (list(reversed(points)), upper)]:
        for point in sequence:
            while len(target) >= 2 and cross(target[-2], target[-1], point) <= 0:
                target.pop()
            target.append(point)
    return lower[:-1]+upper[:-1]


def clipped_bipyramid_volume(radius, threshold):
    equator = [(radius*F(-1), radius*F(-1), F(0)),
               (radius*F(2), radius*F(-1), F(0)),
               (radius*F(-1), radius*F(2), F(0))]
    tips = [(F(0), F(0), radius), (F(0), F(0), -radius)]
    # These six actual triangular faces are the complete bipyramid boundary.
    faces = [[tip, equator[i], equator[(i+1) % 3]] for tip in tips for i in range(3)]
    clipped = [clip_face(face, threshold) for face in faces]
    boundary = {p for face in clipped for p in face if p[0] == threshold}
    cut_hull = planar_hull([(p[1], p[2]) for p in boundary])
    if len(cut_hull) >= 3:
        clipped.append([(threshold, y, t) for y, t in cut_hull])
    vertices = set(p for face in clipped for p in face)
    if not vertices:
        return F(0)
    center = tuple(sum(p[j] for p in vertices)/len(vertices) for j in range(3))
    volume = F(0)
    for face in clipped:
        for i in range(1, len(face)-1):
            volume += abs(det3(subtract(face[0], center),
                               subtract(face[i], center),
                               subtract(face[i+1], center)))/6
    return volume


for radius in [F(1, 2), F(4, 5), F(1), F(6, 5), F(3, 2)]:
    for multiple in [F(-2), F(-1), F(-3, 4), F(-1, 5), F(0),
                     F(1, 4), F(3, 2), F(2), F(3)]:
        threshold = radius*multiple
        actual = clipped_bipyramid_volume(radius, threshold)
        if threshold <= -radius:
            expected = 3*radius**3
        elif threshold >= 2*radius:
            expected = F(0)
        else:
            expected = F(4, 3)*(radius-threshold/2)**3-F(3, 2)*max(-threshold, 0)**3
        ck(actual == expected)


for a in [F(-1, 5), F(-1, 10), F(-1, 25), F(1, 50), F(1, 10), F(1, 5)]:
    sm = abs(a)
    total = sum(3*(1+a*z)**3 for z in [-1, 0, 1])
    cap = sum(clipped_bipyramid_volume(1+a*z, 2*a*z) for z in [-1, 0, 1])
    ck(cap == 4-12*sm**3)
    ck(total == 9+18*sm**2)
    ck(cap < 4 and total > 9)
    endpoint = F(4, 3)*(1+sm)**3
    middle_lower = F(4, 3)*(1+2*(1-sm)**3)
    ck(endpoint < middle_lower <= cap)
    ck(endpoint <= F(288, 125) < F(488, 125) <= cap)
    ck(total*4/cap > 9)

ck(F(1012, 3645) > F(27, 128))
ck(F(488, 1215) < F(4, 9))
z = s.symbols('z', real=True)
polynomial = 1+2*(1-z)**3-(1+z)**3
eq(polynomial, 2-9*z+3*z*z-3*z**3)
eq(polynomial.subs(z, s.Rational(1, 5)), s.Rational(37, 125))
eq(s.diff(polynomial, z), -9+6*z-9*z*z)

print(f'PASS {checks} exact slice, 3D clipping, and global-source checks')
