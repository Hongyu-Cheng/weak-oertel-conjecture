"""Exact checks for reflected guards, barycenter coupling, and its obstruction."""
from fractions import Fraction as F
from itertools import product
import sympy as s

checks=0
def check(a,b):
    global checks
    assert s.simplify(a-b)==0,(a,b)
    checks+=1
def dot(a,b):return sum(x*y for x,y in zip(a,b))

P=[(0,0),(1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,1)]
found=[z for z in product(range(-1,2),repeat=2) if abs(z[0]-z[1])<=1]
assert set(P)==set(found); checks+=1
verts=[(F(2),F(-1)),(F(-1),F(2)),(F(-1),F(-1))]
bases=[(1,0),(0,1),(-1,-1)]
sigma=F(1,100)
normals=[(1,0),(0,1),(-1,-1)]
tilts=[(0,0),(10,-10),(10,0)]
expected=[{(1,0),(-1,0)},{(1,0),(0,-1)},{(1,0),(1,1)}]
for u,a,captured in zip(normals,tilts,expected):
    for p,vertex in zip(bases,verts):
        dverts=[tuple((1-sigma)*v+sigma*x for v,x in zip(vertex,w)) for w in verts]
        for sign in [-1,1]:
            z=tuple(sign*q for q in p)
            margins=[dot(a,z)+dot(u,x) for x in dverts]
            assert (min(margins)>F(9,10)) if z in captured else (max(margins)<-F(9,10))
            checks+=1

for z in P:check(max(0,2*z[0]-z[1]-1),1 if z==(1,0) else 0)
for i in range(7):
    for j in range(7-i):
        lam=[F(i,6),F(j,6),F(6-i-j,6)]
        permuted=[tuple(sum(lam[k]*verts[(k+shift)%3][coord] for k in range(3)) for coord in range(2)) for shift in range(3)]
        for coord in range(2):check(sum(x[coord] for x in permuted),0)
        for coord in range(2):
            check(sum((1-sigma)*verts[k][coord]+sigma*permuted[k][coord] for k in range(3)),0)

t=s.symbols('t',real=True)
check(s.integrate((t-1)**2*s.Rational(2,9)*(2-t)/4,(t,1,2)),s.Rational(1,216))
e=s.symbols('e',real=True)
check(1/(2-e)-4*e/9-s.Rational(4,9),(2*e-1)**2/(9*(2-e)))
print(f'PASS: {checks} exact reflected-guard, coupling, cost, and energy certificates')
