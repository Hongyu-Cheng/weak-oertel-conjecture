"""Exact algebra and physical polygon checks for the arbitrary-rank lemma.

These checks supplement the all-real proof; they do not prove local
all-normal persistence or an OC theorem.
"""

from fractions import Fraction as F
from itertools import product
import sympy as sy

checks = 0


def ck(test):
    global checks
    assert test
    checks += 1


def eq(a, b):
    ck(sy.factor(a-b) == 0)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def clip(poly, u, threshold):
    result = []
    for p, q in zip(poly, poly[1:]+poly[:1]):
        dp, dq = dot(u, p)-threshold, dot(u, q)-threshold
        if dp >= 0:
            result.append(p)
        if (dp < 0 < dq) or (dq < 0 < dp):
            t = dp/(dp-dq)
            result.append(tuple(x+t*(y-x) for x, y in zip(p, q)))
    return result


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p, q in zip(poly, poly[1:]+poly[:1])))/2


T = [(F(-1), F(-1)), (F(2), F(-1)), (F(-1), F(2))]
normals = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(-1))]
V = F(9, 2)
ck(area(T) == V)

# Symbolic general-rank completion and its rank-two normal Hessian.
R, bx, by, gx, gy, theta, ax, ay = sy.symbols(
    'R bx by gx gy theta ax ay', positive=True)
W = bx**2/gx+by**2/gy
phi = ((2-theta)**2*R+2*(2-theta)*(ax*bx+ay*by)
       +gx*ax**2+gy*ay**2)/(2*(1-theta))
completed = ((2-theta)**2*(R-W)
             +gx*(ax+(2-theta)*bx/gx)**2
             +gy*(ay+(2-theta)*by/gy)**2)/(2*(1-theta))
eq(phi, completed)
opt = {ax: -2*bx/gx, ay: -2*by/gy, theta: 0}
eq(phi.subs(opt), 2*(R-W))
for var in [ax, ay, theta]:
    eq(sy.diff(phi, var).subs(opt), 0)
hess = sy.hessian(phi, (ax, ay, theta)).subs(
    {bx: 0, by: 0, ax: 0, ay: 0, theta: 0})
ck(hess == sy.diag(gx, gy, R))


def physical_case(P, radial, expected_rank):
    """P is symmetric; test actual optimized and nonoptimal cut polygons."""
    n = len(P[0])
    G = sy.Matrix(n, n, lambda i, j: sum(z[i]*z[j] for z in P))
    ck(G.rank() == expected_rank)
    Gp = G.pinv()
    rs = [radial(z) for z in P]
    ck(all(r > 0 for r in rs))
    RR = sum(r*r for r in rs)
    bb = sy.Matrix([sum(r*z[i] for r, z in zip(rs, P)) for i in range(n)])
    ww = (bb.T*Gp*bb)[0]
    EE = sy.Rational(RR.numerator, RR.denominator)-ww
    alpha = [F(x) for x in -2*Gp*bb]
    ck(EE > 0)
    ck(G*Gp*bb == bb)
    for idx, u in enumerate(normals):
        # Optimized canonical caps: their exact clipped areas equal 2E.
        clipped = F(0)
        for z, r in zip(P, rs):
            poly = [tuple(r*x for x in p) for p in T]
            threshold = -dot(alpha, z)
            value = area(clip(poly, u, threshold))
            ck(value == ((2*r+dot(alpha, z))**2)/2)
            clipped += value
        eq(clipped, 2*EE)
        # A displaced angular/integer normal verifies the full chart formula.
        th = F(1, 17)
        angular = tuple(u[j]+th*normals[(idx+1) % 3][j] for j in range(2))
        displaced = [a+F(j+1, 211) for j, a in enumerate(alpha)]
        physical = F(0)
        expression = F(0)
        for z, r in zip(P, rs):
            poly = [tuple(r*x for x in p) for p in T]
            physical += area(clip(poly, angular, -dot(displaced, z)))
            expression += ((2-th)*r+dot(displaced, z))**2/(2*(1-th))
        ck(physical == expression)
        ck(physical > 2*EE)
    # Exact normalized gain identity, for arbitrary positive R0.
    R0 = F(7, 3)
    eq(V*R0*RR/EE-V*R0, V*R0*ww/EE)


# Genuine concave continuous radial fields: negative quadratic plus small
# affine and cubic perturbations. Their displayed boxes are complete bases.
for n in [1, 2, 3]:
    P = list(product(range(-1, 2), repeat=n))
    def radial(z, n=n):
        return (F(1)-sum(F(x*x, 10*n) for x in z)
                +sum(F((j+1)*x, 200) for j, x in enumerate(z)))
    physical_case(P, radial, n)
    # Each affine velocity is volume-neutral separately within every parity.
    for parity in product([0, 1], repeat=n):
        for coordinate in range(n):
            ck(sum((F(1)-sum(F(x*x, 10*n) for x in z))*z[coordinate]
                   for z in P if tuple(x % 2 for x in z) == parity) == 0)

P = list(product(range(-2, 3), repeat=2))
physical_case(P, lambda z: F(1)-F(z[0]**2+z[1]**2, 40)
              +F(z[0], 200)-F(z[1], 300)+F(z[0]**3, 2000), 2)

# Rank-deficient integer base inside a thin full-dimensional projection.
P = [(j, 0) for j in range(-2, 3)]
physical_case(P, lambda z: F(1)-F(z[0]**2, 20)+F(z[0], 100), 1)

# Exact null complement and nonzero affine moment on a full rank box.
P = list(product(range(-2, 3), repeat=2))
G = sy.Matrix(2, 2, lambda i, j: sum(z[i]*z[j] for z in P))
Z = sy.Matrix([[z[i] for z in P] for i in range(2)])
Q = Z.T*G.inv()*Z
ck(Q.rank() == 2)
ck(Q*Q == Q)
ck(Q.T == Q)
even = sy.Matrix([sy.Rational(z[0]**2-z[1]**2, 100) for z in P])
ck(Z*even == sy.zeros(2, 1))
ck(Q*even == sy.zeros(len(P), 1))
aff = sy.Matrix([sy.Rational(z[0], 100)-sy.Rational(z[1], 200) for z in P])
ck(Q*aff == aff)

print(f'PASS {checks} exact arithmetic, symbolic, and polygon-clipping checks')
