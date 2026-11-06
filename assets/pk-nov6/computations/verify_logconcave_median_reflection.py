"""Exact diagnostics for the finite log-concave median-reflection theorem."""
from fractions import Fraction as F
from itertools import product
from random import Random


def check(w):
    w = tuple(map(F, w))
    n = len(w)
    assert w and all(x > 0 for x in w)
    assert all(w[i] ** 2 >= w[i-1]*w[i+1] for i in range(1, n-1))
    M = sum(w)

    def f(i):
        return w[i] if 0 <= i < n else F(0)

    medians = []
    for j in range(-1, n+1):
        L = sum(f(i) for i in range(n) if i < j)
        R = sum(f(i) for i in range(n) if i > j)
        O = F(0)
        total_T = F(0)
        defect = F(0)
        for h in range(1, n+2):
            a, b = f(j-h), f(j+h)
            T = a*sum(f(j+k) for k in range(h, n+2))
            T += b*sum(f(j-i) for i in range(h+1, n+2))
            assert T <= M*a and T <= M*b
            # The two four-point inequalities, including zero extensions.
            for i in range(h+1, n+2):
                assert b*f(j-i) <= a*f(j+2*h-i)
            for k in range(h, n+2):
                assert a*f(j+k) <= b*f(j+k-2*h)
            O += min(a, b)
            total_T += T
            defect += M*min(a, b)-T
        assert total_T == L*R
        assert M*O >= L*R
        assert defect == M*O-L*R
        B = sum(min(f(i), f(2*j-i)) for i in range(n))
        assert B == f(j)+2*O
        assert B-M/2 == 2*(M/2-L)*(M/2-R)/M+2*defect/M
        if L <= M/2 and R <= M/2:
            assert 0 <= j < n
            assert B >= M/2
            medians.append(j)
    assert medians
    return medians


profiles = {(F(1),), (F(1), F(1)), (F(3), F(2), F(1))}
for n in range(2, 6):
    for w in product(range(1, 5), repeat=n):
        if all(w[i]**2 >= w[i-1]*w[i+1] for i in range(1, n-1)):
            profiles.add(tuple(map(F, w)))

rng = Random(613521)
for _ in range(180):
    n = rng.randrange(3, 14)
    ratios = sorted((F(rng.randrange(1, 10), rng.randrange(1, 10))
                     for _ in range(n-1)), reverse=True)
    w = [F(1)]
    for r in ratios:
        w.append(w[-1]*r)
    profiles.add(tuple(w))

for w in profiles:
    check(w)

# Every median of each factor may be chosen independently.
factors = [(1, 2, 3, 2, 1), (1, 3, 4, 2), (3, 2, 1), (1, 1)]
for a, b in product(factors, repeat=2):
    ma, mb = check(a), check(b)
    w = {(i, k): F(x*y) for i, x in enumerate(a) for k, y in enumerate(b)}
    M = sum(w.values())
    for j, ell in product(ma, mb):
        B = sum(min(v, w.get((2*j-i, 2*ell-k), F(0)))
                for (i, k), v in w.items())
        assert 4*B >= M

assert max(sum(min(F(1), F(1) if 0 <= 2*j-i < 2 else F(0))
               for i in range(2)) for j in range(2)) == 1
print(f"PASS: {len(profiles)} exact log-concave profiles, all grouped inequalities, medians, defects, and products")
