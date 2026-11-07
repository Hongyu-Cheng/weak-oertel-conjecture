"""Exact finite certificates; no floating-point or direction sampling."""
from fractions import Fraction as F
from itertools import product

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


n, d = 3, 2
cube = list(product((0, 1), repeat=n))
zero = (0,) * n
minus = (-1,) * n
plus = (1,) * n
units = [tuple(int(i == j) for i in range(n)) for j in range(n)]
P = [minus] + cube
N = len(P)
eps, a = F(1, 10), F(1, 100)
gamma, b, c2 = F(4, 9), F(1, 3), F(5, 9)
Q, M = gamma + a, F(8) + a
check(N == 9)
check(len({tuple(v % 2 for v in z) for z in P}) == 8)
check(F(1) < M / 8)
check((3 + 9 * a / 2) ** 2 < 10)
check(c2 < F(9, 16))
check(81 > 80)
check(Q == F(409, 900))
check(M == F(801, 100))
check(Q - gamma * M / 8 == F(17, 1800))
check(N * c2 == 5)
check((1 - b) ** d == gamma)

# Actual rational triangle area via determinant.
triangle = [(F(0), F(0)), (F(1), F(0)), (F(0), F(2))]
check((triangle[1][0] * triangle[2][1]
       - triangle[1][1] * triangle[2][0]) / 2 == 1)


def bary(x):
    return (1 - x[0] - x[1] / 2, x[0], x[1] / 2)


small = [(eps * x, eps * y) for x, y in triangle]
check(all(sum(bary(x)) == 1 for x in triangle + small))
check(all(all(t >= 0 for t in bary(x)) for x in triangle + small))


def delta(w, z):
    return (n + 1) * sum(1 - z[j] for j in range(n) if w[j]) + sum(
        z[j] for j in range(n) if not w[j])


for i in range(d + 1):
    # H_i captures A strictly; excludes all nonzero cube fibers strictly.
    check(min(bary(x)[i] - 2 * sum(minus) for x in small) > b)
    for z in cube:
        if z != zero:
            check(max(bary(x)[i] - 2 * sum(z) for x in triangle) < b)
    for w in cube:
        if w == zero:
            continue
        check(delta(w, w) == 0)
        check(delta(w, minus) == (2 * n + 3) * sum(w) - n)
        check(delta(w, minus) >= n + 3)
        check(max(bary(x)[i] - 2 * delta(w, minus) for x in small) < b)
        for z in cube:
            if z != w:
                check(delta(w, z) >= 1)
                check(max(bary(x)[i] - 2 * delta(w, z) for x in triangle) < b)

# KKT multipliers scaled by s=2c. All exact entries below are integers.
mu = {(zero, z): F(1) for z in [minus] + units}
lam = {z: F(0) if z in [minus] + units else F(1) for z in P}
lam[zero] = n + 2
for z in P:
    out = sum(v for (x, y), v in mu.items() if x == z)
    incoming = sum(v for (x, y), v in mu.items() if y == z)
    check(lam[z] == 1 + out - incoming)
    for j in range(n):
        check(sum(v * (y[j] - z[j]) for (x, y), v in mu.items() if x == z) == 0)
    if lam[z] > 0:
        check(z in cube)  # Exactly the positive obstacle contacts.

T = [[F(0) for _ in P] for _ in P]
D = []
for i, z in enumerate(P):
    out = sum(v for (x, y), v in mu.items() if x == z)
    D.append(1 / (1 + out))
    for j, y in enumerate(P):
        T[i][j] = mu.get((z, y), F(0)) / (1 + out)
for i in range(N):
    for j in range(N):
        check(sum(T[i][k] * T[k][j] for k in range(N)) == 0)
pi = [[lam[z] * (int(i == j) + T[i][j]) * D[j]
       for j in range(N)] for i, z in enumerate(P)]
for i, z in enumerate(P):
    check(sum(pi[i]) == lam[z])
    for j in range(n):
        check(sum(pi[i][k] * P[k][j] for k in range(N)) == lam[z] * z[j])
for j in range(N):
    check(sum(pi[i][j] for i in range(N)) == 1)
source = P.index(zero)
for j, y in enumerate(P):
    check(pi[source][j] == int(y in [zero, minus] + units))

# Every critical coefficient beta_j <= -2/3 has the same volume traces.
# Check its maximal possible threshold margins symbolically at beta_j=-2/3;
# monotonicity toward smaller coefficients then gives the full menu.
beta = [-(1 - b)] * n
for z in cube:
    if z != zero:
        check(b - sum(beta[j] * z[j] for j in range(n)) >= 1)
check(b + sum(beta) < 0)

# The row numerator is c+3. Gap positive iff c<3/4, checked above.
# General existence condition n=3d, checked symbolically by Bernoulli proof
# in the source, with finite rational instances only as corroboration.
for dim in range(2, 31):
    nn = 3 * dim
    gg = F(dim, dim + 1) ** dim
    check(gg > F(1, 3))
    check(F(nn, nn + 1) ** dim > 1 - gg)

print(f"PASS: {checks} exact rational checks; analytic all-normal proof in source.")
