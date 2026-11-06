"""Exact rational checks for the proved annular/mass reduction.

The proof is in the companion markdown note. These checks independently
evaluate finite tails and identities; they are not a proof by sampling.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement


def tail(a, r, s):
    if s <= 0:
        return r*r
    if s >= a*r:
        return Q(0)
    if a == 1:
        return (r-s)**2
    if s <= (1-a)*r:
        return r*r-s*s/(a*(1-a))
    return (a*r-s)**2/(a*(2*a-1))


def density(a, r, s):
    if s <= 0 or s >= a*r:
        return Q(0)
    if a == 1:
        return 2*(r-s)
    if s <= (1-a)*r:
        return 2*s/(a*(1-a))
    return 2*(a*r-s)/(a*(2*a-1))


count = 0
for a in [Q(2,3), Q(7,10), Q(3,4), Q(5,6), Q(1)]:
    for r, rp in combinations_with_replacement([Q(j,8) for j in range(9)], 2):
        for s in [Q(j,24) for j in range(1,25)]:
            diff = density(a, rp, s)-density(a, r, s)
            assert 0 <= diff <= 2*(rp-r)/(2*a-1)
            count += 1

for m in range(0, 6):
    # Concavity is encoded exactly by nondecreasing one-sided drops.
    for drops in combinations_with_replacement([Q(j,12) for j in range(5)], m):
        if sum(drops) > 1:
            continue
        radii = [Q(1)]
        for drop in drops:
            radii.append(radii[-1]-drop)
        mass = 2*sum(r*r for r in radii)
        moment_bound = (3*mass-1)/4-Q(1,4*(2*m+1))
        assert sum(radii) <= moment_bound
        for a in [Q(2,3), Q(3,4), Q(1)]:
            for beta in [Q(0), Q(1,78), Q(1,12), Q(1,3)]:
                t = Q(1,3)
                even = sum(tail(a,r,t-beta*h)+tail(a,r,t+beta*(h+1))
                           for h,r in enumerate(radii))
                odd = tail(a,Q(1),t)+sum(tail(a,radii[h],t-beta*h)
                           +tail(a,radii[h],t+beta*h) for h in range(1,m+1))
                annular = sum(tail(a,radii[h-1],t+beta*h)
                           -tail(a,radii[h],t+beta*h) for h in range(1,m+1))
                annular += tail(a,radii[-1],t+beta*(m+1))
                assert even-odd == annular
                assert annular >= 0
                assert annular >= tail(a,Q(1),t)-2*beta*sum(radii)/(2*a-1)
                assert annular >= tail(a,Q(1),t)-beta*(3*mass-1)/(2*(2*a-1))
                if beta <= Q(1,78) or beta >= Q(1,3) or mass >= 9:
                    assert even >= Q(2,9)*mass
                count += 1

for a in [Q(j,60) for j in range(40,61)]:
    f = (a-Q(1,3))**2/(a*(2*a-1))
    assert f-Q(4,9) == (a-1)**2/(9*a*(2*a-1))
    for x in [Q(j,10) for j in range(20,91)]:
        H = 2*(2*a-1)*(f-(9-x)/36)/(3*x-1)
        assert H >= Q(1,78)
        count += 1

assert Q((12+1)*(2*12+1),3*12) == Q(325,36) > 9
print(f"PASS: {count} exact section, telescope, moment, and threshold checks")
