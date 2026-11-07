"""Exact arithmetic checks for the proved all-d optimizer identities.

The analytic theorem, including monotonicity and sharpness, is in
multi-source-density-sandwich-sharp-source-cost.md. This does not replace it.
"""
from fractions import Fraction as F

checked = 0
for d in range(1, 25):
    q = F(d + 1, d)
    gamma = F(d, d + 1) ** d
    for den in range(2, 40):
        for num in range(1, den):
            u = F(num, den)
            z = d * (1 - u) - u ** d
            big_d = (d + 1) * (1 - u) - u ** (d + 1)
            if z <= 0:
                continue
            k = big_d ** d / z ** (d + 1)
            if k < 2:
                continue
            t = z / big_d
            s = t ** d
            r = (u * t) ** d
            assert 0 < r < s < 1
            assert q * t + k * u ** d * (q-u) * t ** (d+1) == 1
            assert k * s * z == 1
            assert q * (1 + k*r) * t == 1 + k * (u*t) ** (d+1)
            assert ((1 + u ** (d-1))*big_d - (1+u**d)*z ==
                    (1-u)*(1+u**d+u**(d-1)*(d+1-d*u)))
            assert s + r >= gamma * (F(1, 1)/k+r)
            checked += 1

for m in range(2, 101):
    k = 3*m*m - 1
    r = F(m-1, k)
    s = F(2*m-1, k)
    g = (F(1, 2)+k*r*(1-r/2))/(1+k*r)
    assert 1-g == s
    assert s+r == F(3*m-2, k)
    assert 2*(s+r)/(1+r) <= F(2, m)

print(f"PASS: {checked} exact all-d optimizer identities and 99 rational interval examples.")
