from fractions import Fraction as F
from itertools import combinations

P=(-1,0,1,2)
lengths={z:F(z+2,5) for z in P}
assert sum(lengths.values())==2
assert sum(z*lengths[z] for z in P)==2
moment=sum(m-m*m/2 for m in lengths.values())
assert moment==F(7,5)
assert moment/2==F(7,10)
assert [pair for pair in combinations(P,2) if sum(pair)==2]==[(0,2)]
for z in P:
    assert z*z>=z
    assert (z*z==z)==(z in (0,1))
    assert F(2,5)-F(z,10)>=F(1,5)
    assert F(3,10)+F(z,10)>=F(1,5)
bad=[max(F(0),min(F(1),F(3*z,10))) for z in P]
assert bad==[0,0,F(3,10),F(3,5)]
assert sum(bad)==F(9,10)
assert sum(bad)/4==F(9,40)<F(1,4)
assert 2*0**2+2*1**2==2
assert 1*(-1)**2+3*1**2==4
print('PASS: moment uniqueness data, integer variance equality, zero cross-capture margins')
