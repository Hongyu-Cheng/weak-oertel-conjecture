"""Exact moments, partition Jacobians, densities, and sharpness certificates."""
from fractions import Fraction as F
from itertools import product
from math import factorial, comb, prod

checks = 0


def check(p):
    global checks
    assert p
    checks += 1


def uniform_moment(alpha):
    m, degree = len(alpha), sum(alpha)
    return F(factorial(m-1)*prod(factorial(a) for a in alpha), factorial(m-1+degree))


def averaged_moment(alpha, b):
    m, degree = len(alpha), sum(alpha)
    result = F(0)
    for i in range(m):
        for k in range(alpha[i]+1):
            power = list(alpha)
            power[i] -= k
            result += F(comb(alpha[i], k), m)*b**k*(1-b)**(degree-k)*uniform_moment(power)
    return result


def merged_moment(alpha):
    m, degree = len(alpha), sum(alpha)
    result = F(0)
    for i in range(m):
        for k in range(alpha[i]+1):
            power = list(alpha)
            power[i] -= k
            beta_moment = F(m*factorial(k)*factorial(m+degree-k-1), factorial(m+degree))
            result += F(comb(alpha[i], k), m)*beta_moment*uniform_moment(power)
    return result


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for k in range(total+1):
            for tail in compositions(total-k, count-1):
                yield (k,)+tail


def reconstructed_moment(alpha, critical):
    d, degree = len(alpha), sum(alpha)
    total = F(0)
    for i in range(d):
        others = [j for j in range(d) if j != i]
        for powers in product(*(range(alpha[j]+1) for j in others)):
            k = sum(powers)
            tpower = degree-k
            coefficient = prod(comb(alpha[j], power) for j, power in zip(others, powers))
            t_moment = F((d-1)*factorial(tpower)*factorial(k+d-2), factorial(degree+d-1))
            face_moment = averaged_moment(powers, F(1, d)) if critical else uniform_moment(powers)
            total += F(coefficient, d**(tpower+1))*t_moment*face_moment
    return total


def determinant(matrix):
    rows = [list(row) for row in matrix]
    value = F(1)
    for i in range(len(rows)):
        j = next(j for j in range(i, len(rows)) if rows[j][i])
        if j != i:
            rows[i], rows[j] = rows[j], rows[i]
            value = -value
        pivot = rows[i][i]
        value *= pivot
        for j in range(i+1, len(rows)):
            ratio = rows[j][i]/pivot
            for k in range(i, len(rows)):
                rows[j][k] -= ratio*rows[i][k]
    return value


for m in range(1, 9):
    for degree in range(5):
        for alpha in compositions(degree, m):
            check(merged_moment(alpha) == uniform_moment(alpha))
    # Mean of the random step is precisely the needed lower-dimensional one.
    check(F(m*factorial(1)*factorial(m-1), factorial(m+1)) == F(1, m+1))

moments = 0
for d in range(2, 8):
    rho = F(d-1, d)
    check(d*rho**(d-1) == (d-1)*rho**(d-2))
    check(F(d-1)*rho**(d-2)/(d*rho**(d-1)) == 1)
    g = [F(1, d)]*(d-1)
    vertices = [[F(int(i == j)) for j in range(d-1)] for i in range(d)]
    for i in range(d):
        others = [vertices[j] for j in range(d) if j != i]
        columns = [[p[j]-g[j] for j in range(d-1)] for p in others]
        matrix = [[columns[j][k] for j in range(d-1)] for k in range(d-1)]
        check(abs(determinant(matrix)) == F(1, d))
    for degree in range(4):
        for alpha in compositions(degree, d):
            check(reconstructed_moment(alpha, False) == uniform_moment(alpha))
            check(reconstructed_moment(alpha, True) == averaged_moment(alpha, F(1, d)))
            moments += 1
    for k in range(1, 31):
        t = F(k, 31)
        for w in (F(0), F(1, d), F(1, 2), F(1)):
            y = t/d+(1-t)*w
            check((y >= F(1, d)) == (w >= F(1, d)))
        s = F(k, 31*d)
        check((1-F(d-1)*s/rho)**(d-1) == (1-d*s)**(d-1))
    # The concave minimum is an exact strict counter above the threshold.
    original_min = F(1, d*d)
    for k in range(1, 31):
        b = F(1, d)+(1-F(1, d))*F(k, 30)
        check((1-b)/F(d*(d-1)) < original_min)
    check((1-F(1, d))/F(d*(d-1)) == original_min)

# Two-coordinate critical law is uniform, not just smaller in convex order.
for degree in range(15):
    for alpha in compositions(degree, 2):
        check(averaged_moment(alpha, F(1, 2)) == uniform_moment(alpha))

print(f"PASS: {checks} exact checks; {moments} reconstructed moment identities; "
      "critical cell determinants, random-step moments, sharp minimum counter.")
