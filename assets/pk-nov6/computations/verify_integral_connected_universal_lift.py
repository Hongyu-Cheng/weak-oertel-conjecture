"""Exact graph-lattice check for the archived connected recession example."""

from itertools import product, combinations
import sympy as sp

P = [(0,0,1),(0,0,2),(0,0,3),(0,1,1),(0,1,2),(0,1,3),(0,2,1),
     (1,0,0),(1,0,1),(1,1,0),(1,1,1),(1,2,0),(2,0,0)]
g = [0,0,0,3,3,3,6,0,0,0,1,0,0]
facets = [((-1,0,-1),-1),((-1,0,0),0),((0,-1,0),0),((0,0,-1),0),
          ((1,2,1),5),((2,1,1),4),((3,0,2),6)]

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

assert [p for p in product(range(3),range(3),range(4))
        if all(dot(u,p)<=h for u,h in facets)] == P
assert all(any(dot(u,p)==h for u,h in facets) for p in P)

# Every anchored representation stays on the anchor's minimal face.
# Requiring g to be affine on those faces is exact, and gives all
# linear relations defining L(P).
rows = []
adjacency = [set([i]) for i in range(len(P))]
for p in P:
    active = [(u,h) for u,h in facets if dot(u,p)==h]
    face = [i for i,w in enumerate(P) if all(dot(u,w)==h for u,h in active)]
    base_matrix = sp.Matrix([[1,*P[i]] for i in face])
    augmented = sp.Matrix([[1,*P[i],g[i]] for i in face])
    assert augmented.rank() == base_matrix.rank()
    for rel in base_matrix.T.nullspace():
        row = [sp.Integer(0)] * len(P)
        for i,c in zip(face,rel):
            row[i] = c
        rows.append(row)
    if len(face)>1:
        for i in face:
            adjacency[i].update(face)

assert len(P)-sp.Matrix(rows).rank() == 5
reached = {0}
while True:
    expanded = set().union(*(adjacency[i] for i in reached))
    if expanded == reached:
        break
    reached = expanded
assert reached == set(range(len(P)))
assert sp.Matrix([[1,*p] for p in P]).rank() == 4
assert sp.Matrix([[1,*p,t] for p,t in zip(P,g)]).rank() == 5

# The displayed affine dependence witnesses the nonaffine mode.
b,c,e,f = 2,5,7,11
assert sp.Matrix(P[c]) == sp.Matrix(P[b])-sp.Matrix(P[e])/2+sp.Matrix(P[f])/2
assert g[c]-g[b]+sp.Rational(g[e]-g[f],2) == 3

# Enumerate integer points in the lifted hull with exact rational
# barycentric coordinates.  Nonvertex base points lift into their
# original vertex faces by the face-affinity check above.
vertex_indices = [0,2,5,6,7,11,12]
lifted = [(*p,t) for p,t in zip(P,g)]
inverse_bases = []
for indices in combinations(vertex_indices,5):
    matrix = sp.Matrix.hstack(*(sp.Matrix([1,*lifted[i]]) for i in indices))
    if matrix.det() != 0:
        inverse_bases.append(matrix.inv())
assert inverse_bases

def in_lifted_hull(point):
    augmented = sp.Matrix([1,*point])
    return any(all(c>=0 for c in inv*augmented) for inv in inverse_bases)

actual_integer_points = set()
for p in P:  # Any integer point in the lift projects to the original Q.
    for height in range(7):
        point = (*p,height)
        if in_lifted_hull(point):
            actual_integer_points.add(point)
assert actual_integer_points == set(lifted)

print("PASS: connected L-dimension 5, nonaffine mode, and exact lattice-convex integral lift in Z^4")
