#!/usr/bin/env python3
"""Exploratory floating-point local search; no output is a proof certificate.

Uses the arbitrary-point, arbitrary-three-normal geometry from the existing
triangle_fan_search.py. Each source is a triangle with the common zero point
as a vertex, contained in its single-paid cone. Block counts may be unequal.
"""
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln, logsumexp

from triangle_fan_search import geometry


HERE = Path(__file__).resolve().parent
GAMMA = (99/100)**99


def values(x, counts):
    g = geometry(x[:5])
    if g is None:
        return None
    theta, beta, p, normals = g
    if min(theta) <= 0:
        return None
    m = x[5]
    delta = (m/theta)**(1/99)-1
    if min(delta) <= 0:
        return None
    E = []
    for th, de, N in zip(theta, delta, counts):
        r = np.arange(1, min(N, int((1-1e-10)/de))+1)
        logC = gammaln(N+1)-gammaln(r+1)-gammaln(N-r+1)
        E.append(th*np.exp(logsumexp(logC+99*np.log1p(-r*de))))
    E = np.array(E)
    details = dict(theta=theta.tolist(), beta=beta.tolist(), p=p.tolist(),
                   normals=normals.tolist(), m=m, delta=delta.tolist(),
                   E=E.tolist(), counts=counts)
    return np.r_[E.sum()-m+1, GAMMA*m-beta-E], details


def main():
    start = json.loads((HERE/'triangle_fan_search.json').read_text())['params'][:5]
    results = []
    for counts in [(56,56,55), (56,55,55), (57,55,55), (56,56,54), (55,55,55)]:
        x0 = np.r_[start, 3.321, 0.]
        def constraints(x):
            v = values(x, counts)
            return v[0]-x[6] if v is not None else np.repeat(-1e3, 4)
        res = minimize(
            lambda x: -x[6], x0, method='SLSQP',
            bounds=[(.1,.8), (.1,.9), (0,2*np.pi), (.1,np.pi-.001),
                    (.1,np.pi-.001), (1.1,10), (-1,1)],
            constraints={'type':'ineq', 'fun':constraints},
            options={'maxiter':1500, 'ftol':1e-12})
        result = values(res.x, counts)
        print(counts, res.success, res.message, min(result[0]), result[0], flush=True)
        results.append(dict(success=bool(res.success), message=res.message,
                            minimum=float(min(result[0])), margins=result[0].tolist(),
                            parameters=res.x.tolist(), **result[1]))
    report = {
        'status':'FLOATING_POINT_EXPLORATION_ONLY',
        'limitations':'Local optimization of five block-count profiles, not an exclusion theorem or a global optimum proof.',
        'results':results,
    }
    (HERE/'asymmetric_finite_triangle_search.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__ == '__main__':
    main()
