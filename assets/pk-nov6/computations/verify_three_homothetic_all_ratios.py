"""Exact scalar and actual triangular-cap diagnostics for three homothetic fibers."""
from fractions import Fraction as F
from itertools import product


scalar_checks = 0
for d in range(2, 21):
    gamma = F(d,d+1)**d
    assert gamma <= F(1,2)
    for lam in (F(1),F(5,4),F(3,2),F(2),F(3),F(7)):
        for numerator in range(31):
            t = F(numerator,60)
            assert (1-2*t)**d >= (1+lam**d-(lam+t)**d)/2
            scalar_checks += 1
assert 2*(1-2*F(1,3))**2+(1+F(1,3))**2 == 2
# Dimension one is explicitly excluded from that scalar theorem.
assert 2*(1-2*F(2,5))+(1+F(2,5)) < 2

radius_checks = 0
for d in range(2, 9):
    gamma = F(d,d+1)**d
    for r,s,R in product((F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(2)), repeat=3):
        if r > s or 2*R < r+s:
            continue
        target = gamma*(r**d+R**d+s**d)/2
        alpha = 2*R-r-s
        assert alpha >= 0
        if R**d >= r**d+s**d:
            assert gamma*R**d >= target
        elif s**d >= r**d+R**d:
            assert gamma*s**d >= target
        elif R <= s:
            assert r <= 2*R-s <= R
            assert gamma*R**d+r**d/2 >= target
        else:
            eps = R-s
            assert 0 < 2*eps < r
            inner = r-2*eps
            assert alpha+inner == s
            deficit = r**d+s**d-R**d
            assert deficit > 0
            assert inner**d >= deficit/2 >= gamma*deficit
            payment = gamma*R**d+inner**d/2
            assert payment-target >= (1-2*gamma)*deficit/4 > 0
        radius_checks += 1


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(poly, poly[1:]+poly[:1])))/2


def clip(poly, u, threshold):
    if not poly:
        return []
    out = []
    for p,q in zip(poly, poly[1:]+poly[:1]):
        vp = u[0]*p[0]+u[1]*p[1]-threshold
        vq = u[0]*q[0]+u[1]*q[1]-threshold
        if vp >= 0:
            out.append(p)
        if (vp < 0 < vq) or (vq < 0 < vp):
            t = vp/(vp-vq)
            out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return out


K = [(F(-1,3),F(-1,3)),(F(2,3),F(-1,3)),(F(-1,3),F(2,3))]
V = area(K)
assert V == F(1,2)
def body(radius, c=(F(0),F(0))):
    return [(c[0]+radius*p[0],c[1]+radius*p[1]) for p in K]


normals = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(2,-1),(-1,2)]
tilts = [F(k,3) for k in range(-12,13)]
triangles = [(F(1),F(1),F(4,3)), (F(1,2),F(1),F(11,10)),
             (F(1,4),F(1),F(101,100)), (F(3,4),F(1),F(6,5)),
             (F(1,2),F(1),F(4,5)), (F(1,2),F(1),F(3,4)),
             (F(1),F(1),F(3,2)), (F(1,4),F(2),F(5,4))]
cap_checks = 0
for r,s,R in triangles:
    assert r <= s and 2*R >= r+s
    alpha = 2*R-r-s
    target = F(4,9)*V*(r*r+R*R+s*s)/2
    candidate = 1 if s*s >= r*r+R*R else 0
    for k0 in K+[(F(0),F(0))]:
        c = (alpha*k0[0],alpha*k0[1])
        source = {-1:body(r,c),0:body(R),1:body(s)}
        if s < R and R*R < s*s+r*r:
            inner = r-2*(R-s)
            for x,y in body(inner,c):
                assert x >= -s/3 and y >= -s/3 and x+y <= s/3
        for u,a in product(normals,tilts):
            captured = sum(area(clip(poly,u,-a*(z-candidate)))
                           for z,poly in source.items())
            assert captured >= target
            if candidate == 0 and R >= s:
                assert area(clip(body(R),u,0))-area(clip(body(s),u,0)) == (R*R-s*s)*area(clip(K,u,0))
            cap_checks += 1
        for sign in (-1,1):
            vertical = sum(area(poly) for z,poly in source.items()
                           if sign*(z-candidate) >= 0)
            assert vertical >= target

print(f"PASS: {scalar_checks} exact scalar checks, {radius_checks} radius cases, {cap_checks} actual triangular caps, and vertical caps")
