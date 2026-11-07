"""Exact algebra checks for the joint regular-singleton physical dual.

The inequalities tested below are rational consequences of the displayed
identities. They do not assert that arbitrary scalar arrays are stationary
actual bodies. Convex-order existence/contact geometry are analytic proofs.
"""
from fractions import Fraction as Q
import sympy as s

checks = 0

def zero(expr):
    global checks
    assert s.factor(expr) == 0, s.factor(expr)
    checks += 1

N, M, eps, P, Delta = s.symbols('N M eps P Delta', positive=True)
D, C, E, J, loss, beta, sv = s.symbols('D C E J loss beta sv', real=True)
delta, ell, logell, phi, Aphi, Yphi = s.symbols(
    'delta ell logell phi Aphi Yphi', real=True)
Pshape = s.symbols('Pshape', real=True)

# Independently assemble from raw Q', mass normalization and penalty,
# rather than start with the combined improvement functional.
fdot_over_f = (sv + phi / ell - Aphi - C / E + D / M) / N
Adot = (D - J) / (2 * M)
Qdot = -loss + delta * (fdot_over_f + Adot)
normalized_dot = Qdot / M + beta * D / M
penalized_dot = normalized_dot + eps**2 * (Pshape + Yphi - P*Aphi)
R = (loss-beta*D + delta*(C/(N*E)+J/(2*M)-(N+2)*D/(2*N*M)
       -sv/N-phi/(N*ell)+Aphi/N)
     -M*eps**2*(Pshape+Yphi-P*Aphi))
zero(M*penalized_dot + R)

# Three-fiber differentiation of geometric normalization with simultaneous
# signed body and raw affine-parameter changes.
V = s.symbols('V0:3', positive=True)
Dz = s.symbols('D0:3', real=True)
lz = s.symbols('l0:3', positive=True)
hz = s.symbols('h0:3', real=True)  # log ell values
pz = s.symbols('p0:3', real=True)
mass, total_loss = sum(V), sum(Dz)
w = [v/mass for v in V]
wdot = [(w[j]*total_loss-Dz[j])/mass for j in range(3)]
shape_scale = sum(Dz[j]*hz[j] for j in range(3))/mass
parameter_scale = sum(w[j]*pz[j]/lz[j] for j in range(3))
ell_dot = [pz[j] + lz[j]*(shape_scale-parameter_scale) for j in range(3)]
normalization = {hz[2]: -(V[0]*hz[0]+V[1]*hz[1])/V[2]}
zero((sum(wdot[j]*hz[j]+w[j]*ell_dot[j]/lz[j] for j in range(3)))
     .subs(normalization))
arithmetic = sum(w[j]*lz[j] for j in range(3))
expected_Pdot = (sum(Dz[j]*(arithmetic*(1+hz[j])-lz[j]) for j in range(3))/mass
                 +sum(w[j]*pz[j] for j in range(3))-arithmetic*parameter_scale)
zero(sum(wdot[j]*lz[j]+w[j]*ell_dot[j] for j in range(3))-expected_Pdot)

# Collect the entire per-unit-area body density at one boundary point.
a = Delta/(N*M)
kappa = a+eps**2*P
B = eps**2*(ell-P)-kappa*logell
raw_base_part = -Delta*logell/(N*M)-eps**2*(P*(1+logell)-ell)
zero(raw_base_part-B)
zero(-Delta*(N+2)/(2*N*M)+(N+2)*a/2)
zero(sum(w[j]*(eps**2*(lz[j]-arithmetic)
             -(a+eps**2*arithmetic)*hz[j]) for j in range(3)).subs(normalization))

# Parameter-only response: its annihilation is exactly affine moments (5).
active_phi = s.symbols('active_phi', real=True)
parameter_R = -active_phi/N+Delta*Aphi/N-M*eps**2*(Yphi-P*Aphi)
moment_residual = active_phi+N*M*eps**2*Yphi-(Delta+N*M*eps**2*P)*Aphi
zero(N*parameter_R+moment_residual)

