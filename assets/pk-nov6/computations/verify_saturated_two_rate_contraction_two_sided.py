"""Exact algebra checks for the saturated two-rate certificate.

The arbitrary scalar menus below check the response identities and hinge
feasibility algebra, not realizability or criticality of those menus.
The source proof supplies the actual-body hypotheses separately.
"""

from fractions import Fraction as F
from itertools import product

checks = 0


def check(assertion):
    global checks
    assert assertion
    checks += 1


def hinge(status, x):
    return {"proper": x, "full": max(x, 0), "empty": min(x, 0),
            "strict_full": F(0), "strict_empty": F(0)}[status]


def z_value(row, loss, u, v, d):
    status, U, k, sigma, c, e = row
    H = 2 * loss - 2 * d * u * U + k * (u * c + v * e)
    return ((loss - d * u * U) / k
            - sigma * hinge(status, H) / (k * (k + 2 * sigma)))


def phi(rows, loss, u, v, d):
    return sum(z_value(row, loss, u, v, d) for row in rows)


def exact_loss(rows, u, v, d):
    knots = sorted(set(d * u * row[1] - row[2] * (u * row[4] + v * row[5]) / 2
                       for row in rows if row[0] in ("full", "empty")
                       and row[3] > 0))
    endpoints = [None] + knots + [None]
    for left, right in zip(endpoints, endpoints[1:]):
        if left is None and right is None:
            x, y = F(0), F(1)
        elif left is None:
            x, y = right - 2, right - 1
        elif right is None:
            x, y = left + 1, left + 2
        else:
            x, y = (2 * left + right) / 3, (left + 2 * right) / 3
        slope = (phi(rows, y, u, v, d) - phi(rows, x, u, v, d)) / (y - x)
        check(slope > 0)
        root = x - phi(rows, x, u, v, d) / slope
        if (left is None or root >= left) and (right is None or root <= right):
            check(phi(rows, root, u, v, d) == 0)
            return root
    raise AssertionError("No scalar response root")


statuses = ("proper", "full", "empty", "strict_full", "strict_empty")
a, b, body_k, Q = F(3), F(5), F(7), F(4)
ratio = Q / (a + b + body_k)
tau0 = a / (a + body_k)

for d in (1, 2, 4):
    for menu in product(statuses, repeat=3):
        rows = []
        for index, status in enumerate(menu):
            U = (F(index + 1, 2) if status == "proper"
                 else a if status in ("full", "strict_full") else F(0))
            sigma = F(index + 2, 3) if not status.startswith("strict") else F(0)
            c = (-F(index + 1) if status in ("full", "strict_full")
                 else F(index + 1) if status in ("empty", "strict_empty")
                 else F(index - 1, 2))
            rows.append((status, U, F(index + 2), sigma, c, F(index, 2)))

        for u, v in ((F(1), F(0)), (F(0), F(1)), (F(1), F(2, 5)),
                     (F(3), F(7))):
            loss = exact_loss(rows, u, v, d)
            z = [z_value(row, loss, u, v, d) for row in rows]
            check(sum(z) == 0)
            for row, zi in zip(rows, z):
                status, U, ki, sigma, c, e = row
                response = -ki * zi - d * u * U - sigma * hinge(status, 2 * zi + u * c + v * e)
                check(response == -loss)
            target = d * ratio * (a * u + b * v)
            check((loss > target) == (phi(rows, target, u, v, d) < 0))
            check(exact_loss(rows, 2 * u, 2 * v, d) == 2 * loss)

        def psi(tau):
            return phi(rows, d * ratio * (a + b * tau), F(1), tau, d)

        full_knots = []
        for status, U, ki, sigma, c, e in rows:
            A = 2 * d * ratio * a - 2 * d * U + ki * c
            B = 2 * d * ratio * b + ki * e
            check(B > 0)
            if status == "empty":
                check(A > 0)
            if status == "full" and sigma:
                check(A < 0)
                full_knots.append(-A / B)
        knots = sorted(set([F(0), tau0] + full_knots))
        tail = max(knots) + 1
        sample_points = knots + [tail, tail + 1]
        slopes = [(psi(y) - psi(x)) / (y - x)
                  for x, y in zip(sample_points, sample_points[1:])]
        check(all(x >= y for x, y in zip(slopes, slopes[1:])))

        infinity_weights = [1 / (row[2] + 2 * row[3])
                            if row[0] in ("proper", "full") else 1 / row[2]
                            for row in rows]
        W = sum(infinity_weights)
        J = sum(w * row[3] * row[5]
                for w, row in zip(infinity_weights, rows)
                if row[0] in ("proper", "full")) / W
        final_slope = psi(tail + 1) - psi(tail)
        check(final_slope == W * (d * ratio * b - J))
        check(phi(rows, d * ratio * b, F(0), F(1), d) == final_slope)
        check(phi(rows, d * a * Q, a + body_k, a, d)
              == (a + body_k) * psi(tau0))

        # Exact finite verification: a piecewise-affine function can attain
        # its lowest bounded-interval value only at these endpoints; its
        # final ray is decided exactly by the slope.
        candidate_values = [psi(tau0)] + [psi(t) for t in full_knots if t > tau0]
        feasible = any(x < 0 for x in candidate_values) or final_slope < 0
        claimed = psi(tau0) < 0 or J > d * ratio * b
        check(feasible == claimed)

