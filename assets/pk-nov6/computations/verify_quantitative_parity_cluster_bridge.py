#!/usr/bin/env python3
"""Exact finite checks; the note supplies the general proof."""
from fractions import Fraction as F
from itertools import combinations
from random import Random

checks = 0


def check(statement):
    global checks
    assert statement
    checks += 1


def transport(left, right):
    """Positive overlaps of the two consecutive probability partitions."""
    left, right = sorted(left.items()), sorted(right.items())
    total_a = sum(a for _, a in left)
    total_b = sum(b for _, b in right)
    p = [a / total_a for _, a in left]
    q = [b / total_b for _, b in right]
    i = j = 0
    lp, rq = p[0], q[0]
    entries = []
    while i < len(left) and j < len(right):
        mass = min(lp, rq)
        check(mass > 0)
        entries.append((i, j, mass))
        lp -= mass
        rq -= mass
        if lp == 0:
            i += 1
            if i < len(left):
                lp = p[i]
        if rq == 0:
            j += 1
            if j < len(right):
                rq = q[j]
    check(i == len(left) and j == len(right))
    check(sum(t for _, _, t in entries) == 1)
    check(len(entries) <= len(left) + len(right) - 1)
    targets = []
    for i, j, mass in entries:
        u, a = left[i]
        v, b = right[j]
        check(a >= mass * total_a)
        check(b >= mass * total_b)
        targets.append(tuple(x + y for x, y in zip(u, v)))
    check(len(set(targets)) == len(targets))
    check(all(a < b for a, b in zip(targets, targets[1:])))
    for i, (_, mass) in enumerate(left):
        check(sum(t for ii, _, t in entries if ii == i) == mass / total_a)
    for j, (_, mass) in enumerate(right):
        check(sum(t for _, jj, t in entries if jj == j) == mass / total_b)
    return left, right, entries, targets


rng = Random(281674)
for n in range(1, 6):
    for trial in range(75):
        left, right = {}, {}
        for array in (left, right):
            size = rng.randrange(1, 12)
            while len(array) < size:
                index = tuple(rng.randrange(-15, 16) for _ in range(n))
                array[index] = F(rng.randrange(1, 20), rng.randrange(1, 10))
        ll, rr, entries, targets = transport(left, right)
        parity = tuple(rng.randrange(2) for _ in range(n))
        for (i, j, _), target in zip(entries, targets):
            z = tuple(r + 2*u for r, u in zip(parity, ll[i][0]))
            w = tuple(r + 2*v for r, v in zip(parity, rr[j][0]))
            actual = tuple(F(a+b, 2) for a, b in zip(z, w))
            check(actual == tuple(r+t for r, t in zip(parity, target)))
            check(all(x.denominator == 1 for x in actual))

# Simultaneous events, non-product index ordering and a one-entry family.
transport({(-5, 9): F(1), (0, -8): F(1), (0, 7): F(1)},
          {(-4, 99): F(1), (1, -20): F(1), (1, 3): F(1)})
transport({(0,): F(7)}, {(0,): F(3)})

for d in range(1, 13):
    for r in (F(1, 7), F(2, 3), F(1), F(9, 4)):
        for s in (F(1, 9), F(3, 5), F(1), F(7, 2)):
            a, b = r**d, s**d
            phi = ((r+s)/2)**d
            check(phi**2 >= a*b)
            check(phi >= max(a,b)/2**d)
            check(phi > max(a,b)/2**d)
            if r == s:
                check(phi == a)

for d in range(1, 11):
    N = d+1
    for delta in (F(1,100), F(1, 2*(d+2)), F(49,100)):
        low_q = 1-delta/N
        high_r = F(1,2)+d*delta/N
        check(low_q > high_r)
        check(F(1,2)-delta/N > d*delta/N)
        # Barycentric coordinates of every vertex of every cluster.
        clusters = {}
        for i in range(N):
            clusters[i] = [tuple(F(int(k==i)) + delta*(int(k==j)-F(1,N))
                                 for k in range(N)) for j in range(N)]
            check(all(sum(v)==1 for v in clusters[i]))
            check(min(v[i] for v in clusters[i]) == low_q)
        regions = {}
        for i,j in combinations(range(N), 2):
            regions[i,j] = [tuple((a+b)/2 for a,b in zip(x,y))
                            for x in clusters[i] for y in clusters[j]]
            check(all(max(v) < low_q for v in regions[i,j]))
            # Minkowski midpoint equals the common-shape translated simplex:
            # its vertices are midpoints of equally indexed source vertices.
            diagonal = [tuple((a+b)/2 for a,b in zip(clusters[i][t],clusters[j][t]))
                        for t in range(N)]
            check(all(v in regions[i,j] for v in diagonal))
        for pair, other in combinations(regions, 2):
            label = next(iter(set(pair)-set(other)))
            check(min(v[label] for v in regions[pair]) >
                  max(v[label] for v in regions[other]))
        if d >= 2 and delta < F(1,d):
            for i, vv in clusters.items():
                check(all(v[i] > F(1,N) for v in vv))
                check(all(v[j] < F(1,N) for v in vv for j in range(N) if j != i))
            for (i,j), vv in regions.items():
                check(all(v[i] > F(1,N) and v[j] > F(1,N) for v in vv))

gamma5 = F(5,6)**5
check(F(17,84)-gamma5/2 == F(157,108864))
check(F(17,84) > gamma5/2)
check(3*gamma5-1 == F(533,2592))
check(3/(3*gamma5-1)-6 == F(4578,533))
for s in range(7):
    check(F(s*(s-1)+(6-s)*(5-s),4) >= 3)
print(f"PASS {checks} exact checks")
