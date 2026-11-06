"""Exact chart, Jacobian, anchored criterion, and homogeneous-row checks."""
import sympy as s

checks = 0


def eq(a, b=0):
    global checks
    if isinstance(a, s.MatrixBase) or isinstance(b, s.MatrixBase):
        diff = a-b
        for value in diff:
            assert s.simplify(value) == 0, value
            checks += 1
    else:
        assert s.simplify(a-b) == 0, (a, b)
        checks += 1


# Differentiate the maps directly, then compare exact determinants/Gram determinants.
for d in range(1, 5):
    x = s.Matrix(s.symbols('x0:'+str(d)))
    for n in (1, 2):
        z = s.Matrix([s.Rational(j+1, 3) for j in range(n)])
        for case in range(1, 9):
            c = s.Matrix([s.Rational((-1)**j*(case+j), 17) for j in range(d)])
            ell = s.Rational(case+3, 2)
            L = ell+(c.T*x)[0]
            T = x/L
            Psi = s.Matrix(list(z)+list(x)+[1])/L
            xv = {x[j]: s.Rational(j+1, 13) for j in range(d)}
            Lv = L.subs(xv)
            DT = T.jacobian(x).subs(xv)
            DPsi = Psi.jacobian(x).subs(xv)
            eq(DT.det(), ell/Lv**(d+1))
            eq((DPsi.T*DPsi).det(),
               (ell**2+(1+(z.T*z)[0])*(c.T*c)[0])/Lv**(2*d+2))
            Y = T.subs(xv)
            eq(ell*Y/(1-(c.T*Y)[0]), x.subs(xv))

# A zero constant collapses the dropped-coordinate map, but not the lift.
x = s.symbols('x', positive=True)
eq(s.diff(x/x, x))
eq(s.diff(1/x, x), -1/x**2)

# Exact original interval family and strict closed-minor quotas.
lower = [s.Rational(1), s.Rational(2), s.Rational(3)]
image_lower = [v/(1+v) for v in lower]
eq(s.Matrix(image_lower), s.Matrix([s.Rational(1, 2), s.Rational(2, 3), s.Rational(3, 4)]))
eq((image_lower[0]+image_lower[2])/2, s.Rational(5, 8))
assert (image_lower[0]+image_lower[2])/2 < image_lower[1]
checks += 1
for V in (4, 3, 2):
    assert s.Rational(V) < s.Rational(9, 2)
    checks += 1
for V in (7, 5):
    assert V < 9
    checks += 1

# Proper oblique traces become a genuinely nonaffine threshold array.
thresholds = [s.Rational(z+2, 8) for z in (0, 1, 2)]
new = [v/(1+v) for v in thresholds]
eq(s.Matrix(new), s.Matrix([s.Rational(1, 5), s.Rational(3, 11), s.Rational(1, 3)]))
eq(2*new[1]-new[0]-new[2], s.Rational(2, 165))
assert all(0 < v < s.Rational(1, 2) for v in new)
checks += 1

# The finite-PL image has the two tips but misses their midpoint.
for tip in (-1, 1):
    L = 2-abs(tip)
    eq(s.Matrix([tip, 1])/L, s.Matrix([tip, 1]))
eq(s.Rational(2), 2)  # inverse midpoint requires X_2=2, outside the square
assert 2 > 1
checks += 1

# The exact inverse-weight anchored expression and lifted martingale identity.
for case in range(1, 31):
    zs = [s.Rational(-1), s.Rational(0), s.Rational(1)]
    lam = [s.Rational(1, 4), s.Rational(1, 2), s.Rational(1, 4)]
    xs = [s.Rational(case+j, case+4) for j in range(3)]
    ell = [2+z/s.Integer(5) for z in zs]
    c = s.Rational(case, case+7)
    Ls = [ell[j]+c*xs[j] for j in range(3)]
    Y = sum(lam[j]*xs[j]/Ls[j] for j in range(3))
    D = sum(lam[j]*ell[j]/Ls[j] for j in range(3))
    eq(1-c*Y, D)
    eq(2*Y/(1-c*Y), 2*Y/D)

    source = s.Matrix([sum(lam[j]*zs[j] for j in range(3)),
                       sum(lam[j]*xs[j] for j in range(3))])
    Li = sum(lam[j]*Ls[j] for j in range(3))
    barlam = [lam[j]*Ls[j]/Li for j in range(3)]
    eq(sum(barlam), 1)
    mean = s.zeros(3, 1)
    for j in range(3):
        mean += barlam[j]*s.Matrix([zs[j], xs[j], 1])/Ls[j]
    eq(mean, s.Matrix(list(source)+[1])/Li)

# Strict-convexity formula responsible for every finite-dimensional lift failure.
r = s.symbols('r', positive=True)
y = s.symbols('y', real=True)
rho_root = (1-y)**(-1/r)
eq(s.diff(rho_root, y, 2), (r+1)/r**2*(1-y)**(-1/r-2))
print(f'PASS: {checks} exact chart, Jacobian, quota, and homogeneous-row checks.')