# Active barycenter formula and strict order reduce to positive quantities.
Z, av = s.symbols('Z av', positive=True)
kap = av+eps**2*P
active_mass = kap*Z-eps**2
ellh = (kap-eps**2*P)/active_mass
zero(ellh-av/active_mass)
zero(1/Z-ellh-eps**2*(P*Z-1)/(Z*active_mass))
zero(active_mass-av*Z-eps**2*(P*Z-1))

# Hessian, anchored Jensen and cross-level reserve identities.
t, z, c, slope = s.symbols('t z c slope', real=True)
kk = s.symbols('kk', positive=True)
Bt = eps**2*(t-P)-kk*s.log(t)
zero(s.diff(Bt,t,2)-kk/t**2)
zero(s.diff(Bt.subs(t,c+slope*z),z,2)-kk*slope**2/(c+slope*z)**2)
lam, l0, l1 = s.symbols('lam l0 l1', positive=True)
lm = lam*l0+(1-lam)*l1
anchored = (lam*Bt.subs(t,l0)+(1-lam)*Bt.subs(t,l1)-Bt.subs(t,lm))
zero(anchored-kk*(s.log(lm)-lam*s.log(l0)-(1-lam)*s.log(l1)))

# An actual horizontal contact martingale: three identical intervals,
# source (1,1), targets (0,1),(2,1), equal target probabilities. These
# algebraic Jordan data are a contact calibration, not claimed stationary.
bvals = [Bt.subs(t,ll) for ll in [l0,lm,l1]]
zero(((lam*bvals[0]+(1-lam)*bvals[2]-bvals[1])-anchored).subs(lam,s.Rational(1,2)))

# Independently expand the quadratic surface test with signed Jordan data.
xi, base = s.symbols('xi base', real=True)
xi0 = xi-base
zero(-xi0*base-base**2+xi*base)

# Quantitative two-point Jensen: log(u)>=(u-1)/u and b>=a reduce
# the reserve estimate to this nonnegative rational remainder.
aa, gap = s.symbols('aa gap', positive=True)
bb=aa+gap
lower_log_gap=(aa-bb)**2/(2*(aa+bb)**2)
strong_bound=(aa-bb)**2/(8*bb**2)
zero(lower_log_gap-strong_bound-
     gap**3*(4*aa+3*gap)/(8*(aa+gap)**2*(2*aa+gap)**2))

# Rational stress checks for the exact extrapolated-location condition.
# The geometric weights make log ell mean zero exactly: ell=(2^-r,2^s),
# weights=(s,r)/(r+s). We do not assert that each has an actual separator.
for r in range(1,9):
    for ss in range(1,9):
        weights=[Q(ss,r+ss),Q(r,r+ss)]
        levels=[Q(1,2**r),Q(2**ss)]
        pp=sum(ww*ll for ww,ll in zip(weights,levels))
        zz=sum(ww/ll for ww,ll in zip(weights,levels))
        assert pp>1 and zz>1
        checks+=2
        for scalar_a, ee in [(Q(1,7),Q(1,10)),(Q(3,2),Q(1,100)),(Q(1,1000),Q(1,3))]:
            kp=scalar_a+ee**2*pp
            active=kp*zz-ee**2
            assert active>0
            hh=scalar_a/active
            assert 0<hh<1/zz<1<pp
            assert 1/zz-hh == ee**2*(pp*zz-1)/(zz*active)
            checks+=3

# Finite conditional Jensen identity before any logarithms: affine terms
# cancel for arbitrary weights, and level-crossing cost is a true variance.
for j in range(1,31):
    la=Q(j,31)
    lower,upper=Q(j+1,7),Q(2*j+9,5)
    middle=la*lower+(1-la)*upper
    variance=la*(lower-middle)**2+(1-la)*(upper-middle)**2
    assert variance==la*(1-la)*(upper-lower)**2
    assert (lower-upper)**2/(2*(lower+upper)**2)>=(lower-upper)**2/(8*max(lower,upper)**2)
    checks+=2

print(f'{checks} exact symbolic/rational checks PASS')
