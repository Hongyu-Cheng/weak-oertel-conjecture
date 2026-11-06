from fractions import Fraction as F

b, c, gamma = F(1, 3), F(2, 3), F(4, 9)
checks = 0
for denom in [100, 101, 128, 200, 1000, 10000]:
    eps = F(1, denom)
    e = eps * (c + eps)
    assert (b + eps) ** 2 - b**2 == e
    for N in range(3, 80):
        theta = e / (4 * N)
        assert 0 < theta <= eps / 16
        weights = 2 * (b - theta) / (c + eps)
        assert 0 < weights < 1
        B0 = N * (c - 2 * theta) ** 2 + e * ((c - 2 * theta) / (c + eps)) ** 2
        Bi = N * (c + theta) ** 2 + e * (1 - (b - theta) ** 2 / (b * (b + eps)))
        upper = N * gamma + e * (F(1, 3) + F(217, 6400))
        target = gamma * (N + e)
        assert B0 <= N * gamma + e * (F(1, 3) + theta)
        assert Bi <= N * gamma + e * (F(1, 3) + 3 * eps + F(25, 4) * theta)
        assert max(B0, Bi) <= upper < target
        assert target - upper == F(4447, 57600) * e
        assert N * gamma / (N + e) > gamma / 2
        if N % 2:
            assert gamma * ((N + 1) // 2) / (N + e) > gamma / 2
        checks += 1

eps, N = F(1, 100), 3
e = eps * (c + eps)
theta = e / (4 * N)
B0 = N * (c - 2 * theta) ** 2 + e * ((c - 2 * theta) / (c + eps)) ** 2
Bi = N * (c + theta) ** 2 + e * (1 - (b - theta) ** 2 / (b * (b + eps)))
print(f"PASS: {checks} exact source/meeting/cap budget checks.")
print("N=3, epsilon=1/100:")
print("e =", e, "theta =", theta)
print("canonical cap ratios =", B0 / (N + e), Bi / (N + e))
print("exact upper gap below Gamma2 =", gamma - max(B0, Bi) / (N + e))
