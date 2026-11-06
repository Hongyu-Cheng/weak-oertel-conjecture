"""Exact joint Hessian, acceleration, and physical cap-budget verification."""
from fractions import Fraction as F


class Series:
    """Exact truncated series through degree two."""
    def __init__(self, *coefficients):
        self.c = tuple(F(coefficients[i]) if i < len(coefficients) else F(0)
                       for i in range(3))

    @staticmethod
    def cast(x):
        return x if isinstance(x, Series) else Series(x)

    def __add__(self, x):
        x = self.cast(x)
        return Series(*(a+b for a, b in zip(self.c, x.c)))

    __radd__ = __add__

    def __neg__(self):
        return Series(*(-a for a in self.c))

    def __sub__(self, x):
        return self + -self.cast(x)

    def __rsub__(self, x):
        return self.cast(x) - self

    def __mul__(self, x):
        x = self.cast(x)
        return Series(*(sum(self.c[j]*x.c[i-j] for j in range(i+1))
                        for i in range(3)))

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.cast(x)
        inverse = [1/x.c[0]]
        for i in range(1, 3):
            inverse.append(-sum(x.c[j]*inverse[i-j] for j in range(1, i+1))/x.c[0])
        return self*Series(*inverse)

    def __rtruediv__(self, x):
        return self.cast(x)/self

    def __pow__(self, exponent):
        out = Series(1)
        for _ in range(exponent):
            out *= self
        return out


def determinant(matrix):
    a = [row[:] for row in matrix]
    answer = 1
    for j in range(len(a)):
        pivot = a[j][j]
        assert (pivot.c[0] if isinstance(pivot, Series) else pivot) != 0
        answer *= pivot
        for i in range(j+1, len(a)):
            factor = a[i][j]/pivot
            for k in range(j+1, len(a)):
                a[i][k] -= factor*a[j][k]
    return answer


def cuts(w, a):
    m, d = len(a), len(a)-1
    volume = determinant(w)
    cap = []
    for i in range(m):
        value = volume*(w[i][i]-a[i])**d
        for j in range(m):
            if i != j:
                value /= w[i][i]-w[i][j]
        cap.append(value)
    return volume, cap


def right_inverse(f, d):
    m = d+1
    gamma = F(d, m)**d
    z = [x/(m*gamma) for x in f]
    total = sum(z)
    return [[z[i] if i == j else z[i]-total/d for j in range(m)]
            for i in range(m)]


def first_derivatives(b, d):
    m = d+1
    gamma = F(d, m)**d
    trace = sum(b[i][i] for i in range(m))
    return [gamma*(trace+sum(b[i][j] for j in range(m))) for i in range(m)]


def matrix_data(d):
    m = d+1
    gamma = F(d, m)**d
    e = [[F(0) for _ in range(m)] for _ in range(m)]
    e[0][1], e[1][1] = F(1), F(-1)
    lift = right_inverse(first_derivatives(e, d), d)
    b = [[e[i][j]-lift[i][j] for j in range(m)] for i in range(m)]
    omega = [F(-1), F(1)]+[F(0)]*(d-1)
    diagonal = [b[i][i] for i in range(m)]
    sigma = sum(b[i][j]*b[j][i] for i in range(m) for j in range(m))
    row_energy = [sum((diagonal[i]-b[i][j])**2 for j in range(m) if i != j)
                  for i in range(m)]
    q = [gamma*(-sigma-F(m*m, d)*diagonal[i]**2+row_energy[i]
                +2*F(m*m, d)*diagonal[i]*omega[i]) for i in range(m)]
    q_joint = F(d-1, d)*(2-F(1, m))
    epsilon = gamma*q_joint/2
    c = right_inverse([-x-epsilon for x in q], d)
    return b, omega, q, q_joint, epsilon, c


