"""Exact arithmetic for the geometric examples and constants in the companion note.
The universal layer-cake and concavity inequalities are proved in the note.
"""
from fractions import Fraction as F
from math import comb


def area(vertices):
    return abs(sum(x*y1-y*x1 for (x,y),(x1,y1)
                   in zip(vertices, vertices[1:]+vertices[:1])))/2


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


# Tetrahedron inequalities n dot (z,u,x) <= b.
vertices = [(0,1,1),(0,-1,-1),(1,1,-1),(1,-1,1)]
facets = [((2,1,1),2),((2,-1,-1),2),((-2,1,-1),0),((-2,-1,1),0)]
center = (F(1,2),0,0)
for normal,b in facets:
    assert dot(normal,normal) == 6
    assert b-dot(normal,center) == 1
    values = [dot(normal,v) for v in vertices]
    assert all(v<=b for v in values)
    assert values.count(b) == 3
assert F(126,4) < 36  # fixed normalized outer radius is below 6

for N in range(1,101):
    h = F(1,N)
    eps = h*h
    q0 = [(-1,-1-eps),(1,1-eps),(1,1+eps),(-1,-1+eps)]
    q1 = [(-1,1-eps),(1,-1-eps),(1,-1+eps),(-1,1+eps)]
    A0,A1 = area(q0),area(q1)
    assert A0 == A1 == 4*eps
    assert all(F(u)/h == int(F(u)/h) for u,x in q0+q1)
    count = 2*N+1
    T0 = count*2*eps
    assert A0 == h*(T0-2*eps)
    M,T = A0+A1,2*T0
    assert M == 8*h*h
    assert 2*eps/T == F(1,2*count)
    assert M/(h*T) == 2/(2+h)
    assert F(1,2)*(1-M/(h*T)) == 2*eps/T
    # Exact component discrepancy of the whole closed rectangle.
    assert h*T0-A0 == h*2*eps
    assert h*(2*eps)/A0 == h/2

# Affine widths attain the trapezoid lower inequality for every endpoint pair.
for N in range(2,21):
    for left,right in [(F(0),F(1)),(F(1),F(0)),(F(2),F(5)),(F(3),F(3))]:
        w = [(1-F(j,N-1))*left+F(j,N-1)*right for j in range(N)]
        T,E = sum(w),(left+right)/2
        assert T == N*E
        assert T-E == (1-F(1,N))*T

# A vertical segment gives A=0 and discrepancy exactly hW.
for h,W in [(F(1,7),F(3,5)),(F(2),F(4))]:
    A,T,E = 0,W,W
    assert A == h*(T-E)
    assert h*T-A == h*W

# Cone profile integral, via exact binomial expansion of (1-t)^s.
for s in range(1,21):
    integral = sum(F((-1)**j*comb(s,j),j+1) for j in range(s+1))
    assert integral == F(1,s+1)

print('PASS: exact tetrahedron, grid-hull masses, concentration ratios, sharp sampling examples, and cone constants')
