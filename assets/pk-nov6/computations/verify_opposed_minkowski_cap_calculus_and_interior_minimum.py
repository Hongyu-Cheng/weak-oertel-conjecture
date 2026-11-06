"""Exact planar clipping, chamber derivatives, and all-point-cover budgets."""
from fractions import Fraction as F

checks = 0


def check(p):
    global checks
    assert p
    checks += 1


def det(p, q):
    return p[0]*q[1]-p[1]*q[0]


def sub(p, q):
    return (p[0]-q[0], p[1]-q[1])


def dot(p, q):
    return p[0]*q[0]+p[1]*q[1]


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and det(sub(out[-1], out[-2]), sub(p, out[-1])) <= 0:
                out.pop()
            out.append(p)
        return out
    return half(points)[:-1]+half(points[::-1])[:-1]


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(det(poly[i], poly[(i+1) % len(poly)])
                   for i in range(len(poly))))/2


def clip(poly, u, t):
    out = []
    for p, q in zip(poly, poly[1:]+poly[:1]):
        fp, fq = dot(u, p)-t, dot(u, q)-t
        if fp >= 0:
            out.append(p)
        if fp*fq < 0:
            a = fp/(fp-fq)
            out.append((p[0]+a*(q[0]-p[0]), p[1]+a*(q[1]-p[1])))
    return out


def mix(A, C, s):
    return hull([((1-s)*a[0]+s*c[0], (1-s)*a[1]+s*c[1])
                 for a in A for c in C])


def support(P, n):
    return max(dot(p, n) for p in P)


def flux(P, A, C, u, t, tdot, sign):
    """Exact support velocity integral minus moving-line velocity integral.

    Edge normals are unnormalized; captured length/normal length equals
    the captured fraction of that edge. Chord length/|u| is rational.
    """
    value, crossing = F(0), []
    for p, q in zip(P, P[1:]+P[:1]):
        edge = sub(q, p)
        n = (edge[1], -edge[0])
        fp, fq = dot(u, p)-t, dot(u, q)-t
        assert fp != 0 and fq != 0  # this verifier's proper chambers
        if fp > 0 and fq > 0:
            fraction = F(1)
        elif fp < 0 and fq < 0:
            fraction = F(0)
        else:
            v = fp/(fp-fq)
            fraction = v if fp > 0 else 1-v
            crossing.append((p[0]+v*edge[0], p[1]+v*edge[1]))
        value += sign*fraction*(support(C, n)-support(A, n))
    if len(crossing) == 2:
        d = sub(crossing[1], crossing[0])
        chord_over_normal = abs(dot(d, (-u[1], u[0])))/dot(u, u)
        value -= tdot*chord_over_normal
    else:
        assert not crossing
    return value


A = [(F(0), F(0)), (F(2), F(0)), (F(0), F(1))]
C = [(F(-1), F(0)), (F(1), F(-1)), (F(2), F(2)), (F(0), F(3))]
C = hull(C)
B = mix(A, C, F(1, 2))
a, c, W = area(A), area(C), area(B)
q = 2*W-(a+c)/2
Delta = 2*q-a-c
step = F(1, 1000000)
chambers = 0
for s in (F(1, 5), F(1, 3), F(2, 5)):
    for u in ((F(1), F(0)), (F(0), F(1)), (F(2), F(-3)), (F(3), F(2))):
        for beta in (F(-2, 7), F(1, 11), F(3, 5)):
            for j in (-1, 0, 1):
                t0, tdot = F(17, 29), F(2, 13)
                def state(v):
                    return (mix(A, C, v), B, mix(C, A, v))
                def thresholds(v):
                    return [t0+tdot*v-(1-2*v)*beta*(z-j) for z in (-1, 0, 1)]
                polys, ts = state(s), thresholds(s)
                # Exclude only event parameters; all normal orientations remain.
                if any(dot(u, p) == t for P, t in zip(polys, ts) for p in P):
                    continue
                def masses(v):
                    Ps, tv = state(v), thresholds(v)
                    return [area(clip(P, u, t)) for P, t in zip(Ps, tv)]
                f0, fm, fp = masses(s), masses(s-step), masses(s+step)
                fmm, fpp = masses(s-2*step), masses(s+2*step)
                for zindex, z in enumerate((-1, 0, 1)):
                    sign = (1, 0, -1)[zindex]
                    derivative = (fp[zindex]-fm[zindex])/(2*step)
                    target = flux(polys[zindex], A, C, u, ts[zindex],
                                  tdot+2*beta*(z-j), sign)
                    check(derivative == target)
                    check(fpp[zindex]-3*fp[zindex]+3*f0[zindex]-fm[zindex] == 0)
                    check(fp[zindex]-3*f0[zindex]+3*fm[zindex]-fmm[zindex] == 0)
                    check(f0[zindex]+area(clip(polys[zindex], (-u[0], -u[1]), -ts[zindex]))
                          == area(polys[zindex]))
                check(sum(area(P) for P in polys) == a+c+W+2*Delta*s*(1-s))
                check(area(polys[0])-area(polys[2]) == (1-2*s)*(a-c))
                check(area(mix(polys[0], polys[2], F(1, 2))) == W)
                chambers += 1

