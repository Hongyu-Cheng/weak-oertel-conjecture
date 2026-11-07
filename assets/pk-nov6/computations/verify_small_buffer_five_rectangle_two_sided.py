"""Exact supplementary checks for the small-buffer analytic certificate.

The continuum proof is in the companion Markdown source. These checks
independently clip actual rectangles at rational normals and reconstruct
the identities, support ranges, and strict constants used by that proof.
"""
from fractions import Fraction as F
import sympy as S

checks = 0
def ck(condition):
    global checks
    assert condition
    checks += 1

def pp(x):
    return max(F(0), x)

def area(width, t, margin):
    if t == 0:
        return width * min(F(2), max(F(0), 1 + margin))
    h = t * width / 2
    return width * (pp(margin+1+h)**2 - pp(margin+1-h)**2
                    - pp(margin-1+h)**2 + pp(margin-1-h)**2)/(4*h)

def positive_integral(width, t, s):
    if t == 0:
        return width * pp(s)
    return (pp(s+t*width/2)**2 - pp(s-t*width/2)**2)/(2*t)

etas = [F(1, 4096), F(1, 8192), F(1, 65536), F(1, 10**6)]
bases = list(range(-2, 3))
T = F(1, 16)
for eta in etas:
    r = [1, 1+4*eta, 1+4*eta, 1+3*eta, 1+2*eta]
    M = 2*sum(r)
    Q = 5+F(23, 2)*eta
    delta = 2048*eta
    c = sum(x**3 for x in r)/(4*sum(r))
    def mass(t, a, g=F(0)):
        return sum(area(width, t, a*z+g) for width, z in zip(r, bases))

    ck(M == 10+26*eta)
    ck(all(r[i+1]-r[i] >= r[i+2]-r[i+1] for i in range(3)))
    ck(F(1, 4) <= c <= F(25, 64))
    ck(0 < delta <= F(1, 2))
    ck(2*r[2]*(1-delta) >= 1)
    ck(M < 11)
    # Every proper closed minor is an actual consecutive subchain.
    for lo in range(5):
        for hi in range(lo, 5):
            if lo == 0 and hi == 4:
                continue
            k = len({z % 2 for z in bases[lo:hi+1]})
            ck(2*sum(r[lo:hi+1]) < k*M/2)

    # All unbuffered angles: actual symmetric-core decomposition.
    for ti in range(13):
        t = F(ti, 8)
        for ai in range(-18, 19):
            a = F(ai, 8)
            core = (area(r[2], t, 0)
                    + sum(area(1+3*eta, t, a*z) for z in [-1, 1])
                    + sum(area(F(1), t, a*z) for z in [-2, 2]))
            ck(core == 5+10*eta)
            ck(mass(t, a) >= Q-eta/2)
            if a >= 0:
                ck(mass(t, a) >= 5+12*eta)

    # Exact vertical statuses, unique tilt, and one-sided tilt slopes.
    for bi in range(97):
        b = F(bi, 32)
        expected = (5+13*eta-3*eta*b if b <= F(1, 2)
                    else 5+11*eta+eta*b if b <= 1 else 5+12*eta)
        ck(mass(F(0), -b) == expected)
        ck((expected == Q) == (b == F(1, 2)))
        if b < F(1, 4) or b > F(3, 4):
            ck(expected-Q >= eta/4)
    for h in [F(1, 100), F(1, 1000)]:
        ck((mass(F(0), -F(1, 2)+h)-Q)/h == 3*eta)
        ck((mass(F(0), -F(1, 2)-h)-Q)/h == eta)

    # Continuum-cell formula is verified by independent exact clipping.
    residual_moment = F(3, 2)*eta+F(11, 4)*eta**2
    ck(residual_moment == ((1+4*eta)**2-(1+3*eta)**2)/4
       + ((1+2*eta)**2-1)/4)
    ck(residual_moment <= F(107, 64)*eta)
    for ti in range(13):
        t = T*ti/12
        for bi in range(25):
            b = F(1, 4)+F(bi, 48)
            s = 2*b-1
            J = (positive_integral(1+2*eta, t, s)
                 - positive_integral(F(1), t, s))
            ck(mass(t, -b) == 5+13*eta-3*eta*b+J)
            ck(J >= 2*eta*pp(s))
            ck(mass(t, -b) >= Q)
            if t > 0:
                ck(mass(t, -b) > Q)
            if s == 0:
                ck(J == t*(eta+eta**2)/2)
        for ai in range(-40, 21):
            a = F(ai, 16)
            ck(abs(mass(t, a)-mass(F(0), a)) <= t*residual_moment)

    # Rational parametrization sqrt(1+c*t^2) for actual invariant norms.
    # Set q=c*lambda, so t=2lambda/(1-c lambda^2).
    gains = []
    for i in range(1, 65):
        lam = F(i, 40)
        den = 1-c*lam**2
        ck(den > 0)
        t = 2*lam/den
        root = (1+c*lam**2)/den
        g = delta*(root-1)
        ck(root**2 == 1+c*t*t)
        gain = area(r[2], t, g)-r[2]
        ck(gain > 0)
        gains.append(gain)
        for ai in range(-28, 13):
            a = F(ai, 8)
            ck(mass(t, a, g) >= mass(t, a)+gain)
            ck(mass(t, a, g) > Q)
            ck(mass(t, a, g+2*delta) >= mass(t, a, g))
    ck(all(a <= b for a, b in zip(gains, gains[1:])))

    # Strip regime and strict gain at T, checked without irrational rounding.
    ck(r[2]*T/2+delta*c*T*T/2 < 1)
    ck(1+c*T*T < 4)  # sqrt(...)+1<3
    ck(delta*F(1, 4)*T*T/3 == F(2, 3)*eta)
    ck(F(2, 3)*eta > eta/2)
    ck(delta**2*c < (r[2]/2)**2)
    ck(delta > eta/2)
    ck(mass(F(0), -F(1, 2), 2*delta) > Q)
    ck(6+16*eta > Q and 6+18*eta > Q)
    ck(area(r[0], F(0), F(1)) == 2*r[0])
    ck(area(r[4], F(0), -F(1)) == 0)
    ck(area(r[2], F(0), F(0)) == r[2])

# Symbolic reconstruction of the exact central clipping identity.
e, b, J = S.symbols('e b J')
s = 2*b-1
raw = 3+11*e+e*b + 1+2*b -(1+2*e)*s+J
ck(S.expand(raw-(5+13*e-3*e*b+J)) == 0)
ck(S.expand(raw-(5+S.Rational(23, 2)*e)
            -(J-S.Rational(3, 2)*e*s)) == 0)
ck(F(107, 1024) < F(1, 4))
ck(F(5, 128)+F(25, 65536) < 1)
ck(F(5, 16) < F(1, 2))
print(f'PASS: {checks} exact checks')
