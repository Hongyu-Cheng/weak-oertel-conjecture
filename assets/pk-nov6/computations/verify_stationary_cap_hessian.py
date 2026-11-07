from fractions import Fraction as F

lower, upper = F(-1, 4), F(1, 100)

def antiderivative(t, c):
    return t + sum(c) * t*t/2 + c[0]*c[1]*t*t*t/3

examples = [
    ((1, 1), F(304213, 375000), F(30301, 608426), (-16, -16)),
    ((-1, -1), F(491413, 375000), F(29701, 982826), (16, 16)),
    ((1, -1), F(382187, 375000), F(29999, 764374), (-8, 8)),
]
for c, expected_volume, expected_fraction, numerator in examples:
    assert all(1 + ci*t > 0 for ci in c for t in (lower, upper))
    total = antiderivative(upper, c) - antiderivative(lower, c)
    cap = antiderivative(upper, c)
    volume, fraction = 4*total, cap/total
    assert volume == expected_volume
    assert fraction == expected_fraction
    assert 0 < fraction < F(1, 10) < F(27, 64)
    assert tuple(-4*(sum(c)+2*ci) for ci in c) == numerator
    print(c, 'V=', volume, 'p=', fraction,
          'Hessian diagonal=', tuple(F(a, 3)/volume for a in numerator))

for k in range(1, 9):
    eigenvalues = [F((-1)**i*(i+1), i+2) for i in range(k)]
    trace = sum(eigenvalues)
    c = [-a/2 + trace/(2*(k+2)) for a in eigenvalues]
    C = sum(c)
    assert C == -trace/(k+2)
    assert [C+2*ci for ci in c] == [-a for a in eigenvalues]

assert F(3, 7) > F(27, 64)
print('PASS: exact frustum volumes, fractions, Hessians, and inverse coefficients')
