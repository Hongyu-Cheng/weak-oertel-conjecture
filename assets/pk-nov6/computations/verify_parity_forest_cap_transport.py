"""Exact full-parity basin cap-color obstruction; no numerical optimization."""
from fractions import Fraction as F
from itertools import product

J=[(0,0),(1,0),(0,1),(1,1),(2,1),(1,2)]
roots=J[:4]
actual=[(z1,z2) for z1 in range(-2,5) for z2 in range(-2,5)
        if z1>=0 and z2>=0 and abs(z1-z2)<=1 and z1+z2<=3]
assert set(actual)==set(J)

def R(z):return tuple((coordinate+(coordinate%2))//2 for coordinate in z)
assert all(R(z)==z for z in roots)
assert R((2,1))==R((1,2))==(1,1)

def center(z):
    z1,z2=z
    return (F(11-4*z1-4*z2),F(4*z1-5))

big={(1,1),(2,1),(1,2)}
radius={z:F(1,10) if z in big else F(1,100) for z in J}
areas={z:(2*radius[z])**2 for z in J}
assert sum(areas.values())==F(303,2500)
assert sum(areas[z] for z in big)==F(3,25)

groups=[((-F(1,10),-F(1,10)),-F(1,100),F(0)),
        ((F(1,10),-F(1,10)),F(1,20),F(1,10)),
        ((-F(1,10),F(1,10)),F(1,20),F(1,10)),
        ((F(1,10),F(1,10)),F(1,10),F(1,5))]
normals=[(1,0),(0,1),(-1,-1)]
contacts=[(F(1,20),F(1,20)),(F(5,8),F(1,8)),
          (F(1,8),F(5,8)),(F(1,2),F(1,2))]

def dot(a,b):return sum(x*y for x,y in zip(a,b))

for s,(a,h,beta) in enumerate(groups):
    assert h<beta
    for r,p in enumerate(roots):
        assert (dot(a,p)==beta) if s==r else (dot(a,p)<beta)
    for r,contact in enumerate(contacts):
        assert (dot(a,contact)==h) if s==r else (dot(a,contact)<h)

for z in J:
    assert any(dot(a,z)>=beta for a,h,beta in groups)

for a,h,beta in groups:
    cap_masses=[]
    for j,u in enumerate(normals):
        mass=F(0)
        for z in J:
            cx,cy=center(z)
            rr=radius[z]
            margins=[dot(u,(cx+dx*rr,cy+dy*rr))+dot(a,z)-h
                     for dx,dy in product([-1,1],repeat=2)]
            assert min(margins)>0 or max(margins)<0
            if min(margins)>0:mass+=areas[z]
        cap_masses.append(mass)
    assert cap_masses==[F(103,2500),F(100,2500),F(100,2500)]

assert F(4,9)*F(3,25)-F(103,2500)==F(91,7500)>0
assert F(104,2500)>max(F(103,2500),F(100,2500))
assert F(104,2500)>F(4,9)*F(303,2500)/4

# The two midpoint bodies, and centroid-anchored images, coincide exactly.
mid1=tuple((a+b)/2 for a,b in zip(center((2,1)),center((0,1))))
mid2=tuple((a+b)/2 for a,b in zip(center((1,2)),center((1,0))))
assert mid1==mid2==center((1,1))
assert (F(1,10)+F(1,100))/2==F(11,200)<F(1,10)
assert F(1,10)/2==F(1,20)

print("PASS: exact full-parity forest, all contacts, cap masses, and basin obstruction")
