"""Exact scalar minima and actual seven-fiber cap calibrations.

The source note proves the all-normal limit. These finite checks do not
replace its compactness argument.
"""
from fractions import Fraction as Q

V = Q(1, 2)
G = Q(4, 9)
ETA = Q(1, 10)
KAPPA = Q(2, 3)
g = (Q(1, 3), Q(1, 3))
T = [(Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(1))]
B = [(Q(-3, 10), Q(-1, 3)), (Q(7, 10), Q(-1, 3)),
     (Q(-2, 5), Q(2, 3))]
CORE = [(0, 0), (0, 1), (1, 0), (1, 1)]
EXTRA = [(-1, 0), (-1, 1), (1, -1)]


def area(poly):
    if len(poly) < 3:
        return Q(0)
    return abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                   - poly[i][1]*poly[(i+1) % len(poly)][0]
                   for i in range(len(poly)))) / 2


def cap(poly, normal, threshold):
    """Closed clipping; boundary edges have zero planar area."""
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        hp = sum(a*b for a, b in zip(normal, p)) - threshold
        hq = sum(a*b for a, b in zip(normal, q)) - threshold
        if hp >= 0:
            out.append(p)
        if (hp < 0 < hq) or (hq < 0 < hp):
            f = hp / (hp - hq)
            out.append(tuple(p[j] + f*(q[j]-p[j]) for j in range(2)))
    return area(out)


def tail(a, x):
    if x <= 0:
        return Q(1)
    if x >= 1:
        return Q(0)
    if x < a:
        return 1 - x*x/a
    return (1-x)**2/(1-a)


def pair_extrema(a, m):
    """Inspect every support/mode-event interval and quadratic critical point."""
    def f(s):
        return tail(a, m+s) + tail(a, m-s)
    knots = sorted({Q(0), abs(m), abs(m-a), abs(m-1)})
    vals = [f(s) for s in knots]
    for lo, hi in zip(knots, knots[1:]):
        md = (lo+hi)/2
        fl, fm, fh = f(lo), f(md), f(hi)
        aa = 2*(fl - 2*fm + fh)/(hi-lo)**2
        bb = (fh-fl)/(hi-lo) - aa*(lo+hi)
        if aa:
            critical = -bb/(2*aa)
            if lo < critical < hi:
                vals.append(f(critical))
    vals.append(Q(1))
    return min(vals), max(vals)


def triangle_pair_extrema(q):
    hts = sorted([Q(0), Q(1), q])
    span = hts[-1] - hts[0]
    a = (hts[1] - hts[0])/span
    m = ((1+q)/3 - hts[0])/span
    return pair_extrema(a, m)


scalar_checks = 0
assert area(T) == area(B) == V
assert tuple(sum(p[j] for p in B)/3 for j in range(2)) == (0, 0)
for i in range(-100, 1):
    q = Q(i, 500)
    mn, mx = triangle_pair_extrema(q)
    expected = 2*(G + q*q/(9*(1-q)))
    assert mn == expected < 1
    a = -q/(1-q)
    assert 0 <= a <= Q(1, 6)
    scalar_checks += 1
assert triangle_pair_extrema(Q(0)) == (Q(8, 9), Q(10, 9))
assert pair_extrema(Q(1), Q(2, 3)) == (Q(8, 9), Q(10, 9))
scalar_checks += 2
for i in range(-300, 301):
    xi = Q(i, 100)
    mn, mx = triangle_pair_extrema(xi-ETA)
    assert mn >= 2*G
    if abs(xi) > ETA:
        assert xi*xi/9 + mn > ETA*ETA/9 + 2*G
    scalar_checks += 1


def H(x):
    return x*x + 2*(x-ETA)**2/(1-x+ETA)


def polynomial(x):
    return 100*x**3 - 320*x*x + 341*x - 21


def half_derivative(x):
    return x + 1/(1-x+ETA)**2 - 1


for i in range(-100, 101):
    x = Q(i, 1000)
    assert half_derivative(x) == polynomial(x)/(100*(1-x+ETA)**2)
    assert 2 + 4/(1-x+ETA)**3 > 0
    scalar_checks += 1
lo, hi = Q(6553, 100000), Q(3277, 50000)
assert 0 < lo < hi < ETA and polynomial(lo) < 0 < polynomial(hi)
for _ in range(60):
    md = (lo+hi)/2
    if polynomial(md) < 0:
        lo = md
    else:
        hi = md
