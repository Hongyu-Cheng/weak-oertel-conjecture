"""Exact finite cap-profile and reflection-variation checks."""
from fractions import Fraction as F

fibers={0:(F(0),F(2)),1:(F(0),F(6)),
        2:(F(0),F(10)),3:(F(0),F(3))}
M=sum(hi-lo for lo,hi in fibers.values())

def cap(j,c,a):
    return sum(max(F(0),min(hi-lo,hi-c-a*(z-j)))
               for z,(lo,hi) in fibers.items())

def retained(j,c):
    ans=F(0)
    for z,(lo,hi) in fibers.items():
        if 2*j-z in fibers:
            l2,h2=fibers[2*j-z]
            ans+=max(F(0),min(hi,2*c-l2)-max(lo,2*c-h2))
    return ans

def profile(j,c):
    knots=sorted({(x-c)/(z-j) for z,pair in fibers.items()
                  if z!=j for x in pair})
    vals=[cap(j,c,a) for a in knots]
    # F is constant outside the first/last knot and affine between knots.
    tv=sum(abs(b-a) for a,b in zip(vals,vals[1:]))
    own=abs(vals[0]+vals[-1]-M)
    depth=min(min(vals),M-max(vals))
    assert M-retained(j,c)==tv+own
    assert M-retained(j,c)<=4*(len(fibers)-1)*(M/2-depth)
    return vals[0],vals[-1],tv,own,retained(j,c),depth

assert profile(2,F(3))==(10,15,5,4,12,6)
assert profile(2,F(4))==(9,14,9,2,10,7)
assert profile(1,F(3))==(16,5,11,0,10,5)
for j,(lo,hi) in fibers.items():
    for numerator in range(13):
        c=lo+(hi-lo)*F(numerator,12)
        profile(j,c)

# Prefix structure makes the pointwise absolute-value equality exact.
for plus in range(20):
    for minus in range(20):
        signed=sum(k*((k<=minus)-(k<=plus))
                   for k in range(1,20))
        absolute=sum(k*abs((k<=minus)-(k<=plus))
                     for k in range(1,20))
        assert abs(signed)==absolute
print('PASS: exact reflection loss, cap depth, and nested-prefix identities.')
