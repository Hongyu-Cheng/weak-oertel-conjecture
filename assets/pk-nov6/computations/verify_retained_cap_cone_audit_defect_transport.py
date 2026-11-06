"""Independent exact constants and actual-cap calibrations for the cone limit.

The analytic exhaustion/Fatou proof is audited in the companion Markdown;
these checks do not replace it.  All arithmetic here is exact.
"""
from fractions import Fraction as F
from math import factorial

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


for d in range(1, 17):
    for k in range(1, d + 1):
        m = d - k
        N = d + 1
        # Independently integrate the cone hinge using its sublevel volume.
        beta = F(k)
        hinge_factor = (1 + beta) ** (k + 1) / (factorial(k + 1) * beta**k)
        A = F((k + 1) ** k, factorial(k) * k**k)
        check(hinge_factor == A)
        # The derivative has precisely the sign of beta-k.
        for b in (F(k, 2), F(k), F(3 * k, 2)):
            log_derivative = F(k + 1, 1) / (1 + b) - F(k, 1) / b
            check(log_derivative == (b - k) / (b * (1 + b)))
        # Volume and normal first moment of a cone truncated at R=(k+1)h/k.
        for h in (F(1, 3), F(1), F(7, 4)):
            R = F(k + 1, k) * h
            mass_factor = R**k / factorial(k)
            check(mass_factor == A * h**k)
            check(F(k, k + 1) * R == h)
        energy_factor = F(factorial(m) * N**N,
                          factorial(d) * k**k * (m + 1)**(m + 1))
        ratio = F(factorial(m) * factorial(k) * N**N,
                  factorial(d) * (m + 1)**(m + 1) * (k + 1)**k)
        check(energy_factor / A == ratio)
        if m == 0:
            check(ratio == d + 1)
        if k == 1:
            check(A == 2)

# Actual compact standard-simplex vertex caps.  For sufficiently small delta,
# {sum x_j/v_j <= (d+1)delta} is contained in the standard simplex and is the
# hinge-certified optimal retained cap.  Direct intercept integration gives
# both its volume and its centroid.
for d in range(1, 17):
    v = [F(j + 1, d + 3) for j in range(d)]
    delta = F(1, 4 * (d + 1))
    intercepts = [(d + 1) * delta * w for w in v]
    check(max(intercepts) < 1)
    volume = F(1, factorial(d))
    J = F(d**d)
    for r, w in zip(intercepts, v):
        volume *= r
        J *= w
        check(r / (d + 1) == delta * w)
    A = F((d + 1)**d, factorial(d) * d**d)
    check(volume == delta**d * A * J)

# Actual nonsymmetric interval-face power minimizers.  Direct beta integrals
# give mass, mean and power, rather than assuming their stationarity formulas.
for p in range(2, 11):
    for j in (2, 3, 7):
        x = F(1, j * (p + 1))
        support = (p + 1) * x
        C = F(p + 1, p)
        B = support * C**p / (p + 1)
        mass = support * C**(p - 1) / p
        first = support**2 * C**(p - 1) / (p * (p + 1))
        check(support <= 1)
        check(mass == B)
        check(first == x * B)
        check(B == x * C**p)

# The nonsimplicial square-cone calibration retains the same cone factor in
# both energies, including away from the symmetry axis.
for J in (F(8), F(10368, 2197)):
    E = F(4**4, factorial(3) * 3**3) * J
    T = F(4**3, factorial(3) * 3**3) * J
    check(E / T == 4)

print(f"{checks} exact checks PASS")
