"""Exact section and volume checks for the level-trimming obstruction."""
from fractions import Fraction as F

fibers={}
for i in range(3):
    for j in range(3):
        a,b=F(i,2),F(j,2)
        s0,s1=max(F(0),a+b-1),min(a,b)
        lower=1-2*a-2*b+4*s0-F(1,2)
        upper=1-2*a-2*b+4*s1+F(1,2)
        fibers[(i,j)]=(lower,upper)
assert fibers[(0,0)]==fibers[(2,2)]==(F(1,2),F(3,2))
assert fibers[(0,2)]==fibers[(2,0)]==(-F(3,2),-F(1,2))
for z in [(0,1),(1,0),(2,1),(1,2)]:
    assert fibers[z]==(-F(1,2),F(1,2))
assert fibers[(1,1)]==(-F(3,2),F(3,2))
assert sum(b-a for a,b in fibers.values())==11
t=F(3,4)
assert all(b-a>t for a,b in fibers.values())
assert F(1,2)+t/2 > -F(1,2)-t/2
assert 1+2*t>t
assert 1-t/2>t/2
assert 2+t>t
assert F(3,22)-F(1,8)==F(1,88)>0
# Determinant of the three affine differences of the center tetrahedron.
assert 2*(2*0-2*(-2))+2*(0*(-2)-2*(-2))==16
print('PASS: all nine fibers, strict active level, trimming gaps and OC witness.')
