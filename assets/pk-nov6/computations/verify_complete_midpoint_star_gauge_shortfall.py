"""Exact arithmetic for the all-candidate central-star certificate shortfall."""
from fractions import Fraction as Q

d, N = 4, 16
h = Q(1, 17)
den = 17 ** 4
gamma4 = Q(4, 5) ** 4
gamma5 = Q(5, 6) ** 5
mass = 1 + 2 * sum((1 - h * k) ** 4 for k in range(1, N + 1))
assert mass == Q(571217, 83521) == Q(33601, 4913)

expected = [129827, 228484, 274375, 282546, 265403, 232930,
            192927, 151250, 112049, 77986, 50453, 29810,
            15625, 6912, 2349, 496, 33, 0]
actual = []
for j in range(18):
    t = h * j
    numerator = (2 * j + 1) * (17 - j) ** 4
    numerator += 2 * sum(max(0, 17 - 5 * k + 4 * j) ** 4
                         for k in range(j + 1, N + 1))
    # Independently evaluate the nonsymmetric-gauge expression.
    value = (1 - t) ** 4
    for k in range(1, N + 1):
        signed = t - h * k
        gauge = signed if signed >= 0 else -4 * signed
        value += 2 * max(Q(0), 1 - h * k - gauge) ** 4
    assert value == Q(numerator, den)
    actual.append(numerator)
assert actual == expected
assert max(actual) == 282546
assert actual.index(max(actual)) == 3
certificate = gamma4 * Q(max(actual), den)
target = gamma4 * mass / 2
assert target - certificate == gamma4 * Q(6125, 167042)

# Every noncentral anchor's rational envelope is a subsum of the central one.
# The analytic Phi <= 2 Gamma rho**4 inequality bounds its actual pair terms.
anchor_checks = 0
for k in range(N + 1):
    for j in range(k, 18):
        total = (17 - j) ** 4
        for distance in range(1, N - k + 1):
            center_index = max(k, distance)
            signed = j - center_index
            gauge = signed if signed >= 0 else -4 * signed
            root = max(0, 17 - center_index - gauge)
            total += 2 * root ** 4
        assert total <= actual[j] <= max(actual)
        anchor_checks += 1

# Continuous source volume, true centroid, closed-cap sampling loss, safety.
W = Q(2, 5) * (1 - h ** 5)
coordinate = Q(1, 6) * (1 - h ** 6) / (1 - h ** 5)
assert 0 < 4 * coordinate < 1
assert W == Q(2839712, 7099285)
assert h * mass == Q(33601, 83521)
lower_absolute_weighted = gamma5 * W - h
lower_normalized = lower_absolute_weighted / (h * mass)
assert lower_normalized == Q(35167522, 138805731)
assert lower_normalized > gamma4 / 2 == Q(128, 625)
assert lower_absolute_weighted - gamma4 * h * mass / 2 == Q(
    4212567682, 215640781875)

print("PASS: all 18 exact central maximum candidates, {} noncentral envelopes,"
      " mass and certificate gap, continuous centroid, and independent"
      " all-cap safety.".format(anchor_checks))
