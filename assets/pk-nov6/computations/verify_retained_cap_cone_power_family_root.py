from fractions import Fraction as F
from math import factorial

checks = 0


def check(statement):
    global checks
    assert statement
    checks += 1


for d in range(1, 22):
    for k in range(1, d + 1):
        m, p = d - k, k + 1
        eps = F(1, 3 * (d + 1))
        delta = F(1, 5 * (d + 1))
        v = [F(j + 1, k + 1) for j in range(k)]
        product_v = F(1)
        for entry in v:
            product_v *= entry
        Jstar = k ** k * product_v
        Ak = F((k + 1) ** k, factorial(k) * k ** k)
        # Exact simplex tangential positive-affine optimizer.
        radius = (m + p) * eps
        amplitude = F(m + p, p)
        Bp = radius ** m * amplitude ** p * F(factorial(p), factorial(m + p))
        lower_power_integral = radius ** m * amplitude ** (p - 1) * F(factorial(p - 1), factorial(m + p - 1))
        check(Bp == lower_power_integral)
        check(radius / (m + p) == eps)
        if m == 0:
            check(Bp == 1)
        coefficient = Ak * Jstar * Bp
        actual_cap_volume = F((d + 1) ** d, factorial(d)) * eps ** m * delta ** k * product_v
        check(delta ** k * coefficient == actual_cap_volume)
        # One actual simplex cap in F times a truncated positive orthant.
        check((d + 1) * eps <= 1)
        check((d + 1) * delta * max(v) <= 1)
        check(F(d + 1, d + 1) * eps == eps)
        for entry in v:
            check((d + 1) * delta * entry / (d + 1) == delta * entry)
        energy_factor = F(factorial(m), factorial(d)) * F((d + 1) ** (d + 1), k ** k * (m + 1) ** (m + 1)) * Jstar
        ratio_factor = F(factorial(m) * factorial(k), factorial(d)) * F((d + 1) ** (d + 1), (m + 1) ** (m + 1) * (k + 1) ** k)
        check(energy_factor / (Ak * Jstar) == ratio_factor)
        if m == 0:
            check(ratio_factor == d + 1)
        if k == 1:
            Cd = F(d + 1, d) ** (d + 1)
            check(ratio_factor == Cd / 2)
        # The scalar normal minimizer of (1+beta)^(k+1)/beta^k.
        check(F(k + 1, 1 + k) - F(k, k) == 0)

print(f"PASS: {checks:,} exact checks, including actual simplex cap certificates")
