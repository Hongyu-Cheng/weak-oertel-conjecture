"""Exact arithmetic checks for the equality and defect identities."""
from fractions import Fraction as F

# Formula for d=1 arithmetic sums and the barrier gap.
for rho in [F(1,4),F(1,2),F(3,4),F(1),F(2),F(7,2)]:
    for m in range(1,15):
        total = sum(rho+j for j in range(m+1))
        q = rho+m
        barrier = (q+F(1,2))**2/2
        assert total == ((q+F(1,2))**2-(rho-F(1,2))**2)/2
        assert barrier-total == (rho-F(1,2))**2/2
        assert (barrier == total) == (rho == F(1,2))

# Every complete odd suffix has square tail sums; its mean is noninteger.
for N in range(2,20):
    a = [F(2*(N-1-j)+1) for j in range(N)]
    tails = [sum(a[j:]) for j in range(N)]
    assert tails == [F((N-j)**2) for j in range(N)]
    mean = sum(j*a[j] for j in range(N))/sum(a)
    assert mean == F((N-1)*(2*N-1),6*N)
    assert mean.denominator != 1

# The exact barrier identity detects a strict prefix and equality suffix.
a = [F(15,2),F(7),F(5),F(3),F(1)]
assert all(a[j]-a[j-1] >= a[j+1]-a[j] for j in range(1,len(a)-1))
gaps = []
for i in range(1,len(a)-1):
    A,b,total = a[i-1],a[i],sum(a[i:])
    delta = A-b
    assert delta > 0
    barrier = (A+b)**2/(8*delta)
    gaps.append(barrier-total)
assert gaps[0] > 0 and gaps[1:] == [0,0]

# Squaring in the double rationalization has the exact claimed numerator.
for A,b,total in [(F(7),F(5),F(9)),(F(15,2),F(7),F(16))]:
    delta = A-b
    assert (2*total-delta)**2-4*(total+A)*(total-b) == (A+b)**2-8*delta*total

print('PASS: arithmetic equality shifts, odd-tail rigidity, and exact defect identities')
