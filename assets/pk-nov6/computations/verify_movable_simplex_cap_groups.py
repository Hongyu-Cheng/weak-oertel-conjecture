"""Exact checks for moving group points and a physical two-fiber improvement."""
from fractions import Fraction as F
from itertools import permutations
from random import Random


class Jet:
    def __init__(self, x=0, dx=0, q=0):
        self.c = (F(x), F(dx), F(q))
    @staticmethod
    def cast(x):
        return x if isinstance(x, Jet) else Jet(x)
    def __add__(self, x):
        x = self.cast(x)
        return Jet(*(a+b for a, b in zip(self.c, x.c)))
    __radd__ = __add__
    def __neg__(self):
        return Jet(*(-a for a in self.c))
    def __sub__(self, x):
        return self+-self.cast(x)
    def __rsub__(self, x):
        return self.cast(x)-self
    def __mul__(self, x):
        x = self.cast(x)
        return Jet(*(sum(self.c[j]*x.c[i-j] for j in range(i+1))
                     for i in range(3)))
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = self.cast(x)
        a, b, c = x.c
        return self*Jet(1/a, -b/a**2, b*b/a**3-c/a**2)
    def __pow__(self, n):
        out = Jet(1)
        for _ in range(n):
            out *= self
        return out


def det3(w):
    return sum(
        (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
        * w[0][p[0]]*w[1][p[1]]*w[2][p[2]]
        for p in permutations(range(3))
    )


def cap(w, a, i):
    value = det3(w)*(w[i][i]-a)**2
    for j in range(3):
        if j != i:
            value /= w[i][i]-w[i][j]
    return value


def trace2(b):
    return sum(b[i][j]*b[j][i] for i in range(len(b)) for j in range(len(b)))


rng = Random(661247)
single_checks = 0
for d in range(2, 9):
    m = d+1
    ah = 1-F(d, 3*m)
    al = F(1, 3*m)
    kappa = F(1, d*m)
    thresholds = [[ah if g == i else al for i in range(m)] for g in range(m)]
    weights = [[kappa/(1-a)**(d-1) for a in row] for row in thresholds]
    assert all(sum(row) == 1 for row in thresholds)
    assert all(sum(weights[g][i]*(1-thresholds[g][i])**d for g in range(m))
               == F(1, m) for i in range(m))
    assert all(weights[g][i]*(1-thresholds[g][i])**(d-1) == kappa
               for g in range(m) for i in range(m))
    for _ in range(8):
        e = [[F(0) for _ in range(m)] for _ in range(m)]
        # Directed triangle circulations and bipartite four-cycles preserve
        # zero diagonal, row sums and column sums.
        for __ in range(5):
            i, j, k = rng.sample(range(m), 3)
            scale = F(rng.randrange(-3, 4))
            for u, v in ((i, j), (j, k), (k, i)):
                e[u][v] += scale
                e[v][u] -= scale
        if m >= 4:
            for __ in range(5):
                i, l, j, k = rng.sample(range(m), 4)
                scale = F(rng.randrange(-3, 4))
                for u, v, sign in ((i, j, 1), (i, k, -1), (l, j, -1), (l, k, 1)):
                    e[u][v] += sign*scale
        assert all(sum(row) == 0 for row in e)
        assert all(sum(e[i][j] for i in range(m)) == 0 for j in range(m))
        bdiag = [F(rng.randrange(-3, 4)) for i in range(d)]
        bdiag.append(-sum(bdiag))
        b = [[bdiag[i]+e[i][j] for j in range(m)] for i in range(m)]
        assert all(sum(b[i][j] for i in range(m)) == 0 for j in range(m))
        q = -trace2(b)
        for g in range(m):
            for i in range(m):
                a = thresholds[g][i]
                x = 1/(1-a)
                v = sum(b[i][j] for j in range(m) if j != i)-d*b[i][i]
                assert v == 0
                h = bdiag[i]
                first = v+d*x*(b[i][i]-h)
                assert first == 0
                second = -trace2(b)-d*x*x*(b[i][i]-h)**2+sum(
                    (b[i][i]-b[i][j])**2 for j in range(m) if j != i)
                q -= weights[g][i]*(1-a)**d*(first*first+second)
        assert q == -sum(x*x for row in e for x in row)/m
        single_checks += 1

# Two exposed triangles. All values below are normalized by their initial V.
b = [[F(-1), F(-2, 5), F(1, 5)],
     [F(2, 5), F(1), F(-1, 5)],
     [F(3, 5), F(-3, 5), F(0)]]
body_vel = [b, [[-x for x in row] for row in b]]
c = [F(1), F(-1), F(0)]
coeff = [[F(-1, 10), F(83, 200)], [F(-83, 200), F(1, 10)]]
a = [[F(1, 10), F(4, 5)], [F(4, 5), F(1, 10)]]
h = [[[coeff[g][z]*c[i] for i in range(3)] for z in range(2)] for g in range(2)]
ell = F(5, 11)
for g, expected in [(0, (F(1), F(2, 11))), (1, (F(1), F(9, 11)))]:
    assert tuple(ell*sum(2*(1-a[g][z])*(1 if j == 0 else z)
                         for z in range(2)) for j in range(2)) == expected
    assert all(sum(h[g][z]) == 0 for z in range(2))

w = [[[Jet(i == j, body_vel[z][i][j]) for j in range(3)]
      for i in range(3)] for z in range(2)]
mass = sum(det3(wz) for wz in w)
caps = [[sum(cap(w[z], Jet(a[g][z], h[g][z][i]), i) for z in range(2))
         for i in range(3)] for g in range(2)]
assert mass.c[0] == 2 and mass.c[1] == 0
assert all(p.c[0] == F(17, 20) and p.c[1] == 0 for row in caps for p in row)
q0 = 2*mass.c[2]
qc = [[2*p.c[2] for p in row] for row in caps]
assert q0-ell*sum(x for row in qc for x in row) == F(3159, 11000)

# Explicit right inverse applied to make each cap second derivative -1/100.
f = [[-F(1, 100)-q for q in row] for row in qc]
sg = [sum(row) for row in f]
traces = [F(5, 77)*(9*sg[0]-2*sg[1]), F(5, 77)*(-2*sg[0]+9*sg[1])]
acc = [[[traces[z]/2*((1 if i == j else 0)-F(1, 3))
         for j in range(3)] for i in range(3)] for z in range(2)]
k = [[[F(0) for i in range(3)] for z in range(2)] for g in range(2)]
for g in range(2):
    for i in range(3):
        k[g][0][i] = -(f[g][i]-sg[g]/3)/(2*(1-a[g][0]))
    assert sum(k[g][0]) == 0
for z in range(2):
    assert all(sum(acc[z][i][j] for i in range(3)) == 0 for j in range(3))

wjet = [[[Jet(i == j, body_vel[z][i][j], acc[z][i][j]/2)
          for j in range(3)] for i in range(3)] for z in range(2)]
massjet = sum(det3(wz) for wz in wjet)
capjet = [[sum(cap(wjet[z], Jet(a[g][z], h[g][z][i], k[g][z][i]/2), i)
               for z in range(2)) for i in range(3)] for g in range(2)]
assert massjet.c[1] == 0 and 2*massjet.c[2] == F(2859, 11000)
assert all(p.c[1] == 0 and 2*p.c[2] == -F(1, 100)
           for row in capjet for p in row)

time = F(1, 1000)
ww = [[[(1 if i == j else 0)+time*body_vel[z][i][j]+time*time*acc[z][i][j]/2
        for j in range(3)] for i in range(3)] for z in range(2)]
aa = [[[a[g][z]+time*h[g][z][i]+time*time*k[g][z][i]/2
        for i in range(3)] for z in range(2)] for g in range(2)]
assert all(det3(wz) > 0 for wz in ww)
for g in range(2):
    for z in range(2):
        assert sum(aa[g][z]) == 3*a[g][z]
        for i in range(3):
            assert ww[z][i][i] > aa[g][z][i]
            assert all(ww[z][i][j] < aa[g][z][i] for j in range(3) if j != i)
actual_mass = sum(det3(wz) for wz in ww)
actual_caps = [[sum(cap(ww[z], aa[g][z][i], i) for z in range(2))
                for i in range(3)] for g in range(2)]
assert actual_mass > 2
assert all(v < F(17, 20) for row in actual_caps for v in row)
print("PASS:", single_checks, "exact all-d joint critical Hessians; affine moments;")
print("six critical derivatives, positive Hessian, explicit acceleration, and rational-time actual body/cap improvement.")
print("Normalized mass gain at t=1/1000:", actual_mass-2)
print("Minimum normalized cap slack:", min(F(17, 20)-v for row in actual_caps for v in row))
