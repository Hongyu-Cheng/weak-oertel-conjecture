"""Exact auxiliary checks for the scaled surface-log trace theorem.

No numerical sample is used to establish the general theorem.
"""
from itertools import product
import sympy as s

checks = 0

def equal(a, b):
    global checks
    assert s.simplify(a-b) == 0, (a, b, s.simplify(a-b))
    checks += 1

N, M, Delta = s.symbols('N M Delta', positive=True)
kappa = Delta/(N*M)
equal((N+2)*Delta/(2*N*M), (N+2)*kappa/2)
equal(2*M*kappa, 2*Delta/N)
e, c, L = s.symbols('e c L', positive=True)
equal(kappa*(M/Delta)*e*c/L, e*c/(N*L))
rb, rs, d, R, H = s.symbols('r_b r_s d R H', positive=True)
equal((d*(2*Delta/N)*H+2*R*Delta/(N*rs))/rb,
      Delta/(N*rb)*(2*d*H+2*R/rs))
equal(N**N/N, N**(N-1))

# Exact inner-parallel weighted first variations on actual boxes.
# Monomial weights use even exponents so no cancellations mask signs.
t = s.symbols('t', real=True)
for dim in range(1, 5):
    radii = [s.Rational(j+3, j+2) for j in range(dim)]
    for powers in product((0, 2, 4), repeat=dim):
        volume_weight = s.prod(2*(a-t)**(p+1)/(p+1)
                               for a, p in zip(radii, powers))
        boundary_weight = sum(
            2*radii[i]**powers[i]
            *s.prod(2*radii[j]**(powers[j]+1)/(powers[j]+1)
                    for j in range(dim) if j != i)
            for i in range(dim))
        equal(-s.diff(volume_weight, t).subs(t, 0), boundary_weight)

# Actual rounded outer rectangle has first area derivative = perimeter.
a, b = s.symbols('a b', positive=True)
outer_area = 4*a*b+4*(a+b)*t+s.pi*t*t
equal(s.diff(outer_area, t).subs(t, 0), 4*(a+b))

# Exact affine interval log normalization and gradient integral.
a, x = s.symbols('a x', positive=True)
J = ((2+a)*s.log(2+a)-a*s.log(a)-2)/2
primitive = (x+1+a)*s.log(x+1+a)-(x+1+a)
equal((primitive.subs(x, 1)-primitive.subs(x, -1))/2, J)
m = s.symbols('m', positive=True)
B = (J-s.log(x+1+a))/m
equal(s.diff(B, x), -1/(m*(x+1+a)))
equal((s.log(2+a)-s.log(a))/m,
      -(B.subs(x, 1)-B.subs(x, -1)))
equal(B.subs(x, -1)-B.subs(x, 1),
      (s.log(2+a)-s.log(a))/m)
equal(s.limit(J, a, 0, dir='+'), s.log(2)-1)

# Convex threshold algebra: on Phi>0 the density exceeds Phi.
W, E, C, beta, phi = s.symbols('W E C beta phi', nonnegative=True)
B0 = beta+(N+2)*kappa/2+phi
Xi = W+E+C+B0-beta-(N+2)*kappa/2
equal(Xi*phi-phi**2, (W+E+C)*phi)

print(f'PASS: {checks} exact checks')
