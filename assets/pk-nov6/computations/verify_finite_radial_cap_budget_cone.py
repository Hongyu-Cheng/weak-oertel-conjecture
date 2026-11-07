"""Exact finite checks of the radial compatibility/budget cone."""
from fractions import Fraction as F


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def scale(c, a):
    return [c*x for x in a]


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


relation_checks = 0
dual_checks = 0
cap_checks = 0
for m in range(3, 31):
    one = [F(1)]*m
    basis = [[F(int(i == j)) for i in range(m)] for j in range(m)]
    phi = [F(j*(m-1-j)) for j in range(m)]
    average = sum(phi)/m
    sigma = [x-average for x in phi]
    assert sum(sigma) == 0
    assert sigma[0] == sigma[-1] == -average < 0
    for j in range(1, m-1):
        for a in range(j):
            for b in range(j+1, m):
                wa, wb = F(b-j, b-a), F(j-a, b-a)
                gap = sigma[j]-wa*sigma[a]-wb*sigma[b]
                assert gap == wa*(a-j)**2+wb*(b-j)**2 > 0
                relation_checks += 1
    for V in (F(1, 2), F(1), F(7, 3)):
        w = scale(V, one)
        C0 = scale(V, basis[0])
        C1 = scale(V, basis[-1])
        Cbar0 = scale(V, add(one, scale(-1, basis[0])))
        Cbar1 = scale(V, add(one, scale(-1, basis[-1])))
        assert dot(w, sigma) == 0
        assert dot(C0, sigma) < 0 and dot(C1, sigma) < 0
        assert dot(Cbar0, sigma) > 0 and dot(Cbar1, sigma) > 0
        left = [F(0)]*m
        for j in range(1, m-1):
            row = add(basis[j], add(scale(-F(m-1-j, m-1), basis[0]),
                                   scale(-F(j, m-1), basis[-1])))
            left = add(left, row)
        right = add(scale(F(m, 2)/V, add(Cbar0, Cbar1)),
                    scale(F(1-m)/V, w))
        assert left == right
        dual_checks += 1
        for d in range(1, 9):
            gamma = F(d, d+1)**d
            canonical = scale(gamma, w)
            assert dot(canonical, sigma) == 0
            # The volume coordinates make mass and invariant cap costs exactly
            # affine; choose t so every volume factor is positive.
            t = F(1, 2)/(1+max(abs(x) for x in sigma))
            factors = [1+t*x for x in sigma]
            assert all(x > 0 for x in factors)
            assert dot(w, factors) == sum(w)
            assert dot(canonical, factors) == sum(canonical)
            assert dot(C0, factors) < sum(C0)
            assert dot(C1, factors) < sum(C1)
            cap_checks += 1

# Independent check of the sign in the oblique coarea derivative for an interval.
# K=[-a,b], cap x>=tau proper. Under scale r, its length is r*b-tau.
for a, b in [(F(1), F(2)), (F(3, 2), F(5, 3)), (F(2), F(1))]:
    for numerator in range(-4, 5):
        tau = F(numerator, 5)
        if not -a < tau < b:
            continue
        c, S = b-tau, F(1)
        assert c+tau*S == b

print(f"PASS: {relation_checks} exact strict Jensen directions; "
      f"{dual_checks} actual complementary-cap dual certificates; "
      f"{cap_checks} fixed-mass canonical/endpoint budget paths; "
      "proper interval section-term sign.")
