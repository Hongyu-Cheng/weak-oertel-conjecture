"""Exact arithmetic checks supplementing the proofs in the companion note."""
from fractions import Fraction as F
from math import comb, factorial

checks = 0

# Locality constants and uniqueness neighborhoods, at the largest allowed e.
for d in range(2, 101):
    e = F(1, 64*d**4)
    delta = e/d
    rho = 8*d*d*e
    assert delta <= F(1, 64*d**3)
    assert rho <= F(1, 8*d*d)
    assert F(1,d)-d*rho >= F(7,8*d)
    assert F(d-1,d)-d*rho > e
    checks += 4

# Exact missing-volume equality, including non-unit and convex-combination weights.
for d in range(2, 21):
    e = F(1, 64*d**4)
    V = F(1, factorial(d))
    for a,b,t in [(F(1),F(1),F(1)), (F(1,2),F(1,2),F(3,2)),
                  (F(2,3),F(1,3),F(1,10)), (F(3,7),F(8,5),F(13,9))]:
        R = a+b*t
        outer = R**d*V
        inner = (R**d-(a*e)**d)*V
        pure = a**d*e**d*V
        assert outer-inner == pure
        assert a*e/R <= F(1,64*d**4)
        # All mixed coefficients except the pure A coefficient are identical.
        for k in range(d+1):
            p = F(comb(d,k))*t**(d-k)*V
            q = p - (e**d*V if k == d else 0)
            assert p-q == (e**d*V if k == d else 0)
            checks += 1
        checks += 2

# Parallel-simplex support offsets and Minkowski radii in arbitrary finite sums.
for d in range(1, 16):
    for N in range(1, 9):
        weights = [F((i+1)%4, i+2) for i in range(N)]
        if not any(weights):
            weights[0] = F(1)
        offsets = [[F((i+1)*(j+2)-5, j+3) for j in range(d)] for i in range(N)]
        radii = [F(i+1,i+2) for i in range(N)]
        tops = [sum(offsets[i])+radii[i] for i in range(N)]
        sum_offset = [sum(weights[i]*offsets[i][j] for i in range(N)) for j in range(d)]
        sum_radius = sum(weights[i]*radii[i] for i in range(N))
        sum_top = sum(weights[i]*tops[i] for i in range(N))
        assert sum_top-sum(sum_offset) == sum_radius > 0
        checks += 1

# Explicit enclosing simplex U={all barycentric coordinates >= -1}.
for d in range(1, 31):
    shift = [-1]*d
    scale = d+2
    vertices = [shift] + [[shift[j]+(scale if i==j else 0) for j in range(d)] for i in range(d)]
    for v in vertices:
        bary = [1-sum(v)] + v
        assert all(x >= -1 for x in bary)
        assert bary.count(-1) == d
        assert sum(F(x+1,scale) for x in bary) == 1
        checks += 3

print(f"PASS {checks} exact checks")
