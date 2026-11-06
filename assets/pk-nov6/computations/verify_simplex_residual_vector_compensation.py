"""Exact interval diagnostics for simplex residual-vector compensation.

All scalar samples and root enclosures are rational.  Root enclosures
are certified by integer powers, not floating-point tolerances.  The
companion Markdown source proves the general results independently.
"""

from fractions import Fraction as F
from functools import lru_cache
from random import Random
from sympy import integer_nthroot


checks = 0
rng = Random(20260929)


def exact(value):
    value = F(value)
    return value, value, ({None: value} if value else {})


def combine_terms(*weighted):
    result = {}
    for scale, terms in weighted:
        for term, coefficient in terms.items():
            result[term] = result.get(term, F(0))+scale*coefficient
    return {term: coefficient for term, coefficient in result.items() if coefficient}


def plus(*intervals):
    return (sum(v[0] for v in intervals), sum(v[1] for v in intervals),
            combine_terms(*((F(1), v[2]) for v in intervals)))


def minus(left, right):
    terms = combine_terms((F(1), left[2]), (F(-1), right[2]))
    if not terms:
        return exact(0)
    return left[0]-right[1], left[1]-right[0], terms


def times(scale, interval):
    assert scale >= 0
    return scale*interval[0], scale*interval[1], combine_terms((scale, interval[2]))


def positive(interval):
    if interval[0] >= 0:
        return interval
    if interval[1] <= 0 or not interval[2]:
        return exact(0)
    raise AssertionError(("Unresolved positive-part sign", interval))


def maximum(left, right):
    if left[2] == right[2] or left[0] >= right[1]:
        return left
    if right[0] >= left[1]:
        return right
    raise AssertionError(("Unresolved maximum branch", left, right))


@lru_cache(None)
def root_interval(value, d):
    assert 0 <= value <= 1
    if value in (0, 1) or d == 1:
        return exact(value)
    numerator_root, numerator_exact = integer_nthroot(value.numerator, d)
    denominator_root, denominator_exact = integer_nthroot(value.denominator, d)
    if numerator_exact and denominator_exact:
        return exact(F(int(numerator_root), int(denominator_root)))
    bits = 100
    denominator = 1 << bits
    scaled_floor = (value.numerator << (bits*d)) // value.denominator
    k = int(integer_nthroot(scaled_floor, d)[0])
    lo, hi = F(k, denominator), F(k+1, denominator)
    assert lo**d <= value <= hi**d
    if lo**d == value:
        return exact(lo)
    return lo, hi, {("root", value, d): F(1)}


def phi(q, d):
    if q <= 0:
        return exact(0)
    if q >= 1:
        return exact(1)
    return root_interval(1-(1-q)**d, d)


def envelope(h, d):
    m = d+1
    return maximum(exact(d), times(m, phi(h/m, d)))


def certify_le(left, right, label):
    global checks
    assert left[2] == right[2] or left[1] <= right[0], (label, left, right)
    checks += 1


def check_equal(left, right):
    global checks
    assert left == right, (left, right)
    checks += 1


def random_thresholds(m, h):
    q = [F(rng.randint(-35, 35), 7) for _ in range(m-1)]
    return q+[h-sum(q)]


