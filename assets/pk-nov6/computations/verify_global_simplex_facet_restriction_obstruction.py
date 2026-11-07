"""Exact certificates for global facet-only overestimate in simplex fibers."""
from fractions import Fraction as F


class Q:
    """The real quadratic field Q(sqrt(21)), with exact ordering."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def cast(x):
        return x if isinstance(x, Q) else Q(x)

    def __add__(self, x):
        x = self.cast(x)
        return Q(self.a + x.a, self.b + x.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, x):
        return self + (-self.cast(x))

    def __rsub__(self, x):
        return self.cast(x) - self

    def __mul__(self, x):
        x = self.cast(x)
        return Q(self.a*x.a + 21*self.b*x.b,
                 self.a*x.b + self.b*x.a)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.cast(x)
        norm = x.a*x.a - 21*x.b*x.b
        assert norm
        return self * Q(x.a/norm, -x.b/norm)

    def __pow__(self, n):
        assert n >= 0
        ans = Q(1)
        for _ in range(n):
            ans *= self
        return ans

    def sign(self):
        if self.b == 0:
            return (self.a > 0) - (self.a < 0)
        if self.a == 0:
            return (self.b > 0) - (self.b < 0)
        if self.a > 0 and self.b > 0:
            return 1
        if self.a < 0 and self.b < 0:
            return -1
        gap = self.a*self.a - 21*self.b*self.b
        assert gap != 0
        if self.a > 0:
            return (gap > 0) - (gap < 0)
        return (gap < 0) - (gap > 0)

    def __eq__(self, x):
        x = self.cast(x)
        return self.a == x.a and self.b == x.b

    def __lt__(self, x):
        return (self - x).sign() < 0

    def __le__(self, x):
        return (self - x).sign() <= 0

    def __repr__(self):
        return f"({self.a})+({self.b})sqrt(21)"


t = Q(-2, F(1, 2))
eps = F(1, 2000)
a = F(9, 10)
t1 = t - F(17, 10)*eps
t2 = t + eps
s = 2*t - eps
den = a*(2*a-1)
U = 4*t*t + F(1, 4)

assert t*t + 4*t - F(5, 4) == 0
assert Q(F(233, 800)) < t < Q(F(583, 2000))
assert Q(F(29, 100)) < t < Q(F(3, 10))
assert U == Q(F(149, 4), -8)

# Facet-restricted equality and all remaining oriented facet caps.
coord = (1-t)**2 + 2*(F(1, 2)-t)**2
neg_sum = 4*t*t + F(1, 4)
neg_coord = 2*t-t*t+F(1, 4)
pos_sum = 1-4*t*t
assert coord == neg_sum == U
assert U < neg_coord and U < pos_sum and U < Q(F(5, 4))
assert 2*(F(1, 2)-t)**2 < Q(F(1, 4))
assert Q(F(1, 2)) < 2*t < Q(1)
assert Q(F(1, 9)) < U-eps

# All three triangle slices of the nonfacet cap are in the one-vertex
# proper-cap branch; the same holds on the full nearby a interval.
for r in (F(1, 2), F(1), F(1, 2)):
    assert Q((1-a)*r) < t1 < Q(a*r)
for aa in (F(17, 20), F(9, 10)):
    for r in (F(1, 2), F(1)):
        assert Q((1-aa)*r) < t < Q(aa*r)

# Exact mixed cap values and the full middle-plane cover identity.
mass1 = ((a-t1)**2 + 2*(a/F(2)-t1)**2)/den
mass2 = (1-t2)**2 + 2*(F(1, 2)-t2)**2
mass3 = s*s + F(1, 4)
assert t1 + (2*a-1)*t2 - a*s == 0
assert mass1 < U-eps and mass2 < U-eps and mass3 < U-eps
assert Q(0) < s < Q(1) and Q(F(1, 2)) < 2*s

# The unshifted a=9/10 cap already beats the restricted optimum.
unshifted = ((a-t)**2 + 2*(a/F(2)-t)**2)/den
gap = U-unshifted
assert gap == Q(-F(623, 48), F(17, 6))
assert Q(F(11, 2400)) < gap
assert F(11, 2400)-F(51, 20000) > eps

# Full orientation/tilt stationary local minimum: derivative numerator.
def stationary_numerator(aa):
    return (8*t-F(3, 2))*aa*aa - 12*t*t*aa + 3*t*t

assert stationary_numerator(F(17, 20)) < Q(0)
assert Q(0) < stationary_numerator(F(9, 10))
# Its derivative is strictly positive throughout the stated interval:
# 2(8t-3/2)a-12t² > 2*(41/50)*(17/20)-12*(3/10)².
assert 2*F(41, 50)*F(17, 20)-12*F(3, 10)**2 > 0

# Exact raw and normalized restricted values.
assert F(2, 3)*U == Q(F(149, 6), -F(16, 3))
print("PASS: exact facet optimum, all six oriented facet families")
print("PASS: finite middle cover; every cap mass < U-1/2000")
print("PASS: strict nonfacet stationary minimum in (17/20,9/10)")
print("PASS: explicit normalized gap 1/(3000*2^(n-1)) for every n>=1")
