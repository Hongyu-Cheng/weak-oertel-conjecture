"""Independent rational reconstruction of all five low-sector certificates."""
import sympy as s
from fractions import Fraction as Q
from math import comb
from itertools import product
from pathlib import Path
import json

a, beta, k, v, w = s.symbols('a beta k v w')
x, y, z = s.symbols('x y z')
c = 1-a
t = s.Rational(1, 3)
L, U = c-t, a-t

def integrated_square(initial, drop):
    return initial**3/(3*drop)

# Recover the cap integrals directly from the two affine squared hinges,
# rather than ingesting the originating expanded polynomial.
Iminus = s.cancel((a*integrated_square(1-t/a, k-beta/a)
                  -c*integrated_square(1-t/c, k-beta/c))/(a-c))
Iplus = [
    s.cancel((a*integrated_square(1-(t+beta)/a, k+beta/a)
              -c*integrated_square(1-(t+beta)/c, k+beta/c))/(a-c)),
    s.cancel(a*integrated_square(1-(t+beta)/a, k+beta/a)/(a-c)),
    s.Integer(0),
]
Ominus = s.cancel((a*(1-t/a)**2-c*(1-t/c)**2)/(a-c))
Oplus = [s.cancel((a*(1-(t+beta)/a)**2-c*(1-(t+beta)/c)**2)/(a-c)),
         s.cancel(a*(1-(t+beta)/a)**2/(a-c)), s.Integer(0)]
betas = [L*v, L+(a-c)*v, U+L*v]
raw = []
for region in range(3):
    H = ((1-k)*(Iminus+Iplus[region])
         +(1+k)*(Ominus+Oplus[region])/2
         -s.Rational(4, 9)*(1/(3*k)+s.Rational(1, 2)+k/5))
    bm = betas[region]
    km = 3*bm+(1-3*bm)*w
    positive = [
        27*810*a*c*k*(a*k-beta)*(a*k+beta)*(c*k-beta)*(c*k+beta),
        9*810*a*c*k*(a*k-beta)*(a*k+beta)*(c*k-beta),
        810*a*c*k*(a*k-beta)*(c*k-beta)/L,
    ][region]
    N = s.cancel((H*positive).subs({beta: bm, k: km}, simultaneous=True))
    D = s.cancel(positive.subs({beta: bm, k: km}, simultaneous=True))
    assert s.fraction(N)[1] == 1
    assert s.fraction(D)[1] == 1
    mappedH = s.cancel(H.subs({beta: bm, k: km}, simultaneous=True))
    assert s.cancel(mappedH*D-N) == 0
    raw.append(s.Poly(N, a, v, w).as_expr())
    print(f'PASS: region {region} independent rational identity', flush=True)

boxes = [
    (0, (Q(0), Q(1)), (Q(0), Q(1)), (12, 8, 6), Q(0)),
    (1, (Q(0), Q(1)), (Q(1, 2), Q(1)), (10, 7, 5), Q(0)),
    (1, (Q(1, 2), Q(1)), (Q(0), Q(1, 2)), (10, 7, 5), Q(0)),
    (1, (Q(0), Q(1, 2)), (Q(0), Q(1, 2)), (10, 7, 5), Q(0)),
    (2, (Q(0), Q(1)), (Q(0), Q(1)), (7, 4, 4), Q(21, 128)),
]

def axis_transform(data, degrees, axis, reverse=False):
    out = {}
    for index in product(*(range(n+1) for n in degrees)):
        i, n = index[axis], degrees[axis]
        val = Q(0)
        for j in range(i+1):
            src = list(index)
            src[axis] = j
            if reverse:
                factor = Q(comb(n, j)*comb(n-j, i-j)*(-1)**(i-j))
            else:
                factor = Q(comb(i, j), comb(n, j))
            val += data.get(tuple(src), Q(0))*factor
        out[index] = val
    return out

author = json.loads(Path(__file__).with_name(
    'half-integer-affine-low-sector-bernstein-candidate.json').read_text())
total = 0
for region, vb, wb, degrees, expected in boxes:
    mapped = s.Poly(raw[region].subs({
        a: s.Rational(1, 2)+x/6,
        v: s.Rational(vb[0].numerator, vb[0].denominator)
             +s.Rational((vb[1]-vb[0]).numerator, (vb[1]-vb[0]).denominator)*y,
        w: s.Rational(wb[0].numerator, wb[0].denominator)
             +s.Rational((wb[1]-wb[0]).numerator, (wb[1]-wb[0]).denominator)*z,
    }, simultaneous=True).expand(), x, y, z)
    assert tuple(mapped.degree(q) for q in (x, y, z)) == degrees
    power = {i: Q(c) for i, c in mapped.terms()}
    bernstein = power
    for axis in range(3):
        bernstein = axis_transform(bernstein, degrees, axis)
    assert min(bernstein.values()) == expected
    assert all(q >= 0 for q in bernstein.values())
    reverse = bernstein
    for axis in range(3):
        reverse = axis_transform(reverse, degrees, axis, reverse=True)
    assert {i: q for i, q in reverse.items() if q} == power
    matches = [b for b in author['boxes'] if b['region'] == region
               and tuple(map(Q, b['v_interval'])) == vb
               and tuple(map(Q, b['w_interval'])) == wb]
    assert len(matches) == 1
    authored = {tuple(row['index']): Q(row['value'])
                for row in matches[0]['coefficients']}
    assert authored == bernstein
    total += len(bernstein)
    print(f'PASS: region {region}, v={vb}, w={wb}, '
          f'{len(bernstein)} coefficients and reverse identity', flush=True)
assert total == 2603
print('PASS: 2603 exact nonnegative coefficients; five reverse polynomial '
      'identities; three independently derived positive-denominator identities.')
