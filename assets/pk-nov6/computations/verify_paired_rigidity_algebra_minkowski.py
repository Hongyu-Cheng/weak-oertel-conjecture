"""Independent exact algebra checks for paired rigidity in dimensions >= 3.

These checks certify the displayed finite identities.  They are not a
replacement for the localization, compactness, or geometric proofs.
Only the Python standard library is used.
"""

from fractions import Fraction as F


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return trim([c * x for x in p])


def mul(p, q):
    ans = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            ans[i + j] += a * b
    return trim(ans)


def power(p, n):
    ans = [F(1)]
    for _ in range(n):
        ans = mul(ans, p)
    return ans


def derivative(p):
    return trim([i * p[i] for i in range(1, len(p))] or [0])


def evaluate(p, r):
    ans = F(0)
    for a in reversed(p):
        ans = ans * r + a
    return ans


checks = 0
A = [1, 1, 1]
N = [1, 1, 1, 3]
P = [1, 4, 10, 8, 23, 80, 90, 108, 81]
left = add(mul([5, 0, 0, 27], power(A, 3)), scale(power(N, 3), -4))
assert left == mul([1, -1], P)
checks += 1
assert all(a > 0 for a in P)
checks += 1

# Direct rational checks of the derived d=3 quotient, including r=0.
for denominator in range(1, 65):
    for numerator in range(denominator):
        r = F(numerator, denominator)
        mean = F(3, 4) * (1 - r ** 4) / (1 - r ** 3)
        tail = ((2 * mean - 1) ** 3 - r ** 3) / (1 - r ** 3)
        gap = F(5, 32) - tail
        assert gap == evaluate(P, r) / (32 * evaluate(A, r) ** 4)
        assert gap > 0
        checks += 1

# Clear denominators in the claimed logarithmic derivative.
# J = -log(v) - R(v)/D(v).
R = [7, -2, -5]
D = [2, 10]
quotient_numerator = add(mul(derivative(R), D),
                         scale(mul(R, derivative(D)), -1))
cleared_derivative = add(scale(power([1, 5], 2), -2),
                         scale(mul([0, 1], quotient_numerator), F(-1, 2)))
assert cleared_derivative == mul(mul([-1, 1], [-1, 5]), [-2, 5])
checks += 1

log5_lower = 2 * sum(F(2, 3) ** (2 * j + 1) / (2 * j + 1)
                     for j in range(4))
assert log5_lower > F(8, 5)
checks += 1
assert 1 - 2 * F(4, 5) ** 4 - F(1, 6) == F(53, 3750)
checks += 1

print(f"PASS: {checks} exact paired-rigidity algebra checks")
print(f"Four-term log(5) lower bound minus 8/5: {log5_lower - F(8, 5)}")
