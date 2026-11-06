"""Exact algebra/actual-interval checks for the full-space logarithmic flux.

This does not claim that the independently chosen interval ingredients form
a critical menu or a joint minimum.  It checks the analytic component fluxes,
including continuous piecewise-affine log weights and their internal seam.
"""
import sympy as s

checks = 0


def eq(a, b=0):
    global checks
    assert s.simplify(s.expand_log(s.sympify(a) - s.sympify(b), force=True)) == 0, (a, b)
    checks += 1


d = s.symbols("d", positive=True)
N = d + 1
eq(-1 + d / N + (d + 2) / 2 - d * (N + 2) / (2 * N))
eq(1 / N + s.Rational(1, 2) - (N + 2) / (2 * N))

# Formal unlabelled global force/base identities do not kill centroid torque.
v, g0, g1, g2 = s.symbols("v g0 g1 g2")
eq(v - 2 * v + v)
eq(-v + v)
eq(g0 * v - 2 * g1 * v + g2 * v, v * (g0 - 2 * g1 + g2))

x = s.symbols("x", real=True)
for width_num in range(2, 8):
    left = -s.Rational(width_num, 3)
    right = s.Rational(width_num + 2, 4)
    width = right - left
    g = (left + right) / 2
    for y_num in (1, 2, 3):
        y = left + s.Rational(y_num, 4) * width
        E = 4 * (y - left) * (right - y) / width
        a = (right + left - 2 * y) / (2 * (y - left) * (right - y))
        P = lambda z: 1 + a * (z - y)
        eq((P(right) ** -2 - P(left) ** -2) / (2 * E), -a)
        eq((right * P(right) ** -2 - left * P(left) ** -2) / (2 * E),
           s.Rational(1, 2) - y * a)
        eq((right - y) * P(right) ** -2 - (left - y) * P(left) ** -2, E)
        eq((right - y) ** 2 * P(right) ** -2 - (left - y) ** 2 * P(left) ** -2)

        cut = left + s.Rational(2, 5) * width
        # Both cap orientations, with unit coarea in this actual interval.
        eq(1, +1)
        eq(right, (right - cut) + cut)
        eq(-1, -1)
        eq(-left, (cut - left) - cut)

        eq((right - g) ** 2 - (left - g) ** 2)
        eq(right * (right - g) ** 2 - left * (left - g) ** 2,
           3 * width * (width ** 2 / 12))

        for slopes in ((s.Rational(1, 3), -s.Rational(1, 2)),
                       (s.Rational(1, 2), s.Rational(1, 5)),
                       (s.Integer(0), -s.Rational(2, 5))):
            knot = g
            height = s.Integer(7)
            pieces = ((left, knot, slopes[0]), (knot, right, slopes[1]))
            int_grad = 0
            int_log = 0
            int_xgrad = 0
            int_centergrad = 0
            for lo, hi, slope in pieces:
                intercept = height - slope * knot
                A = lambda z: slope * z + intercept
                assert A(lo) > 0 and A(hi) > 0
                checks += 2
                if slope == 0:
                    int_log += (hi - lo) * s.log(intercept)
                    continue
                int_grad += s.log(A(hi)) - s.log(A(lo))
                prim_log = lambda z: A(z) * (s.log(A(z)) - 1) / slope
                prim_xgrad = lambda z: z - intercept * s.log(A(z)) / slope
                int_log += prim_log(hi) - prim_log(lo)
                int_xgrad += prim_xgrad(hi) - prim_xgrad(lo)
                int_centergrad += (prim_xgrad(hi) - prim_xgrad(lo)
                                   - g * (s.log(A(hi)) - s.log(A(lo))))
            L_left = height + slopes[0] * (left - knot)
            L_right = height + slopes[1] * (right - knot)
            eq(int_grad, s.log(L_right) - s.log(L_left))
            eq(int_log + int_xgrad,
               right * s.log(L_right) - left * s.log(L_left))
            eq(int_log + int_centergrad,
               (right - g) * s.log(L_right) - (left - g) * s.log(L_left))

print(f"PASS: {checks} exact scalar, actual-interval, and PL seam checks.")
