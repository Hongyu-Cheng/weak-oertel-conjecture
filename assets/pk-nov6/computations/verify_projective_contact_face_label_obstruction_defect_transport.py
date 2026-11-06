"""Exact checks for the contact-face label/Jacobian obstruction.

The general-dimension BM obstruction and marginal proof are analytic in
the companion source; this checks independent rational and symbolic data.
"""
from fractions import Fraction as F
import sympy as S

checks = 0

def check(c):
    global checks
    assert c
    checks += 1

mass = {z: 1 / (1 + F(z, 2))**2 for z in (-1, 0, 1)}
check(mass == {-1: F(4), 0: F(1), 1: F(4, 9)})
check((mass[-1] + mass[1])/2 == F(20, 9))
check(mass[0] < (mass[-1]+mass[1])/2)
for z in (-1, 0, 1):
    L = 1 + F(z, 2)
    face_length = 1/L
    support_height = 1/L
    check(face_length*support_height == mass[z])
    check(F(z)/L == {-1: F(-2), 0: F(0), 1: F(2, 3)}[z])

z, r = S.symbols('z r', real=True, positive=True)
q = (1+z/2)**(-2/r)
check(S.simplify(S.diff(q,z,2) - (2/r)*(2/r+1)*S.Rational(1,4)*(1+z/2)**(-2/r-2)) == 0)

# Surface Gram determinants for m=1,2,3 verify the exact projective factor.
for m in range(1,4):
    # Rational nonzero tangent coefficients avoid hiding the normal term.
    H = S.Rational(5,3)
    s = S.Rational(7,4)
    a = S.Matrix([S.Rational(j+1, 2*j+3) for j in range(m)])
    for trial in range(1,8):
        xi = S.Matrix([S.Rational(trial+j,11) for j in range(m)])
        L = s + (a.T*xi)[0]
        v = xi.col_join(S.Matrix([H]))
        tangent = S.eye(m).col_join(S.zeros(1,m))
        D = tangent/L-v*a.T/L**2
        gram = (D.T*D).det()
        N2 = s*s+H*H*(a.T*a)[0]
        check(S.factor(gram-N2/L**(2*(m+1))) == 0)
        N = (H*a).col_join(S.Matrix([s]))
        check(S.factor((N.T*(v/L))[0]-H) == 0)

# Perspective Hessian: an explicit nonnegative rank-one quadratic form.
H,L,p = S.symbols('H L p', positive=True)
phi=H*(L/H)**p
hess=S.hessian(phi,(H,L))
e,f=S.symbols('e f', real=True)
expected=p*(p-1)*L**(p-2)*H**(-p-1)*(L*e-H*f)**2
check(S.simplify((S.Matrix([e,f]).T*hess*S.Matrix([e,f]))[0]-expected)==0)
print(f'{checks} exact checks PASS')
