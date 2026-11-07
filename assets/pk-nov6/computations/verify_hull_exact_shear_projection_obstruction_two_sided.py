"""Exact supplementary checks; the accompanying note contains the proof."""
from fractions import Fraction as F
from math import gcd

checks = 0


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(points):
    pts = sorted(set(points))
    lo, hi = [], []
    for x in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], x) <= 0:
            lo.pop()
        lo.append(x)
    for x in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], x) <= 0:
            hi.pop()
        hi.append(x)
    return lo[:-1]+hi[:-1]


def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                   -poly[i][1]*poly[(i+1) % len(poly)][0]
                   for i in range(len(poly))))/2


def section(poly, w):
    hits = []
    for i, x in enumerate(poly):
        y = poly[(i+1) % len(poly)]
        if x[0] == y[0]:
            if x[0] == w:
                hits.extend((x[1], y[1]))
        elif min(x[0], y[0]) <= w <= max(x[0], y[0]):
            hits.append(x[1]+(w-x[0])*(y[1]-x[1])/(y[0]-x[0]))
    return max(hits)-min(hits) if hits else F(0)


for L in (F(1, 3), F(2), F(17, 2)):
    for eps in (F(1, 100), F(2, 7)):
        for a in (F(-3), F(-1, 2), F(0), L/2, L, F(13, 3)):
            for b in (F(-2), F(0), L, F(7, 2)):
                heights = [L*z1*z2-a*z1-b*z2
                           for z1 in (0, 2) for z2 in (0, 1)]
                assert max(heights)-min(heights)+eps >= L+eps
                checks += 1
                if a == L/2 and b == L:
                    assert max(heights)-min(heights)+eps == L+eps
                    checks += 1
                for p in range(-4, 5):
                    for q in range(-4, 5):
                        if gcd(p, q) != 1:
                            continue
                        points = [(F(q*z1-p*z2),
                                   L*z1*z2-a*z1-b*z2+delta)
                                  for z1 in (0, 2) for z2 in (0, 1)
                                  for delta in (F(0), eps)]
                        poly = hull(points)
                        A = area(poly)
                        assert A >= L*max(abs(p), 2*abs(q))
                        checks += 1
                        low, high = int(min(x[0] for x in poly)), int(max(x[0] for x in poly))
                        sampled = sum(section(poly, F(w)) for w in range(low, high+1))
                        assert sampled-A == (section(poly, F(low))+section(poly, F(high)))/2
                        checks += 1
                        assert sampled >= L
                        checks += 1

print(f"PASS: {checks:,} exact checks")
