"""Exact geometric and algebraic checks for the cover-dependence game."""
from fractions import Fraction as F
from itertools import product
import sympy as S

checks = 0


def check(p):
    global checks
    assert p
    checks += 1


def dot(u, x):
    return sum(a*b for a, b in zip(u, x))


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(
        poly[i][0]*poly[(i+1) % len(poly)][1]
        - poly[i][1]*poly[(i+1) % len(poly)][0]
        for i in range(len(poly))
    )) / 2


def clip(poly, u, b):
    if not poly:
        return []
    out = []
    for a, c in zip(poly, poly[1:] + poly[:1]):
        fa, fc = dot(u, a)-b, dot(u, c)-b
        if fa >= 0:
            out.append(a)
        if fa < 0 < fc or fc < 0 < fa:
            lam = fa/(fa-fc)
            out.append(tuple(a[k]+lam*(c[k]-a[k]) for k in range(2)))
    return out


square = [(F(-1), F(-1)), (F(1), F(-1)), (F(1), F(1)), (F(-1), F(1))]
normals_plus = [(1, 0), (0, 1), (-1, -1)]
normals_minus = [tuple(-a for a in u) for u in normals_plus]

for t in [F(k, 40) for k in range(-19, 20)]:
    K = [(F(-1), F(-1)), (F(1), F(-1)), (F(1), 1+t), (F(-1), 1-t)]
    check(area(K) == 4)
    # Intersection square cap y <= 1 and >= -1 proves removed area.
    common = clip(K, (0, -1), F(-1))
    check(area(square)-area(common) == abs(t)/2)
    plus = [area(clip(K, u, F(0))) for u in normals_plus]
    diagonal = F(2) if t <= 0 else 2-t*t/(2*(1+t))
    check(plus == [2+t/2, F(2), diagonal])
    minus = [area(clip(K, u, F(0))) for u in normals_minus]
    check(all(a+b == 4 for a, b in zip(plus, minus)))
    fibers = [[tuple((1+sign*t)*a for a in x) for x in K] for sign in (1, -1)]
    check(sum(area(p) for p in fibers) == 8*(1+t*t))
    for anchor in (0, 1):
        for u in normals_plus + normals_minus:
            cap_mass = F(0)
            for q in (0, 1):
                threshold = 10*(1-2*anchor)*(q-anchor)
                cap_mass += area(clip(fibers[q], u, threshold))
                if q != anchor:
                    check(max(dot(u, x) for x in fibers[q]) < threshold)
            own_mass = area(clip(fibers[anchor], u, F(0)))
            check(cap_mass == own_mass)
            base_mass = area(clip(K, u, F(0)))
            check(cap_mass == (1+(1-2*anchor)*t)**2*base_mass)
    if t:
        s = abs(t)
        lower = (1+s)**2/(2*(1+s*s))*(F(1, 2)-s/8)
        check(lower-F(1, 4) == s*(7-2*s-s*s)/(16*(1+s*s)))
        check(lower > F(1, 4))

# Symbolic body/cap derivatives. Both diagonal branches have derivative zero.
t = S.symbols("t", real=True)
diag_plus = 2-t*t/(2*(1+t))
diag_minus = S.Integer(2)
for sign in (1, -1):
    for diag in (diag_plus, diag_minus):
        plus_caps = [2+t/2, S.Integer(2), diag]
        minus_caps = [4-a for a in plus_caps]
        derivatives_plus = [
            S.diff((1+sign*t)**2*a, t).subs(t, 0) for a in plus_caps
        ]
        derivatives_minus = [
            S.diff((1+sign*t)**2*a, t).subs(t, 0) for a in minus_caps
        ]
        check(sum(derivatives_plus)/3 == 4*sign+S.Rational(1, 6))
        check(sum(derivatives_minus)/3 == 4*sign-S.Rational(1, 6))
check(S.diff(8*(1+t*t), t).subs(t, 0) == 0)

# Every pure menu selection has an attained positive normalized balance.
for a, b in product((F(23, 6), F(25, 6)), repeat=2):
    pi0, pi1 = b/(a+b), a/(a+b)
    check(pi0 > 0 and pi1 > 0 and pi0+pi1 == 1)
    check(pi0*a-pi1*b == 0)

# The exact frozen-game radius at pi0=1/2 is 1/6, and the interval
# formula makes every other weight no better.
for pi0 in [F(k, 24) for k in range(25)]:
    values = [
        pi0*a-(1-pi0)*b
        for a, b in product((F(23, 6), F(25, 6)), repeat=2)
    ]
    check(min(values) == 4*(2*pi0-1)-F(1, 6))
    check(max(values) == 4*(2*pi0-1)+F(1, 6))
    check(max(map(abs, values)) == abs(4*(2*pi0-1))+F(1, 6))
    check(max(map(abs, values)) >= F(1, 6))

# Universal allocation certificates in the normalized budget model.
for a, b in product([1+F(k, 8) for k in range(9)], repeat=2):
    lam0, lam1 = 2*b/(a+b), 2*a/(a+b)
    check(lam0 > 0 and lam1 > 0 and lam0+lam1 == 2)
    check(lam0*a-lam1*b == 0)
    # Common erosion and homothety values, independent of allocations.
    check(lam0*(-1)+lam1*(-1) == -2)
    check(lam0+lam1 == 2)

print("PASS", checks, "exact rational/symbolic checks")
