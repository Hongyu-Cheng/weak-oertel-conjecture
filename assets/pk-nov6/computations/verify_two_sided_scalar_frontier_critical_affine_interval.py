"""Exact arithmetic checks for Section5. The accompanying note proves the theorem."""
from fractions import Fraction as F
V=(F(1),F(3,2),F(2)); M=sum(V); Q=F(7,4)
e=(F(0),F(3,4),F(1)); h=(F(1,2),F(3,4),F(1))
f=(F(0),F(3,4),F(2))
assert V[0]+V[2]==2*V[1]
assert max(V)<M/2
assert sum(h)==3*h[1]==F(9,4)
assert h[0]+h[2]==2*h[1]
assert all(a>=b for a,b in zip(h,e))
assert sum(f)/3-f[1]==F(1,6)
assert sum(V)/3==V[1]
assert Q/M==F(7,18)>F(1,4)
for i in range(-1000,1001):
    a=F(i,100)
    T=lambda R,t:min(2*R,max(F(0),R-t))
    end=T(F(1,2),a)+T(F(1),-a)
    assert end>=1
    assert (end==1)==(a<=-1)
print('PASS: exact affine critical interval data and 2001 paired-tail checks')
