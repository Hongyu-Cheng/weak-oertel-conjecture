"""Exact finite calibrations for the paired-roof cone and its dual.

General convex interpolation and Farkas duality are analytic in the source.
The body checks below use the actual globally certified ordinary rectangle
family, but do not repeat its all-normal Bernstein verification here.
"""
from fractions import Fraction as F
from itertools import combinations, product

count = 0

def ck(test):
    global count
    assert test
    count += 1

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def clamp(x, lo, hi):
    return max(lo, min(x, hi))

z = [-2, -1, 0, 1, 2]
r = [F(1), F(51, 50), F(51, 50), F(203, 200), F(101, 100)]
H = [F(1), F(809, 800), F(403, 400), F(803, 800), F(1)]
Q = F(812869, 160000)
M = F(814069, 80000)
ck(2*dot(r, H) == M)
ck(M-2*Q == F(3, 200))

# All nontrivial extreme anchored representations on this chain.
relations = []
tight = []
for qi, q in enumerate(z):
    for i, j in combinations(range(len(z)), 2):
        if not z[i] < q < z[j]:
            continue
        lam_i = F(z[j]-q, z[j]-z[i])
        lam_j = 1-lam_i
        gap = H[qi]-lam_i*H[i]-lam_j*H[j]
        ck(gap >= 0)
        relations.append((qi, i, j, lam_i, lam_j, gap))
        if gap == 0:
            tight.append((qi, i, j, lam_i, lam_j))
ck({q for q, *_ in tight} == {2, 3})

h = [F(0), F(1), F(0), F(0), F(0)]
for qi, i, j, li, lj in tight:
    ck(h[qi] <= li*h[i]+lj*h[j])

def cap(heights):
    return sum(width*clamp(height-F(base, 2), F(0), 2*height)
               for base, width, height in zip(z, r, heights))

ck(cap(H) == Q)
for denominator in range(200, 10001, 37):
    t = F(1, denominator)
    ck(t < F(3, 400))
    Ht = [height-t*speed for height, speed in zip(H, h)]
    ck(all(v > 0 for v in Ht))
    for qi, i, j, li, lj, _ in relations:
        ck(Ht[qi] >= li*Ht[i]+lj*Ht[j])
    Mt = 2*dot(r, Ht)
    Qt = cap(Ht)
    ck(Qt == Q-F(51, 50)*t)
    ck(Mt == M-F(51, 25)*t)
    ck(Qt/Mt-Q/M == F(51, 50)*t*(2*Q-M)/(M*Mt))
    ck(Qt/Mt < Q/M)
    volume = [2*x*y for x, y in zip(r, Ht)]
    ck(all(a < Qt for a in
           [volume[0], sum(volume[:2]), sum(volume[3:]), volume[4]]))
    ck(Ht[1] > F(1, 2))

# Paired-facet coefficient at the exposed lifted roof node -1.
beta = Q/M
c_at_minus_one = r[1]*(1-2*beta)
ck(c_at_minus_one > 0)
ck(c_at_minus_one == r[1]*(M-2*Q)/M)

# Flat three-node cone and an exact nontrivial deficit transport.
# This is an algebraic cone calibration, not an asserted critical-cap law.
g = [-F(1, 2), F(1), -F(1, 2)]
s = [F(1, 2), F(0), F(1, 2)]
c = [F(-1), F(1), F(-1)]
ck(all(x == y-z0 for x, y, z0 in zip(c, g, s)))
for hm, h0, hp in product([F(i, 3) for i in range(7)], repeat=3):
    if h0 <= (hm+hp)/2:
        hh = [hm, h0, hp]
        ck(dot(c, hh) <= 0)
        ck(dot(c, hh) == dot(g, hh)-dot(s, hh))
    if hm == 0 and hp == 0 and h0 <= (hm+hp)/2:
        ck(h0 == 0)

# Source positive mass one at upper node (0,1), sent half to each
# deficit endpoint. Both base and height means are exact.
pi = [F(1, 2), F(1, 2)]
ck(sum(pi) == 1)
ck(dot(pi, [-1, 1]) == 0)
ck(dot(pi, [1, 1]) == 1)
ck(all(v <= 1 for v in pi))

# With a strict tent the central lifted node is a vertex; its own-only
# inward velocity is feasible and detects the same positive coefficient.
tent = [F(1), F(2), F(1)]
ck(tent[1] > (tent[0]+tent[2])/2)
ck(dot(c, [0, 1, 0]) == 1)
for t in [F(i, 19) for i in range(1, 19)]:
    ck(tent[1]-t >= (tent[0]+tent[2])/2)

# Signed-cone strengthening: the sink-containing old vector fails at
# the constant outward roof speed, while the midpoint row has saturated
# transport and all full lifted moments vanish.
ck(dot(c, [-1, -1, -1]) == 1)
ck(sum(g) == 0)
ck(dot(g, [-1, 0, 1]) == 0)
ck(dot(g, [1, 1, 1]) == 0)
for hm, h0, hp in product([F(i, 3) for i in range(-6, 7)], repeat=3):
    if h0 <= (hm+hp)/2:
        ck(dot(g, [hm, h0, hp]) <= 0)
ck(pi == [F(1, 2), F(1, 2)])  # Both target deficits exactly saturated.

# A nontrivial signed polar built from the actual five-node tight rows.
generators = []
for qi, i, j, li, lj in tight:
    gg = [F(0)]*len(z)
    gg[qi] += 1
    gg[i] -= li
    gg[j] -= lj
    generators.append(gg)
cc = [sum(F(k+1, 7)*gg[j] for k, gg in enumerate(generators))
      for j in range(len(z))]
ck(sum(cc) == 0)
ck(dot(cc, z) == 0)
ck(dot(cc, H) == 0)
for hh in product([F(-1), F(0), F(1)], repeat=len(z)):
    if all(hh[qi] <= li*hh[i]+lj*hh[j] for qi, i, j, li, lj in tight):
        ck(dot(cc, hh) <= 0)

# Explicit signed-node convex interpolants for the tent: expansion at
# the center uses |z|-1 (negative), shrink uses (|y|-1)_+ (positive).
for zz, height in zip([-1, 0, 1], tent):
    for sign in [-1, 1]:
        yy = sign*height
        ck(abs(zz)-1 == (-1 if zz == 0 else 0))
        ck(max(F(0), abs(yy)-1) == (1 if zz == 0 else 0))
        for roof_normal in [-1, 1]:
            ck(roof_normal**2*(abs(zz)-1) == (abs(zz)-1))
        ck(0**2*(abs(zz)-1) == 0)

print(f'PASS: {count:,} exact paired-roof cone checks; '
      f'{len(relations)} anchored relations, {len(tight)} tight relations')
