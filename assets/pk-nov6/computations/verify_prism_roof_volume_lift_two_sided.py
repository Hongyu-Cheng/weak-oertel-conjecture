from fractions import Fraction as F
from itertools import product

checks = 0

def check(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1

# Exact affine-roof row and its original-volume change of law.
z = [F(0), F(1), F(2)]
H = [F(1), F(2), F(3)]
p = [F(1, 3)] * 3
hm = sum(pi * hi for pi, hi in zip(p, H))
zm = sum(pi * zi for pi, zi in zip(p, z))
ph = [pi * hi / hm for pi, hi in zip(p, H)]
check(hm, F(2)); check(zm, F(1)); check(sum(ph), F(1))
check(ph, [F(1, 6), F(1, 3), F(1, 2)])
check(sum(pi * zi for pi, zi in zip(ph, z)), F(4, 3))
check(sum(pi * hi for pi, hi in zip(ph, H)), F(7, 3))
check(sum(pi * zi / hi for pi, zi, hi in zip(ph, z, H)), F(1, 2))
check(sum(pi / hi for pi, hi in zip(ph, H)), F(1, 2))
check(sum(hi * hi for hi in H) - 3 * hm * hm, F(2))
check(sum(2 * hi for hi in H), F(12))
check(sum(2 * hi for zi, hi in zip(z, H) if zi <= 1), F(6))

# Verify row identities for varied rational finite laws, including
# constant-height rows and nonsymmetric positive heights.
for hs in product(range(1, 5), repeat=3):
    for weights in [(1, 1, 1), (1, 2, 3), (3, 1, 2)]:
        pp = [F(i, sum(weights)) for i in weights]
        hh = list(map(F, hs))
        h = sum(pi * hi for pi, hi in zip(pp, hh))
        zz = [F(-2), F(1), F(3)]
        zzm = sum(pi * zi for pi, zi in zip(pp, zz))
        bias = [pi * hi / h for pi, hi in zip(pp, hh)]
        var = sum(pi * (hi - h) ** 2 for pi, hi in zip(pp, hh))
        cov = sum(pi * (zi - zzm) * (hi - h)
                  for pi, zi, hi in zip(pp, zz, hh))
        check(sum(bias), F(1))
        check(sum(q * zi for q, zi in zip(bias, zz)) - zzm, cov / h)
        check(sum(q * hi for q, hi in zip(bias, hh)) - h, var / h)
        check(sum(q / hi for q, hi in zip(bias, hh)), 1 / h)
        check(sum(q * zi / hi for q, zi, hi in zip(bias, zz, hh)), zzm / h)
        check(var == 0, len(set(hh)) == 1)
        for t in [F(-1), F(-2, 5), F(0), F(3, 7), F(1)]:
            check(sum(q * t * hi for q, hi in zip(bias, hh)) - t * h,
                  t * var / h)

# Direct one-column flux identity, including full, empty, and proper cuts.
# Cap y >= a inside [-H,H], raw b=1; proper coarea is one atom at a.
for hi in range(1, 6):
    h = F(hi)
    for a in [F(-hi-1), -h, -h/2, F(0), h/2, h, F(hi+1)]:
        cap = max(F(0), min(2*h, h-a))
        if -h < a < h:
            rhs = h - a
        elif a < -h:
            rhs = 2*h
        elif a > h:
            rhs = F(0)
        elif a == -h:  # inside supporting allocation alpha+sigma=1
            sigma = F(2, 7)
            alpha = 1-sigma
            rhs = h*(1+alpha)-a*sigma
        else:  # outside supporting allocation alpha=sigma
            sigma = F(3, 8)
            rhs = h*sigma-a*sigma
        check(cap, rhs)

print(f"PASS: {checks} exact roof-lift, covariance, projective and flux checks")
