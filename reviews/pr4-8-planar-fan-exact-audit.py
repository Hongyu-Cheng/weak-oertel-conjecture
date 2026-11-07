"""Independent exact-rational checks of the PR #4 planar fan pair claims.

This clips the reference triangle directly and enumerates every vertex triangle
in each missed-pair polygon. It does not reuse the proofs' case selections or
their scalar formulae. The finite sample is regression evidence, not a proof of
the universally quantified statements.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from random import Random

TRIANGLE = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
SEED = 20261107
RANDOM_FANS = 12000


def cross(p, q):
    return p[0] * q[1] - p[1] * q[0]


def value(normal, center, point):
    return sum(normal[k] * (point[k] - center[k]) for k in range(2))


def clip(polygon, normal, center, orientation):
    """Clip by orientation * normal dot (x - center) >= 0, exactly."""
    if not polygon:
        return []
    answer = []
    for a, b in zip(polygon, polygon[1:] + polygon[:1]):
        va = orientation * value(normal, center, a)
        vb = orientation * value(normal, center, b)
        if va >= 0:
            answer.append(a)
        if (va < 0 < vb) or (vb < 0 < va):
            t = va / (va - vb)
            answer.append(tuple(a[k] + t * (b[k] - a[k]) for k in range(2)))
    result = []
    for p in answer:
        if not result or p != result[-1]:
            result.append(p)
    if len(result) > 1 and result[0] == result[-1]:
        result.pop()
    return result


def area_ratio(polygon):
    if len(polygon) < 3:
        return F(0)
    return abs(sum(cross(a, b) for a, b in zip(polygon, polygon[1:] + polygon[:1])))


def triangle_capacity_ratio(polygon):
    # Separate convexity of the determinant makes vertex triples sufficient.
    return max((abs(cross((b[0] - a[0], b[1] - a[1]),
                          (c[0] - a[0], c[1] - a[1])))
                for a, b, c in combinations(polygon, 3)), default=F(0))


def classify(signs):
    counts = [sum(v > 0 for v in row) for row in signs]
    pattern = "".join(map(str, sorted(counts)))
    if pattern == "112":
        apexes = [row.index(next(v for v in row if v > 0))
                  for row in signs if sum(v > 0 for v in row) == 1]
        return pattern + ("-repeated" if apexes[0] == apexes[1] else "-distinct")
    if pattern == "122":
        apexes = [row.index(next(v for v in row if v < 0))
                  for row in signs if sum(v > 0 for v in row) == 2]
        return pattern + ("-repeated" if apexes[0] == apexes[1] else "-distinct")
    return pattern


counts = {}
minimum_pair_surplus = {}
minimum_capacity_gap = {}


def check(center, normals):
    signs = [[value(n, center, p) for p in TRIANGLE] for n in normals]
    if any(v == 0 for row in signs for v in row):
        return False
    assert cross(normals[0], normals[1]) != 0
    assert all(sum(n[k] for n in normals) == 0 for k in range(2))
    kind = classify(signs)
    assert kind in {"111", "222", "112-repeated", "112-distinct",
                    "122-repeated", "122-distinct"}
    own = [area_ratio(clip(TRIANGLE, n, center, 1)) for n in normals]
    target = F(1) if kind in {"222", "112-repeated"} else F(8, 9)
    strict = kind not in {"111", "112-distinct"}
    certificates = []
    for i, j in combinations(range(3), 2):
        missed = clip(clip(TRIANGLE, normals[i], center, -1),
                      normals[j], center, -1)
        capacity = triangle_capacity_ratio(missed)
        surplus = own[i] + own[j] - target
        if capacity < F(1, 4) and (surplus > 0 if strict else surplus >= 0):
            certificates.append((surplus, F(1, 4) - capacity))
    assert certificates, {
        "center": str(center), "normals": normals,
        "class": kind, "own": list(map(str, own)),
    }
    # Select a reproducible pair only after checking all three directly.
    surplus, gap = max(certificates)
    counts[kind] = counts.get(kind, 0) + 1
    minimum_pair_surplus[kind] = min(minimum_pair_surplus.get(kind, surplus), surplus)
    minimum_capacity_gap[kind] = min(minimum_capacity_gap.get(kind, gap), gap)
    return True


# Symmetric sharp fan and its reversal.
for s in (1, -1):
    check((F(1, 3), F(1, 3)), [(s, 0), (0, s), (-s, -s)])

rng = Random(SEED)
accepted = 0
attempts = 0
while accepted < RANDOM_FANS:
    attempts += 1
    weights = [rng.randrange(1, 101) for _ in range(3)]
    total = sum(weights)
    center = (F(weights[1], total), F(weights[2], total))
    u = (rng.randrange(-30, 31), rng.randrange(-30, 31))
    v = (rng.randrange(-30, 31), rng.randrange(-30, 31))
    if cross(u, v) == 0:
        continue
    normals = [u, v, (-u[0] - v[0], -u[1] - v[1])]
    accepted += check(center, normals)

assert len(counts) == 6
print(json.dumps({
    "verdict": "PASS_EXACT_RATIONAL_PLANAR_FAN_PAIR_SAMPLES",
    "seed": SEED,
    "random_accepted": accepted,
    "random_attempts": attempts,
    "total_checked": sum(counts.values()),
    "sign_class_counts": counts,
    "minimum_selected_pair_surplus": {k: str(v) for k, v in minimum_pair_surplus.items()},
    "minimum_selected_capacity_gap_to_one_quarter": {k: str(v) for k, v in minimum_capacity_gap.items()},
    "scope": "Finite exact regression of six strict sign classes; analytic perturbation and all-direction center arguments are audited separately."
}, indent=2))
