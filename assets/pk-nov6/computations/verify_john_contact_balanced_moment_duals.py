from fractions import Fraction as F

z = [-1, 0, 1]
lo = [F(-21, 80), F(-1, 2), F(-59, 80)]
hi = [F(-13, 80), F(1, 2), F(5, 16)]
w = [b - a for a, b in zip(lo, hi)]
t, T = F(11, 20), F(6, 5)
c, R = F(-359, 5280), F(1597, 5280)
pairs = [(F(1), F(-19, 80), F(1, 30)), (F(-1), F(-39, 80), F(3, 20))]
expected_masses = [[F(1, 24), F(7, 15), F(1, 24)], [F(1, 10), F(7, 20), F(1, 10)]]
expected_centers = [F(619, 2640), F(-163, 440)]
hinges = []
for (u, a, b), expected, center in zip(pairs, expected_masses, expected_centers):
    masses, moments, hinge = [], [], F(0)
    for j, l, h in zip(z, lo, hi):
        threshold = (b - a * j) / u
        left, right = (max(l, threshold), h) if u > 0 else (l, min(h, threshold))
        if left >= right:
            left = right
        mass = right - left
        moment = (right * right - left * left) / 2
        masses.append(mass)
        moments.append(moment)
        hinge += u * moment + (a * j - b) * mass
    assert masses == expected
    assert sum(masses) == t
    assert sum(j * m for j, m in zip(z, masses)) == 0
    assert sum(moments) == t * center
    assert hinge == t * (u * center - b)
    hinges.append(hinge / R)
assert expected_centers == [c + R, c - R]
abar = sum(a / R for u, a, b in pairs) / 2
B = sum((b - u * c) / R for u, a, b in pairs) / 2
total_hinge = sum(hinges) / 2
assert abar == -F(1914, 1597)
assert B == F(484, 1597)
assert total_hinge == F(12243, 31940) == t * (1 - B)
base_hinge = sum(ww * max(abar * j - B, F(0)) for ww, j in zip(w, z))
assert base_hinge == F(143, 1597) <= total_hinge
assert total_hinge <= t * T / (T - t) == F(66, 65)

bad_slope = F(-707, 1056)
bad_masses = [max(F(0), min(h, c + bad_slope * j) - l) for j, l, h in zip(z, lo, hi)]
assert bad_masses == [F(1, 10), c + F(1, 2), F(0)]
assert sum(bad_masses) == F(2809, 5280) < sum(w) / 4 == F(2838, 5280)
assert sum(j * m for j, m in zip(z, bad_masses)) == -F(1, 10)
print('PASS: exact John source duals, surviving integer coefficient, hinge identity, and bad cap')
