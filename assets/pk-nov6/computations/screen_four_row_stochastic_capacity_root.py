"""Bounded falsification search. Numerical output is not a theorem."""
import json
import numpy as np
from scipy.optimize import minimize


def capacity(row):
    x, y, w, z = np.sort(np.maximum(row, 0.0))
    if z == 0 or y < 1e-14:
        return 0.0
    if x < 1e-14:
        return (y*w*z)**(1/3)
    h = z - np.sqrt(max(0.0, (z-x)*(z-y)*(z-w)/z))
    if (z-w > 1e-14 and h >= w) or z-y < 1e-14:
        return (z*h*h)**(1/3)
    # The stable rationalization avoids subtracting nearby radicals.
    aa = (w-x)*(z-x)
    bb = (w-y)*(z-y)
    numerator = w*z*(x*x+x*y+y*y)-x*y*(w+z)*(x+y)+x*x*y*y
    denominator = y**1.5*np.sqrt(aa)+x**1.5*np.sqrt(bb)
    return (numerator/denominator)**(2/3)


def objective(v):
    X = v[:16].reshape(4, 4)
    p = v[16:]
    ph = np.array([capacity(row) for row in X])
    c = np.array([np.prod(np.delete(p, i)) for i in range(4)])
    return np.sum(p**3) - 3*np.dot(ph, c)


def main():
    rng = np.random.default_rng(4397)
    constraints = [
        {'type': 'eq', 'fun': lambda v: v[:16].reshape(4, 4).sum(axis=0)-1},
        {'type': 'eq', 'fun': lambda v: v[16:].sum()-4},
    ]
    best = None
    for i in range(48):
        X = rng.dirichlet(np.repeat([.3, 1, 4][i % 3], 4), size=4).T
        p = 4*rng.dirichlet(np.ones(4))
        start = np.r_[X.ravel(), p]
        r = minimize(objective, start, method='SLSQP',
                     bounds=[(1e-10, 1)]*16+[(1e-8, 4)]*4,
                     constraints=constraints,
                     options={'maxiter': 700, 'ftol': 2e-11})
        err = max(np.max(np.abs(constraints[0]['fun'](r.x))),
                  abs(constraints[1]['fun'](r.x)))
        if err < 1e-6 and (best is None or r.fun < best['gap']):
            best = {'gap': float(r.fun), 'X': r.x[:16].reshape(4,4).tolist(),
                    'p': r.x[16:].tolist(), 'error': float(err),
                    'success': bool(r.success), 'iteration': i}
            print(json.dumps(best), flush=True)
    with open('./four_row_stochastic_capacity_screen_root.json', 'w') as f:
        json.dump(best, f, indent=2)


if __name__ == '__main__':
    main()
