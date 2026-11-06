"""Exact d=1 checks of the new arithmetic interpolation inequality."""
from fractions import Fraction as F
from itertools import product
from random import Random


def union_length(intervals):
    result = F(0)
    if not intervals:
        return result
    intervals = sorted(intervals)
    lo, hi = intervals[0]
    for left, right in intervals[1:]:
        if left > hi:
            result += hi - lo
            lo, hi = left, right
        else:
            hi = max(hi, right)
    return result + hi - lo


def output_mass(a_source, b_source, lam):
    outputs = {}
    for p, (lo_a, hi_a) in a_source.items():
        for q, (lo_b, hi_b) in b_source.items():
            target = tuple((1 - lam) * x + lam * y for x, y in zip(p, q))
            assert all(z.denominator == 1 for z in target)
            outputs.setdefault(target, []).append(((1 - lam) * lo_a + lam * lo_b,
                                                  (1 - lam) * hi_a + lam * hi_b))
    return sum((union_length(intervals) for intervals in outputs.values()), F(0))


def source_data(source):
    masses = [hi - lo for lo, hi in source.values()]
    return sum(masses, F(0)), max(masses)


def check(a_source, b_source, lam, actual=None):
    m_a, peak_a = source_data(a_source)
    m_b, peak_b = source_data(b_source)
    target = output_mass(a_source, b_source, lam)
    # The stronger normalized-level Bonnesen bound, with no balance condition.
    effective_count = m_a / peak_a + m_b / peak_b - 1
    assert target >= effective_count * ((1 - lam) * peak_a + lam * peak_b)
    if actual is not None:
        assert actual >= target
    cs = [F(i, 8) for i in range(9)]
    if lam == F(1, 2):
        ra, rb = m_a / peak_a, m_b / peak_b
        c_opt = ra - (ra + rb - 1) * peak_a / (peak_a + peak_b)
        if 0 <= c_opt <= 1:
            cs.append(c_opt)
            assert target >= (ra + rb - 1) * (peak_a + peak_b) / 2
    for c in cs:
        x = (1 - lam) * (m_a - c * peak_a)
        y = lam * (m_b - (1 - c) * peak_b)
        gap = target - x - y
        # Exactly equivalent to target >= (sqrt(x)+sqrt(y))^2.
        assert gap >= 0 and gap * gap >= 4 * x * y, (a_source, b_source, lam, c)
    return len(cs)


rng = Random(260918)
checks = 0
for dim in (1, 2, 3):
    for modulus, lam in ((2, F(1, 2)), (3, F(1, 3)), (3, F(2, 3))):
        pool = list(product(range(4), repeat=dim))
        for repetition in range(90):
            sources = []
            for ignored in range(2):
                bases = rng.sample(pool, rng.randint(1, min(8, len(pool))))
                source = {}
                for p in bases:
                    lo = F(rng.randint(-12, 12), rng.randint(1, 4))
                    length = F(rng.randint(1, 14), rng.randint(1, 4))
                    source[tuple(modulus * z for z in p)] = (lo, lo + length)
                sources.append(source)
            checks += check(*sources, lam)


# Different thresholds on the SAME actual convex body:
# -4<=z<=4, |x|<=20-z^2, and ell(z,x)=z+x.
def cap_source(residue, threshold):
    source = {}
    for z in range(-4, 5):
        if residue is not None and z % 2 != residue:
            continue
        radius = F(20 - z * z)
        lo, hi = max(-radius, threshold - z), radius
        if hi > lo:
            source[(z,)] = (lo, hi)
    return source


for residue in (0, 1):
    for s, t in product([F(-30), F(-7), F(0), F(7, 2), F(18), F(22)], repeat=2):
        left, right = cap_source(residue, s), cap_source(residue, t)
        if not left or not right:
            continue
        all_cap = cap_source(None, (s + t) / 2)
        actual = source_data(all_cap)[0]
        checks += check(left, right, F(1, 2), actual=actual)

print("PASS:", checks, "exact radical-free interpolation inequalities")
print("Includes nonconvex output-fiber unions, singleton inputs, c endpoints,")
print("integer ranks 1-3, unequal weights, and oblique cap thresholds on one body.")
print("These finite checks do not prove OC or replace the general proof.")
