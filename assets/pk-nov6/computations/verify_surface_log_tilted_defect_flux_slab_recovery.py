"""Exact polynomial-test flux checks; no numerical weak-limit inference."""
import math
import sympy as s

a, b, C, lo, hi = s.symbols('a b C lo hi')
checks = 0

def check(v):
    global checks
    assert s.cancel(s.expand(v)) == 0, v
    checks += 1

def beta(r, q):
    return s.Rational(math.factorial(r)*math.factorial(q),
                      math.factorial(r+q+1))

def log_integral(n):
    """Integral_a^1 t^n [C+log(t-b)] dt, exact formal endpoint logs."""
    def endpoint(t, log):
        w = t-b
        return sum(s.binomial(n,j)*b**(n-j)*w**(j+1)*
                   (log/s.Integer(j+1)-s.Rational(1,(j+1)**2))
                   for j in range(n+1))
    return C*(1-a**(n+1))/s.Integer(n+1)+endpoint(1,hi)-endpoint(a,lo)

def reciprocal_integral(n):
    """Integral_a^1 t^n/(t-b) dt."""
    return b**n*(hi-lo)+sum(s.binomial(n,j)*b**(n-j)*
           ((1-b)**j-(a-b)**j)/s.Integer(j) for j in range(1,n+1))

# On K={x,y>=0, a<=x+y<=1}, the two slanted facets have
# vector area element +(1,1)dx and -(1,1)dx respectively.
# Check both continuous components of GG for every monomial degree <=8.
for r in range(9):
    for q in range(9-r):
        n = r+q
        diagonal = beta(r,q)*((C+hi)-a**(n+1)*(C+lo))
        boundary_x = diagonal-(log_integral(q) if r == 0 else 0)
        boundary_y = diagonal-(log_integral(r) if q == 0 else 0)
        gradient = beta(r,q)*reciprocal_integral(n+1)
        bulk_x = gradient+(r*beta(r-1,q)*log_integral(n) if r else 0)
        bulk_y = gradient+(q*beta(r,q-1)*log_integral(n) if q else 0)
        check(boundary_x-bulk_x)
        check(boundary_y-bulk_y)

# Exact contact/normalization identities before the limit.
Z=1-a+b*(hi-lo)
V=(1-a*a)/2
I=V+b*(1-a)+b*b*(hi-lo)
check(I-b*Z-V)
c=s.symbols('c',positive=True)
source=I/(2*Z)
Li=c*(2*source-b)
check(Li-c*V/Z)

# The new facet alone gives the nonzero limiting flux and radial moment.
l2=s.log(2)
n0=s.Matrix([-1/s.sqrt(2),-1/s.sqrt(2)])
bm=s.sqrt(2)*l2
zeta=2*l2/c
cv=s.Matrix([c,c])
for v in -n0*bm-s.Rational(1,2)*cv*zeta:
    check(v)
g=s.Matrix([s.Rational(1,3),s.Rational(1,3)])
check(n0.dot(-g)*bm-s.Rational(1,2)*(2*c/3)*zeta)

# Exact finite-m facet area times its logarithm, separating the bounded
# normalization term from the limiting entropy mass.
m, logc=s.symbols('m logc',positive=True)
check(s.sqrt(2)/m*(m*l2-logc)-s.sqrt(2)*l2+s.sqrt(2)*logc/m)

print(f'{checks} exact surface-log / tilted-defect flux checks PASS')
