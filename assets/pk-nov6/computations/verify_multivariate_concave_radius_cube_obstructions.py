#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

def sums(n,p,a,c):
    radii=[F(1) if all(zj==0 for zj in z) else a for z in product((-1,0,1),repeat=n)]
    assert len(radii)==3**n
    assert sum(r**p for r in radii)==1+(3**n-1)*a**p
    return sum(max(F(0),r-c)**p for r in radii),sum(r**p for r in radii)

left,total=sums(3,2,F(1,3),F(1,3))
right=F(2,3)**5*total
assert left==F(4,9) and right==F(1120,2187) and right-left==F(148,2187)
left,total=sums(2,2,F(1,3),F(1,3))
right=F(2,3)**3*total
assert left==F(4,9) and right==F(136,243) and right-left==F(28,243)
left,total=sums(4,2,F(1,2),F(1,2))
right=F(1,16)*F(1,2)**2*total
assert left==F(1,4) and total==21 and right==F(21,64) and right-left==F(5,64)
_,total=sums(6,2,F(1,3),F(1,3))
assert total==F(737,9)>64
assert F(4,9)<F(1,64)*F(4,9)*total
# Explicit inequalities defining the full body and its exact sampled radii.
checks=12
for n in range(1,6):
    a=F(1,3)
    for z in product((-1,0,1),repeat=n):
        radius=min(1-(1-a)*sign*zj for zj in z for sign in (-1,1))
        assert radius==(1 if all(zj==0 for zj in z) else a)
        checks+=1
print(f'PASS {checks} exact cube-radius, truncation-gap, and selected-center checks')
