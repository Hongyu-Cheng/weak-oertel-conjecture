"""Exact rational certificates for the four-monotone-triangle theorem."""
from fractions import Fraction as Q

G = Q(4, 9)


def envelope(r, t):
    if t <= 0:
        return r*r
    if 3*t <= r:
        return (r-t)**2
    if 2*t <= r:
        return 4*t*(r-2*t)
    return Q(0)


def positive_cap(r, t, w):
    w = max(w, 1-w)
    if t <= 0:
        return r*r
    if t >= w*r:
        return Q(0)
    if w == 1:
        return (r-t)**2
    if t <= (1-w)*r:
        return r*r-t*t/(w*(1-w))
    return (w*r-t)**2/(w*(2*w-1))


def exact_tilt_minimum(radii, j):
    q = radii[j]/3
    knots = sorted({(q-t)/(i-j) for i, r in enumerate(radii) if i != j
                    for t in (Q(0), r/3, r/2)})
    if not knots:
        return envelope(radii[j], q)
    # Every other trace is constant beyond the outer breakpoints.
    values = []
    def value(beta):
        return sum((envelope(r, q-beta*(i-j)) for i, r in enumerate(radii)), Q(0))
    values.extend(value(k) for k in knots)
    for left, right in zip(knots, knots[1:]):
        middle = (left+right)/2
        aa = bb = cc = Q(0)
        for i, r in enumerate(radii):
            z = i-j
            t = q-middle*z
            if t <= 0:
                cc += r*r
            elif 3*t <= r:
                aa += z*z
                bb += 2*(r-q)*z
                cc += (r-q)**2
            elif 2*t <= r:
                aa -= 8*z*z
                bb += 4*z*(4*q-r)
                cc += 4*q*(r-2*q)
        assert value(middle) == aa*middle*middle+bb*middle+cc
        if aa > 0:
            vertex = -bb/(2*aa)
            if left <= vertex <= right:
                values.append(value(vertex))
    return min(values)


def main():
    scalar_checks = normal_checks = growth_checks = 0
    for bi in range(12, 25):
        b = Q(bi, 24)
        for xi in range(12, 25):
            x = Q(xi, 72)
            assert envelope(b,x)+envelope(Q(1),Q(2,3)-x) >= G*b*b
            scalar_checks += 1
    for ri in range(1, 13):
        r = Q(ri, 4)
        for ti in range(-2, 25):
            t = r*Q(ti, 36)
            for wi in range(12, 25):
                assert positive_cap(r,t,Q(wi,24)) >= envelope(r,t)
                normal_checks += 1
            if 0 < t < r/2:
                w = Q(1) if 3*t <= r else t/(4*t-r)
                assert positive_cap(r,t,w) == envelope(r,t)
    for di in range(12, 61):
        d = Q(di, 12)
        for ti in range(12, 19):
            t = Q(ti, 36)
            assert envelope(d,t)-envelope(Q(1),t) >= Q(2,3)*(d*d-1)
            growth_checks += 1
    profiles = nonheavy = 0
    for a in range(1, 6):
        for s0 in range(7):
            for s1 in range(s0+1):
                for s2 in range(s1+1):
                    r = list(map(Q, [a, a+s0, a+s0+s1, a+s0+s1+s2]))
                    total = sum(x*x for x in r)
                    target = G*total/2
                    if 2*r[-1]**2 >= total:
                        assert G*r[-1]**2 >= target
                    else:
                        assert exact_tilt_minimum(r, 2) >= target, r
                        nonheavy += 1
                    profiles += 1
    calibration = list(map(Q,[2,3,4,5]))
    assert exact_tilt_minimum(calibration, 2) >= Q(12)
    print(f"PASS: {scalar_checks} scalar, {normal_checks} cap-envelope, "
          f"{growth_checks} growth checks; {profiles} four-profiles, "
          f"including exact all-tilt minimization for {nonheavy} nonheavy profiles.")


if __name__ == '__main__':
    main()
