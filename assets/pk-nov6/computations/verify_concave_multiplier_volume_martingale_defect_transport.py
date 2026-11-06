"""Exact finite-flow, parameter-algebra, and actual calibration checks.

Generated flow arrays test the finite theorem, not realization as critical
body data. The nonaffine interval calibration is actual and independently
proved in the cited source.
"""
from fractions import Fraction as Q
import sympy as s

checks=0
N,M,e,P,D,H,A,Y=s.symbols('N M e P D H A Y',positive=True)
weighted_derivative=(H-D*A)/(N*M)+e**2*(Y-P*A)
assert s.expand(N*M*weighted_derivative-(H+N*M*e**2*Y-(D+N*M*e**2*P)*A))==0
checks+=1

def absorb(n, edges, nu):
    """edges=(p,[(z,lambda)],tau); all scalars exact rationals."""
    global checks
    out=s.zeros(n,1); inc=s.zeros(n,1); flow=s.zeros(n,n)
    for p,targets,tau in edges:
        assert sum(w for z,w in targets)==1
        assert sum(z*w for z,w in targets)==p
        out[p]+=tau
        for z,w in targets:
            inc[z]+=tau*w
            flow[p,z]+=tau*w
        checks+=2
    mu=nu+out-inc
    assert all(x>=0 for x in mu) and all(x>0 for x in nu)
    visits=nu+out
    transition=s.diag(*[1/x for x in visits])*flow
    stopping=s.diag(*[nu[p]/visits[p] for p in range(n)])
    assert all(sum(transition[p,z] for z in range(n))<1 for p in range(n))
    # Actual expected cumulative visits; this checks the source-injection
    # and all-stopping accounting even with reciprocal transition cycles.
    observed=(s.eye(n)-transition.T).inv()*mu
    assert observed==visits
    pi=s.diag(*mu)*(s.eye(n)-transition).inv()*stopping
    assert all(pi[p,z]>=0 for p in range(n) for z in range(n))
    assert pi*s.ones(n,1)==mu
    assert pi.T*s.ones(n,1)==nu
    coords=s.Matrix(range(n))
    assert pi*coords==s.diag(*mu)*coords
    checks+=7
    return mu,pi

# An actual base interval's nonaffine concave roof; its tight edges live
# separately in the two linear pieces. Positive target volumes can be
# chosen proportional to ell^2, an actual compatible homothetic family.
roof=s.Matrix([1,2,3,2,1])
nu=s.Matrix([1,2,3,2,1])
mu,pi=absorb(5,[(1,[(0,s.Rational(1,2)),(2,s.Rational(1,2))],s.Integer(2)),
               (3,[(2,s.Rational(1,2)),(4,s.Rational(1,2))],s.Integer(2))],nu)
assert mu==s.Matrix([0,4,1,4,0])
assert pi*roof==s.diag(*mu)*roof
assert sum(mu.multiply_elementwise(roof))==19
checks+=3

# Explicit reciprocal transitions 1<->2: positive absorption prevents a
# hidden cyclic component and verifies the final marginal exactly.
half=s.Rational(1,2)
mu,pi=absorb(4,[(1,[(0,half),(2,half)],s.Integer(6)),
               (2,[(1,half),(3,half)],s.Integer(8))],s.Matrix([10]*4))
assert mu==s.Matrix([7,12,15,6])
checks+=1

for n in range(3,9):
    for r in range(1,13):
        edges=[]
        incoming=s.zeros(n,1)
        for p in range(1,n-1):
            tau=s.Rational((p*r)%7+1,r+2)
            targets=[(p-1,half),(p+1,half)]
            edges.append((p,targets,tau))
            incoming[p-1]+=tau/2
            incoming[p+1]+=tau/2
        # This exact choice ensures mu=1+out>0; no unjustified capacity
        # inequality is needed to make the finite witness feasible.
        nu=s.ones(n,1)+incoming
        mu,pi=absorb(n,edges,nu)
        affine=s.Matrix([p+1 for p in range(n)])
        assert pi*affine==s.diag(*mu)*affine
        checks+=1

# Geometric normalization and concavity force the middle value >=1.
# Clearing the positive seventh root gives the exact polynomial test.
for aa in range(1,16):
    for cc in range(1,16):
        a,c=Q(aa,7),Q(cc,5)
        for gap in [Q(0),Q(1,10),Q(2,3)]:
            b=(a+c)/2+gap
            assert b**4-a*a*c*c>=0
            assert (b**4==a*a*c*c)==(a==b==c)
            # b/g >=1 iff b^7 >=a^2 b^3 c^2.
            assert b**7-a*a*b**3*c*c==b**3*(b**4-a*a*c*c)
            checks+=3

# Exact actual interval quantities and positive buffered mark shift.
vol=[Q(2),Q(3),Q(2)]
mass=sum(vol)
sigma=sum(v**3/Q(12) for v in vol)/mass
assert sigma==Q(43,84)
assert Q(3,14)<Q(1,4) and Q(1,4)-Q(3,14)==Q(1,28)
checks+=2
for j in range(4,13):
    eps=Q(1,10**j)
    t=Q(43,1764)*eps**2
    def poly(x):
        return (1+t)*x*x-t*x-Q(35,4)*t
    assert poly(0)<0<poly(eps/2)
    assert Q(1,4)+eps/4<Q(26,100)
    checks+=2

print(f'{checks} exact symbolic/rational checks PASS')
