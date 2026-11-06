"""Independent exact finite-union audits for the all-planar tail mechanism.

The proof's infinite-union step is measure-theoretic, not supplied by
these checks. Finite unions here can have arbitrarily overlapping cuts.
"""
from fractions import Fraction as F
from random import Random

checks = 0


def check(p):
    global checks
    assert p
    checks += 1


def union_area(triangles, floor=F(0)):
    """Area of union {u/a+v/b<1,u,v>=0}, restricted to v>=floor."""
    if not triangles:
        return F(0)
    ceiling = max(b for a, b in triangles)
    if floor >= ceiling:
        return F(0)
    cuts = {floor, ceiling}
    for a, b in triangles:
        if floor < b < ceiling:
            cuts.add(b)
    for a, b in triangles:
        for c, d in triangles:
            if a/b != c/d:
                x = (a-c)/(a/b-c/d)
                if floor < x < min(b, d):
                    cuts.add(x)
    cuts = sorted(cuts)
    value = F(0)
    for left, right in zip(cuts, cuts[1:]):
        mid = (left+right)/2
        a, b = max(triangles, key=lambda ab: ab[0]*(1-mid/ab[1]))
        if a*(1-mid/b) > 0:
            value += (right-left)*a*(2-(left+right)/b)/2
    return value


def clip(poly, a, b, c):
    out = []
    for p, q in zip(poly, poly[1:]+poly[:1]):
        fp, fq = a*p[0]+b*p[1]-c, a*q[0]+b*q[1]-c
        if fp >= 0:
            out.append(p)
        if fp*fq < 0:
            t = fp/(fp-fq)
            out.append((p[0]+t*(q[0]-p[0]), p[1]+t*(q[1]-p[1])))
    return out


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p, q in zip(poly, poly[1:]+poly[:1])))/2


B, level = F(501, 1000), F(309, 1000)
r = 1-level/B
check(r == F(64, 167))
check(r*r < F(3, 20))
check(F(9, 29)-F(1, 1550) > level)
rng = Random(719283)
for index in range(301):
    triangles = [(F(rng.randint(1, 100), 10000),
                  F(rng.randint(1, 501), 1000))
                 for _ in range(1+index % 23)]
    total, tail = union_area(triangles), union_area(triangles, level)
    check(tail <= r*r*total)
    # Explicit pointwise preservation in the SAME triangle.
    for a, b in triangles:
        if b >= level:
            for n in range(1, 5):
                v = level+(b-level)*F(n, 5)
                u = a*(1-v/b)*F(3, 7)
                check((u/r)/a+((v-level)/r)/b <= 1)
for a in (F(1, 10000), F(1, 1000), F(1, 100)):
    check(union_area([(a, B)], level) == r*r*union_area([(a, B)]))

# Many-cut actual bodies with touching side midpoints and central candidates.
# barycentric affine functions in coordinates x=lambda1,y=lambda2.
lam = [(F(-1), F(-1), F(1)), (F(1), F(0), F(0)), (F(0), F(1), F(0))]
Gamma = F(4, 9)
normals = [(a, b) for a in range(-4, 5) for b in range(-4, 5) if a or b]
for index in range(24):
    groups = [[] for _ in range(3)]
    oriented = [[[], []] for _ in range(3)]
    Q = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
    for i in range(3):
        j, k = [v for v in range(3) if v != i]
        for num in range(1+index % 8):
            a = F(rng.randint(1, 10), 1000000)
            b = F(rng.randint(25, 50), 100)
            orientation = rng.randrange(2)
            first, second = (a, b) if orientation == 0 else (b, a)
            groups[i].append((first, second))
            oriented[i][orientation].append((a, b))
            ax = lam[j][0]/first+lam[k][0]/second
            ay = lam[j][1]/first+lam[k][1]/second
            constant = lam[j][2]/first+lam[k][2]/second
            Q = clip(Q, ax, ay, 1-constant)
    tau_i = [2*union_area(g) for g in groups]
    tau = sum(tau_i)
    check(1-2*area(Q) == tau)
    check(tau < F(1, 10000))
    losses = tau_i[:]
    for i in range(3):
        j, k = [v for v in range(3) if v != i]
        # orientation0 short j/long k; orientation1 short k/long j.
        losses[k] += F(3, 20)*2*union_area(oriented[i][0])
        losses[j] += F(3, 20)*2*union_area(oriented[i][1])
    check(sum(losses) <= F(13, 10)*tau)
    check(all(0 <= loss <= tau for loss in losses))
    avg = sum(losses)/3
    bary = [F(1, 3)+F(3, 4)*(avg-loss) for loss in losses]
    check(sum(bary) == 1)
    check(all(abs(v-F(1, 3)) <= F(1, 10000) for v in bary))
    lower = Gamma-F(13, 30)*tau-F(9, 4)*tau*tau
    check(lower/(1-tau)-Gamma >= tau/180)
    y = (bary[1], bary[2])
    for a, b in normals:
        cap = area(clip(Q, F(a), F(b), a*y[0]+b*y[1]))
        check(2*cap >= lower)

print(f"PASS: {checks} exact checks;301 overlapping union families; "
      "24 actual many-cut polygons with80 directions each.")
