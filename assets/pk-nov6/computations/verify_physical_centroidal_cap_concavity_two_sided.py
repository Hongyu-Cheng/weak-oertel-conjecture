"""Exact supplementary checks; the general theorem is proved in the note."""
from fractions import Fraction as F
import sympy as sp

checks = 0

def check(claim):
    global checks
    assert claim
    checks += 1

def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def hull(points):
    pts = sorted(set(points))
    lo, hi = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2],lo[-1],p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2],hi[-1],p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

def area_centroid(poly):
    a2 = sx = sy = F(0)
    for p,q in zip(poly, poly[1:]+poly[:1]):
        cr = p[0]*q[1]-p[1]*q[0]
        a2 += cr
        sx += (p[0]+q[0])*cr
        sy += (p[1]+q[1])*cr
    return a2/2, (sx/(3*a2),sy/(3*a2))

def upper_clip(poly):
    out = []
    for p,q in zip(poly, poly[1:]+poly[:1]):
        if p[1] >= 0:
            out.append(p)
        if (p[1] < 0 < q[1]) or (q[1] < 0 < p[1]):
            t = -p[1]/(q[1]-p[1])
            out.append((p[0]+t*(q[0]-p[0]),F(0)))
    return hull(out)

D = hull([(F(0),F(1)),(F(-1),F(0)),(F(1),F(0))])
K1 = hull([(F(0),F(1)),(F(-2),F(-1)),(F(2),F(-1))])
K2 = hull([(F(0),F(1)),(F(-2),F(-1)),(F(3,2),F(-1)),(F(3,2),F(-1,2))])
check(area_centroid(D) == (1,(0,F(1,3))))
check(area_centroid(K1)[0] == 4)
check(area_centroid(K2)[0] == F(31,8))
check(len(K1) == 3 and len(K2) == 4)
for den in range(2,41):
    for num in range(1,den):
        lam = F(num,den)
        M = hull([((1-lam)*p[0]+lam*q[0],(1-lam)*p[1]+lam*q[1])
                  for p in K1 for q in K2])
        check(upper_clip(M) == D)
        check(all(abs(x) <= 1-t for x,t in M))

t, d = sp.symbols('t d', positive=True)
f = t*(d+1-d*t)**(1/d)
claimed = -(d+1)*(2-t)*(d+1-d*t)**(1/d-2)
check(sp.simplify(sp.diff(f,t,2)-claimed) == 0)
for dim in range(1,21):
    for num in range(1,40):
        t0 = F(num,40)
        T = t0**dim
        E = T*(dim+1-dim*t0)
        check(T < E < (dim+1)*T)
        check(F(dim+1)*(2-t0) > 0)

P = [(0,0),(1,0),(0,1),(1,1)]
c = {(0,0):F(0),(1,0):F(0),(0,1):F(0),(1,1):F(1)}
check(c[(0,0)]+c[(1,1)] != c[(1,0)]+c[(0,1)])
for p in P:
    ell = lambda z: sum((1 if p[j] else -1)*(z[j]-p[j]) for j in (0,1))
    check(all(ell(z) <= -1 for z in P if z != p))
    for a in (F(-1),F(1)):
        # Halfspace a*(x-cp)+4*ell(z)>=0 isolates p and its own half.
        check(all(a*(c[z]-c[p])+1+4*ell(z) < 0 for z in P if z != p))

print(f'PASS: {checks} exact checks')
