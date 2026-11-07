"""Exact supplementary checks for the actual crossflow/midpoint note.

The measure-theoretic proof is in the Markdown source. These checks verify
the complete rational square-face transport, its actual cap selectors,
normal normalization, and the all-cap midpoint indicator implication.
No numerical tolerance, ordinary criticality, or global OC claim is used.
"""

from fractions import Fraction as F
from itertools import product, permutations

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


b = F(1, 3)
beta = F(19, 36)
normals = [(1, 0), (-1, 0), (0, 1), (0, -1)]
caps = [(v, a) for v in normals for a in (-2, 2)]


def dot(v, x):
    return sum(F(a) * F(c) for a, c in zip(v, x))


def cap_bit(z, x, v, a, level=-b):
    return int(F(a) * z + dot(v, x) >= level)


def load(z, x):
    return sum(F(cap_bit(z, x, v, a), 8) for v, a in caps)


# Entire exact status intervals are certified by testing their endpoints
# and interior on the affine cap equations, with knot values kept separate.
knots = [-F(1), -b, b, F(1)]
for n in normals:
    e = (-n[1], n[0])
    for z in (-1, 1):
        for t in [F(j, 30) for j in range(-30, 31)]:
            x = tuple(n[i] + t * e[i] for i in (0, 1))
            check(load(z, x) == F(1, 2))
    for lo, hi in zip(knots[:-1], knots[1:]):
        t = (lo + hi) / 2
        x = tuple(n[i] + t * e[i] for i in (0, 1))
        check(load(0, x) == (F(3, 4) if abs(t) < b else F(1, 2)))
        for v, a in caps:
            vals = [dot(v, tuple(n[i] + t0 * e[i] for i in (0, 1))) + b
                    for t0 in (lo, hi)]
            check(vals[0] * vals[1] >= 0)

middle_selected = 2 * b * F(3, 4) + (2 - 2 * b) * F(1, 2)
check(middle_selected == F(7, 6))
check((middle_selected + 2) / 6 == beta)
check(F(1, 2) / beta == F(18, 19))
check(F(3, 4) / beta == F(27, 19))
check(middle_selected - 2 * beta == F(1, 9))

# A full face target has unit density. The baseline plus each pushforward
# branch has density 18/19 + (9/19)*(1/3)*(1/3) = 1.
baseline = F(18, 19)
extra = F(9, 19)
branch = F(1, 3)
jacobian = F(3)
check(baseline + extra * branch / jacobian == 1)
check(extra * branch / jacobian == F(1, 19))
check(2 * b * extra * branch == F(2, 19))
check(2 * beta * F(2, 19) == F(1, 9))
check(2 * baseline + 2 * b * extra == F(42, 19))
check(F(42, 19) == 2 + 2 * F(2, 19))
check(2 * baseline * 2 + F(42, 19) == 6)

# Conditional probabilities after the two overlapping source components
# are combined: baseline 2/3 and each of the three branches 1/9.
check(baseline / (baseline + extra) == F(2, 3))
check(extra * branch / (baseline + extra) == F(1, 9))
check(F(2, 3) + 3 * F(1, 9) == 1)

for n in normals:
    e = (-n[1], n[0])
    for j in range(-30, 31):
        t = F(j, 90)
        source = (F(0), *(n[i] + t * e[i] for i in (0, 1)))
        targets = [
            (F(0), *(n[i] + 3 * t * e[i] for i in (0, 1))),
            (F(-1), *(n[i] + 3 * t * e[i] for i in (0, 1))),
            (F(1), *(n[i] - 3 * t * e[i] for i in (0, 1))),
        ]
        for k in range(3):
            check(sum(row[k] for row in targets) / 3 == source[k])
        for row in targets:
            check(max(abs(row[1]), abs(row[2])) <= 1)
            check(dot(n, row[1:]) == 1)
        midpoint = tuple((targets[1][i] + targets[2][i]) / 2 for i in range(3))
        check(midpoint == (F(0), F(n[0]), F(n[1])))

