from fractions import Fraction as F

# All-d certificate: the d=2 sum bounds every higher-dimensional sum.
eps = F(1,16)
p = (F(1,2), F(47,32))
r1 = min(1/abs(x) for x in p)
r2 = min(eps/p[0], (2-eps)/p[1])
assert r1 == F(32,47) and r2 == F(1,8)
I = r1*r1+r2*r2
assert I == F(67745,141376) < F(1,2)
assert 0 < r1 < 1 and 0 < r2 < 1

# A finite rational failure even for dilation factor two in the plane.
eps = F(1,100)
assert (1+(2-eps)**2)/F(11,5)**2 == F(49601,48400) > 1
p = (F(1,10), F(52,25))
r1 = min(1/abs(x) for x in p)
r2 = min(eps/p[0], (2-eps)/p[1])
assert r1 == F(25,52) and r2 == F(1,10)
assert r1*r1+r2*r2 == F(16301,67600) < F(1,4)

# Strict midpoint-containment variant.
assert F(1,100)+F(5,3)*F(101,200) == F(511,600) < 1
p = (F(1,10), F(9,10))
r1 = 1/(p[0]+F(5,3)*p[1])
r2 = min(F(1,100)/p[0], 1/p[1])
assert r1 == F(5,8) and r2 == F(1,10)
assert r1*r1+r2*r2 == F(641,1600) < F(1,2)
print('PASS: all-d 2^(1/d) failure, planar factor-two failure, strict compatibility')
