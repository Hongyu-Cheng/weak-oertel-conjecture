"""Exact checks for the affine-weight global fixed-body counterexample."""
from fractions import Fraction as F
import sympy as S

checks = 0
def ck(condition):
    global checks
    assert condition
    checks += 1

z = [-2, -1, 0, 1, 2]
r = [F(1), F(51, 50), F(51, 50), F(203, 200), F(101, 100)]
H = [F(4001, 4000), F(8091, 8000), F(403, 400),
     F(8029, 8000), F(3999, 4000)]
V = [2*a*b for a, b in zip(r, H)]
nu = [1600400, 1650564, 1644240, 1629887, 1615596]
M = F(8140687, 800000)
ck(V == [F(v, 800000) for v in nu])
ck(sum(V) == M)
ck(sum(F(v, 8140687) for v in nu) == 1)
ck(sum(j*v for j, v in zip(z, V)) == F(1943, 160000))

a, scale = S.symbols('a scale')
sv = [S.Rational(v.numerator, v.denominator) for v in V]
sm = S.Rational(M.numerator, M.denominator)
tilt = sum(j*v/(1+a*j) for j, v in zip(z, sv))
poly = 25985788*a**3+52316*a**2-16144435*a+9715
den = 800000*(a-1)*(a+1)*(2*a-1)*(2*a+1)
ck(S.factor(tilt-poly/den) == 0)
ck(tilt.subs(a, S.Rational(1, 2000)) > 0)
ck(tilt.subs(a, S.Rational(1, 1000)) < 0)
ck(S.factor(S.diff(tilt, a)
            + sum(j*j*v/(1+a*j)**2 for j, v in zip(z, sv))) == 0)
mass = sum(v/(1+a*j) for j, v in zip(z, sv))
ck(S.factor(mass-(sm-a*tilt)) == 0)
ck(S.factor(sum(v*scale*(1+a*j)/(sm*(1+a*j))
               for j, v in zip(z, sv))-scale) == 0)
for j in z:
    ck(1+F(j, 2000) > 0 and 1+F(j, 1000) > 0)
    # Target and original-volume row identities are pointwise.
    density = 1/(sm*(1+a*j))
    L = scale*(1+a*j)
    ck(S.factor(density/scale-1/(sm*L)) == 0)
    ck(S.factor(L*density/scale-1/sm) == 0)

# The actual all-normal source cap and every pure-base gap are unchanged.
delta = F(1, 4000)
Q = F(8130713, 1600000)
ck(2*r[0]*H[0]+sum(r[i]*(H[i]-F(z[i], 2)+delta)
                   for i in [1, 2, 3]) == Q)
ck(all(v < Q for v in [V[0], V[0]+V[1], V[3]+V[4], V[4]]))
ck(V[0]+V[1]+V[2] > Q and V[2]+V[3]+V[4] > Q)
ck(Q/M == F(8130713, 16281374))
ck(Q/M > F(2, 9))
ck(delta < H[2])

# All inside allocations are treated in the proof. The checks below
# independently integrate many actual rational step allocations.
eta = F(1, 200)
m = (r[3]-r[1], F(0), (r[3]-r[1])/2)
ck(m == (-eta, F(0), -eta/2))
ck(r[0] == 1 and r[4] == 1+2*eta)
for n in range(1, 24):
    edges = [-F(1, 2)+F(i, n) for i in range(n+1)]
    for seed in range(1, 18):
        q = [F((seed*(i+1)+i*i) % 19, 18) for i in range(n)]
        qmass = sum(qi*(b-a) for qi, a, b in zip(q, edges, edges[1:]))
        qx = sum(qi*(b*b-a*a)/2 for qi, a, b in zip(q, edges, edges[1:]))
        inside = (-2*qmass, qx, -qmass)
        # q_O=q_I(-x) on the common core, and 1/4 on the two extra strips.
        outside_mass = qmass+eta/2
        outside_x = -qx
        outside = (2*outside_mass, outside_x, outside_mass)
        ck(all(m[k]+outside[k] == -inside[k] for k in range(3)))
        ck(F(0) <= outside_mass <= 1+2*eta)
        # The y-reflected critical cap reverses only the last component.
        ck(-m[2]-outside[2] == inside[2])

print(f'PASS: {checks} exact checks')
