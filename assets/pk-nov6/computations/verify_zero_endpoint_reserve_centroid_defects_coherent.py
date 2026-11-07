"""Exact rational certificates for two actual three-fiber reserve obstructions."""
from fractions import Fraction as F
from itertools import combinations, product

checks = 0
def check(value):
    global checks
    assert value
    checks += 1

def polygon_area_centroid(poly):
    twice_area = F(0)
    moments = [F(0), F(0)]
    for a, b in zip(poly, poly[1:]+poly[:1]):
        cross = a[0]*b[1]-a[1]*b[0]
        twice_area += cross
        for j in range(2):
            moments[j] += (a[j]+b[j])*cross
    check(twice_area > 0)
    return twice_area/2, tuple(x/(3*twice_area) for x in moments)

T = [(F(0),F(0)), (F(1),F(0)), (F(0),F(1))]
Q = [(F(0),F(0)), (F(1),F(0)), (F(1),F(1)), (F(0),F(1))]
A2 = [(F(0),F(0)),(F(1),F(0)),(F(1),F(1,2)),
      (F(1,2),F(1)),(F(0),F(1))]
areas, centroids = zip(*(polygon_area_centroid(x) for x in (T,A2,Q)))
check(areas == (F(1,2),F(7,8),F(1)))
check(centroids == ((F(1,3),F(1,3)),(F(19,42),F(19,42)),(F(1,2),F(1,2))))
check(tuple(centroids[1][j]-(centroids[0][j]+centroids[2][j])/2
            for j in range(2)) == (F(1,28),F(1,28)))
check(sum(areas) == F(19,8))
check(all(2*x < sum(areas) for x in areas))
dot = lambda a,b: sum(x*y for x,y in zip(a,b))
support = lambda vertices,u: max(dot(x,u) for x in vertices)
normsT = [(-1,0),(0,-1),(1,1)]
normsQ = [(-1,0),(0,-1),(1,0),(0,1)]
for u in set(normsT+normsQ):
    check(2*support(A2,u) == support(T,u)+support(Q,u))
for a,b in product(T,Q):
    midpoint = tuple((a[j]+b[j])/2 for j in range(2))
    check(all(F(0)<=s<=F(1) for s in midpoint))
    check(sum(midpoint) <= F(3,2))
for a in A2:
    check(any(tuple((x[j]+y[j])/2 for j in range(2)) == a
              for x,y in product(T,Q)))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def determinant(a,b,c):
    return dot(a,cross(b,c))
t = F(1,10)
eps = F(1,1000)
gens = [(F(1),F(0),F(0)), (F(0),F(1),F(0)), (F(0),F(0),F(1)),
        (F(1),t,F(0)), (F(0),F(1),t), (t,F(0),F(1))]
u = (F(0),-t,F(1))
c = (F(-9,40),F(-11,40),F(1,2))
v = tuple(c[j]+eps*u[j] for j in range(3))
check(v == (F(-9,40),F(-2751,10000),F(501,1000)))
hA = lambda n: sum(abs(dot(n,g)) for g in gens)/4
h0 = lambda n: sum(abs(x) for x in n)/2
h2 = lambda n: sum(abs(dot(n,g)) for g in gens[3:])/2
h1 = lambda n: max(hA(n),dot(n,v))
expected_slacks = [24000,249900,2400,-1010,249900,300000,
                   24000,30000,252400,274900,300000,24990,
                   1490,280160,249899]
violations = []
for (i,j), expected in zip(combinations(range(6),2),expected_slacks):
    n = cross(gens[i],gens[j])
    check(n != (0,0,0))
    check(F(10**6)*(hA(n)-abs(dot(n,v))) == expected)
    for sign in (-1,1):
        r = tuple(sign*x for x in n)
        if dot(r,v)>hA(r):
            violations.append((i,j,sign))
        # Every finite Minkowski-sum generator point satisfies the listed planes.
        for signs in product((-1,1), repeat=6):
            x = tuple(sum(F(signs[k],4)*gens[k][l] for k in range(6))
                      for l in range(3))
            check(dot(r,x) <= hA(r))
check(violations == [(0,4,1)])
check(cross(gens[0],gens[4]) == u)
check(dot(u,c) == hA(u) == F(211,400))
check(dot(u,v)-hA(u) == F(101,100000))
check([i for i,g in enumerate(gens) if dot(u,g)==0] == [0,4])
face_center = tuple(sum((1 if dot(u,g)>0 else -1)*g[j]/4
                        for g in gens if dot(u,g)!=0)
                    for j in range(3))
check(face_center == c)

# Every endpoint facet remains at exactly its original Minkowski support value.
for I, own, other in ((range(3),h0,h2),(range(3,6),h2,h0)):
    for i,j in combinations(I,2):
        n = cross(gens[i],gens[j])
        for sign in (-1,1):
            r = tuple(sign*x for x in n)
            check(dot(r,v) < hA(r))
            check(2*h1(r)-other(r) == own(r))

expected_dets = [1000,0,100,1000,100,1000,0,10,100,1000,
                 1000,0,100,100,1000,10,1000,10,100,1001]
dets = [abs(determinant(*(gens[i] for i in I)))
        for I in combinations(range(6),3)]
check([1000*x for x in dets] == expected_dets)
VA = sum(dets)/8
check(VA == F(8631,8000))
added = abs(determinant(tuple(x/2 for x in gens[0]),
                        tuple(x/2 for x in gens[4]),
                        tuple(eps*x for x in u)))/3
check(added == F(101,1200000))
gadd = tuple(c[j]+eps*u[j]/4 for j in range(3))
check(gadd == (F(-9,40),F(-11001,40000),F(2001,4000)))
check(dot(u,gadd) == F(211101,400000)>0)
V1 = VA+added
check(V1 == F(1294751,1200000))
check(added/V1 == F(101,1294751))
V2 = abs(determinant(*gens[3:]))
check(V2 == F(1001,1000))
total = 1+V1+V2
check(total == F(3695951,1200000))
check(all(2*x < total for x in (F(1),V1,V2)))

# Exact occupied-parity and no-heavy arithmetic after binary base padding.
for n in range(1,7):
    bases = [(j,)+b for j in range(3) for b in product((0,1), repeat=n-1)]
    check(len(bases) == 3*2**(n-1))
    check(len({tuple(x%2 for x in p) for p in bases}) == 2**n)
    check(total*2**(n-1)/2**n == total/2)
    check(sum(areas)*2**(n-1)/2**n == sum(areas)/2)
print(f"PASS: {checks} exact support, centroid, volume, reserve, and padding checks")
