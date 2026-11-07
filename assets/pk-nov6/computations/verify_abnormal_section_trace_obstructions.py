from fractions import Fraction as F

# Positive-base restriction is necessary: in the square-to-segment
# hull the original area source is only at z=0, but the untrimmed
# horizontal section has equal positive lengths at both integer bases.
original_fiber_areas = {0: F(4), 1: F(0)}
untrimmed_section_lengths = {0: F(2), 1: F(2)}
positive_bases = [z for z, mass in original_fiber_areas.items() if mass > 0]
assert positive_bases == [0]
assert sum(untrimmed_section_lengths.values()) == 4
assert sum(untrimmed_section_lengths[z] for z in positive_bases) == 2

# A saturated diagonal base lattice has the stated integer reduction.
U = ((1, 0), (-1, 1))
assert U[0][0] * U[1][1] - U[0][1] * U[1][0] == 1
for j in range(-5, 6):
    assert (U[0][0]*j + U[0][1]*j, U[1][0]*j + U[1][1]*j) == (j, 0)

eps = F(1, 10)
assert 1 - 3 * eps > 0
assert F(1, 3) < F(4, 9)
cluster_area_fraction = eps ** 2
trace_mass_fraction = 3 * F(1, 3) * cluster_area_fraction
assert trace_mass_fraction == eps ** 2
assert F(1, 3) * cluster_area_fraction / trace_mass_fraction == F(1, 3)

for L in (F(3, 4), F(1), F(7, 2)):
    assert L > F(1, 2)
    intervals = [(L - F(1, 2), L + F(1, 2))] * 2
    intervals += [(-L - F(1, 2), -L + F(1, 2))] * 2
    assert all(not (lo <= 0 <= hi) for lo, hi in intervals)
    positive_mass = sum(hi-lo for lo, hi in intervals if lo > 0)
    negative_mass = sum(hi-lo for lo, hi in intervals if hi < 0)
    positive_hinge = sum((hi**2-lo**2)/2 for lo, hi in intervals if lo > 0)
    negative_hinge = sum((lo**2-hi**2)/2 for lo, hi in intervals if hi < 0)
    assert positive_mass == negative_mass == 2
    assert positive_hinge == negative_hinge == 2 * L
print('PASS: positive-base reduction, effective triangle trace, and empty-section endpoint')