# Support-function optimization checks. These rectangular domains are
# actual compact center sets, but the prescribed scalar menus are only
# algebra fixtures, not claimed critical cap configurations.
vertices_A = tuple(product((F(-1), F(1)), (F(-3, 4), F(3, 4))))
vertices_B = tuple(product((F(-1), F(1)), (F(-5, 4), F(5, 4))))
normals = ((F(1), F(0)), (F(0), F(1)), (F(-1), F(-1)))


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def support(vertices, normal):
    return max(dot(p, normal) for p in vertices)


d = 2
for menu in product(statuses, repeat=3):
    params = []
    for i, (status, normal) in enumerate(zip(menu, normals)):
        low = -support(vertices_A, tuple(-x for x in normal))
        high = support(vertices_A, normal)
        beta = (low if status == "full" else high if status == "empty"
                else low - 1 if status == "strict_full"
                else high + 1 if status == "strict_empty" else F(0))
        U = (a if status in ("full", "strict_full") else F(0)
             if status in ("empty", "strict_empty") else F(i + 1, 2))
        params.append((status, U, F(i + 2), F(i + 1, 3)
                       if not status.startswith("strict") else F(0),
                       beta, support(vertices_B, normal), normal))

    theta_domains = [((0, 1) if row[0] == "full" else (1,)
                      if row[0] == "proper" else (0,)) for row in params]
    branches = []
    for theta in product(*theta_domains):
        weights = [1 / (row[2] + 2 * ti * row[3]) for row, ti in zip(params, theta)]
        vector = tuple(sum(w * ti * row[3] * row[6][j]
                           for row, ti, w in zip(params, theta, weights))
                       for j in range(2))
        constant = (d * a * Q * sum(weights)
                    - d * (a + body_k) * sum(w * row[1] for row, w in zip(params, weights))
                    - sum(w * ti * row[3] * ((a + body_k) * row[4] + a * row[5])
                          for row, ti, w in zip(params, theta, weights)))
        branches.append((constant, vector))

    actual_values = []
    for p, q in product(vertices_A, vertices_B):
        rows = [(status, U, ki, sig, beta - dot(normal, p), h - dot(normal, q))
                for status, U, ki, sig, beta, h, normal in params]
        actual = phi(rows, d * a * Q, a + body_k, a, d)
        branch_min = min(c + (a + body_k) * dot(V, p) + a * dot(V, q)
                         for c, V in branches)
        check(actual == branch_min)
        actual_values.append(actual)
    support_min = min(c - (a + body_k) * support(vertices_A, tuple(-x for x in V))
                      - a * support(vertices_B, tuple(-x for x in V))
                      for c, V in branches)
    check(min(actual_values) == support_min)

    theta_inf = [int(row[0] in ("proper", "full")) for row in params]
    weights = [1 / (row[2] + 2 * ti * row[3]) for row, ti in zip(params, theta_inf)]
    V = tuple(sum(w * ti * row[3] * row[6][j]
                  for row, ti, w in zip(params, theta_inf, weights)) for j in range(2))
    Jmax = (sum(w * ti * row[3] * row[5] for row, ti, w in zip(params, theta_inf, weights))
            + support(vertices_B, tuple(-x for x in V))) / sum(weights)
    direct = max(sum(w * ti * row[3] * (row[5] - dot(row[6], q))
                     for row, ti, w in zip(params, theta_inf, weights)) / sum(weights)
                 for q in vertices_B)
    check(Jmax == direct)

print(f"PASS: {checks:,} exact scalar response, rate-feasibility, and support-envelope checks")
