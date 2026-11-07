"""Exact polygon checks of the proved joint clipping identity."""
from fractions import Fraction as F
from random import Random


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(a[0] * b[1] - a[1] * b[0]
                   for a, b in zip(poly, poly[1:] + poly[:1]))) / 2


def clip(poly, n, h):
    out = []
    for x, y in zip(poly, poly[1:] + poly[:1]):
        a = sum(n[j] * x[j] for j in range(2)) - h
        b = sum(n[j] * y[j] for j in range(2)) - h
        if a >= 0:
            out.append(x)
        if a * b < 0:
            t = a / (a - b)
            out.append(tuple(x[j] + t * (y[j] - x[j]) for j in range(2)))
    return out


def inv(S):
    aug = [list(S[i]) + [F(i == j) for j in range(3)] for i in range(3)]
    for i in range(3):
        j = next(j for j in range(i, 3) if aug[j][i])
        aug[i], aug[j] = aug[j], aug[i]
        t = aug[i][i]
        aug[i] = [x / t for x in aug[i]]
        for j in range(3):
            if j != i:
                t = aug[j][i]
                aug[j] = [x - t * y for x, y in zip(aug[j], aug[i])]
    return [row[3:] for row in aug]


checks = cases = 0
rng = Random(2431)
ns = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(-1))]
for trial in range(1500):
    p, r, s = [F(rng.randrange(1, 30), 30) for _ in range(3)]
    P = [(F(0), p), (r, F(0)), (s, 1 - s)]
    if not area(P):
        continue
    raw = [F(rng.randrange(1, 6)) for _ in range(3)]
    a0 = [x / sum(raw) for x in raw]
    y = [sum(a0[j] * P[j][i] for j in range(3)) for i in range(2)]
    u = [y[0], y[1], 1 - y[0] - y[1]]
    lam = [[x[0], x[1], 1 - x[0] - x[1]] for x in P]
    captured = [[j for j in range(3) if lam[j][i] > u[i]] for i in range(3)]
    if any(len(row) != 1 for row in captured):
        continue
    if any(lam[j][i] == u[i] for j in range(3) for i in range(3)):
        continue
    order = [row[0] for row in captured]
    if len(set(order)) != 3:
        continue
    P = [P[j] for j in order]
    S = [[P[j][i] if i < 2 else 1 - sum(P[j])
          for j in range(3)] for i in range(3)]
    R = inv(S)
    aa = [sum(R[i][j] * u[j] for j in range(3)) for i in range(3)]
    k = area(P)
    thresholds = [u[0], u[1], u[2] - 1]
    q = [area(clip(P, ns[i], thresholds[i])) / k for i in range(3)]
    pairs = []
    for i in range(3):
        poly = P
        for j in range(3):
            if j != i:
                poly = clip(poly, ns[j], thresholds[j])
        pairs.append(area(poly) / k)
    alpha = [2 * u[i] / S[i][i] for i in range(3)]
    beta = [2 - 2 * aa[i] / R[i][i] for i in range(3)]
    assert all(R[i][i] > 0 and 0 < beta[i] < 2 and pairs[i] > 0
               and 0 < alpha[i] < 2 for i in range(3))
    checks += 1
    scales = sorted(set([F(j, 10) for j in range(21)] + alpha + beta))
    for rho in scales:
        poly = [tuple(rho * x for x in point) for point in P]
        poly = clip(poly, (-1, 0), -2 * u[0])
        poly = clip(poly, (0, -1), -2 * u[1])
        poly = clip(poly, (1, 1), rho - 2 * u[2])
        actual = area(poly) / k
        formula = rho * rho
        for i in range(3):
            formula -= 4 * q[i] * (max(F(0), rho - alpha[i]) / (2 - alpha[i])) ** 2
            formula += 4 * pairs[i] * (max(F(0), rho - beta[i]) / (2 - beta[i])) ** 2
        assert actual == formula, (P, u, rho, actual, formula)
        checks += 1
    cases += 1
print(f"PASS: {checks} exact checks on {cases} actual triangle/source configurations")
