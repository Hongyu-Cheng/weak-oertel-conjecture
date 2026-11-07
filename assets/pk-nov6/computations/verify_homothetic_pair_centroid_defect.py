"""Exact arithmetic certificates for the homothetic centroid-defect note."""
from fractions import Fraction as Q


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def mul(c, x):
    return tuple(c * a for a in x)


def simplex_vertices(d):
    g = (Q(1, d + 1),) * d
    out = [mul(-1, g)]
    for i in range(d):
        e = tuple(Q(int(j == i)) for j in range(d))
        out.append(add(e, mul(-1, g)))
    return out


def in_scaled_simplex(x, radius, d):
    return min(x) >= -radius / (d + 1) and sum(x) <= radius / (d + 1)


checks = 0
for d in range(1, 11):
    vertices = simplex_vertices(d)
    v = vertices[0]
    for rho in [Q(1), Q(3, 2)]:
        for delta in [Q(0), rho / (2 * d), rho / d, 2 * rho / d]:
            center = mul(-delta, v)
            for x in vertices:
                # Every endpoint vertex lies in the proposed middle simplex.
                relative = add(mul(rho, x), mul(-1, center))
                assert in_scaled_simplex(relative, rho + delta, d)
            assert sum(center) == d * delta / (d + 1)
            gauge = d * delta
            assert in_scaled_simplex(center, gauge, d)
            if delta > 0:
                assert sum(center) == gauge / (d + 1)
            if delta == rho / d:
                assert sum(center) == rho / (d + 1)
                # The endpoint cap is a supporting facet, hence volume zero.
                assert all(sum(mul(rho, x)) <= sum(center) for x in vertices)
            if delta <= rho / d:
                a = (1 - d * delta / rho) / (d + 1)
                assert 0 <= 2 * a <= 1
                branch = rho ** d * (1 - (1 - 2 * a) ** d)
                assert branch >= 0
                if delta == rho / d:
                    assert branch == 0
            checks += 1

# Exact inner copies: arbitrary rational asymmetric endpoint data in d=2.
rp, rq, theta = Q(2), Q(3), Q(2, 5)
rho = (rp + rq) / 2
cp, cq = (Q(1), Q(-2)), (Q(-3), Q(4))
m = mul(Q(1, 2), add(cp, cq))
k = simplex_vertices(2)[1]
target = add(m, mul(theta * rho, k))
new_cp = add(cp, mul(theta * rp, k))
new_cq = add(cq, mul(theta * rq, k))
assert mul(Q(1, 2), add(new_cp, new_cq)) == target
for radius, center, shifted in [(rp, cp, new_cp), (rq, cq, new_cq)]:
    for x in simplex_vertices(2):
        new_vertex = add(shifted, mul((1 - theta) * radius, x))
        assert in_scaled_simplex(add(new_vertex, mul(-1, center)), radius, 2)

d, rho, delta = 3, Q(1), Q(1, 5)
gamma = Q(d, d + 1) ** d
own_radius = rho + delta
theta = d * delta / rho
certificate = gamma * (own_radius ** d + 2 * (1 - theta) ** d)
mass = own_radius ** d + 2
target = gamma * mass / 2
assert mass == Q(466, 125)
assert certificate == gamma * Q(232, 125)
assert target == gamma * Q(233, 125)
assert target - certificate == gamma / 125
assert 2 * gamma > target
assert 3 * gamma > target

print("PASS: {} exact simplex offset cases, inner-copy centroids and containment,"
      " optimal d threshold, and the safe three-fiber certificate shortfall."
      .format(checks))
