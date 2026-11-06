from fractions import Fraction as F
from math import comb

def value(d,k):
    q=d-k;z=F(k-1,q+k-1)
    return F(1,2)*F(q,q+k-1)**q*sum((F(comb(q+j-1,j))*z**j*F(1,2)**(ell-j) for ell in range(k) for j in range(ell+1)),F(0))
expected={
3:[F(1,2),F(1,2)],4:[F(1,2),F(13,27)],5:[F(1,2),F(243,512),F(1,2)],
6:[F(1,2),F(1472,3125),F(12177,25000)],7:[F(1,2),F(21875,46656),F(350,729),F(1,2)],
8:[F(1,2),F(384912,823543),F(3134375,6588344),F(404112,823543)],
9:[F(1,2),F(15647317,33554432),F(61965,131072),F(16265625,33554432),F(1,2)]}
margins={3:F(1,128),4:F(61,16875),5:F(2147,373248),6:F(439904,52521875),7:F(32753357,3057647616),8:F(1348942633648,106352477257509),9:F(939511987337,65536000000000)}
for d,vals in expected.items():
    assert vals==[value(d,k) for k in range(1,(d+1)//2+1)]
    assert min(vals)==vals[1]
    assert min(vals)-F(7,6)*F(d,d+1)**d==margins[d]>0
assert F(9,20)-F(7,6)*F(10,11)**10==F(310464227,1556245476060)>0
print('PASS: all admissible saturated values in dimensions3..9 and every exact angular margin')
