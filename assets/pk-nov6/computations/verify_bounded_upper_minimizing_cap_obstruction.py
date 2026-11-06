from fractions import Fraction as F


def second(v):
    return [v[j - 1] - 2 * v[j] + v[j + 1] for j in range(1, len(v) - 1)]


def cap(z, w, r, a):
    return sum(max(F(0), min(ww, rr + a * i)) for i, ww, rr in zip(z, w, r))


def breaks(z, w, r):
    return sorted({a for i, ww, rr in zip(z, w, r) if i for a in (-rr / i, (ww - rr) / i)})


def minimum(z, w, r, interval=None):
    candidates = breaks(z, w, r)
    if interval is not None:
        lo, hi = interval
        candidates = [lo, hi] + [a for a in candidates if lo <= a <= hi]
    return min(cap(z, w, r, a) for a in candidates)


z = list(range(-2, 3))
w = [F(92, 5), F(223, 10), F(126, 5), F(231, 10), F(18)]
r = [F(59737, 4280) + v for v in (F(0), F(0), -F(3, 4), -F(21, 4), -F(21, 2))]
l = [rr - ww for rr, ww in zip(r, w)]
rm = [-ll for ll in l]
M, Q, H = sum(w), sum(ww * ww for ww in w), max(w)
assert (M, Q, H) == (107, F(4657, 2), F(126, 5))
assert second(w) == [-1, -5, -3]
assert second(r) == [-F(3, 4), -F(15, 4), -F(3, 4)]
assert second(l) == [F(1, 4), F(5, 4), F(9, 4)]
assert sum(i * ww for i, ww in zip(z, w)) == 0
assert sum(ww * rr for ww, rr in zip(w, r)) == Q / 2
assert l[2] < 0 < r[2]

expected = [
    [(-74534, 230723), (-71414, 232283), (-19015, 232283), (-14797, 228065),
     (59737, 228065), (62243, 230571), (119474, 230571), (123202, 232435)],
    [(-123202, 225525), (-119474, 227389), (-62243, 227389), (-59737, 229895),
     (14797, 229895), (19015, 225677), (71414, 225677), (74534, 227237)],
]
intervals = []
for rr, table in zip((r, rm), expected):
    actual = [(8560 * a, 4280 * cap(z, w, rr, a)) for a in breaks(z, w, rr)]
    assert actual == table
    lo = max((H - v) / i for i, v in zip(z, rr) if i < 0)
    hi = min((H - v) / i for i, v in zip(z, rr) if i > 0)
    assert rr[2] <= H and lo <= hi
    intervals.append((lo, hi))
assert intervals == [(F(-48119, 8560), F(93059, 8560)), (F(-88841, 8560), F(45613, 8560))]
assert minimum(z, w, r) == F(45613, 856)
assert minimum(z, w, rm) == F(45105, 856)
assert minimum(z, w, r, intervals[0]) == F(45613, 856)
assert minimum(z, w, rm, intervals[1]) == F(225677, 4280)
assert F(225677, 4280) - F(45105, 856) == F(19, 535)
assert rm[0] + 2 * F(61601, 4280) == F(142217, 4280) > H
assert sum(ww for i, ww in zip(z, w) if i <= 0) == F(659, 10) > F(45105, 856)
assert sum(ww for i, ww in zip(z, w) if i >= 0) == F(663, 10) > F(45105, 856)
assert Q / (2 * H) == F(23285, 504)
assert F(45105, 856) - Q / (2 * H) == F(43765, 6741)

z3 = [-1, 0, 1]
w3 = [F(1), F(3, 2), F(1)]
r3 = [F(11, 28), F(25, 28), F(11, 28)]
rm3 = [ww - rr for ww, rr in zip(w3, r3)]
assert rm3 == [F(17, 28)] * 3
assert sum(ww * rr for ww, rr in zip(w3, r3)) == sum(ww * ww for ww in w3) / 2
assert minimum(z3, w3, r3) == F(47, 28)
assert minimum(z3, w3, rm3) == F(45, 28)
assert cap(z3, w3, rm3, F(0)) == F(51, 28)
assert cap(z3, w3, rm3, F(17, 28)) == F(45, 28)
print('PASS: exact five-fiber and three-fiber angular-minimum obstructions')
