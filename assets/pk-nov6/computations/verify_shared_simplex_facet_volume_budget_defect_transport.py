"""Exact algebra checks for the proved planar shared-simplex budget.

The geometric proof is in the companion Markdown note. These checks
verify its box maximization and sharp corner-truncation algebra.
"""
from itertools import product
from fractions import Fraction
import sympy as s

r, t, u = s.symbols('r t u', nonnegative=True)
x, y, z = s.symbols('x y z')
F = x*(u-z)+(r-x)*y+z*(t-y)
allowed = [0, r*t, t*u, u*r]
checks = 0
for bx, by, bz in product((0, 1), repeat=3):
    value = s.expand(F.subs({x:bx*r, y:by*t, z:bz*u}))
    assert any(s.expand(value-v)==0 for v in allowed)
    checks += 1
for rr, tt, uu in product((Fraction(0), Fraction(1,7), Fraction(2,3), Fraction(1)), repeat=3):
    mx=max(rr*tt,tt*uu,uu*rr)
    for xx,yy,zz in product((Fraction(0),Fraction(1,5),Fraction(1,2),Fraction(1)),repeat=3):
        X,Y,Z=xx*rr,yy*tt,zz*uu
        value=X*(uu-Z)+(rr-X)*Y+Z*(tt-Y)
        assert value<=mx
        checks+=1
a,b=s.symbols('a b')
assert s.expand(1-(1-a)*(1-b)-(a+b-a*b))==0
checks+=1
print(f'PASS {checks} exact checks')
