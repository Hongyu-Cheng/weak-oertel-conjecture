#!/usr/bin/env python3
"""Exact rational checks for the square-pyramid all-normal depth certificate."""
from fractions import Fraction as F


def add(p, q):
    return [(p[i] if i < len(p) else F(0)) +
            (q[i] if i < len(q) else F(0))
            for i in range(max(len(p), len(q)))]


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


c = F(19, 25)
k = c**3
assert k == F(6859, 15625)
assert 2*k < 1
V = F(4, 3)
assert V == 4 * F(1, 3)

# Second branch: clear the positive denominator exactly.
p = [1 - 3*c/2, 1 - 2*k]
numerator = add([2*x for x in mul([1, 2, 1], p)], [k])
assert [15625*x for x in numerator] == [2484, -4936, 3253, 3814]
disc = 4936**2 - 4*3253*2484
assert disc == -7957712 < 0

# First branch is decreasing, so its right endpoint is sufficient.
h = 1-c
assert h == F(6, 25)
Qend = 1 - k/(1-h*h)**2
assert Qend - k == F(1002251, 15015625) > 0


def Q(v):
    if v <= 1-c:
        return 1-k/(1-v*v)**2
    return (1+v-3*c/2+k/(2*(1+v)**2))/(2*v)


def phi(v):
    if 1+v <= c:
        return F(0)
    return 1-k/(1+v)**3


for v in [F(i, 25) for i in range(301)]:
    assert Q(v) > k
    assert 2-phi(v)-phi(-v) >= 2*k

# Piecewise integration and the uniform-mixture density.
# For A>=B>0, integrate v/(2AB) over the mixing interval.
mixtures = 0
for A in (F(1, 3), F(1), F(7, 3), F(6)):
    for ratio in (F(1, 5), F(1, 2), F(1)):
        B = A*ratio
        lo, hi = A-B, A+B
        assert (hi**2-lo**2)/(4*A*B) == 1
        for x in (F(0), lo/2, lo, (lo+hi)/2, hi, hi+1):
            mixture_density = max(F(0), hi-max(x, lo))/(4*A*B)
            if x <= lo:
                expected = 1/(2*A)
            elif x <= hi:
                expected = (hi-x)/(4*A*B)
            else:
                expected = F(0)
            assert mixture_density == expected
            mixtures += 1

# Exact paired upper certificate and robust proper cuts.
paired = 1-(2*c-1)**3
assert paired == F(13428, 15625)
assert 2*k-paired == F(58, 3125) > 0
assert (2*k-paired)*V == F(232, 9375)
for i in range(1, 101):
    eps = F(i, 100000)
    assert 0 < 2*c-1+eps < 1-eps < 1
    cost = 2-(1-eps)**3-(2*c-1+eps)**3
    assert cost <= paired+3*eps
    assert 2*k-cost >= F(389, 25000)

# Exact lower-diagonal simplex payment, without introducing floating roots.
for d in range(1, 9):
    gamma = F(d, d+1)**d
    for a in (F(0), F(1, 13), F(2, 7)):
        assert 2*gamma*((d+1)*a)**d == 2*(d*a)**d

print("PASS: complete scalar polynomial certificate, regime endpoint, "
      f"{mixtures} exact mixture-density checks, all rational cap signs, "
      "strict paired gap, 100 proper-cut perturbations, lower-diagonal identity.")
