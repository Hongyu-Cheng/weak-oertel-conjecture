"""Exact calibrations for the quantitative face-exhaustion inequalities.

The all-body assertions are analytical. The body checks below use actual
two-base interval families; the envelope checks are only scalar identities.
"""
from fractions import Fraction as F

checks = 0


def ck(condition):
    global checks
    assert condition
    checks += 1


# P={0,1}, centered intervals of total volume 1. At an exposed base the
# exact ambient ordinary maximum is half the own interval length.
d, R, rb, v = 1, F(1, 2), F(1, 8), F(1, 4)
A = F(2)
qstar = rb
CV = 1 / rb
CD = CV + A
cm = d * v / (2 * R)
cF = qstar * cm / (2 * CD * (1 + CV))
ck(cF == F(1, 5760))
for numerator in range(1, 126):
    gap = F(numerator, 1000)
    lengths = [F(1, 2) + 2 * gap, F(1, 2) - 2 * gap]
    ck(sum(lengths) == 1 and min(lengths) >= v)
    Q = lengths[0] / 2
    ck(Q - F(1, 4) == gap)
    eta = gap
    ck(lengths[1] / 2 < Q - eta)
    t = eta / (2 * CD)
    new_lengths = [lengths[0], lengths[1] + 2 * t]
    ck(max(new_lengths) / 2 == Q)
    added = sum(new_lengths) - 1
    ck(cm * t <= added <= CV * t)
    drop = Q - Q / sum(new_lengths)
    ck(drop >= cF * eta)
    # The exact maximal expansion preserving Q reaches equal lengths and
    # the global ordinary infimum 1/4 in this two-base interval class.
    equalized = [lengths[0], lengths[1] + 4 * gap]
    ck(equalized[0] == equalized[1])
    ck(Q / sum(equalized) == F(1, 4))

for H in [F(1), F(3, 2), F(2), F(10), F(11520)]:
    for epsilon in [F(1, 100), F(1, 10), F(1)]:
        for c in [F(1, 100), F(1), F(3)]:
            crossing = c * epsilon / H
            for ratio in [F(0), F(1, 4), F(1, 2), F(1), F(2), F(10)]:
                g = ratio * crossing
                ck(max(g, c * epsilon - (H - 1) * g) >= crossing)
            ck(max(crossing, c * epsilon - (H - 1) * crossing) == crossing)

print(f"PASS: {checks:,} exact quantitative face-gap calibration checks")
