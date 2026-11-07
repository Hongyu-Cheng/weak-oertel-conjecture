"""Falsification screen only; none of its output is a mathematical certificate."""
import importlib.util
import json
import math
import random
import sys

import numpy as np
from scipy.optimize import minimize

spec = importlib.util.spec_from_file_location(
    "profile_basic", "./screen-profile-prestationary-multipliers-rate-geometry.py"
)
basic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(basic)

rng = random.Random(8763145)
grid = np.linspace(-1.0, 1.0, 7)
sample_slopes = np.concatenate(([0.0], np.geomspace(0.002, 100.0, 58)))
m = int(sys.argv[1]) if len(sys.argv) > 1 else 2
starts = int(sys.argv[2]) if len(sys.argv) > 2 else 60
target = ((m + 1) / (m + 2)) ** (m + 1)


def initial_mixtures(h):
    rec = np.array([basic.data(h, s, m) for s in sample_slopes])
    p, c, moment = rec.T
    positive = np.flatnonzero(moment > 1e-8)
    negative = np.flatnonzero(moment < -1e-8)
    if not len(positive) or not len(negative):
        return None
    i, j = np.meshgrid(positive, negative, indexing="ij")
    i, j = i.ravel(), j.ravel()
    weights = -moment[j] / (moment[i] - moment[j])
    pp = np.concatenate(([p[0]], weights * p[i] + (1 - weights) * p[j]))
    cc = np.concatenate(([c[0]], weights * c[i] + (1 - weights) * c[j]))
    pairs = [(0, 0, 0.5)] + list(zip(i, j, weights))
    lower, upper = 0.0, 0.5
    for _ in range(35):
        g = (lower + upper) / 2
        if np.max((pp - 1 + g) / cc) <= np.min((pp - g) / cc):
            lower = g
        else:
            upper = g
    mu = pairs[int(np.argmin((pp - lower) / cc))]
    nu = pairs[int(np.argmax((pp - 1 + lower) / cc))]
    return mu, nu, lower


def decode(x):
    heights = x[:7]
    source = x[7]
    slopes = np.expm1(x[8:12])
    weights = x[12:14]
    h = list(zip(grid - source, heights))
    rec = np.array([basic.data(h, float(s), m) for s in slopes])
    first = weights[0] * rec[0] + (1 - weights[0]) * rec[1]
    second = weights[1] * rec[2] + (1 - weights[1]) * rec[3]
    return h, slopes, weights, rec, first, second


def objective(x):
    try:
        _, _, _, _, a, b = decode(x)
        return float((b[1] * a[0] + a[1] * (1 - b[0])) / (a[1] + b[1]))
    except (FloatingPointError, ZeroDivisionError, OverflowError):
        return 100.0


def moments(x):
    *_, a, b = decode(x)
    return np.array([a[2], b[2]])


def concavity(x):
    return 2 * x[1:6] - x[:5] - x[2:7]


best = 1.0
completed = 0
attempts = 0
while completed < starts and attempts < 100 * starts:
    attempts += 1
    raw = [(float(z), rng.uniform(0.001, 1)) for z in grid]
    hull = basic.hull(raw)
    heights = np.interp(grid, [z for z, _ in hull], [r for _, r in hull])
    heights /= max(heights)
    source = rng.uniform(-0.9, 0.9)
    h = list(zip(grid - source, heights))
    initial = initial_mixtures(h)
    if initial is None:
        continue
    mu, nu, floor = initial
    slopes = [sample_slopes[mu[0]], sample_slopes[mu[1]], sample_slopes[nu[0]], sample_slopes[nu[1]]]
    x = np.concatenate((heights, [source], np.log1p(slopes), [mu[2], nu[2]]))
    peak = int(np.argmax(heights))
    bounds = [(0.00001, 1.0)] * 7 + [(-0.985, 0.985)] + [(0.0, 7.0)] * 4 + [(0.0, 1.0)] * 2
    bounds[peak] = (1.0, 1.0)
    result = minimize(
        objective,
        x,
        method="SLSQP",
        bounds=bounds,
        constraints=[{"type": "eq", "fun": moments}, {"type": "ineq", "fun": concavity}],
        options={"maxiter": 450, "ftol": 2e-11, "disp": False},
    )
    completed += 1
    feasible = max(abs(moments(result.x))) < 2e-7 and min(concavity(result.x)) > -2e-7
    if feasible and result.fun < best:
        best = float(result.fun)
        h, slopes, weights, records, a, b = decode(result.x)
        report = {"m": m, "trial": completed, "value": best, "target": target,
                  "success": bool(result.success), "profile": h,
                  "slopes": slopes.tolist(), "weights": weights.tolist(),
                  "records": records.tolist(), "moments": moments(result.x).tolist()}
        print("DISCOVERY ONLY", json.dumps(report), flush=True)
        if best < target - 1e-6:
            with open("./balanced-two-mixture-profile-candidate-rate-geometry.json", "w") as stream:
                json.dump(report, stream, indent=2)
            break
    if completed % 10 == 0:
        print("completed", completed, "best", best, flush=True)
