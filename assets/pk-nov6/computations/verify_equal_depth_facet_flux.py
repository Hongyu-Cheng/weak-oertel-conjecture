from fractions import Fraction as F

# The scalar maximization used in the exact flux inequality.
for h in [F(k, 7) for k in range(-28, 36)]:
    maximum = max(t1 * (h - 1) - t0 * h for t0 in (0, 1) for t1 in (0, 1))
    distance = max(F(0), -h, h-1)
    assert maximum == distance

# Exact layered-cube calibration.
for n in range(1, 5):
    A = 3**n
    external_flux = 2 * 5**(n-1) * F(1, 2)
    assert external_flux == 5**(n-1)
    assert (A <= external_flux) == (n == 4)
print('PASS: exact supporting-flux algebra and layered-cube threshold')