# Supporting-edge traces: the two one-sided derivatives really differ.
for speed in (F(-2), F(-1), F(0), F(1), F(2)):
    def edgecap(v):
        rect = [(F(-1), F(-1)), (1+v, F(-1)), (1+v, F(1)), (F(-1), F(1))]
        return area(clip(rect, (F(1), F(0)), 1+(1-speed)*v))
    check((edgecap(step)-edgecap(F(0)))/step == 2*max(speed, 0))
    check((edgecap(F(0))-edgecap(-step))/step == 2*min(speed, 0))

# Persistent vertex incidence is a proper cap, not a supporting cap.
for k in range(26):
    s = F(k, 25)
    r = 1+s
    P = [(F(0), F(0)), (2*r, F(0)), (F(0), r)]
    upper = area(clip(P, (F(1), F(-1)), F(0)))
    lower = area(clip(P, (F(-1), F(1)), F(0)))
    check(upper == 2*r*r/3)
    check(lower == r*r/3)
    check(0 < upper < area(P) and 0 < lower < area(P))

# Rational actual six-cap cover under the scaled shared tilt.
K = [(F(-1), F(-1)), (F(1), F(-1)), (F(1), F(1)), (F(-1), F(1))]
def scale(P, r):
    return [(r*x, r*y) for x, y in P]

def Dtheta(t):
    return max((1+t)**2/2, F(1, 2)+(1-t)**2)/(3+2*t*t)

for k in range(101):
    s = F(k, 400)
    theta = F(1, 2)-s
    Ps = [scale(K, F(1, 2)+s), K, scale(K, F(3, 2)-s)]
    L = 10*(1-2*s)
    budgets = []
    # (anchor, base coefficient), followed by both continuous orientations.
    for anchor, basecoef in ((-1, -L), (0, -L), (1, L)):
        for contsign in (-1, 1):
            cap = sum(area(clip(P, (F(contsign), F(0)), -basecoef*(z-anchor)))
                      for z, P in zip((-1, 0, 1), Ps))
            exact = { -1: area(Ps[0])/2,
                       0: area(Ps[0])+area(K)/2,
                       1: area(Ps[2])/2 }[anchor]
            check(cap == exact)
            budgets.append(cap)
    check(max(budgets)/sum(area(P) for P in Ps) == Dtheta(theta))
    check(area(mix(Ps[0], Ps[2], F(1, 2))) == area(K))
    check(Dtheta(theta) > F(2, 9))

# Polynomial identities for exact active branches, finite-difference checked
# at enough rational points to certify the displayed low-degree identities.
for k in range(101):
    t = F(k, 200)
    denominator = 3+2*t*t
    end, mid = (1+t)**2/2, F(3, 2)-2*t+t*t
    check(end-mid == -(t*t-6*t+2)/2)
    check((1+t)*denominator-4*t*end == 3+t-2*t*t)
    check((-2+2*t)*denominator-4*t*mid == 4*t*t-6)
    check(3+t-2*t*t > 0 and 4*t*t-6 < 0)

# Radical identities in Q[sqrt(7)], with tuples denoting a+b sqrt(7).
def plus(x, y): return (x[0]+y[0], x[1]+y[1])
def mult(x, y): return (x[0]*y[0]+7*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def times(c, x): return (c*x[0], c*x[1])
th = (F(3), F(-1))
th2 = mult(th, th)
check(plus(plus(th2, times(-6, th)), (F(2), F(0))) == (0, 0))
depth = (F(19, 62), F(-2, 217))
den = plus((F(3), F(0)), times(2, th2))
num = times(F(1, 2), mult(plus((F(1), F(0)), th), plus((F(1), F(0)), th)))
check(mult(depth, den) == num)
check(F(21, 8)**2 < 7 < F(8, 3)**2)  # 1/3<theta_*<3/8, hence D_*>2/9.

# A genuinely nonhomothetic nested pair, with the exact same all-point cover.
for k in range(101):
    s = F(k, 200)
    def rectangle(x, y):
        return [(-x, -y), (x, -y), (x, y), (-x, y)]
    Ps = [rectangle(1+s, F(1, 2)+F(5, 2)*s),
          rectangle(F(3, 2), F(7, 4)),
          rectangle(2-s, 3-F(5, 2)*s)]
    aa, cc, ww = 2+12*s+10*s*s, 24-32*s+10*s*s, F(21, 2)
    check(list(map(area, Ps)) == [aa, ww, cc])
    check(cc-2*aa-ww == F(19, 2)-56*s-10*s*s)
    check(area(mix(Ps[0], Ps[2], F(1, 2))) == ww)
    total = aa+cc+ww
    ap, cp = 12+20*s, -32+20*s
    check(cp*(aa+ww)-cc*ap < 0)
    check(ap*(cc+ww/2)-cp*(aa+ww/2) > 0)
    for anchor, basecoef in ((-1, F(-10)), (0, F(-10)), (1, F(10))):
        for contsign in (-1, 1):
            cap = sum(area(clip(P, (F(contsign), F(0)), -basecoef*(z-anchor)))
                      for z, P in zip((-1, 0, 1), Ps))
            check(cap == {-1: aa/2, 0: aa+ww/2, 1: cc/2}[anchor])
    check(max(cc/2, ww/2+aa)/total > F(1, 4))

print(f"PASS: {checks} exact checks; {chambers} cap chambers; "
      "202 six-cap source covers; supporting-edge one-sided traces.")
