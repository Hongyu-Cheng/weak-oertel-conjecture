"""Independent exact radial-density arithmetic for the sharp roof constant."""
from fractions import Fraction as F
from math import comb

checks = 0


def check(p):
    global checks
    assert p
    checks += 1


def polynomial_power(c, slope, degree):
    return [F(comb(degree, k))*c**(degree-k)*slope**k for k in range(degree+1)]


def multiply(p, q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def integrate(p, a, b):
    return sum(v*(b**(k+1)-a**(k+1))/F(k+1) for k, v in enumerate(p))


for d in range(2, 21):
    m, b, h = d-1, F(1, d+1), F(d, d+1)
    theta = d*b
    check(theta == h)
    lower = [v*F(m*m, d)/h**(d-1)
             for v in polynomial_power(h, -F(m, d), d-2)]
    upper = [v*m/h**(d-1) for v in polynomial_power(F(1), F(-1), d-2)]
    def qr_moment(k):
        factor = polynomial_power(F(1), F(-1), k)
        return integrate(multiply(lower, factor), F(0), theta)+integrate(multiply(upper, factor), theta, F(1))
    check(qr_moment(0) == 1)
    pR = F(d-1, d)
    qR = qr_moment(1)
    mean_min = (1-qR)/d
    expected_min = (1-F(1, d**(d+1)))/F(d*d-1)
    check(mean_min == expected_min)
    constant = (1-F(1, d**(d-1)))/F((d-1)**2*(d+1))
    check(1-qR/pR == constant)
    check(0 < constant < 1)
    # Sharpness of psi=min: supporting majorant is the constant1/d.
    check(mean_min-F(1, d*d) == constant*(F(1, d)-F(1, d*d)))
    for power in range(1, 8):
        pr_power = F(d-1, d-1+power)
        check(qr_moment(power) <= qR/pR*pr_power)
    for j in range(101):
        t = theta*F(j, 101)
        step = (b-t/d)/(1-t)
        check(0 < step <= b <= F(1, m))
        base = (h-F(m, d)*t)/(1-t)
        check(1-step == base)
        ratio = F(m, d)/h**(d-1)*base**(d-2)
        if j:
            check(ratio >= old_ratio)
        old_ratio = ratio
    check(F(m, d)/h**(d-1) <= 1/h**(d-1))

check((1-F(1, 2))/F(3) == F(1, 6))
check((1-F(1, 9))/F(16) == F(1, 18))

# Independent extension to every sampled subcritical step, not just1/(d+1).
for d in range(2, 13):
    m = d-1
    for z in range(1, 20):
        b = F(z, 20*d)
        h, a, theta = 1-b, 1-d*b, d*b
        lower = [v*F(m*m, d)/h**(d-1)
                 for v in polynomial_power(h, -F(m, d), d-2)]
        upper = [v*m/h**(d-1) for v in polynomial_power(F(1), F(-1), d-2)]
        def all_step_moment(k):
            p = polynomial_power(F(1), F(-1), k)
            return integrate(multiply(lower, p), F(0), theta)+integrate(multiply(upper, p), theta, F(1))
        check(all_step_moment(0) == 1)
        mean_min = h/F(d*m)-a**d/F(d*d*m)/h**(d-1)
        check((1-all_step_moment(1))/d == mean_min)
        constant = (a-a**d/h**(d-1))/F(m*m)
        check(0 < constant < 1)
        check(1-all_step_moment(1)/F(m, d) == constant)
        check(mean_min-F(1, d*d) == constant*(F(1, d)-F(1, d*d)))
        for k in range(1, 6):
            check(all_step_moment(k) <= (1-constant)*F(m, m+k))

print(f"PASS: {checks} exact checks; dimensions2--20, radial moments, "
      "209 general steps, monotone density ratios, sharp minimum equality.")
