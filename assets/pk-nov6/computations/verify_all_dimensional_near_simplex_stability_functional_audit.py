"""Exact algebraic consistency checks for the all-dimensional local theorem.

The compact normal gap is proved in the source, not numerically sampled
or assigned an unverified explicit value here.
"""
from fractions import Fraction as F
from math import prod

checks = 0


def check(p):
    global checks
    assert p
    checks += 1


for d in range(2, 41):
    m = d+1
    Gamma = F(d, m)**d
    c = (1-F(1, d**(d-1)))/F((d-1)**2*m)
    C = 8*m
    eta = min(F(1, 8*m), Gamma*c/F(4*C*2**(d+1)))
    E = C*eta*2**(d+1)
    B = F(2**d)/Gamma
    check(0 < c < 1)
    check(0 < eta < F(1, m))
    check(E <= Gamma*c/4)
    # Include all explicit restrictions independent of the compact gap.
    delta = min(F(1, 4), c/F(4*d), Gamma*c/F(4*B*d))
    check(delta <= F(1, 2))
    check(eta/(1-delta) <= F(1, 4*m))
    check((1-delta)**d >= 1-c/4)
    check((1-c)/(1-delta)**d <= 1-3*c/4)
    check(m*Gamma*(1-c)/(1-delta)**d + m*E <= m*Gamma*(1-c/2))
    check(1-(1-delta)**d <= d*delta)
    for k in range(11):
        f = delta/(1-delta)*F(k, 10)
        rho = 1+f
        w = 1-rho**(-d)
        check(d*(1-delta)**d*f <= w <= d*f)
        if k:
            check(w/f == sum(rho**(-j) for j in range(1, d+1)))
    for denom in (1, 2, 7, 31):
        tau = d*delta/denom
        check(0 < tau <= Gamma/2)
        check(tau <= Gamma*c/(4*B))
        for shift in range(3):
            weights = [1+(i+shift) % 3 for i in range(m)]
            losses = [m*Gamma*(1-c/2)*tau*w/sum(weights) for w in weights]
            factor = min(F(1), tau/max(losses))
            losses = [factor*v for v in losses]
            average = sum(losses)/m
            bary = [F(1, m)+(average-v)/(m*Gamma) for v in losses]
            check(sum(bary) == 1)
            check(all(F(0) <= v <= tau for v in losses))
            check(sum(losses) <= m*Gamma*(1-c/2)*tau)
            check(all(v >= F(1, 2*m) > delta/m for v in bary))
            for i in range(m):
                vertex_cap = d**d*prod(bary[j] for j in range(m) if j != i)
                displacement = bary[i]-F(1, m)
                check(vertex_cap >= Gamma-m*Gamma*displacement-B*tau*tau)
                actual_lower = vertex_cap-losses[i]
                check(actual_lower >= Gamma-average-B*tau*tau)
                check(actual_lower/(1-tau)-Gamma >= Gamma*c*tau/4)
    # Geometric frame conversion and support slack in Section6.
    L = 8*(d+1)**3
    epsilon = min(F(1, 64*(d+1)**3), delta/F(d*(d+1)*(L+1)))
    check(epsilon <= F(1, 64*d**3))
    check(epsilon <= F(1, 8*d*d))
    check(8*d**3*epsilon <= L*epsilon)
    check(delta/F(d*(d+1)) >= (L+1)*epsilon)

print(f"PASS: {checks} exact checks in dimensions2--40; gauge weights, "
      "strip budgets, balanced candidates, product remainders, affine locality.")
