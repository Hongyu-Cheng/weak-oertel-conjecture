from fractions import Fraction

expected = [
    [27, -108, -108, 432, 432, 432],
    [54, -162, -135, 486, 405, 351],
    [-47, 94, -100, -188, 200, 316],
    [-20, 20, 124, -20, -124, 22],
    [-28, 0, 468, 0, 0, 480],
    [-20, -20, -82, -20, -82, 64],
    [-47, -94, -194, -188, -388, -272],
    [54, 162, 27, 486, 81, 27],
    [27, 108, 0, 432, 0, 0],
]
rows = []
points = 0
for x in range(-4, 5):
    row = [0] * 6
    for y in range(-4, 5):
        ell = (-x-y, 2*x-y, 2*y-x)
        if min(ell) < -4:
            continue
        points += 1
        high = 0
        for s in range(3):
            w = sum(t > 0 for t in ell)
            w += int(ell[1] == 0 and s >= 1)
            w += int(ell[2] == 0 and s <= 1)
            assert w in (1, 2)
            high += int(w == 2)
        coefficient = 27-31*high
        for i, value in enumerate((1, x, y, x*x, x*y, y*y)):
            row[i] += coefficient * value
    rows.append(row)
assert points == 31
assert rows == expected
totals = [sum(row[i] for row in rows) for i in range(6)]
assert totals == [0, 0, 0, 1420, 524, 1420]
assert Fraction(totals[3]+totals[5], 120) == Fraction(71, 3)
print('PASS: exact R4 projected stress moments and variance 71/3 per facet length')
