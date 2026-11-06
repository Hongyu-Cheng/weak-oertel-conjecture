"""Exact finite KKT decomposition of an interval moment-centroid path.

This verifier uses rational arithmetic (SymPy), not optimization tolerances.
The example is the archived fixed-half-mass selector obstruction.
"""
from itertools import product
import sympy as s

t = s.Symbol('t', real=True)
w = tuple(map(s.Rational, (9, 75, 140, 200, 25)))
j = 3
d = tuple(s.Integer(i-j) for i in range(len(w)))
T = s.Integer(250)


def intersect(interval, expr):
    """Intersect a rational interval with the affine inequality expr >= 0."""
    lo, hi = interval
    p = s.Poly(s.expand(expr), t)
    assert p.degree() <= 1
    c, a = p.nth(0), p.nth(1)
    if a > 0:
        lo = max(lo, -c/a)
    elif a < 0:
        hi = min(hi, -c/a)
    elif c < 0:
        return None
    return (lo, hi) if lo < hi else None


def support_pieces(v):
    """Maximize sum(v_i m_i - m_i^2/2) at mass t, base moment zero."""
    pieces = []
    for pat in product((0, 1, 2), repeat=len(w)):
        A = [i for i, q in enumerate(pat) if q == 1]
        F = [i for i, q in enumerate(pat) if q == 2]
        if not A:
            continue  # Such a pattern can occur only at an isolated mass.
        S, Z, ZZ = len(A), sum(d[i] for i in A), sum(d[i]**2 for i in A)
        C0 = sum(v[i] for i in A) + sum(w[i] for i in F)
        C1 = sum(d[i]*v[i] for i in A) + sum(d[i]*w[i] for i in F)
        det = S*ZZ-Z*Z
        interval = (s.Integer(0), T)
        if det:
            b = s.expand(((C0-t)*ZZ-Z*C1)/det)
            nu = s.expand((S*C1-Z*(C0-t))/det)
            m = [s.Integer(0) if q == 0 else w[i] if q == 2
                 else s.expand(v[i]-b-nu*d[i]) for i, q in enumerate(pat)]
            constraints = []
            for i, q in enumerate(pat):
                residual = s.expand(v[i]-m[i]-b-nu*d[i])
                if q == 0:
                    constraints.append(-residual)
                elif q == 2:
                    constraints.append(residual)
                else:
                    constraints += [m[i], w[i]-m[i]]
        else:
            # An open mass interval with one free coordinate must use base j.
            if len(A) != 1 or d[A[0]] != 0 or C1 != 0:
                continue
            i0 = A[0]
            m = [s.Integer(0) if q == 0 else w[i] if q == 2
                 else t-sum(w[k] for k in F) for i, q in enumerate(pat)]
            b = s.expand(v[i0]-m[i0])
            constraints = [m[i0], w[i0]-m[i0]]
            lower, upper = [], []
            for i, q in enumerate(pat):
                if q == 1:
                    continue
                # Empty: nu*d >= v-b; full: nu*d <= v-w-b.
                rhs = s.expand(v[i]-m[i]-b)
                if d[i] == 0:
                    constraints.append(-rhs if q == 0 else rhs)
                elif (q == 0 and d[i] > 0) or (q == 2 and d[i] < 0):
                    lower.append(rhs/d[i])
                else:
                    upper.append(rhs/d[i])
            constraints += [u-l for l in lower for u in upper]
        for con in constraints:
            interval = intersect(interval, con)
            if interval is None:
                break
        if interval is None:
            continue
        assert s.expand(sum(m)-t) == 0
        assert s.expand(sum(d[i]*m[i] for i in range(len(w)))) == 0
        val = s.expand(sum(v[i]*m[i]-m[i]**2/2 for i in range(len(w))))
        pieces.append((*interval, val, tuple(m)))
    breaks = sorted({s.Integer(0), T} | {q for p in pieces for q in p[:2]})
    out = []
    for lo, hi in zip(breaks, breaks[1:]):
        mid = (lo+hi)/2
        match = [p for p in pieces if p[0] <= mid <= p[1]]
        assert match, (lo, hi)
        val, alloc = match[0][2:]
        assert all(s.expand(p[2]-val) == 0 for p in match)
        if out and out[-1][2] == val:
            out[-1] = (out[-1][0], hi, val, alloc)
        else:
            out.append((lo, hi, val, alloc))
    return out


U = support_pieces(tuple(s.Integer(0) for _ in w))
V = support_pieces(w)  # V = -L for fibers [-w_i,0].
cuts = sorted({q for p in U+V for q in p[:2]})
path = []
for lo, hi in zip(cuts, cuts[1:]):
    mid = (lo+hi)/2
    up = next(p for p in U if p[0] <= mid <= p[1])
    vp = next(p for p in V if p[0] <= mid <= p[1])
    c = s.cancel((up[2]-vp[2])/(2*t))
    path.append((lo, hi, c))
    print(f'{lo} <= t <= {hi}: c(t) = {c}')
for left, right in zip(path, path[1:]):
    assert left[1] == right[0]
    assert s.cancel(left[2].subs(t, left[1])-right[2].subs(t, right[0])) == 0
assert s.limit(path[0][2], t, 0, dir='+') == -100
assert path[-1][2].subs(t, T) == -s.Rational(353, 4)
def center(mass):
    return next(c.subs(t, mass) for lo, hi, c in path if lo <= mass <= hi)
assert center(s.Rational(449, 2)) == -s.Rational(39025, 449)
assert center(s.Integer(235)) == -s.Rational(175, 2)
# The same exact five-fiber body has depth 225/2 at this latter point.
assert s.Rational(225, 2) > sum(w)/4
print('PASS: exact entire path, bad half mass, and deep mass t=235.')
