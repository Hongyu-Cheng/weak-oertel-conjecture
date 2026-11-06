"""Falsification experiment for an auxiliary local-minimum dimension bound.

On P={-1,0,1}^2 use centered interval fibers [-r_p,r_p]. Radii are
concave on P, positive, and sum to one. Search for a family of exact
mixed depth <=1/8 while maximizing its smallest radius. Any positive
certified solution would refute a proposed 1/[2(dim(P)+1)] bound for
all-positive local minima: the mixed Helly theorem already gives 1/8.

This script's floating output is not an exact certificate. It records
the candidate for independent rational verification. It does not test OC.
"""

from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


P = list(product(range(-1, 2), repeat=2))
N = len(P)
ir = list(range(N))
ie = N
ia = np.arange(N + 1, N + 1 + 2 * N).reshape(N, 2)
im = np.arange(N + 1 + 2 * N, N + 1 + 2 * N + N * N).reshape(N, N)
iy = np.arange(im[-1, -1] + 1, im[-1, -1] + 1 + N * N).reshape(N, N)
NV = int(iy[-1, -1] + 1)
rows, lows, highs = [], [], []


def add(coeff, lo=-np.inf, hi=np.inf):
    rows.append(coeff)
    lows.append(lo)
    highs.append(hi)


def barycentric(p, inds):
    """Exact affine-independent representations with one to three points."""
    if len(inds) == 1:
        return (F(1),) if P[inds[0]] == p else None
    if len(inds) == 2:
        a, b = [P[i] for i in inds]
        k = 0 if a[0] != b[0] else 1
        t = F(p[k] - a[k], b[k] - a[k])
        if any(F(p[j]) != (1 - t) * a[j] + t * b[j] for j in range(2)):
            return None
        return (1 - t, t) if 0 <= t <= 1 else None
    a, b, c = [P[i] for i in inds]
    vx, vy = b[0] - a[0], b[1] - a[1]
    wx, wy = c[0] - a[0], c[1] - a[1]
    det = vx * wy - vy * wx
    if not det:
        return None
    px, py = p[0] - a[0], p[1] - a[1]
    t, s = F(px * wy - py * wx, det), F(vx * py - vy * px, det)
    vals = (1 - t - s, t, s)
    return vals if min(vals) >= 0 else None


add({i: 1 for i in ir}, 1, 1)
for i in ir:
    add({i: 1, ie: -1}, 0)

# Every extreme anchored representation has <=3 affine-independent sites.
seen = set()
for pidx, p in enumerate(P):
    for k in (2, 3):
        for inds in combinations([j for j in ir if j != pidx], k):
            weights = barycentric(p, inds)
            if weights is None:
                continue
            row = {pidx: F(1)}
            for j, w in zip(inds, weights):
                if w:
                    row[j] = row.get(j, F(0)) - w
            key = tuple(sorted(row.items()))
            if key not in seen:
                seen.add(key)
                add({j: float(v) for j, v in row.items()}, 0)

# Each restricted center may choose its own ambient cap x+a.(q-p)>=0.
# Actual intersection length is clamp(r_q+a.(q-p),0,2*r_q).
# A binary picks either upper majorant max(x,0) or 2*r_q; minimizing the
# budget makes their minimum exact. Any feasible chosen majorant is valid.
BIG = 20.0
for pidx, p in enumerate(P):
    add({int(im[pidx, q]): 1 for q in ir}, hi=0.25)
    for qidx, q in enumerate(P):
        m, y = int(im[pidx, qidx]), int(iy[pidx, qidx])
        row = {m: 1, qidx: -1, y: BIG}
        for k in range(2):
            row[int(ia[pidx, k])] = -(q[k] - p[k])
        add(row, 0)
        add({m: 1, qidx: -2, y: -BIG}, -BIG)

A = lil_matrix((len(rows), NV))
for ridx, row in enumerate(rows):
    for col, value in row.items():
        A[ridx, col] = value

lb, ub = np.zeros(NV), np.ones(NV)
lb[ia.ravel()] = -4
ub[ia.ravel()] = 4
ub[im.ravel()] = 2
ub[ie] = 1 / N
for pidx in ir:
    ub[iy[pidx, pidx]] = 0
integrality = np.zeros(NV)
integrality[iy.ravel()] = 1
c = np.zeros(NV)
c[ie] = -1

res = milp(c, integrality=integrality, bounds=Bounds(lb, ub),
           constraints=LinearConstraint(A.tocsr(), np.array(lows), np.array(highs)),
           options={"time_limit": 45, "mip_rel_gap": 1e-9})
out = {"status": int(res.status), "message": res.message,
       "mip_gap": getattr(res, "mip_gap", None),
       "dual_bound": getattr(res, "mip_dual_bound", None),
       "constraint_count": len(rows), "variable_count": NV}
if res.x is not None:
    out.update({"epsilon": float(res.x[ie]),
                "radii": [float(res.x[i]) for i in ir],
                "cap_slopes": res.x[ia].tolist(),
                "cap_majorants": res.x[im].tolist(),
                "binary_choices": res.x[iy].tolist()})
    actual = []
    for i, p in enumerate(P):
        a = res.x[ia[i]]
        actual.append(sum(np.clip(res.x[qidx] + a @ (np.array(q) - p),
                                  0, 2 * res.x[qidx])
                          for qidx, q in enumerate(P)))
    out["actual_cap_lengths"] = actual
Path("./symmetric_interval_grid_sharpness_milp_root.json").write_text(
    json.dumps(out, indent=2) + "\n")
print(json.dumps({k: v for k, v in out.items()
                  if k not in {"cap_majorants", "binary_choices"}}, indent=2))
