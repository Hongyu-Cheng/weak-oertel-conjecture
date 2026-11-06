"""Exact checks for the near-triangle quadrilateral stability theorem.

All arithmetic is rational. Finite directional checks supplement, and do
not replace, the all-direction proof in the companion Markdown note.
"""
from fractions import Fraction as F

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(poly[i][0] * poly[(i + 1) % len(poly)][1]
                   - poly[i][1] * poly[(i + 1) % len(poly)][0]
                   for i in range(len(poly)))) / 2


def clip(poly, a, b, c):
    """Closed polygon intersection with a*x+b*y>=c."""
    if not poly:
        return []
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp, fq = a * p[0] + b * p[1] - c, a * q[0] + b * q[1] - c
        if fp >= 0:
            out.append(p)
        if (fp < 0 < fq) or (fq < 0 < fp):
            t = fp / (fp - fq)
            out.append((p[0] + t * (q[0] - p[0]),
                        p[1] + t * (q[1] - p[1])))
    return out


G = F(4, 9)
eps = F(1, 10000)
U, P = F(30000, 9997), F(90000, 40009)
check(P - F(29, 20) * (U - F(29, 20)) == F(110147293, 159987989200))
check(P - F(31, 20) * (U - F(31, 20)) == F(95744053, 159987989200))
check(F(16, 33) - G - eps == F(39901, 990000))
check(F(9, 29) - F(1, 1550) - F(3, 10) == F(218, 22475))
check(F(1, 5) - F(49, 289) == F(44, 1445))
check(F(29, 20) < U / 2 < F(31, 20))
check(F(29, 20) * F(99, 100) > 1)

T = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
normals = [(F(a), F(b)) for a in range(-7, 8) for b in range(-7, 8)
           if a or b]
profiles = 0
for h in (F(1, 10000), F(1, 20000), F(1, 100000), F(1, 1000000)):
    for k in (h / 100, h, F(1, 100), F(1, 10), F(1, 3), F(1, 2), (1+h)/2):
        profiles += 1
        p = (1+h-k, k)
        outer_b = 1 + h/(1-k)
        original_q = [(F(0), F(0)), (F(1), F(0)), p, (F(0), F(1))]
        original_s = [(F(0), F(0)), (outer_b, F(0)), (F(0), F(1))]
        tau, r1, r2 = h*k/(1+h-k), h/(1+h-k), k
        check(area(original_q) == (1+h)/2)
        check(1 - area(original_q)/area(original_s) == tau)
        check(tau == r1*r2)
        check(0 < tau <= h <= eps)
        check(0 < r1 <= 2*h/(1+h) < F(1, 100))
        check(0 < r2 < F(51, 100))
        # The line through e1,p cuts exactly the missing corner from S.
        check(area(clip(original_s, k, k-h, k)) == tau*area(original_s))
        check(area(clip(original_q, k, k-h, k)) == 0)
        q = [(r1, F(0)), (F(1), F(0)), (F(0), F(1)), (F(0), r2)]
        removed = [(F(0), F(0)), (r1, F(0)), (F(0), r2)]
        check(area(q) == (1-tau)/2)
        check(area(removed) == tau/2)
        lam = (F(1, 3)-9*tau/20, F(1, 3)+3*tau/10, F(1, 3)+3*tau/20)
        check(sum(lam) == 1)
        check(all(F(1, 3)-eps <= v <= F(1, 3)+eps for v in lam))
        check(lam[1] > r1)
        budgets = (4*lam[1]*lam[2]-tau, 4*lam[0]*lam[2],
                   4*lam[0]*lam[1]-tau/5)
        identities = (G-2*tau/5+9*tau*tau/50,
                      G-2*tau/5-27*tau*tau/100,
                      G-2*tau/5-27*tau*tau/50)
        check(budgets == identities)
        low = identities[2]
        check(min(budgets) == low)
        check(low/(1-tau)-G-tau/45 == tau*(10-233*tau)/(450*(1-tau)))
        check(low/(1-tau) >= G+tau/45)
        check(area(clip(removed, F(0), F(1), F(3, 10))) <= tau/10)
        y = (lam[1], lam[2])
        for a, b in normals:
            threshold = a*y[0]+b*y[1]
            actual = area(clip(q, a, b, threshold))
            check(actual >= low/2)
            full = area(clip(T, a, b, threshold))*2
            if full <= G+eps:
                verts = [a*x+b*y0 >= threshold for x, y0 in T]
                check(sum(verts) == 1)
                i = verts.index(True)
                vtx = T[i]
                coeff = [(a*vtx[0]+b*vtx[1]-a*x-b*y0)/(a*vtx[0]+b*vtx[1]-threshold)
                         for j, (x, y0) in enumerate(T) if j != i]
                check(all(F(29, 20) < v < F(31, 20) for v in coeff))
                loss = area(clip(removed, a, b, threshold))*2
                check(loss <= (tau, F(0), tau/5)[i])

for delta in [F(1, 240000*q) for q in range(1, 101)]:
    hbound = (20*delta+16*delta*delta)/(1-12*delta)
    check((1-6*delta)**2-(6*delta)**2 == 1-12*delta)
    check((1+4*delta)**2/(1-12*delta)-1 == hbound)
    check(hbound <= 24*delta <= eps)

print(f"PASS: {checks} exact checks; {profiles} quadrilaterals; "
      f"{len(normals)} through-point directions per quadrilateral.")
