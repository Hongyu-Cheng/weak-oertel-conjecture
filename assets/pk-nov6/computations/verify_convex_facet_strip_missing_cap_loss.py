"""Exact convex strip integrals and actual slender missing-cap examples."""
from fractions import Fraction as Q
from math import comb, factorial


def integrate_poly(coeff, lo, hi):
    return sum(c*(hi**(j+1)-lo**(j+1))/(j+1)
               for j, c in enumerate(coeff))


def ridge_integral(k, a, p, left, lo, hi):
    if left:
        hi = min(hi, a)
        coeff = [Q(comb(p, j))*(-1)**j*a**(p-j) for j in range(p+1)]
    else:
        lo = max(lo, a)
        coeff = [Q(comb(p, j))*(-a)**(p-j) for j in range(p+1)]
    if lo >= hi:
        return Q(0)
    weight = [Q(k*comb(k-1, j))*(-1)**j for j in range(k)]
    product = [Q(0)]*(p+k)
    for i, c in enumerate(coeff):
        for j, e in enumerate(weight):
            product[i+j] += c*e
    return integrate_poly(product, lo, hi)


strip_checks = 0
for k in range(1, 11):
    for b in [Q(1, k+2), Q(1, 10), Q(1, 2), Q(9, 10)]:
        r = min(b, (1-b)/k)/4
        C = 2/r
        for eta in [r, r/2, r/17]:
            assert b-eta-r > 0 and b+eta+r < 1
            for a in [Q(0), Q(1, 1000), Q(1, 3),
                      Q(2, 3), Q(999, 1000), Q(1)]:
                for p in [1, 2, 5]:
                    for left in [False, True]:
                        total = ridge_integral(k, a, p, left, Q(0), Q(1))
                        strip = ridge_integral(k, a, p, left, b-eta, b+eta)
                        assert 0 <= strip <= C*eta*total
                        strip_checks += 1
                    if k >= 2:
                        # A genuinely different-coordinate ridge:
                        # f=(s_j-a)_+^p with j != the strip coordinate.
                        degree = p+k
                        factor = Q(factorial(k)*factorial(p), factorial(degree))
                        total = factor*(1-a)**degree
                        strip = factor*(max(1-a-b+eta, Q(0))**degree
                                        - max(1-a-b-eta, Q(0))**degree)
                        assert 0 <= strip <= C*eta*total
                        strip_checks += 1

radial_checks = 0
for d in range(2, 21):
    b = Q(1, d+1)
    r = min(b, (1-b)/(d-1))/4
    assert r == Q(1, 4*(d+1))
    assert 2/r == 8*(d+1)
    for delta in [Q(0), Q(1, 100), Q(1, 2*(d+1)), Q(1, 4), Q(1, 2)]:
        for j in range(11):
            rho = 1 + delta/(1-delta)*Q(j, 10)
            f = rho-1
            w = 1-rho**(-d)
            assert w == f*sum(rho**(-i) for i in range(1, d+1))
            assert d*(1-delta)**d*f <= w <= d*f
            if delta <= Q(1, 2*(d+1)):
                assert (1-delta)**(d+1) >= Q(1, 2)
            radial_checks += 1


def area(poly):
    if len(poly) < 3:
        return Q(0)
    return abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                   - poly[i][1]*poly[(i+1) % len(poly)][0]
                   for i in range(len(poly))))/2


def clip(poly, u, threshold):
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        hp = u[0]*p[0]+u[1]*p[1]-threshold
        hq = u[0]*q[0]+u[1]*q[1]-threshold
        if hp >= 0:
            out.append(p)
        if (hp < 0 < hq) or (hq < 0 < hp):
            f = hp/(hp-hq)
            out.append((p[0]+f*(q[0]-p[0]), p[1]+f*(q[1]-p[1])))
    return out


S = [(Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(1))]
g = (Q(1, 3), Q(1, 3))
facet_centroids = [(Q(1, 2), Q(0)), (Q(0), Q(1, 2)), (Q(1, 2), Q(1, 2))]
actual_checks = 0
for delta in [Q(1, 2), Q(1, 4), Q(1, 8), Q(1, 64),
              Q(1, 1024), Q(1, 2**20)]:
    eps = delta/2
    for a in [Q(1, 2), Q(9, 10), Q(999, 1000)]:
        # K retains every facet centroid but removes a thin triangular
        # region along y=0, without changing the enclosing simplex.
        K = clip(S, (-eps, Q(1)), -eps*a)
        assert all(y-eps*x >= -eps*a for x, y in facet_centroids)
        inner = [(g[0]+(1-delta)*(x-g[0]),
                  g[1]+(1-delta)*(y-g[1])) for x, y in S]
        assert all(y-eps*x >= -eps*a for x, y in inner)
        missing = area(S)-area(K)
        assert missing == eps*(1-a)**2/(2*(1+eps)) > 0
        for denominator in [1, 4, 16, 128]:
            eta = (1-delta)/(12*denominator)
            # Perturb all three affine coefficients. On S the margin
            # error is at most eta, by the sum of their absolute errors.
            alpha, beta, shift = eta/3, -eta/3, eta/3
            normal = (-1-alpha, -1-beta)
            threshold = -Q(2, 3)+shift
            canonical_normal = (Q(-1), Q(-1))
            canonical_threshold = -Q(2, 3)
            loss = area(clip(S, normal, threshold))-area(clip(K, normal, threshold))
            loss0 = (area(clip(S, canonical_normal, canonical_threshold))
                     - area(clip(K, canonical_normal, canonical_threshold)))
            assert abs(loss-loss0) <= 24*eta*missing/(1-delta)**3
            actual_checks += 1

print("PASS", strip_checks, "exact convex-ridge strip integrals;",
      radial_checks, "radial comparisons;", actual_checks,
      "actual slender missing-cap comparisons")
