from fractions import Fraction as F

eps, r = F(1, 10), F(11, 20)
for d in range(1, 101):
    a = eps**d
    c = F(d, d + 1)
    gamma = c**d
    h = (1 + (1 + a) * r) / (2 + a)
    assert h == (31 + 11 * a) / (40 + 20 * a)
    assert 0 < h <= F(31, 40) < 1
    q = c * h
    assert q + 1 > eps and q - 1 < 0
    assert max(a, F(1)) < (2 + a) / 2
    actual = q**d + a
    assert actual == gamma * h**d + a
    assert a / gamma == (eps / c) ** d <= F(1, 5) ** d
    assert actual / gamma <= F(31, 40) ** d + F(1, 5) ** d <= F(39, 40)
    assert actual < gamma * (2 + a) / 2
    # Actual uniform midpoint law: its sharp-bound density integrates to a.
    density = a / r**d
    assert density * r**d == a
    # Its H0 cost cannot exceed the actual endpoint-inclusive cap.
    eta_cap = density * min(q, r) ** d
    assert q**d + eta_cap <= actual
print("PASS: 100 exact dimensional instances; all-dimensional proof uses the printed power inequalities.")
