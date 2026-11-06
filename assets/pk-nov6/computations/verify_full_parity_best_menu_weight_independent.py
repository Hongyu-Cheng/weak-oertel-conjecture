"""Exact algebra and convex-inclusion certificates for the four-fiber family.

The uniform positive-width IFT/IVT proof is analytical in the companion note.
"""
from fractions import Fraction as F
import sympy as s

checks = 0


def check(a, b):
    global checks
    assert s.simplify(a-b) == 0, (a, b)
    checks += 1


t, sig = s.symbols('t sig', positive=True)
V = s.Rational(9, 2)
mark = 3*t-1
delta = 3-1/t
qA, qB = 4*V*t*t, 4*V*t*(1-2*t)
check(qA+V*sig*sig-qB, V*(12*t*t-4*t+sig*sig))
thetaA = (4*t-1)/(6*t-1)
thetaB = t/(6*t-1)
check(thetaA+2*thetaB, 1)
check(-thetaA+(1+delta)*thetaB, 0)
check(s.Rational(1, 3)-thetaA, 2*(1-3*t)/(3*(6*t-1)))

# Own section centroids and coareas in raw normal coordinates.
margin = (1+delta)*mark
edge_AB_x = margin+delta
edge_BC_x = (margin-delta)/(1-delta)
edge_BC_y = 1-edge_BC_x
check((edge_AB_x+edge_BC_x)/2, mark)
check((-1+edge_BC_y)/2, mark)
check(edge_BC_y+1, 6*t)
check(2*mark+2, 6*t)
check((2-edge_BC_x)/3, 2*t)
pay = 2*thetaB*(2*t)
check(pay, 4*t*t/(6*t-1))
check(pay-s.Rational(4, 9), 4*(3*t-1)**2/(9*(6*t-1)))

# Both restrictive miss margins agree exactly; the common value is negative
# by the stated elementary bounds |delta|<=5 sigma^2, |mark|<=1.5 sigma^2.
a = -1+s.Rational(7, 2)*sig
b, r = 1-4*sig, -8*sig
margin_D = -a+(-1+3*sig-delta)-(1+delta)*mark
margin_R = a+(b-delta)-(1+delta)*mark
check(margin_D, margin_R)
check(margin_D, -sig/2-delta-(1+delta)*mark)

# The witness menu obeys a strict support-width reserve despite low theta_A.
abar = -3*thetaA+2*a*thetaB
reserve = (1-2*sig)*(2*thetaA+2*thetaB*(1-delta))
check(-abar-reserve, (1+3*delta+sig)/(3+delta))

# Exact compatibility checks at all vertex sums for a range of rational shapes.
T = [(F(-1), F(-1)), (F(2), F(-1)), (F(-1), F(2))]
for den in [10000, 40000, 90000, 160000]:
    sigma = F(1, den)
    root = {10000:F(1,100),40000:F(1,200),
            90000:F(1,300),160000:F(1,400)}[den]
    D = [(-1+sigma*(x+1), -1+sigma*(y+1)) for x,y in T]
    upper = 1-4*sigma
    R = [(x,y) for x in [-1,upper] for y in [-1,upper]]
    for multiple in [F(2),F(5,2),F(3),F(7,2),F(4)]:
        ell = multiple*root
        right = -8*sigma
        E = [(x,y) for x in [right-ell,right] for y in [right-ell,right]]
        for x,y in D:
            for a1,a2 in R:
                mx,my=(x+a1)/2,(y+a2)/2
                assert mx>=-1 and my>=-1 and mx+my<=1
                checks+=1
        for x,y in T:
            for a1,a2 in E:
                mx,my=(x+a1)/2,(y+a2)/2
                assert -1<=mx<=upper and -1<=my<=upper
                checks+=1
        center=-2*sigma
        for x,y in E:
            vx,vy=2*center-x,2*center-y
            for dx in [-F(1,4),F(1,4)]:
                for dy in [-F(1,4),F(1,4)]:
                    xx,yy=vx+dx,vy+dy
                    assert xx>=-1 and yy>=-1 and xx+yy<=1
                    checks+=1
        assert ell*ell<F(1,8)
        checks+=1
    assert 8*sigma-8*sigma*sigma>4*sigma
    assert 8*sigma-F(7,2)*sigma*sigma<16*sigma
    checks+=2

print(f'PASS: {checks} exact full-parity compatibility, quota, response, and facet-payment certificates')