checks = 0
for d in range(2, 13):
    m = d+1
    gamma = F(d, m)**d
    b, omega, q, q_joint, epsilon, c = matrix_data(d)
    diagonal = [b[i][i] for i in range(m)]
    assert diagonal == [F(0), -F(d-1, m)]+[F(1, m)]*(d-1)
    assert all(sum(b[i][j] for i in range(m)) == 0 for j in range(m))
    assert all(sum(c[i][j] for i in range(m)) == 0 for j in range(m))
    assert first_derivatives(b, d) == [0]*m
    assert sum(diagonal) == 0
    assert sum(x*x for x in diagonal) == F(d*(d-1), m*m)
    assert sum(b[i][j]**2 for i in range(m) for j in range(m) if i != j) == (
        F(d-1, d)+F(d-1, m*m))
    assert first_derivatives(c, d) == [-x-epsilon for x in q]
    sigma = sum(b[i][j]*b[j][i] for i in range(m) for j in range(m))
    assert -sigma-sum(q)/(m*gamma) == q_joint
    assert -sigma+sum(c[i][i] for i in range(m)) == q_joint/2
    checks += 1

    # Independently recover Hessians by expanding the exact cap formula.
    time = Series(0, 1)
    thresholds = [Series(F(1, m))+time*omega[i] for i in range(m)]
    straight = [[Series(i == j)+time*b[i][j] for j in range(m)] for i in range(m)]
    vol_straight, cap_straight = cuts(straight, thresholds)
    for i in range(m):
        increment = cap_straight[i]-(1-thresholds[i])**d
        assert increment.c == (0, 0, q[i]/2)
    assert vol_straight.c == (1, 0, -sigma/2)
    path = [[Series(i == j)+time*b[i][j]+time*time*c[i][j]/2
             for j in range(m)] for i in range(m)]
    volume, cap = cuts(path, thresholds)
    assert volume.c == (1, 0, q_joint/4)
    for i in range(m):
        increment = cap[i]-(1-thresholds[i])**d
        assert increment.c == (0, 0, -gamma*q_joint/4)
    checks += 1

    # Actual rational matrices and all individual global budget signs.
    t = F(1, 10000)
    a = [F(1, m)+t*omega[i] for i in range(m)]
    w = [[F(i == j)+t*b[i][j]+t*t*c[i][j]/2 for j in range(m)] for i in range(m)]
    assert sum(a) == 1 and all(0 < x < 1 for x in a)
    assert all(sum(w[i][j] for i in range(m)) == 1 for j in range(m))
    assert all(sum(abs(w[i][j]-F(i == j)) for i in range(m)) < 2 for j in range(m))
    for j in range(m):
        for k in range(m):
            assert sum(max(F(0), (w[i][j]-F(i == k))/2) for i in range(m)) < 1
    assert all(w[i][i] > a[i] and all(w[i][j] < a[i] for j in range(m) if i != j)
               for i in range(m))
    volume, cap = cuts(w, a)
    assert volume > 1 and all(cap[i] < (1-a[i])**d for i in range(m))
    checks += 1
    if d == 2:
        planar_a, planar_w = a, w
        planar_gain = (volume-1)/2


def area(poly):
    if not poly:
        return F(0)
    return abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                   -poly[i][1]*poly[(i+1) % len(poly)][0] for i in range(len(poly))))/2


def clip(poly, u, constant):
    out = []
    for i, p in enumerate(poly):
        nxt = poly[(i+1) % len(poly)]
        v = sum(x*y for x, y in zip(u, p))+constant
        w = sum(x*y for x, y in zip(u, nxt))+constant
        if v >= 0:
            out.append(p)
        if v < 0 < w or w < 0 < v:
            ratio = v/(v-w)
            out.append(tuple(p[j]+ratio*(nxt[j]-p[j]) for j in range(2)))
    return out


third = F(1, 3)
k = [(-third, -third), (1-third, -third), (-third, 1-third)]
minus_k = [(-x, -y) for x, y in k]
middle = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(1)),
          (F(-1), F(0)), (F(0), F(-1)), (F(1), F(-1))]
moving = [(planar_w[1][i]-third, planar_w[2][i]-third) for i in range(3)]
assert area(moving)-area(k) == planar_gain > 0
for i, u in enumerate([(-F(1), -F(1)), (F(1), F(0)), (F(0), F(1))]):
    beta = planar_a[i]-third
    old = area(clip(k, u, -beta))
    new = area(clip(moving, u, -beta))
    total = new+area(clip(middle, u, F(0)))+area(clip(minus_k, u, beta))
    assert total == 2+new-old < 2
    checks += 1

print("PASS:", checks, "exact joint-Hessian, acceleration, compatible-path and planar global-cap checks.")
print("Dimensions 2 through 12; rational path time 1/10000.")
print("Planar absolute volume gain:", planar_gain)
