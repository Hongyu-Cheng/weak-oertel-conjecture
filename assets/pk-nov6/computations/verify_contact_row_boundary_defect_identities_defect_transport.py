"""Exact checks of limiting contact-row identities with zero-L atoms."""
from fractions import Fraction as F

checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1

# On the actual affine contact line L(x)=x, use probability rows with an
# atom at x=0. These are algebra calibrations, not sampled-body claims.
for den in range(3,23):
    for num in range(1,den):
        p=F(num,den)
        q=1-p
        targets=(F(0),F(1),F(2))
        row=(p,q/F(3),2*q/F(3))
        y=sum(r*x for r,x in zip(row,targets))
        Li=y
        meanL=sum(r*x for r,x in zip(row,targets))
        eq(meanL,Li)
        bar=tuple(r*x/Li for r,x in zip(row,targets))
        eq(sum(bar),F(1))
        eq(bar[0],F(0))
        cov=sum(r*(x-y)**2 for r,x in zip(row,targets))
        meanbar=sum(r*x for r,x in zip(bar,targets))
        eq(meanbar-y,cov/Li)
        # Tilted mass and first moment split into positive-L and zero-L.
        nu=tuple(r/Li for r in row)
        zeta=nu[0]
        eq(sum(nu),sum(nu[1:])+zeta)
        eq(sum(n*x for n,x in zip(nu,targets)),F(1))
        eq(sum(nu[1:][i]/F(1) for i in range(2)),(1-p)/Li)
        eq(sum(n*x for n,x in zip(nu,targets)),
           sum(n*x for n,x in zip(nu[1:],targets[1:])))
print(f'PASS: {checks} exact checks')
