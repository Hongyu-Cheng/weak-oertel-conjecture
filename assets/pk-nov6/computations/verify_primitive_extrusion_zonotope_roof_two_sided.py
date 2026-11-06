from fractions import Fraction as F
from itertools import product, combinations
from math import gcd, isqrt

checks = 0

def check(value):
    global checks
    assert value
    checks += 1

def floor(x):
    return x.numerator // x.denominator

def ceil(x):
    return -floor(-x)

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def contains(poly, p):
    if len(poly) == 1:
        return p == poly[0]
    if len(poly) == 2:
        a,b = poly
        return (cross(a,b,p) == 0 and
                all(min(a[q],b[q]) <= p[q] <= max(a[q],b[q]) for q in (0,1)))
    return all(cross(poly[i],poly[(i+1)%len(poly)],p) >= 0 for i in range(len(poly)))

def lattice_count(poly):
    lo = [ceil(min(p[q] for p in poly)) for q in (0,1)]
    hi = [floor(max(p[q] for p in poly)) for q in (0,1)]
    return sum(contains(poly,(F(i),F(j)))
               for i in range(lo[0],hi[0]+1)
               for j in range(lo[1],hi[1]+1))

def quotient_count(poly, v):
    c = gcd(abs(v[0]),abs(v[1]))
    if c == 0:
        return 0
    normal = (-v[1]//c, v[0]//c)
    values = [normal[0]*p[0]+normal[1]*p[1] for p in poly]
    return floor(max(values))-ceil(min(values))+1

def add_segments(poly, directions, lengths):
    pts = poly
    for v,k in zip(directions,lengths):
        pts = hull(pts+[(p[0]+k*v[0],p[1]+k*v[1]) for p in pts])
    return pts

def predicted(poly, directions, lengths):
    answer = lattice_count(poly)
    for v,k in zip(directions,lengths):
        answer += k*gcd(abs(v[0]),abs(v[1]))*quotient_count(poly,v)
    for i,j in combinations(range(len(directions)),2):
        a,b = directions[i], directions[j]
        answer += abs(a[0]*b[1]-a[1]*b[0])*lengths[i]*lengths[j]
    return answer

polys = [
    [(F(0),F(0))],
    [(F(1,5),F(1,5)),(F(4,5),F(1,5)),(F(4,5),F(4,5)),(F(1,5),F(4,5))],
    [(F(-2,3),F(1,4)),(F(7,3),F(-1,2)),(F(1,5),F(8,3))],
    [(F(-1),F(-1)),(F(2),F(-1)),(F(1),F(2)),(F(-1),F(1))],
]
families = [
    [(1,0),(0,1)],
    [(1,0),(1,2)],
    [(1,0),(1,2),(2,0)],
    [(2,0),(0,3),(1,1)],
    [(0,0),(1,2),(-1,-2)],
]
for poly in polys:
    poly = hull(poly)
    for vs in families:
        for ks in product(range(4),repeat=len(vs)):
            check(lattice_count(add_segments(poly,vs,ks)) == predicted(poly,vs,ks))

# Exact one-dimensional count, including initially empty lattice intervals.
for aa in range(-8,9):
    for bb in range(aa,9):
        a,b = F(aa,3),F(bb,3)
        old = floor(b)-ceil(a)+1
        check(old >= 0)
        for k in range(7):
            new = list(range(ceil(a),floor(b)+k+1))
            old_points = list(range(ceil(a),floor(b)+1))
            roof = [floor(b)+r for r in range(1,k+1)]
            check(new == old_points+roof)
            check(len(new) == old+k)

# A genuine variable-fiber n=2,d=1 simplex and two integer segments.
# C={(z1,z2,x)>=0:z1+z2+x<=L}; after coordinate extrusion the
# continuous fiber length is L-max(z1-k1,0)-max(z2-k2,0), if positive.
for L in (F(7,3),F(3),F(17,4)):
    def mixed_simplex(k1,k2):
        return sum(max(F(0),L-max(i-k1,0)-max(j-k2,0))
                   for i in range(floor(L)+k1+1)
                   for j in range(floor(L)+k2+1))
    original = mixed_simplex(0,0)
    quotient = sum(max(F(0),L-j) for j in range(floor(L)+1))
    for k1,k2 in product(range(6),repeat=2):
        check(mixed_simplex(k1,k2) == original+(k1+k2)*quotient+k1*k2*L)

# Roof masses and tangent-cap index identity use exact rational endpoints.
for N in (1,2,3,7,16,31,64):
    widths = [F(2*j-1,N*N) for j in range(1,N+1)]
    check(sum(widths) == 1)
    old_mass = sum(F(1)-F(j*j,N*N) for j in range(N+1))
    check(old_mass == F((N+1)*(4*N-1),6*N))
    for j0 in range(1,N+1):
        for lam in (F(0),F(1,3),F(1,2),F(1)):
            x0 = F((j0-1)**2,N*N)+lam*widths[j0-1]
            mass = F(0)
            for j in range(1,N+1):
                low,high = F((j-1)**2,N*N),F(j*j,N*N)
                cut = x0+F(2*j0*(j-j0),N*N)
                captured = max(F(0),min(high,cut)-low)
                if captured > 0:
                    check((j-j0-1)**2 <= 2*j0)
                mass += captured
            integer_radius = isqrt(2*N)+1
            check(mass <= F((2*integer_radius+1)*2,N))

N = 4096
check(2*N < 91**2)
check(F(366,N) == F(183,2048))
check(F(183,2048) < F(1,4))
check(F(183,2048) < F(1,6))

# Exact discrete optimization of the retained boundary-depth formula.
for N in range(1,15):
    Q = F(3,7)
    for L,R in product((F(0),F(1,5),F(2),F(4)),repeat=2):
        crossing = F(N-1,2)+(R-L)/(2*Q)
        direct = max(min((j+1)*Q+L,(N-j)*Q+R) for j in range(N))
        dist = min(abs(crossing-j) for j in range(N))
        check(direct == ((N+1)*Q+L+R)/2-Q*dist)
        if abs(R-L) <= (N-1)*Q:
            check(direct >= (N*Q+L+R)/2)

print(f'PASS: {checks} exact primitive-extrusion, zonotope, roof and depth-budget checks')
