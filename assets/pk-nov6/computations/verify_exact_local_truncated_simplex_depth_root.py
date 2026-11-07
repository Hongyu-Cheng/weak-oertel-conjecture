"""Exact algebra checks; geometric all-direction proof is in the note."""
from fractions import Fraction as Q
from math import prod
import random

rng = random.Random(74901)
checks = 0
for d in range(1, 10):
    m = d + 1
    G = Q(d, m) ** d
    for iteration in range(40):
        raw = [Q(10000 + rng.randrange(20)) for _ in range(m)]
        lam = [x / sum(raw) for x in raw]
        c = d**d * prod(lam)
        D = min(c / x for x in lam) - Q(1, 10**8)
        ts = [c / x - D for x in lam]
        assert D > 0 and min(ts) >= 0 and max(lam) < Q(1, d)
        A = sum(1 / (D + t) for t in ts)
        assert A == 1 / c
        assert prod(D + t for t in ts) * A**d == d**d
        assert all(d**d * prod(lam[j] for j in range(m) if j != i)
                   - ts[i] == D for i in range(m))
        ws = [1 - d * x for x in lam]
        assert sum(ws) == 1 and min(ws) > 0
        assert all(sum(ws[i] for i in range(m) if i != j)
                   == d * lam[j] for j in range(m))
        checks += 1

        taus = [Q(rng.randrange(20), 17) for _ in range(m)]
        T1 = sum(taus)
        mean = T1 / m
        bs = [x - mean for x in taus]
        D1 = -mean
        D2 = -Q(d - 1, 2 * m) * sum(x*x for x in bs) / G
        A0 = m / G
        A1 = -sum(D1 + x for x in taus) / G**2
        A2 = sum((D1 + x)**2 for x in taus) / G**3 - m*D2/G**2
        J1 = sum(D1 + x for x in taus) / G + d*A1/A0
        J2 = (m*D2/G - sum((D1 + x)**2 for x in taus)/(2*G**2)
              + d*(A2/A0 - A1*A1/(2*A0*A0)))
        assert J1 == J2 == 0
        lambda1 = [(mean-x)/(m*G) for x in taus]
        assert sum(lambda1) == 0
        for i in range(m):
            assert G*m*sum(lambda1[j] for j in range(m) if j != i)-taus[i] == D1
        norm2 = (G-Q(1,m))*T1*T1 - Q(d-1,2*m)*sum(x*x for x in bs)/G
        assert norm2 == D2 + D1*T1 + G*T1*T1
        checks += 1

# Planar closed form checked without irrational floating point: parameterize
# sqrt(1+3t) by a rational r>1, so all quantities remain rational.
for k in range(1, 201):
    r = 1 + Q(k, 100000)
    t = (r*r-1)/3
    b = (1+r)/6
    D = 2*(1+r)/9-2*t/3
    assert 4*b*(3*b-1) == t
    assert D == 4*(1-2*b)*b == 4*b*b-t
    assert D/(1-t) > Q(4,9)
    checks += 1

# A single-corner rational parameterization, valid as algebra in every d.
for d in range(1, 10):
    m = d+1
    for k in range(1, 30):
        b = Q(1,m)+Q(k,10**7)
        t = d**d*b**(d-1)*(m*b-1)
        D = d**d*(1-d*b)*b**(d-1)
        assert D+t == d**d*b**d
        assert (D+t)*D**d*(1/(D+t)+d/D)**d == d**d
        if d == 1:
            assert D == (1-t)/2
        else:
            assert D/(1-t) > Q(d,m)**d
        checks += 1

print(f"PASS {checks} exact defining-equation, stress, derivative, and closed-form checks")
