"""Check the dimension-19 support, local inequalities, and exact mass margins."""

from fractions import Fraction as F
from itertools import combinations, product
from math import comb


ordinary, n, d = 11, 14, 5
a, delta = F(2, 3), F(69, 100)
large_scale, small_scale = 1 + delta, 1 - delta
assert n + d == 19 and 0 < a < 1 and 0 < small_scale < large_scale

# The free vertices have all three scores zero. The other vertices of U_0
# are represented by their first three barycentric coordinates.
coefficients = (1, -a, a - 1)
score_rows = [tuple(coefficients[(i - j) % 3] for i in range(3)) for j in range(3)]
assert all(sum(row) == 0 and max(map(abs, row)) == 1 for row in score_rows)
assert all(sum(column) == 0 for column in zip(*score_rows))
vertices = ((1, 0, 0), (F(1, 3),) * 3, (1 / (1 + a), 0, a / (1 + a)))
assert all(sum(vertex) == 1 and min(vertex) >= 0 for vertex in vertices)
max_scores = [
    max(sum(c * x for c, x in zip(row, vertex)) for vertex in vertices)
    for row in score_rows
]
assert max_scores[1:] == [0, 0]


def resource(base):
    return sum(base[:ordinary]) - 5 * sum(base[ordinary:])


def check_base(base, scale):
    entries = set(base)
    assert len(base) == n and (entries <= {0, 1} or entries <= {0, -1})
    assert base not in sites
    sites.add(base)
    r = resource(base)
    assert r >= 0 and scale > 0
    if r == 0:
        assert scale <= 1 + delta * sum(base[ordinary:])
    return r, tuple(5 * r + 3 * entry for entry in base[ordinary:])


sites = set()
origin_data = check_base((0,) * n, F(1))
assert origin_data == (0, (0, 0, 0))
balanced_large = 0
for indicator in product((0, 1), repeat=n):
    if not any(indicator):
        continue
    base = indicator if resource(indicator) >= 0 else tuple(-entry for entry in indicator)
    r, thresholds = check_base(base, large_scale)
    if r > 0:
        assert min(thresholds) > large_scale
    else:
        balanced_large += 1
        assert all(entry >= 0 for entry in base)
        selectors = base[ordinary:]
        owners = [j for j, entry in enumerate(selectors) if entry]
        assert owners
        for j, entry in enumerate(selectors):
            if entry:
                assert thresholds[j] > large_scale
            else:
                assert thresholds[j] == 0
                assert all(max_scores[(j - owner) % 3] == 0 for owner in owners)

large_count = len(sites) - 1
small_counts = [0] * 3
for j in range(3):
    for subset in combinations(range(ordinary), 5):
        support = {*subset, ordinary + j}
        base = tuple(-int(i in support) for i in range(n))
        assert tuple(-entry for entry in base) in sites
        r, thresholds = check_base(base, small_scale)
        assert r == 0 and thresholds[j] < -small_scale
        assert all(thresholds[i] == 0 for i in range(3) if i != j)
        small_counts[j] += 1

assert large_count == 2**n - 1 and balanced_large == 1419
assert small_counts == [comb(ordinary, 5)] * 3 and len(sites) == 17_770

gamma = F(d, d + 1) ** d
beta = 1 / ((1 + a) * (2 - a))
m = vertices[1][1] * vertices[2][2] * large_scale**d
small_mass = (F(2, 3) - beta) * small_scale**d
assert 0 < m and 0 < small_mass
total = 1 + large_count * m + sum(small_counts) * small_mass
surplus = total - 2**n * m
slack = gamma * m - max(beta + count * small_mass for count in small_counts)

assert surplus == F(6486053963, 300000000000) > 0
assert slack == F(1235613187493, 583200000000000) > 0
assert gamma * m / total < gamma / 2**n
print(f"support = {len(sites)} (1 origin, {large_count} large, {sum(small_counts)} small)")
print(f"balanced large sites = {balanced_large}")
print(f"mass surplus = {surplus} ({float(surplus):.12g})")
print(f"row slack = {slack} ({float(slack):.12g})")
print(f"relative depth gap = {surplus / total} ({float(surplus / total):.12g})")
