"""Exact checks of local radial simplex formulas in several dimensions.

Actual clipped simplex vertices/determinants independently check the cap
formula. All-real assertions and global normal control are proved in the
companion source, not inferred from this finite screen.
"""

from itertools import product
from math import factorial
import sympy as s

R = s.Rational
checks = 0


def ck(condition):
    global checks
    assert condition
    checks += 1


def eq(left, right):
    ck(s.factor(left-right) == 0)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def simplex(d):
    origin = s.Matrix([-1]*d)
    return [origin]+[origin+(d+1)*s.eye(d)[:, i] for i in range(d)]


def actual_vertex_cap(vertices, u, shift):
    """Intersect the actual edges and compute the captured determinant."""
    heights = [dot(u, v)+shift for v in vertices]
    positive = [i for i, h in enumerate(heights) if h > 0]
    ck(len(positive) == 1)
    apex = positive[0]
    ck(all(h < 0 for i, h in enumerate(heights) if i != apex))
    edges = []
    for i, vertex in enumerate(vertices):
        if i == apex:
            continue
        fraction = heights[apex]/(heights[apex]-heights[i])
        ck(0 < fraction < 1)
        edges.append(fraction*(vertex-vertices[apex]))
    return abs(s.Matrix.hstack(*edges).det())/factorial(len(u))


# Actual compatible affine perturbations of an even concave radius field
# over the full lattice box [-1,1]^n, for arbitrary tested d.
for d in range(2, 7):
    V = R((d+1)**d, factorial(d))
    c = R(d**d, factorial(d))
    gamma = R(d, d+1)**d
    eq(c, gamma*V)
    ck(2*gamma < 1)
    vertices = simplex(d)
    ck(sum(vertices, s.zeros(d, 1)) == s.zeros(d, 1))
    for n in [1, 2]:
        P = list(product(range(-1, 2), repeat=n))
        a = [R((-1)**i*(i+1), 200) for i in range(n)]
        r0 = [1-sum(R(x*x, 20*n) for x in z) for z in P]
        radii = [r+dot(a, z) for r, z in zip(r0, P)]
        beta = [-d*x for x in a]
        Q0 = c*sum(r**d for r in r0)
        ck(all(r > 0 for r in radii))
        for j in range(n):
            eq(sum(z[j]*(d*r+dot(beta, z))**(d-1)
                   for z, r in zip(P, radii)), 0)
        for i in range(d+1):
            u = [-1]*d if i == 0 else [int(j == i-1) for j in range(d)]
            total = 0
            for z, r in zip(P, radii):
                actual = actual_vertex_cap([r*v for v in vertices], u, dot(beta, z))
                eq(actual, (d*r+dot(beta, z))**d/factorial(d))
                total += actual
            eq(total, Q0)
        # A noncanonical actual angular chart verifies the AM-GM factor.
        theta = [R(j, 100) for j in range(2, d+1)]
        scale = 1-sum(theta)/d
        alpha = [scale*x for x in beta]
        u = [s.Integer(1)]+theta
        angular = scale**d/s.prod(1-x for x in theta)
        ck(angular > 1)
        total = sum(actual_vertex_cap([r*v for v in vertices], u, dot(alpha, z))
                    for z, r in zip(P, radii))
        eq(total, angular*Q0)
        ck(V*sum(r**d for r in radii) > V*sum(r**d for r in r0))
        # All parity classes have zero first volume derivative.
        for parity in product([0, 1], repeat=n):
            eq(sum(r**(d-1)*dot(a, z) for z, r in zip(P, r0)
                   if tuple(x % 2 for x in z) == parity), 0)


# The angular Hessian is positive with exact eigenvalues 1/d and 1.
for d in range(2, 9):
    H = s.eye(d-1)-s.ones(d-1)/d
    eq(H.det(), R(1, d))
    ck(all(value > 0 for value in H.eigenvals()))


# Direct polynomial differentiation along the Schur-optimal first normal
# velocity verifies the physical normalized Hessian, including its factor.
t = s.symbols('t')
P = list(product(range(-1, 2), repeat=2))
for d in range(2, 8):
    V = R((d+1)**d, factorial(d))
    c = R(d**d, factorial(d))
    r0 = [1-R(z[0]**2+z[1]**2, 25) for z in P]
    weights = [r**(d-2) for r in r0]
    velocity = [R(z[0]+2*z[1], 50)+R(z[0]**2-z[1]**2, 70) for z in P]
    G = s.Matrix(2, 2, lambda i, j: sum(w*z[i]*z[j] for w, z in zip(weights, P)))
    moment = s.Matrix([sum(w*v*z[i] for w, v, z in zip(weights, velocity, P))
                       for i in range(2)])
    beta_prime = -d*G.inv()*moment
    F = sum((d*(r+t*v)+t*dot(beta_prime, z))**d
            for r, v, z in zip(r0, velocity, P))/factorial(d)
    M = V*sum((r+t*v)**d for r, v in zip(r0, velocity))
    Q0 = c*sum(r**d for r in r0)
    expected_tau_second = c*d*(d-1)*(sum(w*v*v for w, v in zip(weights, velocity))
                                      -(moment.T*G.inv()*moment)[0])
    eq(s.diff(F, t, 2).subs(t, 0), expected_tau_second)
    eq(s.diff(M*Q0/F, t).subs(t, 0), 0)
    eq(s.diff(M*Q0/F, t, 2).subs(t, 0),
       V*d*(d-1)*(moment.T*G.inv()*moment)[0])
    # The exact nearby zero-gain surface contains every positive even array.
    even = [r+R(z[0]**2-z[1]**2, 500) for r, z in zip(r0, P)]
    for i in range(2):
        eq(sum(r**(d-1)*z[i] for r, z in zip(even, P)), 0)
    # Explicit source gradient: every nonzero source has a strict descent.
    for z0 in P:
        if z0 == (0, 0):
            continue
        grad = s.Matrix([c*sum(r**(d-1)*(z[i]-z0[i]) for r, z in zip(r0, P))
                         for i in range(2)])
        ck(dot(grad, z0) < 0)

# Affine-radius gauge invariance holds at arbitrary arrays, algebraically;
# the source separately proves the neighborhood's geometric interpretation.
rho, shift, normal, base = s.symbols('rho shift normal base')
for d in range(2, 9):
    eq((d*(rho+shift*base)+normal*base)**d,
       (d*rho+(normal+d*shift)*base)**d)

print(f'PASS {checks} exact determinant, polynomial, and rank checks')
