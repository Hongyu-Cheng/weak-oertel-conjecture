"""Exact calibration of a non-Jensen homothetic core guarantee."""
from fractions import Fraction as F

r=[F(1),F(2),F(2),F(1)]
c=[(F(0),F(0)),(F(1,10),F(0)),(F(0),F(1,10)),(F(0),F(0))]

required_markers=[]
for j in [1,2]:
    radius_slack=r[j]-(r[j-1]+r[j+1])/2
    center_slack=tuple(c[j][q]-(c[j-1][q]+c[j+1][q])/2 for q in range(2))
    assert radius_slack==F(1,2)
    assert sum(x*x for x in center_slack)==F(1,80)
    assert sum(x*x for x in center_slack)<radius_slack**2
    required_markers.append(tuple(-x/radius_slack for x in center_slack))
assert required_markers==[(F(-1,5),F(1,10)),(F(1,10),F(-1,5))]
assert required_markers[0]!=required_markers[1]

q=[F(1),F(19,10),F(19,10),F(1)]
weights=[a*a for a in q]
assert sum(weights)==F(461,50)
assert sum(a*a for a in r)==10
for median in [1,2]:
    assert sum(weights[:median+1])>=sum(weights)/2
    assert sum(weights[median:])>=sum(weights)/2
bound=F(1,4)*sum(weights)/sum(a*a for a in r)
assert bound==F(461,2000)
assert bound-F(2,9)==F(149,18000)>0
# The simpler uniform epsilon=.05 criterion also suffices.
assert F(1,2)*F(19,20)**2>F(4,9)

# Representative exact projective chart and both independent Jensen defects.
ell=[F(j+2) for j in range(4)]
for j in [1,2]:
    theta=[ell[j-1]/(2*ell[j]),ell[j+1]/(2*ell[j])]
    assert sum(theta)==1
    assert sum(theta[a]*F(p)/ell[p] for a,p in enumerate([j-1,j+1]))==F(j)/ell[j]
    for coordinate in range(2):
        old=c[j][coordinate]-(c[j-1][coordinate]+c[j+1][coordinate])/2
        new=c[j][coordinate]/ell[j]-sum(
            theta[a]*c[p][coordinate]/ell[p] for a,p in enumerate([j-1,j+1])
        )
        assert new==old/ell[j]

print("PASS: exact compatibility, non-Jensen marking obstruction, core depth, and projective identity.")
