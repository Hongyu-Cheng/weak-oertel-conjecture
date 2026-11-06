#!/usr/bin/env python3
"""Exact finite certificates; the dimension-uniform proof is in the companion note."""
from fractions import Fraction as F

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def pos(x):
    return max(F(0), x)

def sums(d, H):
    t = F(1, d + 1)
    a = t * (1 + F(1, H))
    beta = t / d
    gamma = (1-t)**d
    W = F(0)
    left = F(0)
    right = F(0)
    for h in range(1 + a.denominator // a.numerator):
        r = pos(1-a*h)
        if not r:
            continue
        q = t-beta*h
        p = t+beta*(h+1)
        check(r-d*q == t*(1-F(h,H)))
        check(r-d*p == -h*(a+t))
        W += r**d
        left += d**d * q**(d-1) * pos(r-d*q)
        right += d**d * p**(d-1) * pos(r-d*p)
    K = sum(((1-F(j,d))**(d-1) * (1-F(j,H))
             for j in range(H)), F(0))
    check(left == gamma*K)
    check(right == 0)
    return W, K

expected_margins = {
    2: F(0),
    3: F(5,1026),
    4: F(2717,134400),
    5: F(1349881,39393750),
    6: F(11033401,241297056),
    7: F(147714066079,2686102437606),
    8: F(11558430263869,184757665136640),
    9: F(13502918255940587,196191874965540258),
}
for H, expected in expected_margins.items():
    q = (1-F(1,H))**H
    U = 1/(1-q)-1-F(H-1,3*H)-sum(
        ((1-F(j,H))**H for j in range(2,H)), F(0))
    check(F(1,6)-U == expected)
    check(expected >= 0)

large = F(8,5)-F(13,10)-F(4,5)**10-F(7,10)**10
check(large == F(1643782927,10**10))
check(F(1,6)-large == F(68651219,3*10**10))
check(large < F(1,6))

for d in range(2,51):
    for H in range(1,d+1):
        W,K = sums(d,H)
        check(W-K < F(1,6))
        a = F(H+1,H*(d+1))
        q = (1-a)**d
        check(W <= 1/(1-q))
        if H >= 2:
            qH = (1-F(1,H))**H
            check(q <= qH)
            lower = 1+F(H-1,3*H)+sum(
                ((1-F(j,H))**H for j in range(2,H)), F(0))
            check(K > lower)
            for j in range(2,H):
                check((1-F(j,d))**(d-1) >= (1-F(j,H))**(H-1))

print(f"PASS: {checks} exact rational checks")
