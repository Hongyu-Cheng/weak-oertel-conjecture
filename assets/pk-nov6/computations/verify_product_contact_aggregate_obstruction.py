from fractions import Fraction as F

# This verifies the finite arithmetic certificates over a range of
# parameters; the accompanying note proves all d>=1 and all s>=2.
for d in range(1, 9):
    for s in range(2, 9):
        sd = s ** d
        m = 2 * sd
        M = F(m) * (1 + F(1, sd))
        assert M == 2 * (sd + 1)
        T = F(m, sd)
        assert T == 2
        for theta in (F(1, 2), F(1, sd + 1)):
            A = F(4 * (d + 1)) / (theta * (1 - theta))
            bottom_upper = F(d, 2) - A * theta
            top_lower = -F(d, 2 * s) - F(d) / theta + A * (1 - theta)
            assert bottom_upper < 0
            assert top_lower > 0
            assert F(d, 2) > 0
            assert F(1, 2) - d < 0
        t_bottom = F(1, M)
        t_top = F(1, sd) / M
        assert m * (t_bottom + t_top) == 1
        assert m * t_top == F(1, sd + 1)
        mean_scale = m * t_bottom + m * t_top / s
        assert mean_scale == F(sd * s + 1, s * (sd + 1))
        assert mean_scale < 1
        mean_weight = m * t_bottom + m * t_top / sd
        assert mean_weight == F(sd * sd + 1, sd * (sd + 1))
        sum_t_square = m * (t_bottom ** 2 + t_top ** 2)
        assert sum_t_square == F(sd * sd + 1, 2 * sd * (sd + 1) ** 2)
print('PASS: actual masses, strict cap traces, barycentric coefficients, and lifted signs')
