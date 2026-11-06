"""Exact actual-slice and section checks for the near-quantile note."""
import sympy as s

eps, b, c, t, h = s.symbols('eps b c t h', real=True)
A = 1 + eps**2 / 3
t0 = eps / 3
r, q = 1 + eps*t, t-t0
checks = 0

def eq(actual, expected):
    global checks
    assert s.factor(actual-expected) == 0, (actual, expected)
    checks += 1

raw = s.integrate((2*r+b*q-c)**2/2, (t,-1,1))
expected = 4*A + A*b*b/3 -(4-2*b*t0)*c+c*c
eq(raw, expected)
eq(s.diff(raw,c), -4+2*b*t0+2*c)
eq(s.integrate(r*q,(t,-1,1)),0)
eq(s.integrate(q*q,(t,-1,1)),2*A/3)
eq(raw.subs(c,b*h),4*A-4*b*h+b*b*(s.Rational(1,3)+(t0+h)**2))

# Exact geometric coarea on the n1-tilted section, parameterized by (t,X2).
X1 = c-b*q
width = 2*r-c+b*q
S = s.integrate(width,(t,-1,1))
Mt = s.integrate(q*width,(t,-1,1))
M1 = s.integrate(X1*width,(t,-1,1))
M2 = s.integrate(((r-c+b*q)**2-r*r)/2,(t,-1,1))
eq(S,4-2*b*t0-2*c)
eq(Mt,2*t0*c+2*A*b/3)
poly = c*c-(4-2*b*t0)*c+A*b*b/3
eq(s.rem(s.Poly(M1+4*c,c),s.Poly(poly,c)).as_expr(),0)
eq(s.rem(s.Poly(M2-2*c,c),s.Poly(poly,c)).as_expr(),0)
eq(M1+b*Mt,c*S)

# Coarea moment derivative is the negative second tilt derivative.
J = s.integrate(q*q*(2*r-c),(t,-1,1))
eq(-s.diff(J,c),s.diff(raw,b,2).subs(c,0))
eq(s.diff(raw,b,2).subs(c,0),2*A/3)

root = 2-b*t0-s.sqrt(4-4*b*t0-b*b/3)
eq(s.simplify(poly.subs(c,root)),0)
eq(s.diff(root,b).subs(b,0),0)
eq(s.diff(root,b,2).subs(b,0),A/6)
eq(s.simplify(S.subs(c,root)),2*s.sqrt(4-4*b*t0-b*b/3))

# Actual polynomial integrals on the original triangle and its three caps.
x,y,u = s.symbols('x y u',real=True)
integrand = x*x+y*y
total = s.integrate(s.integrate(integrand,(y,-1,1-x)),(x,-1,2))
cap1 = s.integrate(s.integrate(integrand,(y,-1,1-x)),(x,0,2))
cap2 = s.integrate(s.integrate(integrand,(x,-1,1-y)),(y,0,2))
cap3 = s.integrate(s.integrate(x*x+(-u-x)**2,(x,-1,1-u)),(u,0,2))
eq(total,s.Rational(9,2))
eq((cap1+cap2+cap3)/3,s.Rational(16,9))
eq((cap1+cap2+cap3)/3-s.Rational(4,9)*total,-s.Rational(2,9))

# True moved-mark cancellation on the actual homothety path.
a=s.symbols('a',positive=True)
Ri=(root-a*b)*S.subs(c,root)
eq(s.diff(Ri,b).subs(b,0),-4*a)
eq(s.diff(Ri,b).subs(b,0)+4*a,0)
eq((c-a*b)*S + a*b*S - c*S,0)

print(f'PASS: {checks} exact slice, coarea, moment, and neutral-response checks')
