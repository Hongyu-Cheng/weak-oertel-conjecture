"""Bounded falsification screen, never a proof of a universal assertion."""
from itertools import product, combinations
from fractions import Fraction
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull, QhullError

rng = np.random.default_rng(271828)

def polygon():
    seeds = np.unique(rng.integers(-2, 4, size=(rng.integers(4, 9), 2)), axis=0)
    try:
        hull = ConvexHull(seeds)
    except QhullError:
        return None
    points = [p for p in product(range(-2, 4), repeat=2)
              if max(hull.equations[:, :2] @ p + hull.equations[:, 2]) < 1e-8]
    return np.array(points) if 6 <= len(points) <= 17 else None

def constraints(P):
    N = len(P)
    roots = {}
    for i, p in enumerate(P):
        c = tuple(p % 2)
        if c not in roots or (p @ p, tuple(p)) < (P[roots[c]] @ P[roots[c]], tuple(P[roots[c]])):
            roots[c] = i
    ids = {tuple(p): i for i, p in enumerate(P)}
    eq, ub = [], []
    for i, p in enumerate(P):
        v = roots[tuple(p % 2)]
        w = ids[tuple((p + P[v]) // 2)]
        row = np.zeros(3*N); row[i] += 1; row[v] += 1; row[w] -= 2
        eq.append(row)
        row = np.zeros(3*N); row[i] += 1; row[v] -= 1
        ub.append(row)
    for i, p in enumerate(P):
        for j, q in enumerate(P):
            row = np.zeros(3*N); row[j] += 1; row[i] -= 1
            row[N+2*i:N+2*i+2] -= q-p
            ub.append(row)
    return roots, np.array(eq), np.array(ub)

def candidate_masks(G):
    masks, directions = [], []
    random_normals = rng.normal(size=(700, 3))
    for i in range(len(G)):
        diffs = G-G[i]
        normal_list = [v for v in random_normals]
        for j, k in combinations([j for j in range(len(G)) if j != i], 2):
            v, w = diffs[j], diffs[k]
            c = np.cross(v, w)
            norm = np.linalg.norm(c)
            if norm < 1e-10:
                continue
            c /= norm
            v = v/max(np.linalg.norm(v), 1e-30)
            w = w/max(np.linalg.norm(w), 1e-30)
            for sv, sw in product((-1, 1), repeat=2):
                normal_list.append(c+1e-6*(sv*v+sw*w))
                normal_list.append(-c+1e-6*(sv*v+sw*w))
        directions.append(np.array(normal_list))
        # Boundary-included masks only provide UPPER certificates. Numerical
        # discoveries must be replaced by exact rational incidence checks.
        assert np.isfinite(diffs).all() and np.isfinite(directions[-1]).all()
        values = np.einsum('ij,kj->ki', diffs, directions[-1], optimize=False)
        assert np.isfinite(values).all()
        masks.append(values >= -1e-11)
    return masks, directions

seen = set(); tested = 0; nonlinear = 0; best = 1.0
for attempt in range(180):
    P = polygon()
    if P is None or tuple(map(tuple, P)) in seen:
        continue
    seen.add(tuple(map(tuple, P)))
    N = len(P)
    roots, eq, ub = constraints(P)
    for step in range(7):
        objective = np.r_[rng.normal(size=N), np.zeros(2*N)]
        result = linprog(objective, A_ub=ub, b_ub=np.zeros(len(ub)),
                         A_eq=eq, b_eq=np.zeros(len(eq)),
                         bounds=[(1, 2)]*N + [(None, None)]*(2*N), method='highs')
        assert result.success
        radii = np.array([float(Fraction(float(v)).limit_denominator(100000))
                         for v in result.x[:N]])
        G = np.column_stack((P, radii))
        tested += 1
        if np.linalg.matrix_rank(G[1:]-G[0], tol=1e-7) < 3:
            continue
        nonlinear += 1
        masks, normals = candidate_masks(G)
        for exponent in (1, 2, 3, 5, 8, 16):
            weights = radii**exponent
            costs = [np.sum(mask*weights[None, :], axis=1) for mask in masks]
            upper = np.array([min(cost) for cost in costs])/sum(weights)
            best = min(best, max(upper))
            if max(upper) < 0.25-1e-7:
                data = dict(P=P.tolist(), radii=[str(Fraction(float(v)).limit_denominator(100000)) for v in radii],
                            exponent=exponent, upper=upper.tolist(),
                            normals=[normals[i][np.argmin(costs[i])].tolist() for i in range(N)])
                Path('./actual_zero_forest_weighted_graph_candidate.json').write_text(json.dumps(data, indent=2))
                print('CANDIDATE requiring exact certification', data, flush=True)
                raise SystemExit
    if nonlinear and nonlinear % 10 == 0:
        print('screen', len(seen), tested, nonlinear, best, flush=True)
print('NO COUNTERCERTIFICATE in bounded screen:', len(seen), tested, nonlinear, best, flush=True)