# One common tuple law handles every cap; verify all rational affine sign
# patterns in a finite exact grid, including equality at the midpoint.
for n in normals:
    e = (-n[1], n[0])
    for t in [F(j, 12) for j in range(-4, 5)]:
        xm = tuple(n[i] + 3 * t * e[i] for i in (0, 1))
        xp = tuple(n[i] - 3 * t * e[i] for i in (0, 1))
        for a, u1, u2 in product(range(-2, 3), repeat=3):
            if a == u1 == u2 == 0:
                continue
            u = (u1, u2)
            midpoint_value = dot(u, n)
            for c in (midpoint_value - 1, midpoint_value, midpoint_value + 1):
                endpoints = cap_bit(-1, xm, u, a, c) + cap_bit(1, xp, u, a, c)
                check(endpoints >= int(midpoint_value >= c))

# Actual volume and distinction from an ordinary critical volume budget.
cap_volume = F(4) + 2 * (1 + b)
check(cap_volume == F(20, 3))
check(cap_volume / 12 == F(5, 9))
check(cap_volume / 12 != beta)
check(F(2, 19) > 0)  # positive rho mass on a surface-null singleton

# A DIFFERENT whole martingale regularizes rho in this example. This is
# deliberately distinct from changing the forced pairing of the first law.
check(F(27, 19) - F(21, 19) == F(6, 19))
check(F(18, 19) + F(6, 19) / 2 == F(21, 19))
check(F(21, 19) * F(19, 21) == 1)
check(F(21, 19) * F(1, 21) == F(1, 19))
check(F(19, 21) + 2 * F(1, 21) == 1)
for j in range(-30, 31):
    t = F(j, 90)
    check((t - F(2, 3) + t + F(2, 3)) / 2 == t)
    check(-1 <= t - F(2, 3) <= -b)
    check(b <= t + F(2, 3) <= 1)

# Exact call-payoff rearrangement against every permutation coupling of
# each finite equal-mass test pair. These atomic tests certify the ordering
# statement, not the separate continuous-density claim.
test_rows = [
    ([-3, -1, 2, 6], [-4, 0, 1, 7]),
    ([-2, -2, 1, 1], [-5, 0, 0, 4]),
    ([F(-5, 3), F(-1, 3), F(2, 3), F(8, 3)],
     [F(-3, 2), F(1, 2), F(3, 2), F(7, 2)]),
]
for xs, ys in test_rows:
    quantile_midpoints = [(F(x) + F(y)) / 2 for x, y in zip(xs, ys)]
    for perm in permutations(ys):
        mids = [(F(x) + F(y)) / 2 for x, y in zip(xs, perm)]
        check(sum(mids) == sum(quantile_midpoints))
        knots = sorted(set(mids + quantile_midpoints))
        for k in knots:
            old_call = sum(max(v-k, 0) for v in mids)
            max_call = sum(max(v-k, 0) for v in quantile_midpoints)
            check(old_call <= max_call)

# Exact continuous piecewise-affine quantile expansion. Jumps are allowed;
# every slope at least one implies midpoint density at most one.
rank = [F(j, 12) for j in range(13)]
def qminus(t):
    return -2 + t + max(t-F(1, 3), 0) + int(t > F(2, 3))

def qplus(t):
    return -1 + 2*t + 2*max(t-F(1, 2), 0)

for i, s in enumerate(rank):
    for t in rank[i+1:]:
        check(qminus(t)-qminus(s) >= t-s)
        check(qplus(t)-qplus(s) >= t-s)
        check((qminus(t)+qplus(t)-qminus(s)-qplus(s))/2 >= t-s)

# Harmonic density is attained by uniform equal-mass endpoint intervals.
for cminus, cplus, mass in product([F(1, 4), F(1, 2), F(1)], repeat=3):
    midpoint_length = mass * (1/cminus + 1/cplus) / 2
    density = mass / midpoint_length
    check(density == 2/(1/cminus+1/cplus))
    check(density <= 1)

print(f"PASS: {checks:,} exact checks")
