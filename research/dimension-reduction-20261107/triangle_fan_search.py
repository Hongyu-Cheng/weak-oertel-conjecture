"""Exploratory floating-point search; no output is a proof certificate."""
import itertools
import json
import math
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution, minimize_scalar


def clip(poly, normal, offset):
    out = []
    for a, b in zip(poly, np.roll(poly, -1, axis=0)):
        fa, fb = a @ normal - offset, b @ normal - offset
        ina, inb = fa <= 1e-12, fb <= 1e-12
        if ina:
            out.append(a)
        if ina != inb:
            out.append(a + fa / (fa - fb) * (b - a))
    return np.array(out).reshape(-1, 2)


def area(p):
    if len(p) < 3:
        return 0.
    return abs(np.sum(p[:, 0] * np.roll(p[:, 1], -1) - p[:, 1] * np.roll(p[:, 0], -1))) / 2


def geometry(x):
    p = np.array([x[0], (1-x[0])*x[1]])
    angles = [x[2], x[2] + x[3], x[2] + x[3] + x[4]]
    if max(x[3], x[4], 2*math.pi-x[3]-x[4]) >= math.pi or x[3]+x[4] >= 2*math.pi:
        return None
    normals = np.array([[math.cos(t), math.sin(t)] for t in angles])
    tri = np.array([[0.,0.],[1.,0.],[0.,1.]])
    theta, beta = [], []
    for a in range(3):
        beta.append(2*area(clip(tri, -normals[a], -normals[a] @ p)))
        poly = tri
        for j in range(3):
            if j != a:
                poly = clip(poly, normals[j], normals[j] @ p)
        cap = max((abs(np.linalg.det(np.array([u-p,v-p]))) for u,v in itertools.combinations(poly,2)), default=0)
        theta.append(cap)
    return np.array(theta), np.array(beta), p, normals


def ideal_cost(theta, beta, m, gamma=1/math.e):
    budgets = gamma*m-beta
    need = m-1
    if min(theta) <= 1e-10 or min(budgets) < -1e-8 or sum(budgets) < need-1e-8:
        return 1e8
    best = 1e8
    for order in itertools.permutations(range(3)):
        remain, cost = need, 0.
        for j in order:
            take = min(remain, budgets[j])
            cost += math.log1p(take/theta[j])/math.log1p(theta[j]/m)
            remain -= take
        if remain <= 1e-7:
            best = min(best,cost)
    return best


def evaluate(x, details=False):
    g=geometry(x)
    if g is None: return 1e8
    theta,beta,p,normals=g
    gamma=1/math.e
    lower=max(1.0000000001, max(beta)/gamma, (sum(beta)-1)/(3*gamma-1))
    m=lower + x[5]
    cost=ideal_cost(theta,beta,m,gamma)
    if details:
        return dict(cost=cost,theta=theta.tolist(),beta=beta.tolist(),point=p.tolist(),normals=normals.tolist(),m=m,params=list(x))
    return cost


if __name__=='__main__':
    bounds=[(.02,.96),(.02,.98),(0,2*math.pi),(.1,math.pi-.001),(.1,math.pi-.001),(0,3)]
    result=differential_evolution(evaluate,bounds,popsize=16,maxiter=350,tol=1e-7,seed=9182,polish=True,workers=1)
    report=evaluate(result.x,True)
    print(json.dumps(report,indent=2))
    Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
