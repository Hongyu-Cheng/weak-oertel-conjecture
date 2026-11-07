"""Exact normalization and compatibility checks for the thin-lift note."""
from fractions import Fraction as F

eps=F(1,100)
lengths=[F(1),F(2),F(1)]
areas=[a*eps for a in lengths]
assert sum(areas)==4*eps
prob_density=[1/a for a in lengths]
# In one hidden dimension, radius is density / kappa_1=density/2.
unit_radii=[f/2 for f in prob_density]
assert unit_radii==[F(1,2),F(1,4),F(1,2)]
assert (unit_radii[0]+unit_radii[2])/2>unit_radii[1]
assert all(lengths[i]*2*unit_radii[i]==1 for i in range(3))

weights=[a/sum(areas) for a in areas]
weighted_density=[weights[i]*prob_density[i] for i in range(3)]
assert weights==[F(1,4),F(1,2),F(1,4)]
assert weighted_density==[F(1,4)]*3
weighted_radii=[f/2 for f in weighted_density]
assert (weighted_radii[0]+weighted_radii[2])/2==weighted_radii[1]
assert [lengths[i]*2*weighted_radii[i] for i in range(3)]==weights

# Any common scaling keeps compatible constant section radii compatible.
for c in [F(1,7),F(1),F(9,2)]:
    r=[c*eps/2]*3
    assert (r[0]+r[2])/2<=r[1]
    assert [lengths[i]*2*r[i] for i in range(3)]==[c*a for a in areas]

# Exact optimizing radii in the cross-measure root conversion.
# Choose S=2^m so every m-th root below is rational.
for m in range(2,9):
    for q in range(1,m):
        r=m-q
        S=F(2**m)
        b=[F(1),2*S-1]
        a=[v/S for v in b]
        f=[v**r for v in b]
        terms=[v/F(2**q) for v in b]
        assert sum(a)/2==1
        assert sum(b)/2==S
        assert all(terms[i]**m==f[i]*a[i]**q for i in range(2))
        assert sum(terms)/2==2**r
        assert (sum(terms)/2)**m==S**r

print('PASS: thin areas, normalization obstruction/repair, optimized-radius exponent.')
