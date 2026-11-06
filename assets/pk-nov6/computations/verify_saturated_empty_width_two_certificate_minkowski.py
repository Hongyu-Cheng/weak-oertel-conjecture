"""Independent short exact certificate; no floating-point geometry."""
from itertools import product

P = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),
     (2,2,3,5),(1,3,5,5),(0,0,0,2),(1,2,4,5),
     (1,1,2,3),(0,1,1,1),(0,1,3,2),(1,2,3,4),
     (0,1,2,1),(1,1,2,2),(1,1,1,2),(1,2,3,3)]
normals = [(22,-2,-2,-8),(2,36,-19,-4),(4,-16,6,-2),(-2,-2,-2,-1),
           (16,10,-10,3),(-15,17,-3,2),(-14,-2,-16,17),(2,-14,6,3),
           (7,-24,7,4),(-17,6,-2,3),(-10,-7,6,2),(-8,14,-11,7),
           (3,7,5,-9),(7,-5,6,-3),(6,6,-11,3),(15,15,3,-12)]
gaps = [20,23,2,1,15,13,17,3,1,1,5,1,1,1,1,3]
rows = [(3,3,2,-4,3),(1,-6,2,1,2),(-3,6,-5,3,6),
        (-10,3,-1,2,4),(2,1,-3,1,2),(3,-3,3,-1,4),(-1,-1,-1,-1,-1)]
checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def det(a):
    if not a:
        return 1
    return sum((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]])
               for j in range(len(a)))

check(len(set(P)) == 16)
check(len({tuple(x % 2 for x in p) for p in P}) == 16)
check(det([[P[i][j]-P[0][j] for j in range(4)] for i in (1,2,3,4)]) == -11)
for p,n,gap in zip(P,normals,gaps):
    check(min(dot(n,p)-dot(n,q) for q in P if q != p) == gap > 0)
    for row in rows:
        check(dot(row[:4],p) <= row[4])

found = set()
for x,y,z in product(range(3),range(4),range(6)):
    # Exact ceilings and floors, including negative numerators.
    L = max(0, -(-(3*x+3*y+2*z-3)//4), 3*x-3*y+3*z-4, 1-x-y-z)
    U = min(5, 2-x+6*y-2*z, (6+3*x-6*y+5*z)//3,
            (4+10*x-3*y+z)//2, 2-2*x-y+3*z)
    interval = set(range(L,U+1))
    direct = {w for w in range(6) if all(dot(row[:4],(x,y,z,w)) <= row[4] for row in rows)}
    check(interval == direct)
    found.update((x,y,z,w) for w in direct)
check(found == set(P))
check(max(p[0] for p in P)-min(p[0] for p in P) == 2)
sums = {dot((2,2,3,5),bits) for bits in product((0,1),repeat=4)}
check(not ({1,11} & sums))
print(f"PASS: {checks} exact exposure, seven-inequality emptiness, and width-certificate checks")
