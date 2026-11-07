"""Exact supplementary checks; not a replacement for the section proof."""
from fractions import Fraction as Q
import sympy as s

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1


# The actual cone density has the prescribed retained mass, first moment,
# total mass, and both denominator endpoint values.
t = s.symbols('t')
for d in range(1, 15):
    N = d + 1
    for eta in [Q(1, 5), Q(1, 3), Q(1, 2), Q(2, 3), Q(4, 5), Q(1)]:
        er = s.Rational(eta.numerator, eta.denominator)
        a = d - s.Rational(N)/er
        c = (er - 1)/(N - d*er)
        g = s.Rational(d, N)*((d-t)/N)**(d-1)  # T=1.
        check(s.integrate(g, (t, -1, d)) == 1)
        check(s.integrate(t*g, (t, -1, d)) == 0)
        check(s.integrate(g, (t, a, d)) == er**(-d))
        check(s.simplify(1+c*d-1/(N-d*er)) == 0)
        check(s.simplify(1+c*a-1/er) == 0)
        E = s.simplify(er**(-d)/((1+c*d)*(1+c*a)**d))
        check(E == N-d*er)
        gamma = s.Rational(d, N)**d
        alpha = gamma*er**d
        F = s.Rational(N**N, d**d)*alpha*(1-s.Rational(d,N)*er)
        check(s.simplify(F-er**d*(N-d*er)) == 0)
        # Full denominator stays positive, including the boundary tau=1.
        check(1+c*d > 0 and 1+c*a > 0)
        check(E >= 1 and E <= er**(-d))


# The rational integral primitive used in both energy comparisons.
z, L0, L1 = s.symbols('z L0 L1', positive=True)
for d in range(1, 13):
    primitive = z**d/(L0*(L0+(L1-L0)*z)**d)
    expected = d*z**(d-1)/(L0+(L1-L0)*z)**(d+1)
    check(s.factor(s.diff(primitive, z)-expected) == 0)
    check(s.simplify(primitive.subs(z, 1)-1/(L0*L1**d)) == 0)


# Nested-simplex formula and strict tangent gap; s=q^{-d} is rational.
q = s.symbols('q', positive=True)
for d in range(2, 14):
    A = (d+1-q**d)/d
    G = A**d
    Gpp = (d-1)*(d+1)*q**(d-2)*A**(d-2)*(q**d-1)
    check(s.factor(s.diff(G, q, 2)-Gpp) == 0)
    check(G.subs(q, 1) == 1)
    check(s.diff(G,q).subs(q,1) == -d)
    for qr in [Q(1,4), Q(1,2), Q(2,3), Q(4,5), Q(9,10)]:
        scale = qr**(-d)
        beta0 = 1/(Q(d+1)*scale)
        betarest = (1-beta0)/d
        V = scale
        E = V*(d+1)**(d+1)*beta0*betarest**d
        check(E == (Q(d+1, d)-1/(d*scale))**d)
        check(E > 1)
        check((Q(d+1)-qr**d)**d/Q(d**d) < d+1-d*qr)
        check(E/V < Q(d+1)/scale-Q(d)*qr/scale)

check(Q(121,256) < Q(1,2))
check(Q(27,4)*Q(1,9)*(1-Q(1,3)) == Q(1,2))


# Exact interval equality, including either side as the shorter side.
for l in [Q(1,7),Q(1,2),Q(1),Q(3)]:
    for r in [Q(1,5),Q(2,3),Q(1),Q(4)]:
        V=l+r
        T=2*min(l,r)
        E=4*l*r/V
        check(E/V == 2*T/V-(T/V)**2)


def area(poly):
    return abs(sum(x*yy-y*xx for (x,y),(xx,yy)
                   in zip(poly,poly[1:]+poly[:1])))/2

def clip_x(poly, cut):
    out=[]
    for p, q0 in zip(poly,poly[1:]+poly[:1]):
        inp=p[0]>=cut
        inq=q0[0]>=cut
        if inp:
            out.append(p)
        if inp != inq:
            w=(cut-p[0])/(q0[0]-p[0])
            out.append((cut,p[1]+w*(q0[1]-p[1])))
    return out

# Actual determinant-one endpoint rectangles of coordinates are applied to
# triangles; direct clipping validates the fixed-offset limiting formula.
triangle=[(Q(2),Q(-1)),(Q(-1),Q(2)),(Q(-1),Q(-1))]
V=area(triangle)
compressed=[(x/4,4*y) for x,y in triangle]
check(area(compressed)==V)
check(clip_x(compressed,Q(1)) == [])
for L in [Q(1),Q(2),Q(3),Q(5),Q(10),Q(100)]:
    body=[(L*x,y/L) for x,y in triangle]
    check(area(body)==V)
    captured=area(clip_x(body,Q(-1)))
    check(captured/V == ((2+1/L)/3)**2)
    check(captured > Q(4,9)*V)

print(f'{checks} exact checks PASS')
