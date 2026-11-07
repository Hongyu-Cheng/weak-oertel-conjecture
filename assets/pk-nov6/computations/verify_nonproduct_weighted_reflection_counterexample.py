"""Exact polygon and power-profile counterexample to quarter base retention."""
from fractions import Fraction as F
from itertools import combinations, product


def inside(u, v):
    return -1 <= u <= 1 and 0 <= v <= 4 and 3*u+v >= 0


P = {(u, v) for u in range(-3, 4) for v in range(-2, 7) if inside(u, v)}
expected = {(u, v) for u in (0, 1) for v in range(5)} | {(-1, 3), (-1, 4)}
assert P == expected and len(P) == 12

# Check the full vertex list from all pairs of the five boundary lines.
lines = [(1, 0, -1), (1, 0, 1), (0, 1, 0), (0, 1, 4), (3, 1, 0)]
vertices = set()
for (a,b,c), (d,e,f) in combinations(lines, 2):
    det = a*e-b*d
    if det:
        u, v = F(c*e-b*f, det), F(a*f-c*d, det)
        if inside(u, v):
            vertices.add((u, v))
assert vertices == {(0,0), (1,0), (1,4), (-1,4), (-1,3)}

coefficients = {
    (0,0): (1,0,0,0,0), (1,0): (1,0,0,0,0),
    (0,1): (0,1,2,0,0), (1,1): (0,1,2,0,0),
    (0,2): (0,0,1,4,4), (1,2): (0,0,1,2,2),
    (-1,3): (0,0,0,1,0), (0,3): (0,0,0,3,4),
    (1,3): (0,0,0,1,2), (-1,4): (0,0,0,0,1),
    (0,4): (0,0,0,0,3), (1,4): (0,0,0,0,1),
}
for j in P:
    c = [0]*5
    for p in P:
        q = (2*j[0]-p[0], 2*j[1]-p[1])
        if q in P:
            c[max(p[1], q[1])] += 1
    assert tuple(c) == coefficients[j]


def check_weights(t):
    assert all(t[i] >= t[i+1] > 0 for i in range(4))
    w = {p: t[p[1]] for p in P}
    M = sum(w.values())
    values = {}
    # Every possible midpoint lies in the same coordinate bounding box;
    # the larger scan also checks representative outside-support centers.
    for j in product(range(-3,4), range(-2,7)):
        value = sum(min(wp, w.get((2*j[0]-p[0], 2*j[1]-p[1]), 0))
                    for p, wp in w.items())
        if j not in P:
            assert value == 0
        else:
            assert value == sum(c*x for c,x in zip(coefficients[j], t))
            values[j] = value
    assert M == 2*sum(t[:3])+3*sum(t[3:])
    assert max(values.values()) == max(t[0], t[1]+2*t[2], t[2]+4*t[3]+4*t[4])
    return M, values


M, values = check_weights([F(1,2)**v for v in range(5)])
assert M == F(65,16)
assert max(values.values()) == 1
assert F(1,4)-1/M == F(1,260)
assert {j for j,v in values.items() if v == 1} == {(0,0),(1,0),(0,1),(1,1),(0,2)}

t = [(21-v)**14 for v in range(5)]
A,B,C,D,E = t
M, values = check_weights(t)
assert A-B-2*C == 7506560955740439
assert A-C-4*D-4*E == 272148470172696748
assert M == 12992226819033231463
assert M-4*A == 16547088947196739
assert max(values.values()) == A and 4*A < M
assert {j for j,v in values.items() if v == A} == {(0,0),(1,0)}
assert 2*M < 9*A
gamma = F(14,15)**14
assert gamma <= F(4,9)
assert gamma*M/4 < F(A,2)

# Affine radius, positivity, and exact interpolation at rational base midpoints.
for p,q in product(P, repeat=2):
    for lam in (F(0),F(1,3),F(1,2),F(2,3),F(1)):
        v = (1-lam)*p[1]+lam*q[1]
        assert 21-v == (1-lam)*(21-p[1])+lam*(21-q[1])
        assert 21-v >= 17

assert (-1,3) in P and (1,0) in P and (1,3) in P and (-1,0) not in P
print("PASS: complete 12-point lattice polygon, every reflection row, log-affine and d=14 affine-root strict failures, and actual-body constants")