lower_H = lo*lo + 2*(ETA-hi)**2/(1+ETA-hi)
upper_H = hi*hi + 2*(ETA-lo)**2/(1+ETA-lo)
assert 0 < lower_H <= upper_H < ETA*ETA
assert upper_H-lower_H < Q(1, 10**20)
assert Q(366, 10**6) < lower_H/18 < upper_H/18 < Q(367, 10**6)
scalar_checks += 4


def small_body(tau):
    return [(g[0]+tau**3*p[0], g[1]+tau*p[1]) for p in B]


def ambient_mass(tau, y, normal, shift):
    e = small_body(tau)
    beta = (-4+shift/2, -4-shift/2)
    center_threshold = sum(a*b for a, b in zip(normal, y))
    masses = {}
    for z in CORE + EXTRA:
        poly = T if z in CORE else e
        threshold = center_threshold - beta[0]*z[0] - beta[1]*z[1]
        masses[z] = cap(poly, normal, threshold)
    return sum(masses.values()), masses


actual_checks = 0
for tau in [Q(1, 4), Q(1, 8), Q(1, 16), Q(1, 32),
            Q(1, 64), Q(1, 128)]:
    e = small_body(tau)
    assert area(e) == tau**4 * V
    assert all(x > 0 and y > 0 and x+y < 1 for x, y in e)
    actual_checks += 1

# Rational trial directions and displacements exercise actual oblique caps,
# including the common base tilt, the owned full trace, and empty core traces.
for tau in [Q(1, 16), Q(1, 32), Q(1, 64), Q(1, 128)]:
    t = tau**4
    for xi in [Q(-1, 10), Q(-1, 20), Q(0), Q(1, 20),
               Q(1, 15), Q(1, 10)]:
        q = xi-ETA
        delta = tau*tau*xi
        for v in [(Q(0), Q(0)), (Q(1, 1000), Q(-1, 2000)),
                  (Q(-1, 100), Q(1, 200)), (Q(1, 100), Q(-1, 100))]:
            y = (g[0]+t*v[0], g[1]+t*v[1])
            got, by_base = ambient_mass(tau, y, (Q(1), delta), Q(0))
            own = V*((2-delta)/3-t*(v[0]+delta*v[1]))**2/(1-delta)
            small = t*V*((2-q)/3-tau*(v[0]+delta*v[1]))**2/(1-q)
            assert got == own + 2*small + t*V
            assert by_base[(0, 0)] == own
            assert by_base[(-1, 0)] == t*V
            assert by_base[(-1, 1)] == by_base[(1, -1)] == small
            assert all(by_base[z] == 0 for z in CORE if z != (0, 0))
            # Exact cap slope check with an explicit finite remainder bound.
            expected = -KAPPA*v[0] + V + 2*G*V + V*H(xi)/9
            assert abs((got-G*V)/t-expected) < 2*tau
            actual_checks += 1

    for v in [(Q(0), Q(0)), (Q(1, 1000), Q(-1, 2000)),
              (Q(-1, 100), Q(1, 200))]:
        y = (g[0]+t*v[0], g[1]+t*v[1])
        for i, normal, shift in [
                (2, (Q(0), Q(1)), Q(0)),
                (0, (Q(-1), Q(-1)), tau/3)]:
            got, by_base = ambient_mass(tau, y, normal, shift)
            vi = v[1] if i == 2 else -v[0]-v[1]
            own = V*(Q(2, 3)-t*vi)**2
            assert by_base[(0, 0)] == own
            assert by_base[(-1, 0)] == t*V
            assert all(by_base[z] == 0 for z in CORE if z != (0, 0))
            assert got == own+t*V+by_base[(-1, 1)]+by_base[(1, -1)]
            expected = V+2*G*V-KAPPA*vi
            assert abs((got-G*V)/t-expected) < 2*tau
            actual_checks += 1

# Balance and normalized mass use an arbitrary positive exact surrogate
# Delta: these identities are algebraic and hence hold at the algebraic root.
for dlt in [Q(1, 1000), Q(1, 2000), Q(1, 3000)]:
    js = [2*G*V, 2*G*V+dlt, 2*G*V]
    bar = sum(js)/3
    vi = [(x-bar)/KAPPA for x in js]
    assert sum(vi) == 0
    assert vi[1] == dlt and vi[2] == -dlt/2
    assert all(js[i]-KAPPA*vi[i] == bar for i in range(3))
    assert V+bar == Q(17, 18)+dlt/3
    normalized = (4*(V+bar)-3*G*V)/(16*V)
    assert normalized == Q(7, 18)+dlt/6
    actual_checks += 1

print("PASS", scalar_checks, "exact scalar/normal-cost checks and",
      actual_checks, "actual seven-fiber cap and balance checks")
