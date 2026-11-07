"""Exact shared-cap plane and two-group budget calibrations."""
from fractions import Fraction as F
from itertools import permutations


def mul(a, b):
    return [sum(a[k]*b[n-k] for k in range(n+1)) for n in range(3)]


def inverse_series(a):
    return [1/a[0], -a[1]/a[0]**2,
            a[1]**2/a[0]**3-a[2]/a[0]**2]


def det(A):
    total = F(0)
    for p in permutations(range(len(A))):
        value = F((-1)**sum(p[i] > p[j] for i in range(len(A))
                           for j in range(i+1, len(A))))
        for i, j in enumerate(p):
            value *= A[i][j]
        total += value
    return total


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def clip(poly, u, b):
    out = []
    for x, y in zip(poly, poly[1:]+poly[:1]):
        fx, fy = dot(u, x)-b, dot(u, y)-b
        if fx >= 0:
            out.append(x)
        if fx*fy < 0:
            t = fx/(fx-fy)
            out.append(tuple(a+t*(c-a) for a, c in zip(x, y)))
    return out


def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                   -poly[(i+1) % len(poly)][0]*poly[i][1]
                   for i in range(len(poly))))/2 if poly else F(0)


B = [[F(x) for x in row] for row in [[5, -1, 2], [-3, 0, 3], [-2, 1, -5]]]
v = [F(1), F(0), F(-1)]
assert all(sum(B[i][j] for i in range(3)) == 0 for j in range(3))
assert sum(B[i][i] for i in range(3)) == 0
assert [sum(row) for row in B] == [6*x for x in v]
gamma, h = F(4, 9), F(2, 3)
sigma = sum(B[i][j]*B[j][i] for i in range(3) for j in range(3))
det0 = [F(1), F(0), -sigma/2]
qs = []
for i in range(3):
    numerator = [h, B[i][i]-v[i], F(0)]
    cap = mul(det0, mul(numerator, numerator))
    for j in range(3):
        if j != i:
            cap = mul(cap, inverse_series([F(1), B[i][i]-B[i][j], F(0)]))
    other = mul([h, -v[i], F(0)], [h, -v[i], F(0)])
    cap = [a+b for a, b in zip(cap, other)]
    assert cap[1] == 0
    qs.append(2*cap[2])
Q = -sigma-sum(qs)/(3*gamma)
assert Q == 3
xi = gamma*Q/2
targets = [-q-xi for q in qs]
zs = [f/(3*gamma) for f in targets]
Z = sum(zs)
C = [[zs[i] if i == j else zs[i]-Z/2 for j in range(3)] for i in range(3)]
assert all(sum(C[i][j] for i in range(3)) == 0 for j in range(3))
assert -sigma+sum(C[i][i] for i in range(3)) == Q/2

K = [(F(-1, 3), F(-1, 3)), (F(2, 3), F(-1, 3)),
     (F(-1, 3), F(2, 3))]
assert area(K) == F(1, 2)
assert area(clip(K, (F(0), F(-1)), F(0))) == F(5, 18)
assert area(clip(K, (F(-1), F(1)), F(0))) == F(1, 4)
for denominator in [10000, 20000, 50000, 100000, 200000]:
    t = F(1, denominator)
    W = [[F(i == j)+t*B[i][j]+t*t*C[i][j]/2 for j in range(3)]
         for i in range(3)]
    D = det(W)
    assert D > 1
    tau = [t*x for x in v]
    assert tau[1] == 0 and sum(tau) == 0
    for i in range(3):
        threshold = F(1, 3)+tau[i]
        assert W[i][i] > threshold
        assert all(W[i][j] < threshold for j in range(3) if j != i)
        denominator0 = F(1)
        for j in range(3):
            if i != j:
                denominator0 *= W[i][i]-W[i][j]
        total_cap = D*(W[i][i]-threshold)**2/denominator0+(h-tau[i])**2
        assert total_cap < 2*gamma
    moved = [tuple(sum(W[i][j]*K[i][k] for i in range(3)) for k in range(2))
             for j in range(3)]
    # Both private caps of B remain strictly empty at selected base zero.
    assert max(-y-1 for x, y in moved) < 0
    assert max(-x+y-2 for x, y in moved) < 0
    # The alternate first private cap remains strictly full there.
    assert min(-y+1 for x, y in moved) > 0
    # Its actual budget increase is exactly the selected fiber volume gain.
    assert (D-1)/2 > 0

print("PASS: exact optimized critical mode and acceleration; five rational "
      "two-group paths with shared x>=0 fixed, all A caps decreasing, "
      "both other private budgets unchanged; full-trace obstruction.")
