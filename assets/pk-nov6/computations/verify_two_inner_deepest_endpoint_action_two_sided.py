"""Exact checks supplementary to the analytic four-fiber theorem."""
from fractions import Fraction as F
from itertools import product

checks = 0
def check(p):
    global checks
    assert p
    checks += 1

g = (F(1, 3), F(1, 3))
A = ((F(1,5), F(3,10)), (F(17,60), F(23,60)))
C = ((F(2,5), F(3,5)), (F(37,120), F(43,120)))
corners = lambda rect: list(product(*rect))
area = lambda rect: (rect[0][1]-rect[0][0])*(rect[1][1]-rect[1][0])
check(area(A) == area(C) == F(1,100))
for rect in (A,C):
    for x,y in corners(rect):
        check(0 < x < F(2,3))
        check(0 < y < F(2,3))
        check(F(1,3) < x+y < 1)
    check(not (rect[0][0] <= g[0] <= rect[0][1]
               and rect[1][0] <= g[1] <= rect[1][1]))

T = [(F(0),F(0)), (F(1),F(0)), (F(0),F(1))]
fibers = [corners(A), T, T, corners(C)]
normals = [(F(1),F(0)), (F(0),F(1)), (F(-1),F(-1))]
for source, tilt in ((1,F(-10)),(2,F(10))):
    for u in normals:
        for z in range(4):
            margins = [u[0]*(x-g[0])+u[1]*(y-g[1])+tilt*(z-source)
                       for x,y in fibers[z]]
            if z == source:
                check(min(margins)<0<max(margins))
            elif z == (0 if source == 1 else 3):
                check(min(margins)>0)
            else:
                check(max(margins)<0)

q,V,a = F(2,9),F(1,2),F(1,100)
Q,M = q+a,2*(V+a)
check(Q == F(209,900))
check(M == F(51,50))
check(Q/M == F(209,918))
check(Q/M-F(2,9) == F(5,918))
for volume in (a,V,V,a):
    check(volume<M/2)

# Exact nested contractions keep both endpoint areas equal and every
# canonical cap status strict.  Actual all-normal optimality is analytic.
for denom in range(1,41):
    t = F(1,denom)
    at = a*t*t
    beta = (q+at)/(2*(V+at))
    check(beta > F(2,9))
    check(beta <= Q/M)
    check(beta-F(2,9) == at*(1-F(4,9))/(2*(V+at)))
    for rect, z in ((A,0),(C,3)):
        center = tuple((l+h)/2 for l,h in rect)
        moved = [tuple(center[k]+t*(p[k]-center[k]) for k in range(2))
                 for p in corners(rect)]
        for p in moved:
            check(all(rect[k][0]<=p[k]<=rect[k][1] for k in range(2)))
            for source, tilt in ((1,F(-10)),(2,F(10))):
                for u in normals:
                    margin = sum(u[k]*(p[k]-g[k]) for k in range(2))+tilt*(z-source)
                    check(margin>0 if z==(0 if source==1 else 3) else margin<0)

for d in range(1,31):
    # Each exact radial endpoint flux has mass d*a.  Both groups receive
    # one endpoint and miss the other, for arbitrary normalized weights.
    check((d*a)/(2*d*a) == F(1,2))
    check(-d*a*(V-q)/(2*(V+a)**2)<0)

print(f"{checks} exact checks PASS")
