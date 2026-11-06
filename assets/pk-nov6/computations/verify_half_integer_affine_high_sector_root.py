"""Independent exact certificate, using only standard-library rational algebra."""
from fractions import Fraction as Q
from math import comb
from itertools import product
import json
from pathlib import Path

ZERO = (0, 0, 0)

def clean(p):
    return {i: c for i, c in p.items() if c}

def const(c):
    return clean({ZERO: Q(c)})

def var(j):
    i = [0, 0, 0]
    i[j] = 1
    return {tuple(i): Q(1)}

def add(*ps):
    out = {}
    for p in ps:
        for i, c in p.items():
            out[i] = out.get(i, Q(0)) + c
    return clean(out)

def scale(p, c):
    return clean({i: a*c for i, a in p.items()})

def mul(*ps):
    out = const(1)
    for p in ps:
        nxt = {}
        for i, a in out.items():
            for j, b in p.items():
                k = tuple(x+y for x, y in zip(i, j))
                nxt[k] = nxt.get(k, Q(0)) + a*b
        out = clean(nxt)
    return out

def power(p, n):
    return mul(*([p]*n))

def minus(p, q):
    return add(p, scale(q, -1))

def substitute(p, qs):
    return add(*(scale(mul(*(power(q, e) for q, e in zip(qs, i))), c)
                 for i, c in p.items()))

one = const(1)
b, v, k = (var(j) for j in range(3))
z = mul(b, v)
P = minus(one, b)
P2 = minus(P, mul(k, z))
zz = minus(one, power(z, 2))

# Derive the numerator from the TWO separate lower bounds, independently
# of the originating symbolic program and its expanded polynomial.
pol = add(
    scale(mul(minus(one, k), add(mul(power(P, 3), add(one, z)),
                               mul(power(P2, 3), minus(one, z)))), 90),
    scale(mul(k, add(one, k), zz, add(power(P, 2), power(P2, 2))), 135),
    scale(mul(add(const(40), scale(k, 60), scale(power(k, 2), 24)),
              add(const(2), scale(b, -3)), zz), -1),
)

records = []
for lo, hi in [(Q(0), Q(1, 2)), (Q(1, 2), Q(1))]:
    qs = [add(const(Q(1, 3)), scale(b, Q(1, 6))), v,
          add(const(lo), scale(k, hi-lo))]
    mapped = substitute(pol, qs)
    degrees = tuple(max(i[j] for i in mapped) for j in range(3))
    assert degrees == (4, 4, 4)
    bs = {}
    for i in product(range(5), repeat=3):
        bs[i] = sum((c * Q(comb(i[0], j[0]), comb(4, j[0]))
                       * Q(comb(i[1], j[1]), comb(4, j[1]))
                       * Q(comb(i[2], j[2]), comb(4, j[2]))
                     for j, c in mapped.items()
                     if all(jj <= ii for jj, ii in zip(j, i))), Q(0))
    assert all(c > 0 for c in bs.values())
    expected = Q(5, 2) if lo == 0 else Q(331, 384)
    assert min(bs.values()) == expected
    # Reverse reconstruction checks the full polynomial identity, rather
    # than testing evaluations or trusting the coefficient transform.
    recon = {}
    for i, c in bs.items():
        basis = mul(*(scale(mul(power(x, j), power(minus(one, x), 4-j)),
                            comb(4, j)) for x, j in zip((b, v, k), i)))
        recon = add(recon, scale(basis, c))
    assert recon == mapped
    records.append({"k": [str(lo), str(hi)], "minimum": str(expected),
                    "coefficients": {",".join(map(str, i)): str(c)
                                     for i, c in bs.items()}})

out = Path(__file__).with_name("half-integer-high-sector-root-bernstein.json")
out.write_text(json.dumps(records, indent=2) + "\n")
print("PASS: 250 strictly positive exact Bernstein coefficients; "
      "two independently reconstructed polynomial identities.")

# Separately verify the arithmetic identity for rational p,l and every
# possible terminal fraction in a grid; the proof uses the identity for
# arbitrary real parameters, not this regression grid.
checks = 0
for denominator in range(1, 31):
    for numerator in range(1, 3*denominator+1):
        p = Q(numerator, denominator)
        for stepden in (1, 2, 3, 7, 13):
            step = Q(1, stepden)
            t = p/step
            m = t.numerator // t.denominator
            theta = t-m
            exact = sum(((p-step*h)**2 for h in range(m+1)), Q(0))
            formula = (p**3/(3*step) + p*p/2 + p*step/6
                       + step*step*theta*(1-theta)*(2*theta-1)/6)
            assert exact == formula
            assert exact >= p**3/(3*step) + p*p/2
            if p == 1 and step <= 1:
                assert exact <= 1/(3*step) + Q(1, 2) + step/5
            checks += 1
print(f"PASS: {checks} exact arithmetic-sum formula and bound checks.")
