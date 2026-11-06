"""Exact all-anchor/all-real-parameter certificate optimization (stdlib)."""
from fractions import Fraction as Q


def f(r, a):
    return 4 * a * min(a, max(Q(0), r - 2 * a))


def anchor_terms(radii, j):
    return [(radii[j], 1)] + [
        (min(radii[j-h], radii[j+h]), 2)
        for h in range(1, min(j, len(radii)-1-j) + 1)
    ]


def exact_max(radii, j):
    terms = anchor_terms(radii, j)
    limit = radii[j] / 2
    events = sorted({Q(0), limit} | {
        x for r, _ in terms for x in (r/3, r/2) if x <= limit
    })
    candidates = set(events)
    for left, right in zip(events, events[1:]):
        mid = (left + right) / 2
        high = sum(w for r, w in terms if r >= 3 * mid)
        medium = [(r, w) for r, w in terms if 2*mid < r < 3*mid]
        count = sum(w for _, w in medium)
        radius_sum = sum((w*r for r, w in medium), Q(0))
        aa, bb = 4*high - 8*count, 4*radius_sum
        # Verify the polynomial identification at two distinct interior points.
        for x in ((2*left+right)/3, (left+2*right)/3):
            assert sum((w*f(r, x) for r, w in terms), Q(0)) == aa*x*x + bb*x
        if aa < 0:
            vertex = -bb / (2*aa)
            if left <= vertex <= right:
                candidates.add(vertex)
    values = {x: sum((w*f(r, x) for r, w in terms), Q(0)) for x in candidates}
    best = max(values.values())
    return best, sorted(x for x, v in values.items() if v == best)


def profile_max(radii):
    radii = list(map(Q, radii))
    assert all(r > 0 for r in radii)
    assert all(2*radii[i] >= radii[i-1]+radii[i+1] for i in range(1, len(radii)-1))
    results = [exact_max(radii, j) for j in range(len(radii))]
    return max(v for v, _ in results), results


def main():
    best, anchors = profile_max([1, 2, 2, 1])
    assert [v for v, _ in anchors] == [Q(4, 9), Q(16, 9), Q(16, 9), Q(4, 9)]
    assert best == Q(16, 9) < Q(20, 9)
    assert anchors[1][1] == [Q(2, 3)]
    assert Q(4, 9)*4 + Q(1, 2) == Q(41, 18) > Q(20, 9)
    best, anchors = profile_max([4, 7, 7, 4])
    assert best == Q(196, 9)
    assert Q(2, 9)*sum(Q(r*r) for r in [4, 7, 7, 4]) == Q(260, 9)
    assert best / Q(260, 9) == Q(49, 65)
    checks = 0
    for denominator in range(1, 21):
        for numerator in range((3*denominator+1)//2, 8*denominator+1):
            radius = Q(numerator, denominator)
            value, _ = profile_max([Q(1), radius, radius, Q(1)])
            assert value == max(Q(4, 3), Q(4, 9)*radius*radius)
            assert value < Q(4, 9)*(radius*radius+1)
            checks += 1
    # Layer-cake integral is simply the length of [2a,3a] intersected with [0,r].
    for r in [Q(1), Q(7, 4), Q(2), Q(7)]:
        for k in range(121):
            a = Q(k, 30)
            assert f(r, a) == 4*a*max(Q(0), min(3*a, r)-2*a)
    print(f"PASS: exact all-anchor maxima; {checks} rational family profiles; 484 layer-cake checks.")


if __name__ == '__main__':
    main()