for d in range(1, 13):
    m = d+1
    r = F(d, m)
    kap = root_interval(1-r**d, d)
    eta = minus(times(m, kap), exact(d))
    if d == 1:
        check_equal(eta, exact(0))
        cd = exact(1)
    else:
        assert eta[0] > 0 and eta[1] < 1
        cd = ((r/kap[1])**(d-1), (r/kap[0])**(d-1), {("cd", d): F(1)})
        assert 0 < cd[0] <= cd[1] < 1
        checks += 2

    # Exact one-endpoint envelope at positive, negative, and saturated sums.
    for h in map(F, (-3, 0, 1, 2, d, m, m+2)):
        for _ in range(8):
            q = random_thresholds(m, h)
            certify_le(plus(*(phi(v, d) for v in q)), envelope(h, d),
                       ("endpoint envelope", d, h, q))

        # The floor branch is always actually attained by a negative coordinate.
        large = max(F(1), (h+1)/d)
        q = [large]*d+[h-d*large]
        check_equal(sum(q), h)
        check_equal(plus(*(phi(v, d) for v in q)), exact(d))

    for a, b in ((F(1), F(1)), (F(1), F(2)), (F(1), F(100)),
                 (F(3), F(1))):
        # Zero drift: exact cancellation budget and sharp positive-part bound.
        for _ in range(30):
            qa = random_thresholds(m, F(1))
            qb = [((a+b)/m-a*q)/b for q in qa]
            check_equal(sum(qb), F(1))
            deltas = []
            for u, v in zip(qa, qb):
                if u == v == F(1, m):
                    deltas.append(exact(0))
                else:
                    deltas.append(times(F(1, 2), minus(
                        plus(times(a, phi(u, d)), times(b, phi(v, d))),
                        times(a+b, kap))))
            certify_le(plus(*deltas), exact(0), ("zero drift", d, a, b, qa))
            bound = times(F(d, 2), positive(minus(exact(max(a, b)), times(a+b, kap))))
            certify_le(plus(*(positive(v) for v in deltas)), bound,
                       ("positive losses", d, a, b, qa))

        # General drift: retain paired coordinates and check both global bounds.
        for B in (F(0), min(a, b)/100, -min(a, b)/100,
                  F(1), F(-1), F(10), F(-10), -d*b, d*a):
            h = 1+B/a
            for _ in range(4):
                qa = random_thresholds(m, h)
                qb = [((a+b)/m-a*q)/b for q in qa]
                check_equal(sum(qb), 1-B/b)
                total = plus(*(plus(times(a, phi(u, d)), times(b, phi(v, d)))
                               for u, v in zip(qa, qb)))
                independent = plus(times(a, envelope(1+B/a, d)),
                                   times(b, envelope(1-B/b, d)))
                certify_le(total, independent,
                           ("paired envelope", d, a, b, B, qa))
                loss = times(F(1, 2), minus(total, times(m*(a+b), kap)))
                drift = times(abs(B), cd)
                payment = times(b if B >= 0 else a, eta)
                certify_le(loss, times(F(1, 2), positive(minus(drift, payment))),
                           ("drift price", d, a, b, B, qa))

            # In a certified central regime both endpoint branches are Jensen.
            if B >= -a*eta[0] and B <= b*eta[0]:
                qa = random_thresholds(m, h)
                qb = [((a+b)/m-a*q)/b for q in qa]
                total = plus(*(plus(times(a, phi(u, d)), times(b, phi(v, d)))
                               for u, v in zip(qa, qb)))
                central = times(m, plus(times(a, phi((1+B/a)/m, d)),
                                       times(b, phi((1-B/b)/m, d))))
                certify_le(total, central,
                           ("sharp central bound", d, a, b, B, qa))
                # The constant vectors satisfy every paired constraint exactly.
                check_equal(a*(1+B/a)/m+b*(1-B/b)/m, (a+b)/m)

    # The positive-loss extremizer is checked by its exact threshold statuses.
    a, b = F(1), F(1000)
    assert b > kap[1]*(a+b)
    shifts = [b*r]*d+[-d*b*r]
    check_equal(sum(shifts), F(0))
    qa = [F(1, m)-t/a for t in shifts]
    qb = [F(1, m)+t/b for t in shifts]
    check_equal([phi(q, d) for q in qa], [exact(0)]*d+[exact(1)])
    check_equal([phi(q, d) for q in qb], [exact(1)]*d+[exact(0)])
    check_equal(sum(a**d*min(F(1), max(F(0), 1-q))**d for q in qa), d*a**d)

    # Nonzero circuit drift can make every direction overshoot simultaneously.
    beta = -b*r
    qa = F(1, m)+beta/a
    qb = F(1, m)-beta/b
    assert qa < 0
    check_equal(qb, F(1))
    check_equal(m*beta, -d*b)

print(f"PASS: {checks} exact rational/interval checks")
