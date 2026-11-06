"""Numerical falsification only, using exact finite quadratic cells for alpha."""
import numpy as np
from scipy.spatial import ConvexHull

def area(poly):
    if len(poly) < 3:
        return 0.
    poly = np.asarray(poly)
    return abs(np.sum(poly[:, 0]*np.roll(poly[:, 1], -1)
                      -poly[:, 1]*np.roll(poly[:, 0], -1)))/2


def cap(poly, u, h):
    out = []
    for i, x in enumerate(poly):
        y = poly[(i+1) % len(poly)]
        sx, sy = float(u@x-h), float(u@y-h)
        if sx >= 0:
            out.append(x)
        if (sx < 0 < sy) or (sy < 0 < sx):
            out.append(x+(y-x)*(sx/(sx-sy)))
    return area(out)


def body(w, theta):
    a, b, c = -(1+theta)*w/3, (2*theta-1)*w/3, (2-theta)*w/3
    pts = np.array([[a, 0.], [b, -1/w], [c, 0.], [b, 1/w]])
    return pts[ConvexHull(pts).vertices], (a, b, c)


best = None
u = np.array([1., 0.])
for R in np.geomspace(0.1, 10, 61):
    for ta in np.linspace(0, 1, 21):
        A, ba = body(1., ta)
        for tb in np.linspace(0, 1, 21):
            B, bb = body(R, tb)
            pts = np.array([(a+b)/2 for a in A for b in B])
            M = pts[ConvexHull(pts).vertices]
            q = cap(M, u, 0.)
            def P(alpha):
                return cap(A, u, alpha)+cap(B, u, -alpha)
            breaks = sorted(set(ba+tuple(-x for x in bb)))
            values = [(P(x), x) for x in breaks]
            values.extend([(1., breaks[0]-1), (1., breaks[-1]+1)])
            for x, y in zip(breaks, breaks[1:]):
                mid = (x+y)/2
                fx, fy, fm = P(x), P(y), P(mid)
                aa = 2*(fx+fy-2*fm)/(y-x)**2
                slope_mid = (fy-fx)/(y-x)
                if aa > 1e-10:
                    critical = mid-slope_mid/(2*aa)
                    if x <= critical <= y:
                        values.append((P(critical), critical))
            p, alpha = min(values)
            total = q+p
            if best is None or total < best[0]-1e-10:
                best = (total, R, ta, tb, q, p, alpha, area(M))
                print("BEST", best, flush=True)
print("FINAL", best, flush=True)
