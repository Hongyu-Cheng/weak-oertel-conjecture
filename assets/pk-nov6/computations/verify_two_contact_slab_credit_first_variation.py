"""Exact finite diagnostics for the proved slab first-variation note.

No floats or numerical optimization occur.  The general statements are
proved in the companion Markdown source, not inferred from these checks.
"""

from fractions import Fraction as Q


checks = 0


def check(actual, expected):
    global checks
    assert actual == expected, (actual, expected)
    checks += 1


def clip(poly, a, b, c):
    """Intersect an ordered rational polygon with a*x+b*y >= c."""
    if not poly:
        return []
    result = []
    previous = poly[-1]
    old = a * previous[0] + b * previous[1] - c
    for current in poly:
        new = a * current[0] + b * current[1] - c
        if (old >= 0) != (new >= 0):
            lam = old / (old - new)
            result.append(tuple(previous[j] + lam * (current[j] - previous[j])
                                for j in (0, 1)))
        if new >= 0:
            result.append(current)
        previous, old = current, new
    return result


def area(poly):
    if not poly:
        return Q(0)
    return abs(sum(poly[j-1][0] * poly[j][1] - poly[j-1][1] * poly[j][0]
                   for j in range(len(poly)))) / 2


diamond = [(Q(1), Q(0)), (Q(0), Q(1)),
           (Q(-1), Q(0)), (Q(0), Q(-1))]


def slab(t):
    poly = [((1-t)*x, (1-t)*y) for x, y in diamond]
    return clip(clip(poly, Q(1), Q(0), Q(-1, 2)),
                Q(-1), Q(0), Q(-1, 2))


def data(t, big_l):
    poly = slab(t)
    caps = [(Q(1), Q(0), -big_l*t),
            (Q(0), Q(1), -t/2),
            (Q(-1), Q(-1), -t/2)]
    captured = [area(clip(poly, *cap)) for cap in caps]
    core = poly
    for cap in caps:
        core = clip(core, *cap)
    credit = sum(captured) - Q(3, 4)*min(captured)
    return captured, area(poly), credit, area(core)


check(area(diamond), Q(2))

# Every displayed original cap has actual mixed-integer mass exactly 3.
for big_l in (Q(1, 2), Q(10)):
    for a, b, slope in ((Q(1), Q(0), big_l),
                        (Q(0), Q(1), Q(1, 2)),
                        (Q(-1), Q(-1), Q(1, 2))):
        check(sum(area(clip(diamond, a, b, slope*z))
                  for z in (-1, 0, 1, 2)), Q(3))
for sign in (-1, 1):
    check(sum(area(clip(diamond, Q(sign), Q(0), Q(1-z, 2)))
              for z in (-1, 0, 1, 2)), Q(3))

# Polygon clipping independently verifies the Fubini formulas over each
# claimed interval; these exact samples are diagnostics, not their proof.
for big_l, denominator in ((Q(1, 2), 600), (Q(10), 4000)):
    for k in range(1, 200):
        t = Q(k, denominator)
        captured, volume, credit, core = data(t, big_l)
        expected = [Q(3, 4)+(2*big_l-1)*t-(big_l**2+2*big_l)*t*t,
                    Q(3, 4)-t/2,
                    Q(3, 4)-t/2-t*t/2]
        for a, b in zip(captured, expected):
            check(a, b)
        check(volume, Q(3, 2)-2*t)
        check(min(captured), captured[2])
        check(credit, Q(27, 16)+(2*big_l-Q(13, 8))*t
              -(big_l**2+2*big_l+Q(1, 8))*t*t)
        check(credit-volume, Q(3, 16)+(2*big_l+Q(3, 8))*t
              -(big_l**2+2*big_l+Q(1, 8))*t*t)
        if t < 1/(2*big_l+Q(3, 2)):
            check(core, (big_l+1)**2*t*t/2)


def exact_quadratic_right_derivative(fn, epsilon):
    """Cancel the quadratic term; the selected examples have fixed topology."""
    f0 = fn(Q(0))
    slope = (fn(epsilon)-f0)/epsilon
    half_slope = (fn(epsilon/2)-f0)/(epsilon/2)
    return 2*half_slope-slope


for big_l, t, expected_derivatives in (
        (Q(1, 2), Q(1, 4), [Q(5, 8), Q(1, 2), Q(3, 4),
                             Q(2), Q(21, 16), Q(-11, 16), Q(-9, 16)]),
        (Q(10), Q(1, 40), [Q(-13), Q(1, 2), Q(21, 40),
                           Q(2), Q(-1979, 160), Q(-2299, 160), Q(-121, 40)])):
    def quantities(epsilon):
        a, v, f, core = data(t-epsilon, big_l)
        return a+[v, f, f-v, core]

    for j, expected in enumerate(expected_derivatives):
        check(exact_quadratic_right_derivative(
            lambda epsilon: quantities(epsilon)[j], Q(1, 100000)), expected)


def rectangle(lower, upper):
    return [(Q(0), lower), (Q(1), lower), (Q(1), upper), (Q(0), upper)]


# Coincident nonvertical cuts: neither the generic crossing velocity nor
# an arbitrarily chosen tied bound gives the correct derivative in general.
for cut, expected in (
        ((Q(0), Q(1), Q(0), Q(-2)), Q(2)),
        ((Q(0), Q(1), Q(1), Q(2)), Q(0)),
        ((Q(0), Q(1), Q(1), Q(0)), Q(1)),
        ((Q(0), Q(-1), Q(0), Q(0)), Q(1))):
    a, b, h, velocity = cut
    check(exact_quadratic_right_derivative(
        lambda e: area(clip(rectangle(-e, 1+e), a, b, h+velocity*e)),
        Q(1, 1000)), expected)

# Coincident lower section bounds must select the largest velocity.
check(exact_quadratic_right_derivative(
    lambda e: area(clip(clip(rectangle(-e, 1+e), Q(0), Q(1), e),
                       Q(0), Q(1), 2*e)), Q(1, 1000)), Q(-1))

# Initially zero-height intersection opens with a positive derivative.
check(exact_quadratic_right_derivative(
    lambda e: area(clip(clip(rectangle(-e, 1+e), Q(0), Q(1), Q(1, 2)-e),
                       Q(0), Q(-1), -Q(1, 2)-e)), Q(1, 1000)), Q(2))

# Initially point-width interval: endpoint active slopes and positive part.
check(exact_quadratic_right_derivative(
    lambda e: area(clip(clip(rectangle(-e, 1+e), Q(1), Q(0), Q(1, 2)-e),
                       Q(-1), Q(0), -Q(1, 2)-2*e)), Q(1, 1000)), Q(3))
check(exact_quadratic_right_derivative(
    lambda e: area(clip(clip(rectangle(-e, 1+e), Q(1), Q(0), Q(1, 2)+e),
                       Q(-1), Q(0), -Q(1, 2)+e)), Q(1, 1000)), Q(0))

# Active minima of captured areas: tied caps select the smallest derivative.
def tied_credit(epsilon):
    poly = rectangle(-epsilon, 1+epsilon)
    a1 = area(clip(poly, Q(0), Q(1), Q(1, 2)))
    a2 = area(clip(poly, Q(0), Q(1), Q(1, 2)+epsilon))
    return a1+a2-Q(3, 4)*min(a1, a2)

check(exact_quadratic_right_derivative(tied_credit, Q(1, 1000)), Q(1))

print(f"PASS: {checks} exact rational checks")
