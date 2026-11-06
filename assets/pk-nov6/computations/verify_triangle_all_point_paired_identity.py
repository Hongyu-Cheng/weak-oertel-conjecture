#!/usr/bin/env python3
"""Exact triangle paired-cap checks; the all-real proof is in the companion note."""
from fractions import Fraction as F


def tail(a, x):
    if x <= 0:
        return F(1)
    if x >= 1:
        return F(0)
    if a == 0:
        return (1-x)**2
    if a == 1:
        return 1-x*x
    if x <= a:
        return 1-x*x/a
    return (1-x)**2/(1-a)


def paired_min(a, m):
    knots = sorted({F(0), abs(m), abs(a-m), abs(1-m), F(1)})

    def cost(t):
        return tail(a, m-t)+tail(a, m+t)

    best = min(cost(t) for t in knots)
    for lo, hi in zip(knots, knots[1:]):
        if lo == hi:
            continue
        mid = (lo+hi)/2
        fl, fm, fr = cost(lo), cost(mid), cost(hi)
        qa = 2*(fl+fr-2*fm)/(hi-lo)**2
        qb = (fr-fl)/(hi-lo)-qa*(lo+hi)
        if qa > 0:
            x = -qb/(2*qa)
            if lo < x < hi:
                best = min(best, cost(x))
    return best


normals = sorted({F(i, n) for n in range(1, 10) for i in range(n+1)})
count = branches = 0
for n in range(3, 13):
    for i in range(1, n-1):
        for j in range(1, n-i):
            lam = [F(i, n), F(j, n), F(n-i-j, n)]
            A, B, C = sorted(lam, reverse=True)
            depth = 4*B*C
            assert B <= F(1, 2)
            assert C/(1-B) >= depth
            assert all(x*(1-x) >= 2*B*C for x in lam)
            for a in normals:
                m = a*lam[1]+lam[2]
                value = paired_min(a, m)
                assert value >= 2*depth, (lam, a, value, 2*depth)
                count += 1
                if a > F(1, 2) and F(1, 2) <= m <= a:
                    t = (a-m)/(2*a-1)
                    assert 0 <= m-t <= a <= m+t <= 1
                    J = 1-(2*m-1)**2/(2*a-1)
                    assert tail(a,m-t)+tail(a,m+t) == J
                    v = 2*a-1
                    b, c = lam[1], lam[2]-lam[0]
                    assert 1-J == b*b*v+2*b*c+c*c/v
                    v0 = max(F(0), -c/b, c/(1-b))
                    assert 0 <= v0 <= v <= 1
                    if c < 0:
                        left = F(1)
                    elif c == 0:
                        left = F(1)
                    else:
                        a0 = (1+v0)/2
                        m0 = a0*lam[1]+lam[2]
                        assert a0 == m0
                        left = 1-v0
                        assert left == 2*tail(a0,m0)
                    right = 4*lam[0]*(1-lam[0])
                    assert J >= min(left,right) >= 2*depth
                    branches += 1

assert paired_min(F(1), F(4,5)) == F(16,25)
assert 2*tail(F(1),F(4,5)) == F(18,25)
assert tail(F(1), F(1))+tail(F(1),F(3,5)) == F(16,25)
print(f"PASS: {count} exact full-shift minima at ordered rational "
      f"barycentric points; {branches} feasible straddling branches; "
      "ordinary-depth boundary inequalities; repeated knots; nonzero-shift equality.")
