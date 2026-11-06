from fractions import Fraction as F


def pos(x):
    return max(F(0), x)


checks = 0
for d in [2, 3, 4, 5, 8, 12]:
    p = d - 1
    kappa = F(2 * d, d + 1)
    for q in [F(1, 2), F(3, 4), F(9, 10)]:
        R = q**(-p)
        t = (1 + R) / 2
        J = (1 - q)**(-p)
        assert R == 2 * t - 1 and t > 1
        for xi in [0, 1, 3, 7]:
            x = F(xi, 20)
            cstar = x / (1 - q)
            assert cstar**d - R * pos(cstar - x)**d == J * x**d
            for ci in range(31):
                c = F(ci, 20)
                assert c**d - R * pos(c - x)**d <= J * x**d
                checks += 1
        for bi in range(11, 21):
            b = F(bi, 20)
            B = b**d
            Amax = (2*b - 1)**d
            x = kappa * (1 - b)
            eta_power = d * (t - 1) / (t * kappa**d * J)
            for ci in range(0, bi + 1):
                c = F(ci, 20)
                C = c**d
                H = pos(c - x)**d
                Ahat = min(Amax, H + (1 - B)/t)

                def gap(A):
                    return max(B+t*A, 1+t*H) - (A+B+1+C)/2

                D1 = 1 - B - Amax - C + 2*t*H
                D2 = (t-1)*(1-B) - t*C + t*R*H
                assert 2 * gap(Ahat) == max(D1, D2/t)
                for A in [F(0), Amax/3, Amax, Ahat]:
                    assert gap(A) >= gap(Ahat)
                    assert gap(A) >= D2/(2*t)
                    loss_bound = ((t-1)*(1-B) - t*J*x**d)/(2*t)
                    assert gap(A) >= loss_bound
                    if ((1-b)/b)**p <= eta_power:
                        assert loss_bound >= 0
                        assert gap(A) >= 0
                    checks += 1
                # Exact constrained scalar loss from the derivative formula.
                if x <= b*(1-q):
                    sharp = J*x**d
                    v = x/(1-q)
                else:
                    sharp = b**d - R*pos(b-x)**d
                    v = b
                assert 0 <= v <= b
                assert v**d - R*pos(v-x)**d == sharp
                assert C-R*H <= sharp

# The actual d=2 sharp coefficient has an exact rational eta.
d = 2
t = F(7,4)
R = 2*t-1
kappa = F(4,3)
J = R/(R-1)
eta = d*(t-1)/(t*kappa**d*J)
assert eta == F(81,280)
assert 1/(1+eta) == F(280,361)

print(f'PASS: {checks} exact scalar loss, crossover, weighted-gap and near-plateau checks; eta_2=81/280.')
