"""Exact physical derivatives, right inverse, and rational strict-gain witness."""
from fractions import Fraction as F
from random import Random


class Dual:
    def __init__(self, x, dx=0):
        self.x, self.dx = F(x), F(dx)
    @staticmethod
    def cast(other):
        return other if isinstance(other, Dual) else Dual(other)
    def __add__(self, other):
        b = self.cast(other)
        return Dual(self.x+b.x, self.dx+b.dx)
    __radd__ = __add__
    def __neg__(self):
        return Dual(-self.x, -self.dx)
    def __sub__(self, other):
        return self + (-self.cast(other))
    def __rsub__(self, other):
        return self.cast(other) - self
    def __mul__(self, other):
        b = self.cast(other)
        return Dual(self.x*b.x, self.dx*b.x+self.x*b.dx)
    __rmul__ = __mul__
    def __truediv__(self, other):
        b = self.cast(other)
        return Dual(self.x/b.x, (self.dx*b.x-self.x*b.dx)/(b.x*b.x))
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        if n == 0:
            return Dual(1)
        return Dual(self.x**n, n*self.x**(n-1)*self.dx)


def det(matrix):
    a = [row[:] for row in matrix]
    ans = 1
    for j in range(len(a)):
        pivot = a[j][j]
        # All inputs used here have nonzero diagonal Gaussian pivots.
        assert (pivot.x if isinstance(pivot, Dual) else pivot) != 0
        ans *= pivot
        for i in range(j+1, len(a)):
            factor = a[i][j]/pivot
            for k in range(j+1, len(a)):
                a[i][k] -= factor*a[j][k]
    return ans


def cap_formula(W, a):
    m, d = len(a), len(a)-1
    volume = det(W)
    caps = []
    for i in range(m):
        f = volume*(W[i][i]-a[i])**d
        for j in range(m):
            if j != i:
                f /= W[i][i]-W[i][j]
        caps.append(f)
    return volume, caps


def derivatives(B, a):
    m, d = len(a), len(a)-1
    tr = sum(B[i][i] for i in range(m))
    out = []
    for i in range(m):
        k = F(d)/(1-a[i])-m
        s = sum(B[i][j] for j in range(m) if i != j)
        out.append((1-a[i])**d*(tr+s+(1+k)*B[i][i]))
    return tr, out


def inverse(f, a):
    m, d = len(a), len(a)-1
    h = [d*(1-x)**(d-1) for x in a]
    z = [x/y for x,y in zip(f,h)]
    total = sum(z)
    return [[z[i] if i == j else z[i]-total/d
             for j in range(m)] for i in range(m)]


def improvement(a):
    m, d = len(a), len(a)-1
    triples = [(a[j]+(a[i]-sum(a))/d, i, j)
               for i in range(m) for j in range(m) if i != j]
    value,i,j = max(triples, key=lambda x: abs(x[0]))
    assert value
    sigma = 1 if value > 0 else -1
    E = [[F(0) for _ in a] for _ in a]
    E[i][j], E[j][j] = F(sigma), F(-sigma)
    tr, f = derivatives(E,a)
    S = inverse(f,a)
    B0 = [[E[i][j]-S[i][j] for j in range(m)] for i in range(m)]
    assert derivatives(B0,a) == (abs(value), [F(0)]*m)
    H = sum(1/(d*(1-x)**(d-1)) for x in a)
    eps = abs(value)/(2*H)
    correction = inverse([-eps]*m,a)
    B = [[B0[i][j]+correction[i][j] for j in range(m)] for i in range(m)]
    assert derivatives(B,a) == (abs(value)/2, [-eps]*m)
    return B, eps


rng = Random(92731)
checks = 0
for d in range(1,9):
    m = d+1
    for case in range(12):
        raw = [rng.randrange(1,20) for _ in range(m)]
        a = [F(x,sum(raw)) for x in raw]
        if case % 2:
            a = [x/F(2) for x in a]  # Nonconcurrent full-space cover.
        B = [[F(0) for _ in a] for _ in a]
        for i in range(m):
            for j in range(m):
                if i != j:
                    B[i][j] = F(rng.randrange(-5,6),7)
        for j in range(m):
            B[j][j] = -sum(B[i][j] for i in range(m) if i != j)
        W = [[Dual(i == j,B[i][j]) for j in range(m)] for i in range(m)]
        vd, fd = cap_formula(W,a)
        tr, f = derivatives(B,a)
        assert vd.x == 1 and vd.dx == tr
        assert [x.dx for x in fd] == f
        assert [x.x for x in fd] == [(1-x)**d for x in a]
        target = [F(rng.randrange(-10,11),11) for _ in a]
        S = inverse(target,a)
        assert all(sum(S[i][j] for i in range(m)) == 0 for j in range(m))
        assert derivatives(S,a)[1] == target
        if d >= 2 and len(set(a)) > 1:
            improvement(a)
        if d == 1:
            assert tr == sum(f)  # Unique multipliers both one.
        checks += 1
    # Equal thresholds need not be concurrent to be stationary.
    for a0 in [F(1,m),F(1,m+1),F(2,m+2)]:
        a = [a0]*m
        ell = 1/(d*(1-a0)**(d-1))
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                B = [[F(0) for _ in a] for _ in a]
                B[i][j], B[j][j] = F(1), F(-1)
                tr,f = derivatives(B,a)
                assert tr == ell*sum(f)
                checks += 1


# Concurrent nonuniform rational witness, with specified edge velocity.
a = [F(1,2), F(1,3), F(1,6)]
E = [[F(0),F(1),F(0)], [F(0),F(-1),F(0)], [F(0)]*3]
f = derivatives(E,a)[1]
S = inverse(f,a)
B0 = [[E[i][j]-S[i][j] for j in range(3)] for i in range(3)]
assert derivatives(B0,a) == (F(1,12),[F(0)]*3)
eps = F(5,282)
C = inverse([-eps]*3,a)
B = [[B0[i][j]+C[i][j] for j in range(3)] for i in range(3)]
assert derivatives(B,a) == (F(1,24),[-eps]*3)
t = F(1,100)
W = [[F(i == j)+t*B[i][j] for j in range(3)] for i in range(3)]
assert all(sum(W[i][j] for i in range(3)) == 1 for j in range(3))
assert all(W[i][i] > a[i] and all(W[i][j] < a[i]
           for j in range(3) if i != j) for i in range(3))
volume, caps = cap_formula(W,a)
assert volume > 1
assert all(c < (1-x)**2 for c,x in zip(caps,a))
print('PASS:', checks, 'exact derivative/right-inverse/stationarity checks;')
print('all nonuniform gain directions, d=1 exception, and actual rational concurrent simplex witness')
