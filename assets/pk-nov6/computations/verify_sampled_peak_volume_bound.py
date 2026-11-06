"""Exact polynomial checks of sampled-peak and variation bounds."""

from fractions import Fraction as F
from math import factorial


def phi(s, a, b):
    return sum((a**k * b ** (s-k) for k in range(s+1)), F(0)) / (s+1)


for s in range(1, 25):
    for a in [F(0), F(1, 7), F(1), F(9, 2)]:
        for b in [F(0), F(1, 5), F(1), F(3)]:
            exact = phi(s, a, b)
            lower = min(a**s, b**s) + abs(a**s-b**s)/(s+1)
            assert exact >= lower
            if a == b or min(a,b) == 0 or s == 1:
                assert exact == lower
            else:
                assert exact > lower

    # Rational concave sampled roots: constant, affine, and asymmetric tents.
    for roots in [
        [F(1)], [F(1)]*7, [F(j, 6) for j in range(7)],
        [F(6-j, 6) for j in range(7)],
        [F(1), F(3), F(5), F(6), F(6), F(4), F(1)],
        [F(0), F(3), F(5), F(6), F(6), F(4), F(0)],
    ]:
        assert all(roots[j+1]-roots[j] >= roots[j+2]-roots[j+1]
                   for j in range(len(roots)-2))
        w = [a**s for a in roots]
        total, peak = sum(w), max(w)
        tv = sum(abs(b-a) for a,b in zip(w,w[1:]))
        minima = sum(min(a,b) for a,b in zip(w,w[1:]))
        assert minima == total-peak
        assert tv == 2*peak-w[0]-w[-1]
        interpolated = sum(phi(s,a,b) for a,b in zip(roots,roots[1:]))
        assert interpolated >= total-peak+tv/(s+1)
        assert total-peak+tv/(s+1) == (
            total - F(s-1,s+1)*peak - (w[0]+w[-1])/(s+1)
        )
        if len(set(roots)) == 1:
            assert interpolated == total-peak
        elif len(roots)>1:
            assert interpolated > total-peak

    # Sharp cone and the two-fine-level product budget.
    assert phi(s,F(1),F(0)) == F(1,s+1)
    for k in range(6):
        J = 2**k
        T = 2*J
        coarse_M_over_h = J
        assert F(1,J) * (1-F(coarse_M_over_h,T)) == F(1,2**(k+1))

print("PASS: sampled-peak identity, sharp variation coefficient, and exact depth budget.")
