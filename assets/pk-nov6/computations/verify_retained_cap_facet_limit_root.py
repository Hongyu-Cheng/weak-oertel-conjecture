from fractions import Fraction as F

checks = 0


def check(value):
    global checks
    assert value
    checks += 1


def affine_integral(A, B, lo, hi, degree=0):
    return A * (hi ** (degree + 1) - lo ** (degree + 1)) / (degree + 1) + B * (hi ** (degree + 2) - lo ** (degree + 2)) / (degree + 2)


for denominator in range(4, 75):
    for numerator in range(1, denominator):
        x = F(numerator, denominator)
        if x <= F(1, 3):
            a = -1 / (2 * x)
            lo, hi = F(0), 3 * x
            expected = 9 * x / 4
        elif x >= F(2, 3):
            a = 1 / (2 * (1 - x))
            lo, hi = 3 * x - 2, F(1)
            expected = 9 * (1 - x) / 4
        else:
            variance_shift = x * x - x + F(1, 3)
            a = (x - F(1, 2)) / variance_shift
            lo, hi = F(0), F(1)
            expected = 1 / (12 * variance_shift)
        A, B = 1 - a * x, a
        mass = affine_integral(A, B, lo, hi)
        moment = affine_integral(A, B, lo, hi, 1)
        square = A * A * (hi - lo) + A * B * (hi * hi - lo * lo) + B * B * (hi ** 3 - lo ** 3) / 3
        check(mass == expected)
        check(square == mass)
        check(moment == x * mass)
        check(A + B * lo >= 0 and A + B * hi >= 0)
        check(square / mass ** 2 == 1 / expected)
        # Actual rectangle cap: height=2 delta h, fully contained for delta<=1/3.
        delta = F(1, 7)
        check(2 * delta * max(A + B * lo, A + B * hi) <= 1)
        cap_mass = 2 * delta * mass
        cap_tangential_moment = 2 * delta * moment
        cap_normal_moment = 2 * delta * delta * square
        check(cap_tangential_moment == x * cap_mass)
        check(cap_normal_moment == delta * cap_mass)
        # Normalized hinge: 2(1+a(z-x))-s/delta; its integral is cap mass.
        check(2 * delta * square == cap_mass)

for j in range(1, 50):
    b = F(j, 17)
    check((1 + b) ** 2 / (2 * b) - 2 == (b - 1) ** 2 / (2 * b))

print(f"PASS: {checks:,} exact checks, including actual rectangle cap certificates")
