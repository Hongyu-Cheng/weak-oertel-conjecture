from fractions import Fraction as F


def pos(x):
    return max(F(0), x)


scalar_checks = 0
for d in list(range(2, 13)) + [16, 20, 32, 64]:
    gamma = F(d, d + 1) ** d
    s = F(d + 1, d)
    for bi in range(10, 21):
        b = F(bi, 20)
        for ci in range(bi, 21):
            c = F(ci, 20)
            eta = pos(s * b + 2 * c - 2)
            h = pos(b - F(2 * d, d + 1) * (1 - c))
            gap = 1 + eta**d - (2 * b - 1)**d - b**d - c**d
            assert gap >= 0, (d, b, c)
            assert eta == s * h
            transformed = gamma + h**d / 2 - gamma * (
                1 + (2 * b - 1)**d + b**d + c**d
            ) / 2
            assert transformed == gamma * gap / 2
            scalar_checks += 1
    # All-dimensional diagonal estimate checked on rational u.
    for ui in range(41):
        u = F(ui, 40)
        odd_difference = (1 + u)**d - (1 - u)**d
        assert odd_difference >= 2 * d * u
        v = 2 * d * u
        assert v + pos(1 + (1 - v) / d)**d >= 2
        scalar_checks += 1

for ci in range(25, 41):
    c = F(ci, 40)
    left = F(3, 4) + (2 * c - F(5, 4))**2 - c*c
    assert left == 3 * (c - F(5, 6))**2 + F(11, 48)

d = 20
gamma = F(20, 21)**20
radii = [F(x, 100) for x in (94, 97, 100, 103)]
assert all(radii[i+1] - radii[i] == F(3, 100) for i in range(3))
mass = sum(r**d for r in radii)
target = gamma * mass / 2
middle_upper = gamma + 4 * gamma**2 * radii[1]**d
heavy = gamma * radii[3]**d
assert target > middle_upper
assert target > heavy
integer_middle = 21**20 * (94**20 + 97**20 - 100**20 + 103**20) - 8 * 20**20 * 97**20
integer_heavy = 94**20 + 97**20 + 100**20 - 103**20
assert integer_middle == 1137549378322964594658090728038214421874179602838935201279638978
assert integer_heavy == 277893493887952690657232019960683602976
assert integer_middle > 0 and integer_heavy > 0
assert 2 * sum(r**d for r in radii[:3]) > mass
assert 2 * sum(r**d for r in radii[2:]) > mass
assert gamma * min(sum(r**d for r in radii[:3]), sum(r**d for r in radii[2:])) > target

print(f'PASS: {scalar_checks} exact peak/diagonal checks; d=2 boundary identity; exact d=20 certificate and actual safe-center tail checks.')
