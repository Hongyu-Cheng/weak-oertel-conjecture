"""Bounded falsification screen only; not a proof of a selector theorem."""
import argparse
import json
import numpy as np
from scipy.optimize import minimize_scalar


def fixed_normal(r, j, a):
    n = len(r)
    delta = np.arange(n) - j
    q, b = r[j] / 3, 1 - a
    off = delta != 0
    B = np.max((q + r[off]) / abs(delta[off])) if n > 1 else 0
    knots = np.unique(np.concatenate(
        [np.array([-B, B])] +
        [(q - c * r[off]) / delta[off] for c in [0, b, a]]))
    knots = knots[(knots >= -B) & (knots <= B)]
    mids = (knots[:-1] + knots[1:]) / 2
    if not len(mids):
        mids = np.array([0.0])
    thresholds = q - mids[:, None] * delta
    low = (thresholds > 0) & (thresholds < b * r)
    high = (thresholds >= b * r) & (thresholds < a * r)
    A = np.zeros_like(thresholds)
    BB = np.zeros_like(thresholds)
    if b > 1e-12:
        A += np.where(low, -delta ** 2 / (a * b), 0)
        BB += np.where(low, 2 * q * delta / (a * b), 0)
    if a - b > 1e-12:
        denom = a * (a - b)
        A += np.where(high, delta ** 2 / denom, 0)
        BB += np.where(high, 2 * delta * (a * r - q) / denom, 0)
    A, BB = A.sum(axis=1), BB.sum(axis=1)
    stationary = np.divide(-BB, 2 * A, out=np.zeros_like(A), where=A > 1e-14)
    good = (A > 1e-14) & (stationary > knots[:-1]) & (stationary < knots[1:])
    betas = np.r_[knots, stationary[good]]
    t = q - betas[:, None] * delta
    values = np.where(t <= 0, r ** 2, 0.0)
    if b > 1e-12:
        values += np.where((t > 0) & (t < b * r), r ** 2 - t ** 2 / (a*b), 0)
    if a-b > 1e-12:
        values += np.where((t > 0) & (t >= b*r) & (t < a*r),
                           (a*r-t)**2/(a*(a-b)), 0)
    elif b > 0:
        values += np.where((t >= b*r) & (t < a*r), r**2-t**2/(a*b), 0)
    totals = values.sum(axis=1)
    i = int(np.argmin(totals))
    return float(totals[i]), float(betas[i])


def screen_profile(r):
    target = 2 * np.dot(r, r) / 9
    if 4 * max(r) ** 2 / 9 >= target:
        return None
    caps = []
    grid = np.linspace(0.5, 1, 9)
    for j in range(len(r)):
        sampled = [fixed_normal(r, j, a)[0] for a in grid]
        i = int(np.argmin(sampled))
        a = grid[i]
        left, right = grid[max(i-1, 0)], grid[min(i+1, len(grid)-1)]
        if right > left:
            result = minimize_scalar(lambda x: fixed_normal(r, j, x)[0],
                                     bounds=(left, right), method="bounded",
                                     options={"xatol": 1e-9})
            if result.fun < sampled[i]:
                a = result.x
        value, beta = fixed_normal(r, j, a)
        caps.append((value, float(a), beta))
    return max(c[0] for c in caps) / target, caps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=200)
    ap.add_argument("--seed", type=int, default=802)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)
    best = None
    evaluated = 0
    for it in range(args.count):
        n = int(rng.integers(3, 12))
        peak = int(rng.integers(1, n-1))
        ends = 10 ** rng.uniform(-4, 0, 2)
        r = np.r_[np.linspace(ends[0], 1, peak+1),
                  np.linspace(1, ends[1], n-peak)[1:]]
        if it % 2:
            # Add an independent nonnegative concave tent, then normalize.
            i = int(rng.integers(1, n-1))
            x = np.arange(n)
            tent = np.minimum(x, i) - x*i/(n-1)
            r += 10 ** rng.uniform(-2, 1) * tent
            r /= max(r)
        assert np.max(np.diff(r, 2)) < 1e-10
        result = screen_profile(r)
        if result is None:
            continue
        evaluated += 1
        ratio, caps = result
        if best is None or ratio < best["ratio"]:
            best = {"ratio": float(ratio), "r": r.tolist(), "caps": caps}
        if ratio < 1-1e-7:
            print("CANDIDATE", json.dumps(best))
            return
    print(json.dumps({"tested": args.count, "nonheavy": evaluated, "best": best}))


if __name__ == "__main__":
    main()
