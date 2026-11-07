"""Exact arithmetic for the sequence-norm and actual-centroid formulas."""
from fractions import Fraction as F

for n in range(3,151):
    kappa2 = F(2*n*(2*n-3),3*(n-1)*(n-2))
    assert kappa2<=3
    for j in range(1,n-1):
        tent=[F(i,j) if i<=j else F(n-1-i,n-1-j) for i in range(n)]
        norm=sum(x*x for x in tent)
        assert sum(tent)==F(n-1,2)
        assert norm==F(n-1,3)+F(1,6)*(F(1,j)+F(1,n-1-j))
        assert n*norm<=kappa2*sum(tent)**2
        if j in (1,n-2): assert n*norm==kappa2*sum(tent)**2
    endpoint=[F(i,n-1) for i in range(n)]
    assert sum(endpoint)==F(n,2)
    assert sum(x*x for x in endpoint)==F(n*(2*n-1),6*(n-1))
    assert n*sum(x*x for x in endpoint)<kappa2*sum(endpoint)**2

for den in range(1,21):
    for num in range(den,10*den+1):
        r=F(num,den)
        c=(r*r+2)/(2*(r+2))
        lower=c+min(2*c,F(1))
        upper=r-c+min(max(2*(1-c),F(0)),F(1))
        depth=min(lower,upper)/(r+2)
        if r<=2 or r>=4:
            expected=(r*r+2*r+6)/(2*(r+2)**2)
        elif (r-1)**2<=3:
            expected=(-r*r+8*r+2)/(2*(r+2)**2)
        else:
            expected=(r*r+4*r-2)/(2*(r+2)**2)
        assert depth==expected

print('PASS: exact tent norm extrema and true-centroid all-slope formulas.')
