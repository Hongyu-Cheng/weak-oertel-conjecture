"""Exact arithmetic checks for the proved homothetic Hall-capacity bounds."""
from fractions import Fraction as F

assert 3*F(2,3)**2-F(1)==F(1,3)
assert (1+F(-1,3))**2/2==F(2,9)
assert 5*F(3,5)**2+2*F(3,5)-3==0
assert F(3,5)**2==F(9,25)
assert F(2,9)-F(9,25)/3==F(23,225)>0

# Formula check for every rational threshold triple on this finite mesh;
# the general Jensen proof appears in the accompanying note.
for i in range(-12,25):
    for j in range(-12,25):
        ss=[F(i,36),F(j,36),1-F(i+j,36)]
        if not all(F(-1,3)<=s<=F(2,3) for s in ss):continue
        caps=[F(1) if s<=0 else (1-s)**2 for s in ss]
        assert sum(caps)-1>=F(2,9)

for numerator in range(1,26):
    ratio=F(numerator,100)
    assert ratio<=F(9,25)
    assert ratio+min(ratio,F(2,9))>4*ratio/3

print("PASS: exact threshold, matching-capacity, and balanced-ratio constants")
