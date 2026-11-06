"""Exploratory only: exact-piece quadratic minimization in integer tilt."""
import json
import random
import numpy as np


def tilt_min(r, source, theta):
    r = np.asarray(r, dtype=float)
    j = np.arange(len(r))-source
    nonzero = j != 0
    cuts = np.unique(np.concatenate([
        -(2-theta)*r[nonzero]/j[nonzero],
        (1-2*theta)*r[nonzero]/j[nonzero],
        (1+theta)*r[nonzero]/j[nonzero]]))
    ext = max(1, np.max(np.abs(cuts)))
    bounds = np.concatenate(([-2*ext-1], cuts, [2*ext+1]))
    best = (float('inf'), 0)
    for left, right in zip(bounds, bounds[1:]):
        middle = (left+right)/2
        margins = middle*j
        full = margins >= (1+theta)*r
        empty = margins <= -(2-theta)*r
        proper = ~(full | empty)
        high = proper & (margins <= (1-2*theta)*r)
        low = proper & ~high
        A = B = 0.
        C = np.sum(4.5*r[full]**2)
        if np.any(high):
            assert theta < 1
            den = 2*(1-theta)
            A += np.sum(j[high]**2)/den
            B += np.sum(2*(2-theta)*r[high]*j[high])/den
            C += np.sum(((2-theta)*r[high])**2)/den
        if np.any(low):
            assert theta > 0
            den = 2*theta
            A -= np.sum(j[low]**2)/den
            B += np.sum(2*(1+theta)*r[low]*j[low])/den
            C += np.sum(4.5*r[low]**2-((1+theta)*r[low])**2/den)
        candidates = [left, right]
        if A > 1e-12:
            candidates.append(max(left, min(right, -B/(2*A))))
        for alpha in candidates:
            value = A*alpha*alpha+B*alpha+C
            if value < best[0]:
                best = (value, alpha)
    return best


if __name__ == '__main__':
    random.seed(10493)
    best_gain = 0.
    for trial in range(3000):
        count = random.randrange(3, 12)
        slopes = sorted([random.randint(-15, 15) for _ in range(count-1)], reverse=True)
        raw = [0]
        for slope in slopes:
            raw.append(raw[-1]+slope)
        offset = -min(raw)+random.randrange(1, 20)
        radii = [x+offset for x in raw]
        radii = np.asarray(radii)/max(radii)
        source_results = []
        for source in range(count):
            canonical = min(tilt_min(radii, source, theta)[0] for theta in [0., 1.])
            angular = min((tilt_min(radii, source, theta)[0], theta,
                           tilt_min(radii, source, theta)[1])
                          for theta in np.linspace(.05, .95, 19))
            source_results.append((min(canonical, angular[0]), source, canonical, angular))
        winner = max(source_results)
        gain = winner[2]-winner[0]
        if gain > best_gain+1e-8:
            best_gain = gain
            result = {'trial': trial, 'radii_int': [x+offset for x in raw],
                      'winner': winner, 'all': source_results, 'gain': gain}
            print(json.dumps(result), flush=True)
            if gain > 1e-5:
                break
        if trial % 100 == 0:
            print('progress', trial, 'best_gain', best_gain, flush=True)
