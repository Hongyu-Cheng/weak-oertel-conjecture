from fractions import Fraction as F
import itertools

checks = 0
half = F(1, 2)


def clip(x, top=half):
    return min(top, max(F(0), x))


for a, b in itertools.product((F(i, 16) for i in range(9)), repeat=2):
    for x in (F(i, 16) for i in range(17)):
        w0 = min(x, 1-x)
        wa, wb = min(a, half-a), min(b, half-b)
        atomic = w0+min(wa, wb) if 2*x == a+b else w0
        assert atomic <= half
        checks += 1

maximum = F(0)
argmax = []
for x in (F(i, 128) for i in range(129)):
    breakpoints = [-x, half-x, x, x-half, F(-3), F(3)]
    upper_pair = min(clip(half-x+t)+clip(half-x-t) for t in breakpoints)
    lower_pair = min(clip(x+t)+clip(x-t) for t in breakpoints)
    assert upper_pair == min(half, max(F(0), 1-2*x))
    assert lower_pair == min(2*x, half)
    depth = min(1-x+upper_pair, x+lower_pair)
    assert depth <= F(7, 8)
    checks += 3
    if depth > maximum:
        maximum, argmax = depth, [x]
    elif depth == maximum:
        argmax.append(x)
assert maximum == F(7, 8) and argmax == [F(3, 8)]
assert F(1, 2) < F(9, 16) < maximum
checks += 2
print(f"PASS: {checks:,} exact checks")
