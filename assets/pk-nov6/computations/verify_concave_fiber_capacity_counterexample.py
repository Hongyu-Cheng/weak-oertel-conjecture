"""Exact arithmetic certificate, not a numerical search."""
from fractions import Fraction as F


def u(z):
    return min(z, 2-z) + F(1, 10)


def g(z, x):
    return min(3-z+F(3, 2)*x, 1000*x, 1000*(u(z)-x))


xs = [F(194, 2003), F(2196, 2003), F(198, 2003)]
peaks = [F(6300, 2003), F(7300, 2003), F(2300, 2003)]
for z in range(3):
    formula_x = (1000*u(z)-(3-z))/(1000+F(3, 2))
    assert formula_x == xs[z]
    assert 0 < xs[z] < u(z)
    assert g(z, xs[z]) == peaks[z]
    assert 3-z+F(3, 2)*xs[z] == 1000*(u(z)-xs[z])
    assert 1000*xs[z] > peaks[z]
    assert g(z, 0) == g(z, u(z)) == 0
assert sum(peaks)/2 == F(7950, 2003)
assert max(peaks) == peaks[1]
assert sum(peaks)/2-peaks[1] == F(650, 2003)
assert peaks[1]-(F(43, 20)+peaks[2]) == F(13871, 40060) > 0
assert xs[1] > F(1, 10)

squares = [F(41, 20)**2, F(41, 20)**2, F(21, 20)**2]
assert squares == [F(1681, 400), F(1681, 400), F(441, 400)]
assert F(31, 20)**2+squares[2] == F(1402, 400) < squares[1]
assert sum(squares)/2-squares[1] == F(441, 800) > 0
print("All exact concave-capacity counterexample checks passed.")
