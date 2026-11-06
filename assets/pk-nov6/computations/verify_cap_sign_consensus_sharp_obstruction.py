from fractions import Fraction as F
from itertools import combinations

# C=[0,1] x [0,1], canonical isolated cap margins.
def q(v,z): return z if v==0 else 1-z
def margin(v,orient,z,x):
    return (x-F(1,2) if orient==1 else F(1,2)-x)-q(v,z)
caps=[(v,o) for v in (0,1) for o in (-1,1)]
atoms=[(z,x,F(1,2)) for z in (0,1) for x in (F(1,4),F(3,4))]

for v,o in caps:
    out_mass=sum(w for z,x,w in atoms if margin(v,o,z,x)>=0)
    hinge=sum(w*max(F(0),margin(v,o,z,x)) for z,x,w in atoms)
    assert out_mass==F(1,2)
    assert hinge==F(1,8)
for z,x,w in atoms:
    assert any(margin(v,o,z,x)>=0 for v,o in caps)
    own_quarter=min(x,1-x)
    assert own_quarter==F(1,4)<F(1,2)

# Every fiberwise joint strict complement is a union of the two half cells.
for z in (0,1):
    for k in range(len(caps)+1):
        for I in combinations(caps,k):
            # Midpoints are exact membership representatives of each open half.
            expected=F(0)
            expected_moment=F(0)
            for lo,hi in ((F(0),F(1,2)),(F(1,2),F(1))):
                mid=(lo+hi)/2
                if all(margin(v,o,z,mid)<0 for v,o in I):
                    expected+=hi-lo
                    expected_moment+=(hi*hi-lo*lo)/2
            observed=sum(w for zz,x,w in atoms if zz==z and
                         all(margin(v,o,z,x)<0 for v,o in I))
            observed_moment=sum(w*x for zz,x,w in atoms if zz==z and
                         all(margin(v,o,z,x)<0 for v,o in I))
            assert observed==expected
            assert observed_moment==expected_moment
assert sum(w for _,_,w in atoms)==2
assert F(1,4)/2==F(1,8)<F(1,4)
print('PASS: actual full-cover masses, all fiberwise joint complements and moments, hinges, and four bad atoms.')
