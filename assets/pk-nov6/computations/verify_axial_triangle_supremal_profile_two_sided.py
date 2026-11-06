"""Exact consistency checks for the proved axial formulas."""
from fractions import Fraction as F

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
    if len(poly) < 3:
        return F(0)
    return abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                   -poly[i][1]*poly[(i+1) % len(poly)][0]
                   for i in range(len(poly))))/2


def cap(poly, threshold):
    out = []
    for i, x in enumerate(poly):
        y = poly[(i+1) % len(poly)]
        sx, sy = x[0]-threshold, y[0]-threshold
        if sx >= 0:
            out.append(x)
        if sx*sy < 0:
            ratio = sx/(sx-sy)
            out.append(tuple(x[j]+ratio*(y[j]-x[j]) for j in (0, 1)))
    return area(out)


def triangle(w):
    return [(-w/3, -1/w), (2*w/3, F(0)), (-w/3, 1/w)]


for den in range(1, 17):
    for num in range(den, 7*den+1):
        R = F(num, den)
        A, B = triangle(F(1)), triangle(R)
        M = hull([tuple((a[j]+b[j])/2 for j in (0, 1)) for a in A for b in B])
        qminus = (R+1)**2*(6*R-1)/(36*R**2)
        qplus = (R+1)/2-qminus
        assert area(M) == (R+1)/2
        assert cap(M, F(0)) == qplus
        checks += 2
        star = 2*R*(R-1)/(3*(R**2+1))
        pplus = 4*(R+1)**2/(9*(R**2+1))
        assert cap(A, star)+cap(B, -star) == pplus
        assert qplus+pplus-F(4, 3) == (R-1)*(12*R**4-13*R**3+27*R**2+3*R-1)/(36*R**2*(R**2+1))
        assert qplus+pplus >= F(4, 3)
        checks += 3
        pminus = 1-(2*R-1)**2/(9*R**2)
        assert 2-cap(A, -F(1, 3))-cap(B, F(1, 3)) == pminus
        assert qminus+pminus-F(4, 3) == (3*R-1)*(2*R**2-5*R+5)/(36*R**2)
        assert qminus+pminus > F(4, 3)
        checks += 3
        for t in (-2*R, -R/3, -F(1, 3), F(0), F(2, 3), 2*R/3, 2*R):
            assert cap(A, t)+cap(B, -t) >= pplus
            assert 2-cap(A, t)-cap(B, -t) >= pminus
            checks += 2

print(f"PASS: {checks:,} exact checks")
