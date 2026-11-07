"""Falsification screen only: numerical finite three-cap covers, never a proof."""
import itertools
import math
import numpy as np
from scipy.optimize import minimize
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


T = np.array([[2., -1.], [-1., 2.], [-1., -1.]])
base_normals = np.array([[1., 0.], [0., 1.], [-1., -1.]])
v = area(T)
records = []
matrices = []
for a in (0.5, 0.75, 1., 1.5, 2.):
    for b, c in itertools.product((-1., -0.5, 0., 0.5, 1.), repeat=2):
        matrices.append(np.array([[a, b], [c, (1+b*c)/a]]))

for count, L in enumerate(matrices):
    B = T@L.T
    points = np.array([(x+y)/2 for x in T for y in B])
    K = points[ConvexHull(points).vertices]
    m = area(K)
    if not 1.00001 < m/v <= 3:
        continue
    normals = np.vstack((base_normals, base_normals@np.linalg.inv(L)))
    best = None
    for inds in itertools.combinations(range(6), 3):
        U = normals[list(inds)]
        mat = np.vstack((U.T, np.ones(3)))
        try:
            lam = np.linalg.solve(mat, [0., 0., 1.])
        except np.linalg.LinAlgError:
            continue
        if min(lam) < 1e-7:
            continue
        def masses(w):
            y, al = w[:2], w[2:5]
            return np.array([cap(T, u, float(u@y)+s)
                             +cap(K, u, float(u@y))
                             +cap(B, u, float(u@y)-s)
                             for u, s in zip(U, al)])
        initial = np.zeros(6)
        initial[5] = max(masses(initial))
        ans = minimize(lambda w: w[5], initial, method="SLSQP",
                       constraints=[{"type": "ineq", "fun": lambda w: w[5]-masses(w)}],
                       options={"maxiter": 100, "ftol": 1e-9})
        if not ans.success:
            continue
        cost = max(masses(ans.x))
        if best is None or cost < best[0]:
            best = (cost, inds, ans.x)
    if best:
        ratio = best[0]/((m+v)/3)
        records.append((ratio, L.tolist(), m/v, best[0]/v,
                        best[1], best[2].tolist()))
        if len(records) == 1 or ratio < min(x[0] for x in records[:-1]):
            print("BEST", records[-1], flush=True)

print("FINAL", sorted(records, key=lambda x:x[0])[:8], flush=True)
