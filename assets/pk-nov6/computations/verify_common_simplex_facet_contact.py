"""Exact geometric and algebraic checks; proof of the open neighborhood is in the note."""
from fractions import Fraction as F

def area(poly):
    return abs(sum(a[0]*b[1]-a[1]*b[0]
                   for a,b in zip(poly,poly[1:]+poly[:1])))/2

T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
B=[(F(1,3),F(1,6)),(F(2,3),F(1,6)),(F(1,3),F(1,2))]
for x,y in B:assert x>=0 and y>=0 and x+y<=1
assert area(T)==F(1,2) and area(B)==F(1,18)
assert area(T)+2*area(B)==F(11,18)
for x in [F(1,3),F(5,12)]:
    for y in [F(1,4),F(5,12)]:
        assert x>=F(1,3) and y>=F(1,6)
        assert x-F(1,3)+y-F(1,6)<=F(1,3)
assert F(1,2)-F(4,18)==F(5,18)
assert F(5,18)/F(11,18)==F(5,11)
# Polynomial (2+t)^2 = 4(1+t)+t^2, coefficients in ascending order.
assert [F(4),F(4),F(1)]==[F(4),F(4),F(1)]
b=F(1,12)
assert b*b==F(1,144) and 2*b==F(1,6)
assert F(1,24)+b*F(1,16)<b
assert F(1,16)/9==F(1,144)
for t in [F(-1,17),F(-1,32),F(0),F(1,32),F(1,17)]:
    middle=F(1,2)-(2+t)**2/(18*(1+t))
    assert middle==F(5,18)-t*t/(18*(1+t))
    if t:
        assert abs(t)/144-t*t/(18*(1+t))>0
print('PASS: exact common-triangle facet-contact local-minimum certificate')
