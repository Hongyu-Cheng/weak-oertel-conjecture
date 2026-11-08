"""Exact certificate for simplex free-factor compression; no floating-point proof."""

from fractions import Fraction as F
from math import comb, factorial
import json


def power_interval(base, exponent, digits=80):
    scale = 10**digits
    lo = base.numerator * scale // base.denominator
    hi = -(-base.numerator * scale // base.denominator)
    a = b = scale
    while exponent:
        if exponent & 1:
            a = a * lo // scale
            b = -(-b * hi // scale)
        exponent //= 2
        if exponent:
            lo = lo * lo // scale
            hi = -(-hi * hi // scale)
    return F(a, scale), F(b, scale)


N, n, h = 13, 52, 1_345_226_000_000_000_000
theta, beta = F(3, 32), F(27, 64)
ds, dt, epsilon = F(1, 10**24), F(2, 10**24), F(1, 10**30)
s, t, eta = (1 + ds) / 2, 1 - dt, 1 - F(3, 2 * 10**24)
dq = F(274_778_504_931, 10**11 * h)
q = (1 + dq) / 2
e_upper = sum((F(1, factorial(i)) for i in range(51)), F(0)) + F(52, 51 * factorial(51))
m_interval = tuple(theta * (2 * s)**3 * p for p in power_interval(2 * q, h))
Elo = Ehi = F(0)
for r in range(1, N + 1):
    lo, hi = power_interval(1 - r * dq, h)
    coefficient = 4 * comb(N, r) * theta * (1 - r * dt)**3
    Elo += coefficient * lo
    Ehi += coefficient * hi
mlo, mhi = F(1_463_252_115_845_211, 10**15), F(1_463_252_115_845_212, 10**15)
elo, ehi = F(465_701_482_650_506, 10**15), F(465_701_482_650_507, 10**15)
assert mlo < m_interval[0] <= m_interval[1] < mhi
assert elo < Elo <= Ehi < ehi
margins = {
    "s_above_half": s - F(1, 2),
    "s_below_one": 1 - s,
    "q_above_half": q - F(1, 2),
    "q_below_one": 1 - q,
    "epsilon_positive": epsilon,
    "epsilon_below_quarter": F(1, 4) - epsilon,
    "t_positive": t,
    "eta_above_t": eta - t,
    "eta_below_two_times_loss": 2 * (1 - s) - eta,
    "negative_tetrahedron_scale": 1 - N * dt,
    "negative_free_scale": 1 - N * dq,
    "paid_origin_facet_margin": 1 - N * (ds + 4 * epsilon * (3 * t + 1 - ds)),
    "origin_cut_margin": mlo / e_upper - beta - ehi / 4,
    "mass_surplus": 1 + elo - mhi,
    "simplex_cap_margin": 1 + elo - mhi - 2**n * mhi / (2 * h - 1),
}
assert all(value > 0 for value in margins.values()), margins
x = F(1, 454) - F(1, 3 * 227**2)
m0 = F(14949, 10256)
A13 = F(3, 8) * (F(35, 32)**13 - 1)
barrier_checks = {
    "dimension_227_margin": x + x*x/2 - F(9, 4096),
    "N12_mass_deficit": m0 - 1 - F(3, 8) * ((1 + theta/m0)**12 - 1),
    "e_lower_margin": sum((F(1, factorial(i)) for i in range(7)), F(0)) - F(1359, 500),
}
assert all(value > 0 for value in barrier_checks.values()), barrier_checks
assert 2**52 // (2 * A13) == 2_722_291_674_329_078
print(json.dumps({
    "status": "exact_rational_certificate_passed",
    "integer_dimension": n,
    "continuous_dimension": str(3 + h),
    "free_simplex_dimension": str(h),
    "extra_padding_dimension": 0,
    "parameters": {k: str(v) for k, v in {"s": s, "t": t, "eta": eta, "epsilon": epsilon, "q": q}.items()},
    "m_interval": [str(mlo), str(mhi)],
    "E_interval": [str(elo), str(ehi)],
    "margins": {k: str(v) for k, v in margins.items()},
    "balanced_family_barrier_checks": {k: str(v) for k, v in barrier_checks.items()},
    "four_cut_family_minimum_continuous_dimension": 2**52 // (2 * A13),
}, indent=2))
