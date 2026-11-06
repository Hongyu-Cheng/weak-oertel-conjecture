"""Exact lattice enumeration, component, rank, and finite Helly certificate."""
from fractions import Fraction as F
from itertools import combinations, product

a, b, d, f, h = (0,0,1), (0,0,3), (0,2,1), (1,2,0), (2,0,0)
vertices = [a,b,d,f,h]
points = [(0,0,1),(0,0,2),(0,0,3),(0,1,1),(0,1,2),
          (0,2,1),(1,0,1),(1,2,0),(2,0,0)]


def allowed(p):
    x,y,z=p
    return (2*x+y+4*z>=4 and x+z>=1 and x>=0 and y>=0
            and x+y+z<=3 and 6*x+3*y+4*z<=12)


assert all(allowed(p) for p in vertices)
assert [p for p in product(range(3),range(3),range(4)) if allowed(p)] == points


def barycentric(S,p):
    """Nonnegative coordinates for an affinely independent S, or None."""
    n=len(S)
    mat=[[F(1)]*n+[F(1)]]+[
        [F(v[j]) for v in S]+[F(p[j])] for j in range(3)]
    k=0
    for col in range(n):
        pivot=next((i for i in range(k,4) if mat[i][col]),None)
        if pivot is None:
            return None
        mat[k],mat[pivot]=mat[pivot],mat[k]
        q=mat[k][col]
        mat[k]=[x/q for x in mat[k]]
        for i in range(4):
            if i!=k:
                q=mat[i][col]
                mat[i]=[x-q*y for x,y in zip(mat[i],mat[k])]
        k+=1
    if any(not any(row[:n]) and row[n] for row in mat):
        return None
    ans=[mat[i][n] for i in range(n)]
    return ans if min(ans)>=0 else None


assert barycentric([a,b],points[1]) == [F(1,2)]*2
assert barycentric([a,d],points[3]) == [F(1,2)]*2
assert barycentric([b,d],points[4]) == [F(1,2)]*2
assert barycentric([a,b,h],points[6]) == [F(1,4),F(1,4),F(1,2)]

# Check all vertices are exposed by the claimed functionals.
functionals = [(-1,-1,-1),(0,0,1),(-1,2,0),(1,2,0),(1,0,0)]
for v,u in zip(vertices,functionals):
    dot=lambda p:sum(x*y for x,y in zip(u,p))
    assert all(dot(v)>dot(w) for w in vertices if w!=v)

# Exact minimal faces and their full integer traces.
faces = [[p for p in points if p[0]==0 and p[1]==0],
         [p for p in points if p[0]==0 and p[0]+p[2]==1],
         [p for p in points if p[0]==0 and sum(p)==3],
         [p for p in points if p[1]==0]]
parent={p:p for p in points}
def find(p):
    while parent[p]!=p:
        parent[p]=parent[parent[p]]
        p=parent[p]
    return p
for face in faces:
    for p in face[1:]:
        parent[find(p)]=find(face[0])
components={}
for p in points:
    components.setdefault(find(p),set()).add(p)
assert {frozenset(c) for c in components.values()} == {
    frozenset(points)-{f},frozenset({f})}

u=tuple(b[i]-a[i] for i in range(3))
v=tuple(d[i]-a[i] for i in range(3))
w=tuple(h[i]-a[i] for i in range(3))
det=(u[0]*(v[1]*w[2]-v[2]*w[1])
     -u[1]*(v[0]*w[2]-v[2]*w[0])
     +u[2]*(v[0]*w[1]-v[1]*w[0]))
assert det==-8
assert 2**3+2**0==9>2**3

# Exact convex closures of all subsets, by Caratheodory plus rational solves.
supports=[[] for p in points]
for size in range(1,5):
    for inds in combinations(range(len(points)),size):
        mask=sum(1<<i for i in inds)
        S=[points[i] for i in inds]
        for j,p in enumerate(points):
            if barycentric(S,p) is not None:
                supports[j].append(mask)
closures=[sum(1<<j for j,L in enumerate(supports)
              if any(mask&s==s for s in L))
          for mask in range(1<<len(points))]

def helly(universe):
    best=0
    witness=0
    for W in range(1,1<<len(points)):
        if W&universe!=W:
            continue
        intersection=universe
        for j in range(len(points)):
            if W>>j&1:
                intersection &= closures[W^(1<<j)]
        size=bin(W).count('1')
        if not intersection and size>best:
            best,witness=size,W
    return best,[points[i] for i in range(len(points)) if witness>>i&1]

all_points=(1<<len(points))-1
assert helly(all_points^(1<<7)) == (5,[points[i] for i in [0,1,3,4,6]])
assert helly(1<<7)[0]==1
assert helly(all_points) == (6,[points[i] for i in [0,1,3,4,6,7]])
print('PASS: nine lattice points; component ranks 3,0; rank cost 9>8; '
      'exact Helly values 5,1 and 6')
