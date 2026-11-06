#!/usr/bin/env python3
"""Exact identities behind the analytic affine rate-slice theorem.

This verifies the projection/coarea algebra and exact two-rate measures.
It does not replace the Helly, weak-closure, or geometric limit proofs.
"""
from fractions import Fraction as F
import sympy as s

checks = 0


def check(value):
    global checks
    assert value
    checks += 1


b, lo, hi, y, o = s.symbols('b lo hi y o', real=True)
alpha = (b-hi)/(b-lo)
proj_hi = o+b/(b-hi)*(alpha*y+(1-alpha)*o-o)
proj_lo = o+b/(b-lo)*(y-o)
check(s.factor(proj_hi-proj_lo) == 0)

r, lam, c, mass = s.symbols('r lam c mass', positive=True)
lev = s.exp(-r/lam)
check(s.simplify(-s.diff(lev, r)/lev-1/lam) == 0)
check(s.simplify((-s.diff(lev, r))/(mass*c*lev)
                 -1/(mass*c*lam)) == 0)

for bb in range(2, 13):
    for den in range(3, 12):
        for low in range(1, den-1):
            high = low+1
            bv, lv, hv = F(bb), F(low,den), F(high,den)
            av = (bv-hv)/(bv-lv)
            check(0 < av < 1)
            check(bv/(bv-hv)*av == bv/(bv-lv))
            for m in (1,2,3,5):
                # Forward anchoring expands the projected lower slice
                # exactly to the same anchor-normalized point.
                check((bv/(bv-hv))**m*av**m
                      == (bv/(bv-lv))**m)

# Surface sqrt(2) is removed from the symbolic coefficient.  The radial
# factor sqrt(2)/3 turns the surface coefficients 1,2 into 2/3,4/3.
# Inverse coefficients carry 1/c; M*L(o)=c/3 cancels it.
for rho in (F(1,9),F(1,4),F(2,3),F(1)):
    for q in range(1, 20):
        rate = rho*F(q,10)
        outer = F(2,3)/rho if rate < rho else F(0)
        middle = F(4,3)/(2*rho) if rate < 2*rho else F(0)
        inv_outer = F(2)/rho if rate < rho else F(0)
        inv_middle = F(2)/rho if rate < 2*rho else F(0)
        check(outer == inv_outer/3)
        check(middle == inv_middle/3)
    for k in range(15):
        # Edge lengths: outer region 2/3, middle region 1/3.
        inv_moment = F(2)/rho*(
            rho**(k+1)/F(k+1)
            + F(1,3)*((2*rho)**(k+1)-rho**(k+1))/F(k+1))
        weighted_surface_moment = (
            F(2,3)*F(2,3)*rho**k
            +F(4,3)*F(1,3)*(2*rho)**k)
        check(inv_moment/3 == weighted_surface_moment/F(k+1))

# Exact one-row normalization in the calibration.
ordinary_inverse = F(1)
raw_defect = F(1)+F(1,3)
z = ordinary_inverse+raw_defect
check(z == F(7,3))
check(F(1,4)/z == F(3,28))
check(2*F(3,28) == F(3,14))

# A genuine outer-interval source split has disconnected conditional
# inverse support although the complete geometric slice is uniform.
outer_length = F(1,2)
outer_inverse = outer_length+outer_length
check(outer_inverse == 1)
check((outer_length/F(4))/outer_inverse == F(1,8))
check(F(1,2)*outer_inverse/outer_inverse == F(1,2))

print(f'PASS: {checks:,} exact affine rate-slice checks')
