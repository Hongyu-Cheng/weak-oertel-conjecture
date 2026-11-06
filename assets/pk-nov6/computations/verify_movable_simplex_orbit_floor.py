from fractions import Fraction as F

w = [F(2), F(6), F(10), F(3)]
assert all(w[i+1]-w[i] >= w[i+2]-w[i+1] for i in range(2))
caps = [(F(11), F(1)), (F(11), F(-8)),
        (F(-2), F(9)), (F(-11), F(69,2))]
expected = [F(1), F(5), F(5), F(3,2)]
for j, ((slope, intercept), target) in enumerate(zip(caps, expected)):
    assert slope*j+intercept == w[j]/2
    mass = sum(max(F(0), min(w[z], w[z]-(slope*z+intercept)))
               for z in range(4))
    assert mass == target < sum(w)/4

retained = {1:(F(3), F(6)), 2:(F(0), F(6)), 3:(F(0), F(3))}
for z, (lo, hi) in retained.items():
    assert 0 <= lo <= hi <= w[z]
    assert retained[4-z] == (6-hi, 6-lo)
assert sum(hi-lo for lo,hi in retained.values()) == 12
assert F(12,2) > sum(w)/4

# Barycentric orbit averaging, including repeated entries and endpoints.
from itertools import permutations
for bary in [(F(1),F(0)), (F(1,3),F(2,3)),
             (F(1),F(0),F(0)), (F(1,2),F(1,3),F(1,6)),
             (F(1,4),)*4]:
    orbit = list(permutations(bary))
    n = len(bary)
    assert all(sum(p[i] for p in orbit)/len(orbit) == F(1,n)
               for i in range(n))
print('PASS: exact four-cap failure, mass-12 symmetric moved-point certificate, and barycentric orbit averages')
