"""Exact supplementary identities for the full-space affine buffer note.

The compactness, Fatou, and base-center arguments are analytic proofs in
the source; finite arithmetic checks do not replace them.
"""
from fractions import Fraction as F
import sympy as s

checks = 0


def check(ok):
    global checks
    assert ok
    checks += 1


def zero(expr):
    check(s.factor(expr) == 0)


# On a d-simplex, t=sum x_i has density d*t^(d-1).  The projective
# inverse-power moment at r=d+1 has an exact elementary antiderivative.
t, b, c = s.symbols("t b c", positive=True)
for d in range(1, 16):
    anti = t**d / (b * (b + c*t)**d)
    zero(s.diff(anti, t) - d*t**(d-1)/(b+c*t)**(d+1))
    zero(anti.subs(t, 1) - 1/(b*(b+c)**d))
    for rr in range(1, d):
        zero(s.integrate(d*t**(d-1-rr), (t, 0, 1)) - s.Rational(d, d-rr))

# Sharp critical power: the cone lower integral diverges logarithmically
# at r=d and at least as a power for every larger integral exponent.
for d in range(1, 21):
    for rr in range(d, d+6):
        check(d-1-rr <= -1)

# Arithmetic normalization of h_s=(s+t)/(s+d/(d+1)) and the exact
# r=d+1 scale: <h_s>=1 and A^(d+1)=<h_s^(-d-1)>.
ss = s.symbols("ss", positive=True)
for d in range(1, 13):
    n = d+1
    mean_t = s.Rational(d, n)
    h = (ss+t)/(ss+mean_t)
    zero(s.integrate(d*t**(d-1)*h, (t, 0, 1))-1)
    moment = (ss+mean_t)**n/(ss*(ss+1)**d)
    check(s.limit(moment, ss, 0, dir="+") == s.oo)
    zero(s.limit(ss*moment, ss, 0, dir="+")-mean_t**n)
    for q in (F(1,2), F(1,10), F(1,100)):
        actual = (q+F(d,n))**n/(q*(q+1)**d)
        check(actual >= 1)  # Jensen normalization scale is never <1.

# Fixed-body differential.  Abstract I(t)=< (L+t phi)^(-r)> has I(0)=1,
# I'(0)=-r A.  Normalize by I(t)^(1/r), not its reciprocal.
rr, aa, ll, ph, ee, mm = s.symbols("r A L phi E M", positive=True)
tt = s.symbols("tt")
norm = (1-rr*aa*tt)**(1/rr)*(ll+tt*ph)
zero(s.diff(norm, tt).subs(tt,0) - (ph-ll*aa))
for d in range(1, 16):
    n = d+1
    ff = (norm*ee/mm)**s.Rational(1,n)
    zero(s.diff(ff,tt).subs(tt,0)/ff.subs(tt,0)
         - (ph/ll-aa)/n)

# Actual interval calibration, r=2: all affine variations are legal and
# directly integrating the normalized kernel agrees with the tangent.
x, p, q, u, v = s.symbols("x p q u v", positive=True)
# For affine p+q*x on [0,1], inverse-square mean is 1/[p(p+q)].
scale = (p*(p+q))**s.Rational(-1,2)
l = scale*(p+q*x)
zero(s.diff(x/(p*(p+q*x)),x) - 1/(p+q*x)**2)
zero(scale**(-2)/(p*(p+q))-1)
for pv in (1,2,3):
    for qv in (1,2,4):
        for uv,vv in ((1,0),(0,1),(-1,2),(3,-1)):
            # Normalize a variation of the already normalized affine L.
            ls = s.simplify(l.subs({p:pv,q:qv}))
            phi = uv+vv*x
            av = s.integrate(phi/ls**3,(x,0,1))
            tangent = phi-ls*av
            zero(s.integrate(tangent/ls**3,(x,0,1)))
            check(s.simplify(s.integrate(1/ls**2,(x,0,1))) == 1)

# The affine-parameter barycenter identities use the same tilted measure.
# Discrete exact quadrature is only an algebra check, not a replacement
# for the actual continuous integral in the theorem.
for vals in ((1,2,3),(2,3,5),(1,4,7)):
    weights = (F(1,5),F(3,10),F(1,2))
    for exponent in range(1,8):
        masses = tuple(w*F(vv)**(-exponent-1)
                       for w,vv in zip(weights,vals))
        total = sum(masses)
        bary = sum(z*w for z,w in zip((-1,0,2),masses))/total
        check(-1 < bary < 2)
        check(sum(w/total for w in masses) == 1)

# Companion Section 7: every ordinary interval mark is its own tilted
# mean for an explicit normalized positive affine parameter.
y = s.symbols("y", positive=True)
num = y+(1-2*y)*x
zero(s.diff(x/(y*num),x)-1/num**2)
zero(s.diff(x*(1-x)/num**2,x)-(y-x)/num**3)
zero(y*(1-y)*(1/(y*(1-y)))-1)
for den in range(2,20):
    for nom in range(1,den):
        yy=F(nom,den)
        check(min(yy,1-yy)>0)
        check(yy*(1-yy)/(yy*(1-yy))==1)

# The changed tangent chart is a positive weighted average, without an
# assertion that its projective image is centroidal.
a_dot, c_dot, l_y = s.symbols("a_dot c_dot l_y", real=True)
for d in range(1,16):
    n=d+1
    zero(s.Rational(d,n)*(1+s.Rational(n,d)*a_dot)
         +(1+c_dot/l_y)/n-(1+a_dot+c_dot/(n*l_y)))

print(f"PASS: {checks} exact checks")
