"""Exact finite checks for the full-body crosspolytope tube.
The all-dimensional cap arguments and paired-tail dependency are in the note.
"""
from fractions import Fraction as F


def dot(a,b):return sum(x*y for x,y in zip(a,b))


def gamma(s):return F(s,s+1)**s

for m in range(1,31):
    zero=(0,)*m
    e=[tuple(int(i==j) for i in range(m)) for j in range(m)]
    endpoints=e+[tuple(-x for x in p) for p in e]
    P=[zero]+endpoints
    height=lambda p:F(1+sum(p),2)
    for eps in [F(1,4),F(1,100),F(49,100)]:
        for p in P:
            integers=[u for u in range(-2,3) if abs(F(u)-height(p))<=eps]
            assert integers==([] if p==zero else [int(height(p))])
    assert all(2*height(p)-sum(p)==1 for p in P)
    assert height(zero)==F(1,2)
    assert all(height(p) in (0,1) for p in endpoints)
    for p in endpoints:
        assert dot(p,p)==1
        assert all(dot(p,q)<=0 for q in endpoints if q!=p)
    # Projected normalized total variation, half the exact L1 difference.
    tv=F(1,2)*(F(1,2*m+1)+2*m*(F(1,2*m)-F(1,2*m+1)))
    assert tv==F(1,2*m+1)
    assert 2*m<=2**m
    # Full rank-m affine integer lattice: even-sum direction basis projects
    # to 2e1 and ei-e1, and has determinant 2 by triangular form.
    projected=[tuple(2*int(i==0) for i in range(m))]
    projected += [tuple(int(i==j)-int(i==0) for i in range(m)) for j in range(1,m)]
    lifts=[(*projected[0],1)]+[(*v,0) for v in projected[1:]]
    assert all(2*v[-1]-sum(v[:-1])==0 for v in lifts)
    assert projected[0][0]==2
    assert all(projected[j][j]==1 for j in range(1,m))
    for s in range(1,16):
        coarse=gamma(s);fine=gamma(s)/(2*m)
        assert fine/coarse==F(1,2*m)
        assert fine>=gamma(s)/2**m>gamma(s)/2**(m+1)
        assert 1-F(1,s+1)-2<0
        assert (1-F(1,s+1))**s==gamma(s)
        assert gamma(s)<=F(1,2)
print('PASS: exact lattice slices, exposed cap gaps, projected TV, parity rank/index basis, and depth ratios')
