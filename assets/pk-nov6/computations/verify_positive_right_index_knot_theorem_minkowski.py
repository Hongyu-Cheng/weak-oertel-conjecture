"""Exact checks of the all-dimensional positive-J knot theorem.

The proof is analytic and in the accompanying note. This verifies its
finite algebraic certificate and quadrature chain at rational knots.
"""

from fractions import Fraction as F
from math import comb


P = list(map(F, [9, 9, -60, -52, 88, 88, 32]))
rows = [
    (F(0), F(1, 2), [F(9), F(39,4), F(19,2), F(317,40),
                     F(76,15), F(43,24), F(3,4)]),
    (F(1,2), F(3,5), [F(3,4), F(13,24), F(317,750), F(2071,5000),
                      F(3377,6250), F(10353,12500), F(20448,15625)]),
    (F(3,5), F(1), [F(20448,15625), F(2019,625), F(25726,3125),
                    F(457,25), F(13588,375), F(331,5), F(114)])]
checks = 0
for left, right, expected in rows:
    powers = [sum(P[j]*comb(j,k)*left**(j-k)*(right-left)**k
                  for j in range(k,7)) for k in range(7)]
    bernstein = [sum(powers[j]*F(comb(k,j),comb(6,j))
                     for j in range(k+1)) for k in range(7)]
    assert bernstein == expected
    assert min(bernstein) >= F(2,5)
    checks += 2


def kernel_integral(d, C, slope, A, B):
    """Integral_0^(A/B) (C+slope*x)^(d-1)*(A-B*x) dx."""
    endpoint = A/B
    return sum(F(comb(d-1,j))*C**(d-1-j)*slope**j *
               (A*endpoint**(j+1)/F(j+1)-
                B*endpoint**(j+2)/F(j+2)) for j in range(d))


for d in range(2, 8):
    theta = F(d,d+1)
    for J in range(1,5):
        for H in range(J,(2*d+1)*J+d+1):
            a = F(H+J+1,(d+1)*H*(2*J+1))
            beta = F(H-J,d*(d+1)*H*(2*J+1))
            v = (d+1)*beta/a
            b = d*a*v
            assert 0 <= v <= 1
            assert 1/(a*(d+1)) == J+theta*v*(J+1)
            assert b == theta*v/(J+theta*v*(J+1))
            assert b <= F(1,2*J+1)
            A, B, C = 1-b, d+1+d*v, 1+a*v
            assert A/B == a*J
            assert 1/F(d+1-d*v) == a*H
            checks += 6
            IL = kernel_integral(d,F(1),-v,F(1),d+1-d*v)
            IR = kernel_integral(d,C,v,A,B)
            IR0 = kernel_integral(d,F(1),v,F(1),B)
            m = 1//a
            mass = sum((1-a*h)**d for h in range(m+1))
            left = sum((1-v*a*h)**(d-1)*(1-F(h,H))
                       for h in range(H))
            right = sum((C+v*a*h)**(d-1)*(A-B*a*h)
                        for h in range(J))
            R0 = C**(d-1)*A
            assert mass <= 1/(a*(d+1))+F(1,2)+a*d/8
            assert left >= IL/a+F(1,2)
            assert right >= IR/a+R0/2-b/2
            assert IR >= IR0-a*v/(1+v)
            assert IL+IR0 >= (1+v*v/4)/(d+1)
            assert R0 >= 1-b/2-b*b/2
            U = -v*v/4-v**3/3+v/(1+v)-F(1,2) + \
                3*v/(4*(1+2*v))+v*v/(4*(1+2*v)**2)+ \
                1/(8*(1+2*v))
            pval = sum(c*v**i for i,c in enumerate(P))
            assert -U == pval/(24*(1+v)*(1+2*v)**2)
            assert mass-left-right <= U <= F(-1,1080)
            checks += 8

print(f'PASS: {checks} exact positive-J identities, quadrature bounds, and certificate checks')
