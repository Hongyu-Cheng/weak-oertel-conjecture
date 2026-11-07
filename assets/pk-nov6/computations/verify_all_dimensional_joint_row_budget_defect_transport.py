"""Exact rational interval and algebra checks for the proved joint theorem."""
from fractions import Fraction as F
from math import prod
import random

checks = 0


def require(value):
    global checks
    assert value
    checks += 1


def root_interval(x, n, scale=10**18):
    """An exact enclosing rational interval for a positive nth root."""
    target = x.numerator * scale**n // x.denominator
    lo, hi = 0, 1
    while hi**n <= target:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**n <= target:
            lo = mid
        else:
            hi = mid
    require(F(lo, scale)**n <= x < F(hi, scale)**n)
    return F(lo, scale), F(hi, scale)


rng = random.Random(20260929)
for d in range(2, 8):
    m = d+1
    for sample in range(30):
        raw = [[0 if i==j else rng.randint(1,30) for j in range(m)] for i in range(m)]
        total = sum(map(sum,raw))
        b = [[F(x,total) for x in row] for row in raw]
        a = [sum(b[i][j] for i in range(m) if i!=j) for j in range(m)]
        require(sum(a)==1 and all(x>0 for x in a))
        f = [root_interval(prod(a[i]+b[i][j] for j in range(m) if j!=i),d)
             for i in range(m)]
        f = [(d*x,d*y) for x,y in f]
        require(sum(x[1] for x in f) < d+1)
        for i in range(m):
            upper_i = f[i][1]
            upper_others = sum(f[j][1] for j in range(m) if j!=i)
            require(upper_i < d)
            # Raising to d-1 removes the fractional frontier exponent.
            require((d-upper_i)**(d-1) > (d-1)**(d-1)*(upper_others/d)**d)
            A, B = a[i], sum(b[i][j] for j in range(m) if j!=i)/d
            t, C = (1-A)/d, ((1-A)/d-B)/(d-1)
            require(A>0 and B>0 and t>0 and C>0)
            require(t+A/d==F(1,d))
            require(t+C==(1-A-B)/(d-1))
            bar_i=d*(A+B)
            # The two formulae for the dth power of the other-row sum.
            require((d*d)**d*F(1,d)*(t+C)**(d-1)
                    == d**d*((d-bar_i)/(d-1))**(d-1))


# Actual symmetric equality simplex: exact row and positive barycentric checks.
for d in range(2, 11):
    for numer in range(1, 10):
        x=F(d*numer,10)
        A=(max(F(0),(x-1)/(d-1))+x/d)/2
        B=x/d-A
        t=(1-A)/d
        C=(t-B)/(d-1)
        require(min(A,B,t,C)>0)
        alpha0=B/(A+B)
        alphaj=A/(d*(A+B))
        require(alpha0+d*alphaj==1)
        require(-alpha0*A/d+alphaj*(t-(d-1)*C)==0)
        require(t-(d-1)*C==B)
        require(t+C>0 and A+B>0)
        require(d*(A+B)==x)
        # Exact dth power identity on the joint frontier.
        gpow=(d*d)**d*F(1,d)*(t+C)**(d-1)
        require((d-x)**(d-1)==(d-1)**(d-1)*gpow/d**d)

print(f"PASS: {checks} exact interval, balanced-matrix and actual-simplex checks")
