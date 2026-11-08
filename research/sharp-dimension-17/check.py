from collections import Counter
from fractions import Fraction as F
from itertools import product

a = F(663, 1000)
delta = F(664201, 10**6)
eps = F(13, 20000)
h = F(1111946415, 10**9)
gamma = F(5, 6)**5
assert 0 < a < 1 and 0 < delta < 1 and 0 < eps < 1
assert 0 < h < 1 + 2 * delta < 3
assert (h / (1 + 2 * delta))**5 < a / (1 + a)

counts = Counter()
parities = set()
sites = {(0,) * 12}
for ordinary in product((0, 1), repeat=10):
    u = sum(ordinary[4:]) - sum(ordinary[:4])
    for selector in ((0, 0), (1, 0), (0, 1), (1, 1)):
        parity = ordinary + selector
        if not any(parity):
            continue
        if selector == (0, 0):
            candidate = ordinary + selector
            thresholds = (sum(ordinary),) * 3
        else:
            s1, s2 = selector
            candidate = tuple(-x for x in ordinary[:4]) + ordinary[4:] + selector
            thresholds = (u - s2, u - s1, u - s1 - s2)
        guard_units = sum(thresholds)
        assert guard_units == 3 * sum(candidate[:10]) - 2 * sum(selector)
        assert guard_units != 0
        sign = 1 if guard_units > 0 else -1
        heavy = tuple(sign * x for x in candidate)
        assert tuple(x % 2 for x in heavy) == parity
        assert heavy not in sites
        sites.add(heavy)
        thresholds = tuple(sign * t for t in thresholds)
        assert min(thresholds) >= 0
        assert parity not in parities
        parities.add(parity)
        if selector != (0, 0) and u == 1:
            row = ((1, 0), (0, 1), (1, 1)).index(selector)
            assert thresholds == tuple(int(i == row) for i in range(3))
            light = tuple(-x for x in heavy)
            assert light not in sites
            sites.add(light)
            counts[row] += 1
        else:
            assert abs(guard_units) >= 2
            if 0 in thresholds:
                assert sorted(thresholds) == [0, 1, 1]
                counts["one zero"] += 1
            else:
                counts["positive"] += 1

assert len(parities) == 4095
assert counts == {0: 252, 1: 252, 2: 252, "one zero": 630, "positive": 2709}
assert len(sites) == 4852

theta = a / (3 * (1 + a))
phi = (1 - a) / (3 * (2 - a))
beta = 1 / ((1 + a) * (2 - a))
L = counts[0] * (theta + phi) * (1 - delta)**5
V = theta + phi * (1 - (1 - eps)**5)
W = 3339 * h**5 + 756 * (1 + delta)**5 * V + 1 + 3 * L
budget = gamma * h**5

thresholds = tuple(F(num, 10**9) for num in
                   (166735371, 166735294, 166324902, 166734811, 166734811, 166734811))
q1 = 3 * (1 - a) / (2 - a)
q2 = -(1 - a*a) / (a * (2 - a))
q = (1 - q1 - q2, q1, q2, F(0), F(0), F(0))
assert sum(thresholds) == 1 and q2 < 0

caps = []
for i, (threshold, slope) in enumerate(zip(thresholds, q)):
    assert 0 < threshold < 1
    cap = theta * (1 - threshold)**5
    if i != 2:
        assert 0 <= slope < 1 and threshold >= slope * eps
        tail = 1 - threshold - (1 - slope) * eps
        assert tail >= 0
        cap += phi * ((1 - threshold)**5 - tail**5) / (1 - slope)
    caps.append((1 + delta)**5 * cap)

row_slack = budget - (beta + L)
cap_slack = budget - max(caps)
surplus = W - 4096 * h**5
assert row_slack > F(1, 10**6)
assert cap_slack > F(1, 10**9)
assert surplus > F(4, 10**5)
assert budget / W < gamma / 4096

print(f"integer fibers       {len(sites)} (4095 heavy, 756 light, 1 origin)")
print(f"origin-cut slack     {float(row_slack):.12g}")
print(f"paired-cap slack     {float(cap_slack):.12g}")
print(f"total-volume surplus {float(surplus):.12g}")
